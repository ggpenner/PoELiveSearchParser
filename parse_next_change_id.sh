#!/bin/bash

#NEXT_CHANGE_ID=$(cat next_change_id)
NEXT_CHANGE_ID=$(curl http://api.poe.ninja/api/Data/GetStats | sed -n 's/.*"nextChangeId":"\(.*\)","api.*/\1/p')
curl http://api.pathofexile.com/public-stash-tabs/?id=$NEXT_CHANGE_ID > stashtab-api.json
python parser.py

while (true)
do
	#sed -n 's/.*"next_change_id":"\(.*\)","stashes".*/\1/p' stashtab-api.json > next_change_id
    curl -s http://api.poe.ninja/api/Data/GetStats | sed -n 's/.*"nextChangeId":"\(.*\)","api.*/\1/p' > next_change_id
	NEXT_CHANGE_ID=$(cat next_change_id)

	#echo "curl http://api.pathofexile.com/public-stash-tabs/?id=:$NEXT_CHANGE_ID > stashtab-api.json"
	#echo
	curl -s http://api.pathofexile.com/public-stash-tabs/?id=$NEXT_CHANGE_ID > stashtab-api.json

	python parser.py &
done
