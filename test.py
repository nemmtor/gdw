# -*- coding: utf-8 -*-
import imaplib
imap = imaplib.IMAP4('imap.gpgoldwin.pl')
imap.starttls()
imap.login('sebastian.mojcner@gpgoldwin.pl', 'goldwin1234')
print(imap.list())
