#!/bin/bash
python waitconnection.py |& tee -a serverlog.txt
python manage.py migrate |& tee -a serverlog.txt
python manage.py runserver 0.0.0.0:8000 |& tee -a serverlog.txt