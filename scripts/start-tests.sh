#!/bin/bash
set -e # exit if any statement returns non-true value
source ./scripts/functions.sh  # import functions

# pytest uses .local.env when needed
aerich_migrate_and_upgrade

echo "🐍 Running pytest test runner... 🐍"
pytest tests -vv --cov=src --doctest-modules \
    --junitxml=junit/test-results.xml --cov-report=xml --cov-report=html \
    --cov-report=term --cov-append