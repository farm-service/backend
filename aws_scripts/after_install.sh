#!/bin/sh

pip install -r requirements.txt

sudo cp /aws_scripts/uvicorn_service.service /etc/systemd/system/

