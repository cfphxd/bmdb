#!/bin/bash

listcontains() {
  for word in $1; do
    [[ $word = $2 ]] && return 0
  done
  return 1
}

sudoportlist="80 443"


if [ -z "$1" ]
then
	echo "Usage: ./runserver.sh port"
elif listcontains "$sudoportlist" "$1" 
then
	sudo ./manage.py runserver 103.18.59.118:$1
else
	./manage.py runserver localhost:$1
fi

