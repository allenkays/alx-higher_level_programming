#!/usr/bin/bash
# Print size in bytes of the http header response` of a given url
curl -s "$1" | wc -c
