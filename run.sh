#!/usr/bin/bash

cd ./backend
poetry shell
#!/usr/bin/bash
cd ../client
npm run start-api &
pid[0]=$!
npm start &
pid[1]=$!
trap "kill ${pid[0]} ${pid[1]}; exit 1" INT
wait



