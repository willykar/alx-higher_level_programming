#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ $# -ne 1 ]; then
	echo "Usage: $URL"
	exit 1
fi

URL=$1

curl -sI "$URL" | awk '/Contect-Length/ {print $2}'
