# -*- coding: utf-8 -*-
"""
Gunicorn Uvicorn config to lauch in Digital Ocean's App Platform.

Using their Flask template: https://github.com/digitalocean/sample-flask

"""
import uvicorn

bind = "0.0.0.0:8080"
workers = 2
worker_class = uvicorn.workers.UvicornWorker
