#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, redirect, url_for
from flask.views import MethodView
from web.core import db


class Costumes(MethodView):
    def get(self):

        return render_template('costumes.html')


def configure(app):
    app.add_url_rule('/costumes',
                 view_func=Costumes.as_view('costumes'))
