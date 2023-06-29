#!/bin/bash
# Sends a POST request with data
curl -s -o /dev/null -w "%{http_code}" "$1"
