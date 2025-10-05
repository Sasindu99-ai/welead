# Makefile

# Define a variable for the poetry command to keep it DRY
POETRY = uv
MANAGER = python main.py
PORT = 8010

# Load poetry
.PHONY: load
load:
	export PATH="$$HOME/.local/bin:$$PATH"

# Install dependencies
.PHONY: sync
sync:
	$(POETRY) sync

# Install pre-commit hooks
.PHONY: install-pre-commit
install-pre-commit:
	$(POETRY) run pre-commit uninstall
	$(POETRY) run pre-commit install

# Check code style
.PHONY: lint
lint:
	$(POETRY) run pre-commit run --all-files

# Make migrations
.PHONY: make-migrations
make-migrations:
	$(MANAGER) makemigrations authentication settings main events

# Execute migrations
.PHONY: execute-migrate
execute-migrate:
	$(MANAGER) migrate

# Make and execute migrations
.PHONY: migrate
migrate: make-migrations execute-migrate ;

# Update project dependencies
.PHONY: update
update: migrate install-pre-commit ;

# Run the Django development server
.PHONY: dev
dev:
	$(POETRY) run $(MANAGER) runserver $(PORT)

# Run the Django development server with a specific port
.PHONY: run
run:
	$(POETRY) run daphne main:asgi --port $(PORT) --bind 0.0.0.0

# Create a superuser
.PHONY: superuser
superuser:
	$(POETRY) run $(MANAGER) createsuperuser

.PHONY: db
db:
	$(POETRY) run $(MANAGER) dbshell
