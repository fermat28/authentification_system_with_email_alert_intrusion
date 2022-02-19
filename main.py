import getpass
import os
from datetime import datetime, date, timedelta
import re

current_date = date.today()
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
now1 = datetime.now()
start_time = now1.strftime("%H:%M:%S")
file = open('combolist.txt', 'a+')
combolist = open('combolist.txt').read().splitlines()

lock_time = "unlock_time"
for i in combolist:
    if lock_time in i :
        if datetime.strptime(i.split("- ")[1] , '%Y-%m-%d %H:%M:%S.%f')  >  now1:
            print("the program is locked try later")
            exit()
choice = input("login or register: ")

#login
if choice == 'login':
    def log(att = 0):
        print("Please enter a username/email and password")
        user = input("Username: ")
        passw = getpass.getpass("Password: ")
        combo = user + ':' + passw
        combo2 = "intrusion attempt for user"
        combo1 = "intrusion attempt for user,"+ user + " " + "at" + " "  + "Time:" + str(now1)
        time_change = timedelta(hours=24)
        addition = now1 + time_change
        unlock = "unlock_time - " + str(addition)
        if combo in combolist:
            print("Logged in with the username:", user)
            for i in combolist:
                if (combo2+":"+user) in i:
                    print(i)
            def crypt():    
                    while 1:
                        from hashlib import sha512
                        entree = input("enter the name of the file to encrypt / decrypt : ")
                        if os.path.exists("./"+entree) == False :
                            print("The file that you try to encrypt doesn't exists in current path")
                            crypt()
                        print("The file that you try to encrypt  exists in current path ")
                        sortie = input("enter the name of the file after encryption / decryption : ")
                        key = input("enter the encryption key : ")
                        keys = sha512(key.encode('utf-8')).digest()
                        with open(entree , "rb") as f_entree :
                                    with open(sortie , "wb") as f_sortie:
                                        i=0
                                        while f_entree.peek():
                                            c = ord(f_entree.read(1))
                                            j = i % len(keys)
                                            b = bytes([c^keys[j]])
                                            f_sortie.write(b)
                                            i = i+1
            crypt()                                
        else:
            if att==4:
                print("Too many attemps try later")
                f1 = open('combolist.txt', 'a+')
                f1.writable()
                f1.write(combo1 + "\n")
                f1.write(unlock  + "\n")
                f1.close()
                if(re.fullmatch(regex, user)):
                    from email.mime.text import MIMEText
                    import smtplib
                    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
                    smtp_ssl_port = 465
                    username = user
                    for i in combolist:
                        if user+":" in i:
                            passw = i.split(":")[1]
                            password = passw
                            sender = 'aimericpouga28@gmail.com'
                            targets = [i.split(":")[0]]
                            msg = MIMEText('There Was an intrusion Attempt on your account')
                            msg['Subject'] = 'Intrusion'
                            msg['From'] = sender
                            msg['To'] = ', '.join(targets)

                            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
                            server.login(username, password)
                            server.sendmail(sender, targets, msg.as_string())
                            server.quit()
                else:
                    exit()
                
            else : 
                print("Doesn't exist or wrong username and password")
                log(att+1)
    log()
      
 # register

if choice == 'register':
    username_valid = True
    print("Enter the desired username or email")
    wanted_user = input("Username: ")
    for combo in combolist:
      if wanted_user in combo:
        print("Username is taken! Make another!")
        username_valid = False
    if username_valid == True:
      wanted_pass = getpass.getpass("Password: ")
      wanted_passw = getpass.getpass("Confirm Password: ")
      if wanted_pass != wanted_passw:
        print("Passwords do not match")

      combo = wanted_user + ":" + wanted_pass

      f1 = open('combolist.txt', 'a+')
      f1.writable()
      f1.write(combo + "\n")
      f1.close()

      print("Successfully registered! Try and login.")

if choice != "login" or "register":
  print("Not an option")
