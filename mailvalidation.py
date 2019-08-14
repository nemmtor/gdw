import smtplib
import dns.resolver
# PROXY?


def validate_mail(mail):
    # domena
    domain = str(mail.split('@')[1])
    # print(f'Domena: {domain}')

    # Sprawdzenie servera MX
    records = dns.resolver.query(domain, 'MX')
    mx = str(records[0].exchange)

    # smtplib setup
    server = smtplib.SMTP('smtp.gpgoldwin.pl:587')
    server.starttls()
    server.set_debuglevel(2)

    # smtp conversation
    server.connect(mx)
    # print(server.hostname)
    server.helo('KACPER')
    server.mail('kacper.witas@gpgoldwin.pl')
    code, message = server.rcpt(str(mail))
    server.quit()
    print(code)

    if code != 550:
        print("Mail istnieje!")
    else:
        print("Nie istnieje")


while True:
    mail = input()
    try:
        validate_mail(mail)
    except smtplib.SMTPServerDisconnected:
        print('Coś nie tak')
