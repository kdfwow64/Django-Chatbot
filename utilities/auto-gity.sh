#!/bin/sh
if [ $# -eq 1 ]
  then
    git add -A
    git add *
    git commit -m "$1"
    git push
    git push heroku master
    say "Done and commited to Heroku Master!"
    heroku logs --tail
    exit 0
  else
    message="Please put in your commit message! And make sure it makes sense!"
    echo ${message}
    say "${message}"
    exit 1
fi
