#!/bin/bash
#takes in a uRL sends a request to the url

curl -sD - "$1" | grep "Content-Length" | cut -d " " -f 2-
