#!/usr/bin/bash
# Print the size in bytes of the http header response` of a given url
curl -s $1 | wc -c
