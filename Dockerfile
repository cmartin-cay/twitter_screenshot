FROM python:3.12-slim-bullseye
RUN apt-get update && apt-get install -y curl --no-install-recommends
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin/:$PATH"
ENV UV_SYSTEM_PYTHON=1

COPY requirements.txt .

RUN uv pip install --system ruff
RUN uv pip install -r requirements.txt