#!/bin/bash
#This script sends a GET request to a given URL and displays its body on success
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -sL "$1"
