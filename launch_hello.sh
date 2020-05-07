#! /bin/bash

echo "input $1"
for i in `seq 1 $1`; do
  curl -s -X POST localhost/hello-back -H "content-type: application/json" -d '{"lang":"es", "name": "joseph"}' -w "\n" >> toto
done
