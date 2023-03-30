#!/bin/bash
# Script sends JSON POST requset to URL and displays body response.
curl -s -X POST -H "content-type: JSON/application" -d "@$2" "$1"
