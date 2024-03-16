'''
Cybersecurity Projects with Python Programming Language 
'''
#Project 1: Hashing Passwords
import hashlib
def hash_password(password):
    hashed_password=hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

#Case Study
password="clinicalscience"
result=hash_password(password)
#print("The result of the hashed password is : ",result)


#Project 2: Generating Random Passwords 
import random 
import string 

def generate_random_password(length=40):
    characters=string.ascii_letters +string.digits + string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password

#Case Study
random_password=generate_random_password()
#print("The Random passwords are : ",random_password)


"""
#Project 3: 
#Network scanning with scapy 
from scapy.all import IP,ICMP,sr1
def ping(host):
    packet=IP(dst=host)/ICMP()
    response=sr1(packet,timeout=2,verbose=0)
    if response:
        return f"{host} is online"
    else:
        return f"{host} is offline"

#Case Study 
host_to_scan="hashnode.com"
result=ping(host_to_scan)
print(result)

#Project 4 : Web scraping for security research
import requests
from bs4 import BeautifulSoup

def scrape_security_news():
    url="https://example-security-news.com"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.pasrser')
    headlines=soup.find_all('h2',class_='security-headline')
    return [headline.text for headline in headlines]

#Case study
security_headlines=scrape_security_news()
print("Security headlines: ",security_headlines)

"""


#Project 5 : Password hacking simulation 
import hashlib

def simulate_password_cracking(hashed_password,password_list):
    for password in password_list:
        if hashlib.sha256(password.encode()).hexdigest()==hashed_password:
            return f" Password cracked: {password}"
        return "Password not found"
#Case Study
hashed_password_to_crack="7430e4a696bc440107d86aa7c7548fc163ecda2553cd958235eebbf145bcaf09"
common_passwords=["password","clinicalscience","koladeanthony","admin","qwertyuiop"]
result=simulate_password_cracking(hashed_password_to_crack,common_passwords)
#print(result)

"""
#Project 6: Secure Patient File handling
import os
def secure_file_deletion(file_path):
    with open(file_path,'w') as file:
        file.write(os.urandom(1024))
        #overwrite the file with
        #random data and delete.
    os.remove(file_path)
    print(f"{file_path} securely deleted")
    
#Case study
file_path_to_delete="cancer_patient.txt"
secure_file_deletion(file_path_to_delete)
    

"""

"""
#Project 7 : Port Scanner 
import socket

def portscan(ip):
    print(f"\n Starting a scan on {ip}... ")
    openPorts=0 #1024
    for port in range(1,1024):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.1)
        try:
            result=s.connect_ex((ip,port))
            if result==0:
                print(f"Port: {port} ")
                openPorts +=1
        except socket.error:
            print("Ooops, encountered some errors!!!")
        
        finally:
            s.close()

portscan("127.0.0.1")


#Project 8 : Check internet speed
>pipenv install speedtest-cli
import speedtest

s=speedtest.Speedtest()
print("Testing... \n")
downloadSpeed=s.download()/1048576
uploadSpeed=s.upload()/1048576
pingResult=round(s.results.ping)

print(f"Download speed: {downloadSpeed:.2f} Mbps")
print(f"Uploading speed: {uploadSpeed:.2f} Mbps")
print(f"Ping: {pingResult} ms")


    

#Project 9: simple Maths game 
import random
for i in range(10): #How many questions 
    num1,num2=random.randint(1,100),random.randint(1,100)
    answer=num1 +num2
    question=int(input(f"What is: \n\n{num1} + {num2} ?\n"))
    if question==answer:
        print("Correct !")
    else:
        print('Ooops,Incorrect!!!')
        
"""
        
#Project 10 : Password Generator 
abc='abcdefghijklmnopqrstuvwxyz'
extras='0123456789#_!*&$%@>.'
new_password='' #empty string
for i in range(16): #Password length
    x=random.randint(1,2)
    if x==1:
        new_password+=abc[random.randint(0,25)]
    else:
        new_password+=extras[random.randint(0,20)]
print(new_password)