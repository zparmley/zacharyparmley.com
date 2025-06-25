FROM python:3.13.5
COPY --from=ghcr.io/astral-sh/uv:0.7.13 /uv /uvx /bin/
WORKDIR /site
COPY . /site
CMD ["uv", "run", "main.py", "--port", "8080"]
