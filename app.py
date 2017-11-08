#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Shawling'

from flask import Flask, request, abort, redirect, url_for
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route("/people/")
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return 'Name:{0};UA:{1}'.format(name, user_agent)

