#!/bin/bash
set -e # exit if any statement returns non-true value
source ./scripts/functions.sh  # import functions

# no need for env variables, docker env has them
aerich_migrate_and_upgrade
start_debug_uvicorn_server