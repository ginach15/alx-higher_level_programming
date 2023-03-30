#!/bin/bash
# script that takes a URL then sends it a POST request with certain variables
curl $1 -sX POST -d "email=hr%40holbertonschool%2Ecom&subject=I+will+always+be+here+for+PLD"
