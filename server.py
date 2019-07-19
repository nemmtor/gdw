import smtplib


class Server():
    def __init__(self):
        self.smtp = smtplib.SMTP('smtp.gpgoldwin.pl:587')
        self.smtp.starttls()

    def sprawdz_haslo(self, login, password):
        self.login = login
        self.password = password
        try:
            self.smtp.login(self.login, self.password)
            return True
        except smtplib.SMTPAuthenticationError:
            print("Błędny login.")
            return False

    def quit(self):
        self.smtp.quit()
