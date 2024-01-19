import os
import time

with open('Pratica1/host.txt') as file:
    dump = file.read()

    print(dump)

## Colocaremos um for para percorrer o arquivo:
    dump = dump.splitlines()

    for ip in dump:
        print(ip)

    for ip in dump:
        os.system('ping -n 6{}'.format(ip))

## Adicionando um tempo de espera entre os pings
        
        time.sleep(5)