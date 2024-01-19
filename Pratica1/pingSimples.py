import os

print("#"*60)

ip_ou_host = input("Digite o ip ou host ")
os.system('ping -n 6 {}'.format(ip_ou_host))