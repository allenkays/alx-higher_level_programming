#!/bin/bash
# This script displays all HTTP methods the server will accept for the specified URL
curl -Is -X OPTIONS "$1" | grep "Allow"
