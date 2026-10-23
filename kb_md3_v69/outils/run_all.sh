#!/bin/sh
# Regenerate the whole knowledge base from an IQANdesign text export.
# Usage: sh tools/run_all.sh export.txt kb_dir
set -e
D=$(dirname "$0")
python -I "$D/kb_build.py" "$1" "$2"
python -I "$D/anomalies.py" "$1" "$2"
python -I "$D/reports.py" "$1" "$2"
