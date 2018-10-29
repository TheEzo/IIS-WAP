#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from web.core import db
from wtforms import StringField, Form, SelectField, validators, TextAreaField,IntegerField, FileField, ValidationError
from wtforms.validators import data_required
from web.roles import employee
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class Barva(db.Barva):
    def __repr__(self):
        return "%s" % (self.barva)

class AddAccessory(Form):
    nazev = StringField("Název",[validators.Length(min=5, max=128),data_required('Pole musí být vyplněno')])
    vyrobce = StringField("Výrobce", [validators.Length(min=1, max=45), data_required('Pole musí být vyplněno')])
    popis_vyuziti = TextAreaField("Popis využití", [validators.Length(min=10, max=512),data_required('Pole musí být vyplněno')])
    velikost = SelectField("Velikost",choices=[('S','S'),('M','M'),('L','L'),('XL','XL'),('XXL','XXL'),('XXXL','XXXL')])
    opotrebeni = SelectField("Opotřebení",
                           choices=[('nove', 'Nové'), ('stare', 'Staré'), ('zanovni', 'Zánovní')])
    pocet = IntegerField("Počet",[data_required('Pole musí být vyplněno')])
    material = StringField("Materiál", [validators.Length(min=2, max=45),data_required('Pole musí být vyplněno')])
    typ = StringField("Typ", [validators.Length(min=2, max=45),data_required('Pole musí být vyplněno')])
    datum_vyroby = StringField("Datum výroby", [data_required('Pole musí být vyplněno')])
    cena = IntegerField("Cena za kus",[data_required('Pole musí být vyplněno')])
    obrazek = FileField("Náhled")
    barva = QuerySelectField("Barva",query_factory=lambda: Barva.query,allow_blank=False)

class AccessoriesAdmin(MethodView):
    @employee
    def get(self):

        return render_template('accessories_admin.html', form = AddAccessory())

    @employee
    def post(self):

        form = AddAccessory(request.form)
        if not form.validate():
            return render_template('accessories_admin.html', form=form)
        db.add_accessory(**form.data)
        flash('Doplněk byl úspěšně přidán', 'alert-success')
        return render_template('home.html')

def configure(app):
    app.add_url_rule('/accessories-admin',
                 view_func=AccessoriesAdmin.as_view('accessories-admin'))
