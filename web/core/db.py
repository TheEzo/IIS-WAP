#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web.core.db_connector import session
from web.core.models import *
from werkzeug.security import generate_password_hash


def get_user(email):
    return Osoba.query.filter_by(email=email).first()


def create_user(*args, **kwargs):
    stmt = Osoba(rc=kwargs['rc'],
                 email=kwargs['email'],
                 heslo=generate_password_hash(kwargs['password']),
                 jmeno=kwargs['jmeno'],
                 prijmeni=kwargs['prijmeni'],
                 ulice=kwargs.get('ulice'),
                 cislo_popisne=kwargs.get('cislo_popisne'),
                 tel_cislo=kwargs.get('tel_cislo'))
    session.add(stmt)
    session.commit()
    stmt = Klient(clenstvi='bronzove',
                  osoba_rc=kwargs['rc'])
    session.add(stmt)
    session.commit()


def get_employee_data(rc):
    return Zamestnanec.query.filter_by(osoba_rc=rc).first()


def add_costume(*args, **kwargs):
    stmt = Kostym(vyrobce=kwargs['vyrobce'],
                  material=kwargs['material'],
                  popis=kwargs['popis'],
                  velikost=kwargs['velikost'],
                  datum_vyroby=kwargs['datum_vyroby'],
                  opotrebeni=kwargs['opotrebeni'],
                  pocet=kwargs['pocet'])
    session.add(stmt)
    session.commit()


def add_accessory(*args, **kwargs):
    stmt = Doplnek(nazev=kwargs['nazev'],
                   popis_vyuziti=kwargs['popis_vyuziti'],
                   datum_vyroby=kwargs['datum_vyroby'],
                   velikost=kwargs['velikost'],
                   opotrebeni=kwargs['opotrebeni'],
                   pocet=kwargs['pocet'],
                   typ=kwargs['typ'],
                   material=kwargs['material'],
                   )
    session.add(stmt)
    session.commit()


def get_users_data():
    return session.query(Osoba, Zamestnanec.pozice, Obec.nazev)\
        .outerjoin(Zamestnanec, Osoba.rc == Zamestnanec.osoba_rc)\
        .outerjoin(Obec, Osoba.obec_id == Obec.id)\
        .all()


def insert_base_users():
    stmt = Osoba(rc='9609255832',
                 email='willaschek.t@gmail.com',
                 # Heslo123
                 heslo='pbkdf2:sha256:50000$qeDxpiht$e3f267714dc599d57ce7f6a10e55febb032e717d9561c1c501404c0d4c8ba9f6',
                 jmeno='Tomas',
                 prijmeni='Willaschek',
                 ulice='',
                 cislo_popisne='',
                 tel_cislo='')
    session.add(stmt)
    session.commit()
    stmt = Klient(clenstvi='bronzove',
                  osoba_rc='9609255832')
    session.add(stmt)
    stmt = Zamestnanec(osoba_rc='9609255832',
                       pozice='vedouci')
    session.add(stmt)
    session.commit()


def delete_user(rc):
    session.delete(Osoba(rc=rc))
    session.commit()