#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_login import login_user, logout_user, current_user
from flask import redirect, request, abort, url_for, flash, request, render_template, jsonify, session
from wtforms import StringField, Form, PasswordField
from wtforms.validators import email, regexp, ValidationError, data_required
from werkzeug.security import check_password_hash

from web.core import db


class LoginForm(Form):
    email = StringField('Email', validators=[email(message='Toto není email'),
                                             data_required('Pole musí být vyplněno')])
    password = PasswordField('Heslo', validators=[regexp(r'^(?=.*\d)(?=.*[A-ZĚŠČŘŽÝÁÍÉÚŮ]).{8,}$',
                                                         message='Heslo musí obsahovat číslo, velké písmeno a musí být alespoň 8 znalů dlouhé'),
                                                  data_required('Pole musí být vyplněno')])


def configure_login(app):
    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for('home'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated():
            return redirect(url_for('home'))
        if not request.form:
            return render_template('login.html', form=LoginForm())
        form = LoginForm(request.form)
        data = form.data
        u = db.get_user(data.get('email'))
        if not u:
            flash('Email nebyl rozpoznán. <a href="' + url_for('register') + '">Registrovat?</a>', 'alert-danger')
            return redirect(url_for('login'))
        if not check_password_hash(u.heslo, data.get('password')):
            flash('Nesprávný email nebo heslo', 'alert-danger')
            return redirect(url_for('login'))
        user = User(email=u.email, rc=u.rc, name=u.jmeno, surname=u.prijmeni)
        login_user(user)
        session['cart'] = {'costumes': [], 'accessories': []}
        flash('Příhlášení proběhlo úspěšně', 'alert-success')
        return redirect(url_for('home'))

class User:
    def __init__(self, rc, email='', name='', surname=''):
        self.id = rc
        self.email = email
        self.name = name + ' ' + surname
        employee = db.get_employee_data(rc) if rc else None
        self.employee = employee is not None
        self.admin = True if employee and employee.pozice == 'vedouci' else False

    def is_authenticated(self):
        if self.id is not None:
            return True
        return False

    def is_active(self):
        return True

    def is_employee(self):
        return self.employee

    def is_admin(self):
        return self.admin

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

