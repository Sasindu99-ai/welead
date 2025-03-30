from typing import Dict, List, Optional, Tuple, Type

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import NotFound

from ..db.models import Model
from ..serializers import ModelRequest, Request

__all__ = ["Service"]


class Service(serializers.ModelSerializer):
    model: Type[Model]
    updateExclude: List[str] | Tuple = ("id", "created_at", "updated_at", "deleted_at")
    searchableFields: List[str] | Tuple = ("id", "created_at")
    filterableFields: List[str] | Tuple = ()
    searchKey: str = "search"
    pageKey: str = "pagination"
    annotations: Dict = dict()
    createUniqueFields: List[str] | Tuple = ()

    def __init__(self, *args, model: Optional[Type[Model]] = None, **kwargs):
        if model is not None:
            self.model = model
        super().__init__(*args, **kwargs)

    def getAll(self) -> List[Type[Model]]:
        return self.model.objects.all()

    def getById(self, obj_id):
        try:
            return self.model.objects.get(pk=obj_id)
        except ObjectDoesNotExist:
            raise NotFound(f"{self.model.__name__} with ID {obj_id} does not exist.")

    def delete(self, obj_id):
        obj = self.getById(obj_id)
        if obj is not None:
            obj.delete()
            return True
        raise NotFound(f"Object with ID {obj_id} does not exist.")

    def hard_delete(self, obj_id):
        obj = self.getById(obj_id)
        if obj is not None:
            obj.hard_delete()
            return True
        return False

    def create(self, validated_data: Dict):
        try:
            for uniqueField in self.createUniqueFields:
                if self.model.objects.filter(
                    **{uniqueField: validated_data[uniqueField]}
                ).exists():
                    raise serializers.ValidationError(
                        f"{uniqueField.capitalize()} already exists."
                    )
            return self.model.objects.create(**validated_data)
        except (ObjectDoesNotExist, NotFound, IntegrityError) as e:
            raise serializers.ValidationError(e.args[0])

    def update(self, instance, validated_data: Dict):
        for key, value in validated_data.items():
            if key not in self.updateExclude:
                setattr(instance, key, value)
        instance.save()
        return instance

    def exists(self, obj_id: int) -> bool:
        return self.getById(obj_id) is not None

    def match(self, data: Type[Request] | Type[ModelRequest]) -> List[Type[Model]]:
        return self.search(data.validated_data)

    def search(self, data: Dict) -> List[Type[Model]]:
        queryset = self.model.objects.all()

        # Apply annotations
        for key, value in self.annotations.items():
            queryset = queryset.annotate(**{key: value})

        # Filter by filterable fields
        for field in self.filterableFields:
            if field in data.keys():
                queryset = queryset.filter(**{field: data[field]})

        # Search by searchable fields
        if self.searchKey in data.keys():
            search = data.get(self.searchKey)
            query = Q()
            for field in self.searchableFields:
                query |= Q(**{f"{field}__icontains": search})

            queryset = queryset.filter(query)

        # Distinct
        queryset = queryset.distinct()

        # Paginate
        if self.pageKey in data.keys():
            pagination = data.get(self.pageKey)

            # Sorting
            if isinstance(pagination, dict) and "sortBy" in pagination.keys():
                sortBy = pagination.get("sortBy")
                queryset = queryset.order_by(*sortBy)

            # Paging
            if pagination is not None:
                page = pagination.get("page")
                limit = pagination.get("limit")
                queryset = queryset[(page - 1) * limit : page * limit]

        return queryset
