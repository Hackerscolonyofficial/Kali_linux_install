from Writer import writer
from Hadings import Heading, Sub_head
from URLS import whatsapp, instagram, youtube
from os import system
from colorama import init
from time import sleep 

init()

system("clear")
Heading()
print("\n"*2)
writer("Welcome to our tool..".center(50,"_"))
print()
writer('''\033[31;1mFirst follow on Instagram and subscribe on YouTube.
Our tool has been locked!
The tool will be unlocked when you complete this command!

this Tool for install kali linux without root.
this tool only education purpose.'''. title())
print()
print()
writer("_"*100)
print("\n"*2)

sleep(4)
youtube()
sleep(3)
writer("\033[36;42;1mType ENTER for next step\033[0m")
input()
instagram()
writer("\033[31;42;1mType ENTER for next step\033[0m")
input()
whatsapp()
sleep(5)
system("clear")
Sub_head()
writer("\033[31;44;1m\t\tInstalling..... \033[32m")
system("bash install_kali.sh")
