# Project Rules

## Scope

Use this repo as a Django project with a custom `vvecon.zorion` framework layer. Keep changes aligned with the existing app/domain structure instead of introducing new patterns.

## Code style

- Target Python 3.10+.
- Keep one responsibility per file and one main class per module when possible.
- Follow the current naming style: PascalCase classes and modules, camelCase methods and fields where the codebase already uses them.
- Keep imports grouped as stdlib, third-party, local.
- Export public symbols with `__all__` when the module already follows that pattern.
- Prefer small, explicit functions and avoid broad `try/except` blocks.
- Use type hints on public methods, service APIs, and shared helpers.
- Preserve existing sentinel usage such as `NotImplemented` when matching project patterns.

## File structure

- `core/` holds project URLs and global settings.
- `apps/<domain>/` holds feature code.
- Common app subfolders:
  - `models/`
  - `services/`
  - `views/`
  - `admin/`
  - `migrations/`
  - `payload/request/`
  - `payload/response/`
  - `enums/`
  - `forms/`
  - `tests/`
  - `templates/`
- Keep app templates under the owning app, and share fragments through `includes/` or `common/`.
- Keep `static/` for public assets and `media/` for uploaded/generated files.

## Django and framework usage

- Put business logic in services, not in views.
- Use `vvecon.zorion.core.Service` for reusable data access and filtering.
- Use `vvecon.zorion.db.models.Model` for soft-delete models with `created_at`, `updated_at`, and `deleted_at`.
- Use `@Mapping`, `@GetMapping`, `@PostMapping`, `@PutMapping`, and `@DeleteMapping` for page/API endpoints.
- Use `API` for JSON endpoints and `View` for rendered templates.
- Use request payload classes for validation and response payload classes for shaped output.
- Use `Return.ok`, `Return.created`, `Return.badRequest`, and `Return.notFound` for API responses.
- Use `R` for template resources (`data`, `files`, `images`) instead of hard-coded asset wiring when a helper exists.

## Resources and configuration

- Read environment values through the existing settings loaders in `vvecon.zorion.app.settings`.
- Keep secret and environment-specific values in `.env` or environment variables, not in source.
- Prefer `Logger` for runtime logging.
- Keep external integrations behind service classes.
- Use the existing resource helpers for static files, image URLs, theme assets, and template metadata.

## Data and database changes

- Keep migrations checked in.
- Add model changes first, then services/views that depend on them.
- Use the custom manager/queryset patterns already present in the repo.
- Prefer service-level validation over duplicated checks in views.

## Testing and maintenance

- Add or update tests under each app’s `tests/` folder.
- Keep fixtures, scratch data, and generated files out of source control.
- Use the provided `Makefile` targets for routine tasks (`sync`, `lint`, `migrate`, `dev`, `run`).
