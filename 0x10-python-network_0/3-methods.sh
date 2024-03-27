#!/bin/bash
# script that takes in a URL, sends a DELETE request to the URL, and displays the body of the response
curl -sI "$1" -X OPTIONS | grep -i "Allow:" | sed 's/Allow: //i'
