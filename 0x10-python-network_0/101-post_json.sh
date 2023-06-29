#!/bin/bash
# Sends a POST request with data from JSON file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
