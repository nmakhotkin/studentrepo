#!/bin/bash
TOOLS=`dirname $0`
VENV=$TOOLS/../.tox/venv
source $VENV/bin/activate && $@
