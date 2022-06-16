# download image, make it as a wallpaper and save it to a folder 
import urllib.request as ur
import ctypes

try:
    file_url = input("Provide file url")
    file_name = input("Provide file name")
    resource=ur.urlopen(file_url)
    output = open(r"C:\Users\anshi\Documents\Wallpapers\{}.jpg".format(file_name),"wb")
    output.write(resource.read())   
    output.close()

    file_path = "C:\\Users\\anshi\\Documents\\Wallpapers\\{}.jpg".format(file_name)

    decide = input("Want to see how it looks? Y/N")
    if decide == "Y" or decide == "y":
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path , 0)
    elif decide == "N" or decide == "n":
        print("Okay! wallpaper downloaded to your folder")
    else:
        print("Provide Y/N as an input")

except(ValueError):
    print("Wrong URL entered, provide correct url")

    
 
#EMAIL Validation

mail = input("Provide your email address")
k,j,l=0,0,0
if len(mail)>=6:
    if mail[0].isalpha():
        if mail.count("@") == 1 and "@" in mail:
            
            if (mail[-3] == ".") ^ (mail[-4] == "."):
                for i in mail:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j=1
                    elif i.isdigit:
                        continue        
                    elif i == "_" or i=="." or i=="@":
                        continue
                    else:
                        l = 1
                print("Correct Email")
                if k == 1 or j == 1 or l==1:
                    print("Wrong Email")
            else:
                print("Invalid Email, position of @ wrong")
        else:
            print("Invalid Email, @ issue")
    else:
        print ("Invalid Email, write Alpha first")
else:
    print("Invalid Email, length issue")
    
    
    
#Email validation using Regex

# a-z
# 0-9
# . _ comes only 1 time
# . this comes after 2nd or 3rd position

import re
email_cond = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# ?: it will check if .,_ are one or zero
# ^: check first character
# \w: this will search in the string
# [.]\w{2,3}: searching . in 2 and 3 position
# $: traversing from behind

user_email = input("Enter your email : ")

if re.search(email_cond, user_email):
    print("Right Email")
else:
    print("Wronge Email")

    
    
 #typing speed calculator

from time import *
import random as rd


def mistake(test, user):
    err = 0
    for i in range(len(test)):
            try: 
                if test[i] != user[i]:
                    err = err+1
            except:
                 err = err+1
    return err

def time_diff(user_s, user_e):
    time_diff = user_e - user_s
    time_r = round(time_diff,2)
    return time_r


def speed(user_s, user_e, user_inp):
    time_diff = user_e - user_s
    time_r = round(time_diff,2)
    speed = len(user_inp)/time_r
    return round(speed)


test = ["Greed is not good for you. Be content and satisfied to lead a happy and fulfilling life","When you work hard and persevere, you can achieve your goals. Slow and steady wins the race","Don’t play with people’s trust, when it matters the most, they won’t believe you"]

stat = rd.choice(test)

print("****Typing Master****")
print(stat)
print()
print()
time_1 = time()
user = input(" Enter: ")
print(user)
time_2 = time()

print()
print("Time taken:", time_diff(time_1,time_2))
print("Speed: ", speed(time_1,time_2,user),"w/sec" )
print("Errors: ", mistake(test, user))

