#!/usr/bin/bash

cd ./backend
poetry install

cd ../client
npm run start-api &
npm start &



