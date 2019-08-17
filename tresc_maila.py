from klient import klient
from konsultant import konsultant
from config import rodo, tresc, rodoinf


def stworz_stopke():
    stopka = '<p style="font-size:10pt";>'
    stopka += '<i>Pozdrawiam,</i><br><br>'
    stopka += '{}'.format(konsultant.kto)
    stopka += '<br>'
    # stopka += '<span style="font-size:8pt";>Specjalista ds. sprzedaży</span>'
    # stopka += '<br>'
    stopka += '{}'.format(konsultant.login)
    stopka += '</p>'

    stopka += '<p>'
    stopka += '''<hr align="left";
                   width="25%";
                   style="height:0.1pt;
                   background-color:gray;" ></p>'''

    stopka += '<p style="font-size:9pt;">Grupa Prawna Goldwin S.A.'
    stopka += '<br>'
    stopka += 'Ul. Kościuszki 71/304'
    stopka += '<br>'
    stopka += '87-100 Toruń'
    stopka += '<br>'
    stopka += '''<span style="color:#d49b48">T:</span> +48 222 692 222'''
    stopka += '<br>'
    stopka += '''
               <a href="www.gpgoldwin.pl"
                style="color:#d49b48; text-decoration: none;
                border-bottom:0.5pt solid #d49b48">
                www.gpgoldwin.pl
                </a></p>'''

    stopka += '''<p style="font-size:8pt;">
               KRS: 0000586888 NIP: 8792679200, REGON: 362044066'''
    stopka += '<br>'
    stopka += '''Oznaczenie sądu rejestrowego: Sąd Rejonowy w Toruniu,'''
    stopka += '<br>'
    stopka += '''VII Wydział Gospodarczy Krajowego Rejestru Sądowego,'''
    stopka += '<br>'
    stopka += '''kapitał zakładowy: 150.000,00 zł w całości wpłacony'''
    stopka += '<br>'
    stopka += '</p>'
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
    with open(rodo, 'rb') as f:
        tresc_rodo = f.read().decode("UTF-8")
    body = tresc_rodo
    f.close()
    body += stworz_stopke()
    return(body)


def stworz_rodoinf():
    with open(rodoinf, 'rb') as f:
        tresc = f.read().decode("UTF-8")
    body = tresc
    f.close()
    return(body)


def stworz_oferte(plec, cena):
    if plec == 1:
        pan_pani = "Pan"
        panu_pani = "Panu"
        pana_pani = "Pana"
        panem_pania = "Panem"
    if plec == 2:
        pan_pani = "Pani"
        panu_pani = "Pani"
        pana_pani = "Pani"
        panem_pania = "Panią"

    with open(tresc, 'rb') as f:
        body = f.read().decode("UTF-8")
    f.close()
    body += stworz_stopke()
    return(body.format(pan_pani, panu_pani, pana_pani, panem_pania, str(cena)))


def stworz_body():
    if konsultant.wybor == 1:
        body = '''<html><body style="font-family:Calibri, sans-serif;
        font-size:11pt;">'''
        body += '<p>Nr telefonu: {}'.format(klient.tel)
        body += '<br>'
        body += 'Imie i nazwisko: {}'.format(klient.imnaz)
        body += '<br>'
        body += 'Data doręczenia: {}'.format(klient.datawys)
        body += '<br>'
        body += 'Adres email: {}'.format(klient.mail.replace(',', ''))

        if klient.rodzajadresu == 'rejkordost':
            if klient.rej_var:
                body += '<br>'
                body += '''Adres rejestrowy, korespondencyjny,
                dostarczenia: {}'''.format(
                    klient.rej)

        if klient.rodzajadresu == 'rejkor':
            if klient.rej_var:
                body += '<br>'
                body += '''Adres rejestrowy, korespondencyjny: {}'''.format(
                    klient.rej)
            if klient.dost_var:
                body += '<br>'
                body += 'Adres dostarczenia: {}'.format(klient.dost)

        if klient.rodzajadresu == 'rejdost':
            if klient.rej_var:
                body += '<br>'
                body += '''Adres rejestrowy, dostarczenia: {}'''.format(
                    klient.rej)
            if klient.kor_var:
                body += '<br>'
                body += 'Adres korespondencyjny: {}'.format(klient.kor)

        if klient.rodzajadresu == 'kordost':
            if klient.rej_var:
                body += '<br>'
                body += '''Adres rejestrowy: {}'''.format(
                    klient.rej)
            if klient.kor_var:
                body += '<br>'
                body += 'Adres korespondencyjny, dostarczenia: {}'.format(
                    klient.kor)

        if klient.rodzajadresu == 'osobne':
            if klient.rej_var:
                body += '<br>'
                body += '''Adres rejestrowy: {}'''.format(
                    klient.rej)
            if klient.kor_var:
                body += '<br>'
                body += 'Adres korespondencyjny: {}'.format(
                    klient.kor)
            if klient.dost_var:
                body += '<br>'
                body += 'Adres dostarczenia: {}'.format(
                    klient.dost)

        body += '<br>'
        body += 'Branża: {}'.format(klient.branza)
        body += '<br>'
        body += 'Pytania do prawnika: {}'.format(klient.pytania)
        body += '<br>'
        body += 'Dodatkowe informacje: {}</p>'.format(klient.dodatkowe)
        body += '<br>'
        body += stworz_stopke()
    return(body)
