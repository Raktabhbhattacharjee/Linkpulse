# LinkPulse

Lightweight URL shortener and analytics service built with FastAPI, SQLAlchemy (async), Alembic, and PostgreSQL.

## Quick start

These commands assume a Windows PowerShell environment from the project root.

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install

```powershell
pip install -e .
```

3. Configure environment

Create a `.env` file in the project root (example):

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/linkpulse
```

4. Run database migrations

```powershell
alembic upgrade head
```

5. Start the development server

```powershell
uvicorn app.main:app --reload
```

Open the interactive docs at http://localhost:8000/docs

## Features

- Create shortened links
- Redirect to original URLs
- Track click counts and last-access metadata
- Simple analytics endpoint for each short link

## Project layout

- `app/` — application package (API routes, services, repos, models)
- `alembic/` — migration configuration and versions
- `tests/` — unit and integration tests
- `pyproject.toml` — project metadata and dependencies

Example important files:

- [app/main.py](app/main.py) — FastAPI app entrypoint
- [app/api/routes/link_routes.py](app/api/routes/link_routes.py) — HTTP routes
- [app/services/link_service.py](app/services/link_service.py) — business logic
- [app/repositories/link_repository.py](app/repositories/link_repository.py) — DB access

## API (summary)

- `POST /links/` — create a shortened link
- `GET /links/{short_code}` — redirect to the original URL
- `GET /links/{short_code}/stats` — fetch analytics for a link

Refer to the interactive OpenAPI docs at `/docs` for request/response schemas.

## Database & migrations

This project uses Alembic for migrations. Configure `DATABASE_URL` and run:

```bash
alembic upgrade head
```

If you change models, generate a new migration with:

```bash
alembic revision --autogenerate -m "describe change"
```

## Tests

Run tests with:

```powershell
pytest -q
```

Integration tests may require a running Postgres instance with the same `DATABASE_URL`.

## Development notes

- Code is organized with clear separation: routes → services → repositories → models
- Business rules live in `app/services`, DB access in `app/repositories`.
- Models and Alembic versions live under `app/db` and `alembic/versions`.

## Contributing

Contributions and improvements are welcome. Please open an issue or a pull request with a short description of the change.

## Next steps (ideas)

- Add Dockerfiles and a `docker-compose` for local development
- Add authentication and link ownership
- Add caching (Redis) and rate limiting

## License

MIT
