#!/bin/bash

# exports env variables on a given dotenv path
# args: $1: path to the dotenv file
function export_dotenv_variables() {
    dotenv_path=$1

    echo "🐍 Exporting $dotenv_path variables... 🐍"        
    set -o allexport
    [[ -f $dotenv_path ]] && source $dotenv_path
    set +o allexport
}

# make migrations and runs them with aerich tool
function aerich_migrate_and_upgrade() {
    echo "🐍 Trying to run old migrations (if any)... 🐍"
    aerich upgrade  # there can't be unaplied migrations or weird errors happen, so... let's guarantee that first

    echo "🐍 Generating migrations with aerich (only for MIGRATION runs)... 🐍"
    aerich migrate

    echo "🐍 Running new migrations with aerich (if any)... 🐍"
    aerich upgrade
}

# just run migrations with aerich tool
function aerich_upgrade() {
    echo "🐍 Running new migrations with aerich (if any)... 🐍"
    aerich upgrade
}

# starts uvicorn via python process for debugging
function start_debug_uvicorn_server() {
    SERVER_FULL_BIND_ADDRESS=${SERVER_BIND_ADDRESS}:${SERVER_BIND_PORT}

    echo "🐍 Starting debug uvicorn server on http://${SERVER_FULL_BIND_ADDRESS} 🐍"
    python main.py
} 

# starts uvicorn server
function start_uvicorn_server() {
    echo "🐍 Starting production uvicorn to serve the ASGI application... 🐍"
    uvicorn main:server --host ${SERVER_BIND_ADDRESS} --port ${SERVER_BIND_PORT}
}