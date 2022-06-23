#!/bin/sh
FILE=($PWD/users/util.py)
if grep -q util.py "$FILE"; then
  (echo "00 09 * * 1-5 pipenv run python $FILE") | crontab -
  echo "Added crontab"
fi
  echo "Crontab already exist."
