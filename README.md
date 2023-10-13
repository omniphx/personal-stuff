# Deploy to AWS Beanstalk

A Flask/HTMX app for my personal stuff

### Getting started

1. `python3 -m venv .venv`
2. `. .venv/bin/activate`
3. `pip3 install`

### Generate SSL

`openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`
