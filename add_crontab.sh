#!/bin/sh
(crontab -l ; echo "00 09 * * 1-5 pipenv run python $PWD/users/util.py") | crontab -
