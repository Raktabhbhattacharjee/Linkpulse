# LinkPulse

LinkPulse is a lightweight URL shortener built with FastAPI, SQLAlchemy async, Alembic, and PostgreSQL. The project is designed as a clean backend learning example focused on layered architecture, async database access, and practical API design.

## Why this project exists

LinkPulse is meant to demonstrate how a small but production-minded service can be structured with clear separation between:

- HTTP handling
- business logic
- data access
- persistence and migrations

## Tech stack

| Layer      | Technology             |
| ---------- | ---------------------- |
| Language   | Python 3.13            |
| API        | FastAPI                |
| ORM        | SQLAlchemy 2.x (async) |
| Database   | PostgreSQL             |
| Migrations | Alembic                |
| Validation | Pydantic               |

## Architecture overview

```mermaid
flowchart LR
    Client[Browser / API Client] -->|HTTP requests| API[FastAPI App]
    API --> Routes[Routes Layer]
    Routes --> Service[Service Layer]
    Service --> Repo[Repository Layer]
    Repo --> DB[(PostgreSQL)]
    DB --> Repo
    Repo --> Service
    Service --> Routes
    Routes --> API
    API --> Client
```

The request flow is intentionally simple:

- Routes receive HTTP requests and return responses
- Services contain the business rules for link creation and redirect behavior
- Repositories manage SQLAlchemy access to the database

## Request lifecycle

```mermaid
sequenceDiagram
    participant Client as Client
    participant API as FastAPI
    participant Service as LinkService
    participant Repo as LinkRepository
    participant DB as PostgreSQL

    Client->>API: POST /links
    API->>Service: create_link(url)
    Service->>Service: generate short_code
    Service->>Repo: create(original_url, short_code)
    Repo->>DB: INSERT link
    DB-->>Repo: saved row
    Repo-->>Service: Link object
    Service-->>API: Link response
    API-->>Client: short link payload
```

```mermaid
sequenceDiagram
    participant Client as Client
    participant API as FastAPI
    participant Service as LinkService
    participant Repo as LinkRepository
    participant DB as PostgreSQL

    Client->>API: GET /links/{short_code}
    API->>Service: get_original_url(short_code)
    Service->>Repo: get_by_short_code(short_code)
    Repo->>DB: SELECT link
    DB-->>Repo: link row
    Repo-->>Service: link
    Service->>Service: increment click_count
    Service->>Repo: update(link)
    Repo->>DB: UPDATE link
    DB-->>Repo: updated row
    Service-->>API: original URL
    API-->>Client: redirect response
```

## API endpoints

| Method | Endpoint                  | Description                  |
| ------ | ------------------------- | ---------------------------- |
| POST   | /links/                   | Create a new shortened link  |
| GET    | /links/{short_code}       | Redirect to the original URL |
| GET    | /links/{short_code}/stats | Fetch analytics for a link   |

## Data model

```mermaid
erDiagram
    LINK {
        uuid id PK
        string short_code UK
        text original_url
        int click_count
        timestamp created_at
        timestamp last_accessed_at
    }
```

The current model stores:

- a unique short code for lookup
- the original destination URL
- click count and last access metadata
- timestamps for auditing and analytics

## Project structure

```text
linkpulse/
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── link_routes.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py
│   ├── repositories/
│   │   └── link_repository.py
│   ├── schemas/
│   │   └── link.py
│   ├── services/
│   │   └── link_service.py
│   └── main.py
├── alembic/
├── tests/
├── alembic.ini
├── pyproject.toml
└── README.md
```

## Getting started

### Prerequisites

- Python 3.13+
- PostgreSQL running locally
- pip or uv

### 1. Install dependencies

```bash
pip install -e .
pip install pytest httpx
```

### 2. Configure environment variables

Create a .env file in the project root with a database URL such as:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/linkpulse
```

### 3. Run database migrations

```bash
alembic upgrade head
```

### 4. Start the development server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- http://localhost:8000
- http://localhost:8000/docs

### 5. Run tests

```bash
pytest tests/ -v
```

## Learning highlights

- Clean layered structure with routes, services, and repositories
- Async database access with SQLAlchemy
- Versioned schema changes through Alembic
- Simple analytics flow based on click tracking and timestamps

## Possible next steps

- Add Redis caching for frequently accessed links
- Add authentication and link ownership
- Add rate limiting and observability
- Containerize the app with Docker

## License

This project is open source and available under the MIT License.
