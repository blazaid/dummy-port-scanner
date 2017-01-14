import argparse
import socket


def scan(host):
    print('Iniciando escaneo de puertos en {}'.format(host))
    host_ip = socket.gethostbyname(host)

    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(.2)
        if sock.connect_ex((host_ip, port)) == 0:
            print('Puerto:\t{} OK'.format(port))
        sock.close()

    print('Escaneo finalizado')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Escanea los puertos del host indicado.'
    )
    parser.add_argument('host', help='El host a escanear.')
    args = parser.parse_args()

    scan(args.host)
