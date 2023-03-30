#!/bin/bash
# script that takes a URL, sends a GET request there and displays the body of the response with custom header
curl $1 -sX GET -H "X-HolbertonSchool-User-Id: 98"
