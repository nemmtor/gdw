import smtplib
import dns.resolver


def validate_mail(mail):
    # domena
    domain = str(mail.split('@')[1])
    # print(f'Domena: {domain}')

    # Sprawdzenie servera MX
    records = dns.resolver.query(domain, 'MX')
    mx = str(records[0].exchange)

    # smtp conversation
    server = smtplib.SMTP('smtp.gpgoldwin.pl:587')
    server.login('kacper.witas@gpgoldwin.pl','goldwin1234')
    server.connect(mx)
    server.set_debuglevel(2)
    server.helo('test')
    server.mail('kacper.witas@gpgoldwin.pl')
    code, message = server.rcpt(str(mail))
    server.quit()
    print(code)

    if code != 550:
        print("Mail istnieje!")
    else:
        print("Mail nie istnieje")


while True:
    mail = input("Podaj maila do sprawdzenia: ").strip()
    validate_mail(mail)
