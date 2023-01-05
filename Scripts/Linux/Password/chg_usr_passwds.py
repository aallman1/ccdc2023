import os
import random
import string
import subprocess

usr_accts, usr_up_prs, ref = [], [], ["bash", "sh", "zsh"]

#Get user accts
with open("/etc/passwd") as uLog:
    usrs = uLog.readlines()
    for usr in usrs:
        if any(r in usr for r in ref):
            usr_accts.append(usr.rstrip().split(":")[0])
            
#Set new passwords, save to txt (should accomodate text file, move it off machine, then delete somewhere)
with open("usr_pw_prs.txt", "w") as pLog:           
    for usr in usr_accts:
        pr = (usr, ''.join((random.choices(string.ascii_lowercase, k=9))))
        os.system(f'echo "{pr[0]}:{pr[1]}" | sudo chpasswd')
        pLog.write(str(pr) + "\n")


    
