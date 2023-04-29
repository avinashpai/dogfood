#!/usr/bin/bash

cd ./backend
poetry shell
#!/usr/bin/bash
cd ..
flask --app backend run --debug &
pid[0]=$!
cd ./client
npm start &
pid[1]=$!
trap "kill ${pid[0]} ${pid[1]}; exit 1" INT
wait



