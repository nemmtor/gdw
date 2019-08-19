import smtplib
import dns.resolver


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
    server.set_debuglevel(0)

    # smtp conversation
    server.connect(mx)
    # print(server.hostname)
    server.helo('KACPER')
    server.mail('witas.kacper11@gmail.com')
    code, message = server.rcpt(str(mail))
    server.quit()
    print(code)

    if code != 550:
        print("Mail istnieje!")
    else:
        print("Mail nie istnieje")


while True:
    mail = input("Podaj maila do sprawdzenia: ").strip()
    try:
        validate_mail(mail)
    except smtplib.SMTPServerDisconnected:
        print('Coś nie tak')
