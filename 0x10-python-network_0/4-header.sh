#!/bin/bash
# This script sends a GET request to the specified URL with a custom header and displays the body of the response
curl -H "X-School-User-Id: 98" -s "$1"
