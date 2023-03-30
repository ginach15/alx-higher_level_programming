#!/bin/bash
# script that takes a URL, sends a GET request to it, then returns the body of the response
curl -LsX GET "$1"
