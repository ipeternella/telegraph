#!/bin/bash
set -e # exit if any statement returns non-true value
source ./scripts/functions.sh  # import functions

aerich_upgrade
start_uvicorn_server