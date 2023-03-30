#!/bin/bash
# This script sends a requests and displays only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
