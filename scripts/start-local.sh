#!/bin/sh
set -e # exit if any statement returns non-true value
source ./scripts/functions.sh  # import functions

export_dotenv_variables ".local.env"
aerich_migrate
start_debug_uvicorn_server