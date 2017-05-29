import socket

for host in ['www.google.com', 'www.facebook.com', 'www.python.org']:
    print host
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print 'Hostname :', hostname
        print 'Aliases  :', aliases
        print 'Addresses:', addresses
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host, msg)


