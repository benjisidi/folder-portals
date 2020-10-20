#!/usr/bin/env bash

function goto() {
    target="$(python3 ${PORTALS_ROOT}/commands.py -c go -k $*)"
    cd $target
}

function save() {
    python3 ${PORTALS_ROOT}/commands.py -c save -k $*
}

function rmportal() {
    python3 ${PORTALS_ROOT}/commands.py -c rm -k $*
}

function portals() {
    python3 ${PORTALS_ROOT}/commands.py -c ls
}