#!/usr/bin/bash

cd ./backend
poetry install

cd ../client
#!/usr/bin/env bash
npm run start-api &
pid[0]=$!
npm start &
pid[1]=$!
trap "kill ${pid[0]} ${pid[1]}; exit 1" INT
wait



