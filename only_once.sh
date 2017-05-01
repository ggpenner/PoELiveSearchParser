#!/bin/bash

# usually not needed, but just in case something went wrong and you want to test the parser with some data.
NEXT_CHANGE_ID=$(cat next_change_id)
curl --silent http://api.pathofexile.com/public-stash-tabs/?id=$NEXT_CHANGE_ID > stashtab-api.json
python parser.py
