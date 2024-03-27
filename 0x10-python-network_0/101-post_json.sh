#!/bin/bash
# sends a JSON POST request to a URL passed as an arg, and displays the response body
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
