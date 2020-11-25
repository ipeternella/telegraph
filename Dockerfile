FROM python:3.9.0-buster

# creates app group and user
RUN groupadd --system app-user && adduser --system --ingroup app-user app-user

# creates app directory owned by the app user
WORKDIR /app
RUN chown app-user:app-user /app

# installs pip
RUN pip install --no-cache-dir --upgrade pip pipenv

# dependencies install: separated layer for caching purposes
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile && \
    pip uninstall --yes pipenv

# copies app remaining files to /app and chowns to the app-user
USER app-user
COPY --chown=app-user:app-user . ./