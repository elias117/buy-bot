# Buy Bot for amazon

This bot is written in python3.8.11 and will watch a particular page for a buy now button and continually refresh the page. Currently it is set to watch for the coveted PlayStation 5 but it could be configured to watch for any amazon url.

#### Configuration

You will need to add your amazon email and password to the .env file. The next thing you want to do is make sure docker is installed. Turn on 1-click purchase for your amazon account.


#### Requirements
Python3.8.11

packages:
```
python-dotenv==0.19.0
selenium==3.141.0
```

#### Running

```
docker-compose up -d --build
```