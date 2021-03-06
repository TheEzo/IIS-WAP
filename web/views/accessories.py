    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, redirect, url_for, jsonify
from flask.views import MethodView

from web.core import db


class Accessories(MethodView):
    def get(self):

        return render_template('accessories.html')


def configure(app):
    app.add_url_rule('/accessories',
                 view_func=Accessories.as_view('accessories'))

    @app.route('/accessories_list', methods=['POST'])
    def getAccessoriesData():
        request_json = request.get_json()
        accessories = db.get_products_data(request_json.get('limit', 10), request_json.get('start', 0), request_json.get('url'))
        templates_list = []
        for accessory in accessories:
            templates_list.append(render_template('accessory_template.html', data=accessory))
        return jsonify(templates_list)
