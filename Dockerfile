FROM python:3.8.3-slim

WORKDIR /app

# Creates a specific application user for non-root execution of the app
RUN groupadd --system appuser && adduser --system --ingroup appuser appuser
RUN chown appuser:appuser /app

# Installation of tools to install packages
RUN pip install --no-cache-dir --upgrade pip pipenv

# Required packages installation layer (cached unless new dependencies are added)
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile && \
    pip uninstall --yes pipenv && \
    rm Pipfile Pipfile.lock

# Copies other files that are not related to install dependencies (chowns to app user)
COPY --chown=appuser:appuser . ./

# Execution as a non-root user
USER appuser
