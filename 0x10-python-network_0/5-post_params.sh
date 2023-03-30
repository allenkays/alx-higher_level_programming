#!/bin/bash
# Script sends a custom POST request with key value pair to a given URL
curl -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
