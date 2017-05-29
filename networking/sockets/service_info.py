import socket
from urlparse import urlparse

for url in ['http://www.python.org',
            'https://www.facebook.com',
            'ftp://prep.ai.mit.edu',
            'smtp://mail.example.com',
            'imap://mail.example.com',
            'imaps://mail.example.com',
            'https://www.google.com']:

    parsed_url = urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)
    print '%6s : %s' % (parsed_url.scheme, port)
