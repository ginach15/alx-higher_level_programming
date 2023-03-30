#!/bin/bash
# script that takes a URL, sends a request, and returns the size of the body
curl -w "%{size_download}\n" "$1" -so /dev/null
