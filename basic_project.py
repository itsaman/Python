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
