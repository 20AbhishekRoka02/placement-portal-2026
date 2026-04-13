# GitHub Copilot Instructions

## Project overview
- Django backend application using `backend/` as the Django project root and a `users/` app.
- Uses PostgreSQL for the database, Redis for Celery broker, Celery for background tasks, and Whitenoise for static file serving.
- Entry point is `manage.py`.

## Important files
- `manage.py` — Django CLI entry point for server, migrations, and tests.
- `backend/settings.py` — development and production settings, environment-driven database config, Celery settings.
- `backend/urls.py` — the current URL routing setup.
- `backend/celery.py` — Celery app initialization and task discovery.
- `wait_for_db.py` — helper script to wait for PostgreSQL availability.
- `users/` — application code for user-related models, views, and tests.
- `requirements.txt`, `requirements-local.txt` — Python dependencies.
- `.env.dev`, `.env.prod` — environment variable examples/configuration.

## What to expect
- The repository currently has no higher-level docs like `README.md` or `CONTRIBUTING.md`.
- There is no frontend code in this workspace; focus on Django backend and deployment/configuration.
- The production settings are not fully separated; `backend/settings.py` is the central config file.

## Common developer tasks
- Install dependencies: `python3 -m pip install -r requirements.txt` (or `requirements-local.txt` for local development).
- Run the app locally: `python3 manage.py runserver 0.0.0.0:8000`.
- Apply migrations: `python3 manage.py migrate`.
- Run tests: `python3 manage.py test`.
- Start Celery worker: `celery -A backend worker --loglevel=info`.
- Wait for the database before startup: `python3 wait_for_db.py`.
- Collect static assets: `python3 manage.py collectstatic --noinput`.

## Environment notes
- Development uses `.env.dev` with `POSTGRES_*` and `CELERY_BROKER_URL` values.
- `backend/settings.py` reads `env` from environment vars; `env=prod` enables SSL-mode production database options.
- Current settings use `DEBUG = True` and `ALLOWED_HOSTS = ['*']`; treat this as dev-focused.
- Avoid committing sensitive secrets from `.env.prod` or other env files.

## Best prompts for this workspace
- "Explain how to add a new Django model in `users/models.py`, migrate it, and register it in the admin."
- "What changes are needed to add a DRF API endpoint to `backend/urls.py` and `users/views.py`?"
- "Refactor `backend/settings.py` to support `DATABASE_URL` without breaking the existing `POSTGRES_*` setup."
- "Review the current Celery configuration and suggest any improvements for task discovery and broker configuration."

## When in doubt
- Start from `backend/settings.py` and `manage.py` for configuration and commands.
- Use Python/Django idioms consistent with the existing app structure.
- Prefer minimal changes that preserve the current dev workflow.
