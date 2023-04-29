# DogFood
## Dependencies
* poetry (Python package manager): See [install instructions](https://python-poetry.org/docs/#installation)
* Node.js >=16.8.0
## Development Usage
### Fetch source and activate virtual environment
```sh
    git clone git@github.com:avinashpai/dogfood.git
    cd dogfood/backend
    poetry shell
    cd ../client
```
### In separate terminal windows:
```sh
    npm run start-api   # runs "cd ../backend/api && flask run --server app --debug"
    # Flask API proxy is localhost:5000 (set in package.json)
```
```sh
    npm start           # Launches browser to localhost:3000
```
