# FastAPI Template for DDD

### Hello 👋
##### This is a template designed to help you get started with building FastAPI projects using Domain-Driven Design (DDD) principles.


## Project Structure:
```
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── exception.py
│   ├── main.py
│   ├── core
│   │   ├── __init__.py
│   │   └── database
│   │       ├── __init__.py
│   │       ├── base_model.py
│   │       ├── base_repository.py
│   │       └── connection.py
│   └── users
│       ├── __init__.py
│       ├── dependency.py
│       ├── auth
│       │   ├── __init__.py
│       │   ├── router.py
│       │   ├── schema.py
│       │   └── service.py
│       └── user
│           ├── __init__.py
│           ├── model.py
│           ├── repository.py
│           ├── router.py
│           ├── schema.py
│           └── service.py
├── migrations
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── README.md
└── pyproject.toml
```
