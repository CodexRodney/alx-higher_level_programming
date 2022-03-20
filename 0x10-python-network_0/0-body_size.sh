#!/bin/bash
#takes in a uRL sends a request to the url, prints the 
#size of the ody of the response

curl -sD - "$1" | grep "Content-Length" | cut -d " " -f 2-
