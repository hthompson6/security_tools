import socket

def get_constants(prefix):
    return dict((getattr(socket, n), n)
                for n in dir(socket)
                if n.startswith(prefix)
                )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO')

for response in socket.getaddrinfo('www.python.org', 'http'):

    family, socktype, proto, canonname, sockaddr = response

    print 'Family        :', families[family]
    print 'Sock Type     :', types[socktype]
    print 'Protocol      :', protocols[proto]
    print 'Canonical name:', canonname
    print 'Address       :', sockaddr
