#!/bin/bash

shellcommand="shell"

listcontains() {
  for word in $1; do
    [[ $word = $2 ]] && return 0
  done
  return 1
}

sudoportlist="80 443"
portlist="8000 8080"


echo "Got ./runserver.sh $1 "

if [ -z "$1" ]
then
	echo "Usage: ./runserver.sh port|shell"
elif [ "$1" == "$shellcommand" ];
then
    ./manage.py shell
elif listcontains "$sudoportlist" "$1" 
then
	sudo ./manage.py runserver 103.18.59.118:$1
elif listcontains "$portlist" "$1"
then
    ./manage.py runserver 103.18.59.118:$1
else
	./manage.py runserver localhost:$1
fi

