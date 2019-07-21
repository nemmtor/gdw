import smtplib


class Server():
    def __init__(self):
        '''Tworzy połaczenie smtp.'''
        self.smtp = smtplib.SMTP('smtp.gpgoldwin.pl:587')
        self.smtp.starttls()

    def sprawdz_haslo(self, login, password):
        '''Sprawdza czy login/hasło są prawidłowe.'''
        self.login = login
        self.password = password
        try:
            self.smtp.login(self.login, self.password)
            return True
        except (smtplib.SMTPAuthenticationError,
                TypeError):
            return False

    def quit(self):
        self.smtp.quit()
