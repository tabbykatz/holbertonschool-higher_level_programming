#!/bin/bash
# displays only the status code of the response
curl -s -L -o /dev/null -s -w "%{http_code}" "$1"
