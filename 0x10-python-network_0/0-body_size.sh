#!/usr/bin/bash
# Print the bytesize of the http header of a given url
curl -s -w -o /dev/null $1 | wc -c
