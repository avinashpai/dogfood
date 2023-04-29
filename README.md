# DogFood
## Development Usage
### Fetch source and activate virtual environment
```sh
    git clone git@github.com:avinashpai/dogfood.git
    cd dogfood/server
    poetry shell
    cd ../client
```
### In separate terminal windows:
```sh
    npm run start-api   # runs "cd ../server/src && flask run --server app --debug"
    # Flask API proxy is localhost:5000 (set in package.json)
```
```sh
    npm start           # Launches browser to localhost:3000
```