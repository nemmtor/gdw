from klient import klient
from konsultant import konsultant


def stworz_stopke():
    stopka = '<br>' * 2
    stopka += 'Pozdrawiam,<br>'
    stopka += '<i>{}</i>'.format(konsultant.kto)
    stopka += '<p style="font-size:10pt;">{}</p>'.format(konsultant.login)
    stopka += '''<hr align="left";
                   width="25%";
                   style="height:0.1pt;
                   background-color:gray;" >'''
    stopka += '<br>'
    stopka += '<p style="font-size:9pt;">Grupa Prawna Goldwin S.A.</p>'
    stopka += '<p style="font-size:9pt;">Ul. Kościuszki 71/304</p>'
    stopka += '<p style="font-size:9pt;">87-100 Toruń</p>'
    stopka += '''<p style="font-size:9pt;">
               <span style="color:#d49b48">T:</span> +48 222 692 222</p>'''
    stopka += '''<p style="font-size:9pt;">
               <a href="www.gpgoldwin.pl"
                style="color:#d49b48; text-decoration: none;
                border-bottom:0.5pt solid blue">
                www.gpgoldwin.pl
                </a></p>'''
    stopka += '<br>'
    stopka += '''<p style="font-size:9pt;">
               KRS: 0000586888 NIP: 8792679200, REGON: 362044066
               </p>'''
    stopka += '''<p style="font-size:9pt;">
               Oznaczenie sądu rejestrowego: Sąd Rejonowy w Toruniu,
               </p>'''
    stopka += '''<p style="font-size:9pt;">
               VII Wydział Gospodarczy Krajowego Rejestru Sądowego,
               </p>'''
    stopka += '''<p style="font-size:9pt;">
               kapitał zakładowy: 150.000,00 zł w całości wpłacony
               </p>'''
    stopka += '<br>'
    stopka += '''<p style="font-size:9pt; color:#7d7d7d">
    Wiadomość ta jest poufna i zastrzeżona.
    Zabronione jest przeglądanie, przekazywanie, rozpowszechnianie lub
    inne wykorzystywanie tych informacji, jak również podejmowanie działań
    na ich podstawie przez osoby lub podmioty inne niż zamierzony adresat.
    <br>Jeżeli otrzymali ją Państwo omyłkowo, prosimy poinformować o tym
    Nadawcę i usunąć z komputera wiadomość wraz z załącznikami.
    </p></body></html>'''
    return(stopka)


def stworz_subject(subject_type):
    subject = ''
    if subject_type == 1:
        if klient.nierozw == 1:
            subject += 'Sprawy nierozwiązane_'
        subject += 'Umowa_' + klient.imnaz + '_' +\
            klient.datasprz + '_' + klient.cena_dl
    return(subject)


def stworz_rodo():
    with open('pliki/rodo.txt', 'rb') as f:
        tresc_rodo = f.read().decode("UTF-8")
    body = tresc_rodo
    f.close()
    body += stworz_stopke()
    return(body)


def stworz_oferte():
    with open('pliki/129pan.txt', 'rb') as f:
        body = f.read().decode("UTF-8")
    f.close()
    body += stworz_stopke()
    body = body.format('TEST')
    return(body)


def stworz_body():
    if konsultant.wybor == 1:
        body = '''<html><body style="font-family:Calibri;font-size:11pt;">'''
        body += '<p>Imie i nazwisko: {} </p>'.format(klient.imnaz)
        body += '<p>Nr telefonu: {} </p>'.format(klient.tel)
        body += '<p>Data doręczenia: {} </p>'.format(klient.datawys)
        body += '<p>Adres email: {} </p>'.format(klient.mail)

        # Jeżeli checkbox odznaczony:
        if not klient.rej_var:
            body += '<p>Adres rejestrowy: {} </p>'.format(klient.rej)
        if not klient.kor_var:
            body += '<p>Adres korespondencyjny: {} </p>'.format(klient.kor)
        if not klient.dost_var:
            body += '<p>Adres dostarczenia: {} </p>'.format(klient.dost)

        body += '<p>Branża: {} </p>'.format(klient.branza)
        body += '<p>Pytania do prawnika: {} </p>'.format(klient.pytania)
        body += '<p>Dodatkowe informacje: {} </p>'.format(klient.dodatkowe)
        body += stworz_stopke()
    return(body)
