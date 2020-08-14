#Zniper - Minecraft Grief Tool
#Made by Syntaxis
#Alias: BadL0v3r, Incognito, Bart0
import sys
import os
import time
import utils
import colorama
from colorama import *
os.system("cls || clear")
init()

def logo():
    print(Fore.GREEN + " /$$$$$$$$           /$$                                       " + Fore.RED + "/$$        /$$$$$$ " + Fore.WHITE)
    print(Fore.GREEN + "|_____ $$           |__/                                     " + Fore.RED + "/$$$$       /$$$_  $$" + Fore.WHITE)
    print(Fore.GREEN + "     /$$/  /$$$$$$$  /$$  /$$$$$$   /$$$$$$   /$$$$$$       " + Fore.RED + "|_  $$      | $$$$\ $$" + Fore.WHITE)
    print(Fore.GREEN + "    /$$/  | $$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$        " + Fore.RED + "| $$      | $$ $$ $$" + Fore.WHITE)
    print(Fore.GREEN + "   /$$/   | $$  \ $$| $$| $$  \ $$| $$$$$$$$| $$  \__/        " + Fore.RED + "| $$      | $$\ $$$$" + Fore.WHITE)
    print(Fore.GREEN + "  /$$/    | $$  | $$| $$| $$  | $$| $$_____/| $$              " + Fore.RED + "| $$      | $$ \ $$$" + Fore.WHITE)
    print(Fore.GREEN + " /$$$$$$$$| $$  | $$| $$| $$$$$$$/|  $$$$$$$| $$             " + Fore.RED + "/$$$$$$ /$$|  $$$$$$/" + Fore.WHITE)
    print(Fore.GREEN + "|________/|__/  |__/|__/| $$____/  \_______/|__/            " + Fore.RED + "|______/|__/ \______/ " + Fore.WHITE)
    print(Fore.GREEN + "                        | $$                                " + Fore.RED + "                      " + Fore.WHITE)
    print(Fore.GREEN + "                        | $$                                " + Fore.RED + "                      " + Fore.WHITE)
    print(Fore.GREEN + "                        |__/                                " + Fore.RED + "                      " + Fore.WHITE)
def spanish_Menu():
    try:
        os.system("cls || clear")
        logo()
        print("1) Obtener IP numerica")
        print("2) Obtener puertos de una IP")
        print("3) Obtener host")
        print("4) Herramientas de grief")
        print("5) Cambiar idioma")
        print("6) Salir")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            utils.getIP_es()
        elif opcion == 2:
            utils.portscan_es()
        elif opcion == 3:
            utils.getHost_es()
        elif opcion == 4:
            utils.grief_main_es()
        elif opcion == 5:
            utils.change_lang()
        elif opcion == 6:
            sys.exit()
    except:
        spanish_Menu()
def english_Menu():
    try:
        os.system("cls || clear")
        logo()
        print("1) Get numeric IP")
        print("2) Get IP's ports")
        print("3) Get subdomains")
        print("4) Change language")
        print("5) Exit")
        opcion = int(input("Opcion: "))
        if opcion == 2:
            utils.portscan_en()
        elif opcion == 3:
            utils.subdomain_en()
        elif opcion == 4:
            utils.change_lang()
    except:
        english_Menu()
def french_Menu():
    try:
        os.system("cls || clear")
        logo()
        print("1) Obtenir l'addresse IP")
        print("2) Obtenir les ports d'une addresse IP")
        print("3) Obtenir des sous domaines")
        print("4) Changer de langue")
        print("5) Sortir")
        opcion = int(input("Opcion: "))
        if opcion == 2:
            utils.portscan_fr()
        elif opcion == 3:
            utils.subdomain_fr()
        elif opcion == 4:
            utils.change_lang()
    except:
        french_Menu()
"""
Config por defecto
"""
def default_config():
    english_lang = "LANG=EN"
    f = open("config.yml", 'w+')
    f.write(english_lang)
    f.close()

"""
Crear la config si no existe
"""
def create_config():
    default_config()

if(not os.path.exists("config.yml")):
    create_config()
    os.system("python Zniper.py")
else:
    spanish = "LANG=ES"
    english = "LANG=EN"
    french = "LANG=FR"
    f = open("config.yml",'r')
    content = f.read()
    if(content != spanish and content != english and content != french):
        default_config()
    else:
        if content == spanish:
            spanish_Menu()
        if content == english:
            english_Menu()
        if content == french:
            french_Menu()
    f.close()
