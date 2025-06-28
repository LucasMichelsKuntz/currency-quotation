FROM python:3.13-slim AS base

RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc libffi-dev && \
    rm -rf /var/lib/apt/lists/*

ENV APP_HOME=/app
RUN mkdir -p $APP_HOME/logs
WORKDIR $APP_HOME

RUN adduser --disabled-password --no-create-home appuser && \
    chown -R appuser:appuser $APP_HOME

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser:appuser $APP_HOME

FROM base AS development
USER appuser
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

FROM base AS production
USER appuser
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
