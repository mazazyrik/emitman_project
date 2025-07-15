# EMITMAN Backend

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Initialize aerich:
```bash
aerich init-db
```

3. Run migrations:
```bash
aerich migrate
aerich upgrade
```

4. Run the server:
```bash
python main.py
```

## Environment Variables

Create a `.env` file:
```env
# Database
DATABASE_URL=sqlite://db.sqlite3

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=
REDIS_DB=0

# App
APP_NAME=EMITMAN RANEPA
DEBUG=false
HOST=127.0.0.1
PORT=8000

# CORS
CORS_ORIGINS=["*"]
```

## Migrations

Create new migration:
```bash
aerich migrate --name "migration_name"
```

Apply migrations:
```bash
aerich upgrade
```

Rollback migrations:
```bash
aerich downgrade
```
