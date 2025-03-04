#!/bin/bash
docker build -t fastapi_sqlite_app .
docker run -p 8000:8000 fastapi_sqlite_app
