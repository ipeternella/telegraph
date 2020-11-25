#!/bin/sh
set -e # exit if any statement returns non-true value
source ./scripts/functions.sh  # import functions

export_dotenv_variables ".local.env"

# creates first migration (src/migrations/models -- models folder must NOT exist)
echo "🐍 Running init-db ... 🐍"
aerich init-db