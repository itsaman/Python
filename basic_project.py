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
