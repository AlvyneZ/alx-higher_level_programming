#!/bin/bash
# Sends a POST request with data from JSON file
curl  -s -X POST -d @"$2" "$1"
