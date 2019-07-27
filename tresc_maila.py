# -*- coding: utf-8 -*-
from config import klient, konsultant


def stworz_subject():
    if konsultant.wybor == 1:
        subject = "Umowa_" + klient.imnaz + "_" +\
            klient.datasprz + "_" + klient.cena_dl
    return(subject)


def stworz_body():
    if konsultant.wybor == 1:
        body = '<p>Imie i nazwisko: {} </p>'.format(klient.imnaz)
        body += '<p>Nr telefonu: {} </p>'.format(klient.tel)
        body += '<p>Data doręczenia: {} </p>'.format(klient.datawys)
        body += '<p>Adres email: {} </p>'.format(klient.mail)
        if not klient.rej_var:
            body += '<p>Adres rejestrowy: {} </p>'.format(klient.rej)
        if not klient.kor_var:
            body += '<p>Adres korespondencyjny: {} </p>'.format(klient.kor)
        if not klient.dost_var:
            body += '<p>Adres rejestrowy: {} </p>'.format(klient.dost)
        body += '<p>Branża: {} </p>'.format(klient.branza)
        body += '<p>Pytania do prawnika: {} </p>'.format(klient.pytania)
        body += '<p>Dodatkowe informacje: {} </p>'.format(klient.dodatkowe)
        body += '<br>' * 2
        body += '<p>Pozdrawiam,</p>'
        body += konsultant.kto
    return(body)
