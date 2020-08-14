import colorama
from colorama import *
import socket
import sys
import os
import time
import requests
from datetime import datetime
init()
def portscan_en():
    os.system("cls || clear")
    ip = input("Give me a server: ")
    asking = input("Give me a port range (example: 1-25565): ")
    file_ask = input("Give a name + extention to create a file with the results: ")
    if file_ask == "subdomain-bruteforce.txt":
        print("You can't replace the subdomain bruteforce list!")
        pass
    portsplit = asking.split('-')
    port1 = int(portsplit[0])
    port2 = int(portsplit[1])
    port2 = port2 + 1
    if not os.path.exists("scans"):
        os.makedirs("scans")
        f = open("scans/" + file_ask, 'w+')
        f.write("Scan started at " + str(datetime.now()) + "\nServer: " + ip + "\n\n")
        f.close()
    else:
        f = open("scans/" + file_ask, 'w+')
        f.write("Scan started at " + str(datetime.now()) + "\nServer: " + ip + "\n\n")
        f.close()
    try:
        for port in range(port1, port2):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(Fore.WHITE + "Port " + Fore.GREEN + str(port) + Fore.WHITE + " is open!")
                f = open("scans/" + file_ask, 'a')
                f.write("Port " + str(port) + " is open!\n")
                f.close()
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved!")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

def portscan_es():
    os.system("cls || clear")
    ip = input("Dame un servidor: ")
    asking = input("Dame un rango de puerto (ejemplo: 1-25565): ")
    file_ask = input("Dame un nombre + extension para crear un archivo con los resultados: ")
    if file_ask == "subdomain-bruteforce.txt":
        print("No puedes reemplazar la lista de subdominios para la fuerza bruta!")
        sys.exit()
    portsplit = asking.split('-')
    port1 = int(portsplit[0])
    port2 = int(portsplit[1])
    port2 = port2 + 1
    if (not os.path.exists("scans")):
        os.makedirs("scans")
        f = open("scans/" + file_ask, 'w+')
        f.write("El scan empezo el " + str(datetime.now()) + "\nServidor: " + ip + "\n\n")
        f.close()
    else:
        f = open("scans/" + file_ask, 'w+')
        f.write("El scan empezo el " + str(datetime.now()) + "\nServidor: " + ip + "\n\n")
        f.close()
    try:
        for port in range(port1, port2):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(Fore.WHITE + "El puerto " + Fore.GREEN + str(port) + Fore.WHITE + " esta abierto!")
                f = open("scans/" + file_ask, 'a')
                f.write("El puerto " + str(port) + " esta abierto!\n")
                f.close()
            sock.close()
    except KeyboardInterrupt:
        print("Has presionado Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("El servidor no puede ser resuelto!")
        sys.exit()

    except socket.error:
        print("No consegui conectarme al servidor deseado")
        sys.exit()

def portscan_fr():
    os.system("cls || clear")
    ip = input("Donne moi un serveur: ")
    asking = input("Donne moi un rang de port (exemple: 1-25565): ")
    file_ask = input("Donne moi un nom + extention pour creer un fichier avec les resultats: ")
    if file_ask == "subdomain-bruteforce.txt":
        print("Tu ne peux pas remplacer la liste de sous domaines pour la force brute!")
        pass
    portsplit = asking.split('-')
    port1 = int(portsplit[0])
    port2 = int(portsplit[1])
    port2 = port2 + 1
    if not os.path.exists("scans"):
        os.makedirs("scans")
        f = open("scans/" + file_ask, 'w+')
        f.write("Le scan a commence a " + str(datetime.now()) + "\nServeur: " + ip + "\n\n")
        f.close()
    else:
        f = open("scans/" + file_ask, 'w+')
        f.write("Le scan a commence a " + str(datetime.now()) + "\nServeur: " + ip + "\n\n")
        f.close()
    try:
        for port in range(port1, port2):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(Fore.WHITE + "Le port " + Fore.GREEN + str(port) + Fore.WHITE + " est ouvert!")
                f = open("scans/" + file_ask, 'a')
                f.write("Le port " + str(port) + " est ouvert!\n")
                f.close()
            sock.close()
    except KeyboardInterrupt:
        print("Tu as appuye sur Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("Le serveur n'as pas pu etre resolu!")
        sys.exit()

    except socket.error:
        print("Je n'ai pas reussi a me connecter au serveur")
        sys.exit()

def subdomain_en():
    domain = input("Domain: ")
    save = input("Save file: ")
    save_file = open(save)
    save_file.write("Subdomain bruteforce started at " + datetime.now() + "\nTarget: " + domain + "\n\n")
    save_file.close()
    f = open("subdomain-bruteforce.txt")
    content = f.read()
    subdomains = content.splitlines()

    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("Discovered subdomain:", url)
            save_file = open(save, 'a')
            save_file.write("Discovered subdomain: " + url + "\n")

def subdomain_es():
    domain = input("Dominio: ")
    save = input("Archivo guardado: ")
    save_file = open(save)
    save_file.write("Fuerza bruta a subdominio ha empezado el " + datetime.now() + "\nObjetivo: " + domain + "\n\n")
    save_file.close()
    f = open("subdomain-bruteforce.txt")
    content = f.read()
    subdomains = content.splitlines()

    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("Subdominio descubierto:", url)
            save_file = open(save, 'a')
            save_file.write("Subdominio descubierto: " + url + "\n")

def subdomain_fr():
    domain = input("Domaine: ")
    save = input("Fichier enregistré: ")
    save_file = open(save)
    save_file.write("Le force brute de sous domaines a commencé le " + datetime.now() + "\nObjectif: " + domain + "\n\n")
    save_file.close()
    f = open("subdomain-bruteforce.txt")
    content = f.read()
    subdomains = content.splitlines()

    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("Sous domaine découvert:", url)
            save_file = open(save, 'a')
            save_file.write("Sous domaine découvert: " + url + "\n")

def change_lang():
    os.system("cls || clear")
    print("1) Español")
    print("2) English")
    print("3) Français")
    ask = int(input("Opcion: "))
    spanish = "LANG=ES"
    english = "LANG=EN"
    french = "LANG=FR"
    if ask == 1:
        f = open("config.yml", 'w+')
        f.write(spanish)
        f.close()
        print("El idioma ha sido cambiado a español")
    elif ask == 2:
        f = open("config.yml", 'w+')
        f.write(english)
        f.close()
        print("The language has been changed to english")
    elif ask == 3:
        f = open("config.yml", 'w+')
        f.write(french)
        f.close()
        print("La langue a été changée en français")
    else:
        print(Fore.CYAN + "Error: " + Fore.RED + "please provide a valid option!")
        time.sleep(3)
        sys.exit()

def getIP_es():
    try:
        os.system("cls || clear")
        domain = input("Dominio: ")
        ip = socket.gethostbyname(domain)
        print("La direccion ip de " + domain + " es " + ip)
    except:
        print("Hubo un error de conexion hacia el dominio " + domain)

def getIP_en():
    try:
        os.system("cls || clear")
        domain = input("Domain: ")
        ip = socket.gethostbyname(domain)
        print("The ip address of " + domain + " is " + ip)
    except:
        print("There was a connection error to the " + domain + " domain")

def getIP_fr():
    try:
        os.system("cls || clear")
        domain = input("Domaine: ")
        ip = socket.gethostbyname(domain)
        print("L'addresse ip de " + domain + " est " + ip)
    except:
        print("Il y a eu un probleme de connection avec le domaine " + domain)

def getHost_es():
    try:
        os.system("cls || clear")
        ip = input("IP: ")
        host = socket.gethostbyaddr(ip)
        print("La ip " + ip + " redirecciona al host " + host[0])
    except:
        print("Hubo un error de conexion hacia la ip " + ip)

def getHost_en():
    try:
        os.system("cls || clear")
        ip = input("IP: ")
        host = socket.gethostbyaddr(ip)
        print("The ip address " + ip + " redirect to the host " + host[0])
    except:
        print("There was a connection error with the ip address " + ip)

def getHost_fr():
    try:
        os.system("cls || clear")
        ip = input("IP: ")
        host = socket.gethostbyaddr(ip)
        print("L'addresse ip " + ip + " est connecte au host " + host[0])
    except:
        print("Hubo un error de conexion hacia la ip " + ip)

def grief_main_es():
    print("1) Anunciar/spamear mensajes")
    print("2) Remover bloques / crear esferas de lava")
    print("3) Encontrar un staff")
    print("4) Salir")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        grief_broadcast_es()
    elif opcion == 2:
        rmBlock_es()
    elif opcion == 3:
        findStaff_es()
    elif opcion == 4():
        sys.exit()
    else:
        print(Fore.CYAN + "Error: " + Fore.RED + "Por favor selecciona una opcion valida")
def grief_broadcast_es():
    print("1) Usan essentials")
    print("2) No usan essentials")
    essentials_check = int(input("Opcion: "))
    if essentials_check == 1:
        bc = input("Pon el mensaje que quieras que aparezca: ")
        cmd = "/pt bc " + bc
        os.system("cls || clear")
        print("Coge un item y ejecuta el siguiente comando: " + cmd)
    elif essentials_check == 2:
        bc = input("Pon el mensaje que quieras que aparezca: ")
        cmd = "/minecraft:say " + bc
        print("Ejecuta este comando todas las veces que quieras para hacer el anuncio: " + cmd)
    else:
        print(Fore.CYAN + "Error: " + Fore.RED + "Por favor selecciona una opcion valida")

def rmBlock_es():
    print("1) Usan WorldEdit")
    print("2) No usan WorldEdit")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        print("1) Destruir bloques")
        print("2) Invocar esferas de lava")
        opcion1 = int(input("Opcion: "))
        if opcion1 == 1:
            print("1) Radio de 5 bloques")
            print("2) Radio superior a 5 bloques")
            opcion11 == int(input("Opcion: "))
            if opcion11 == 1:
                print("Saca un pico y ejecuta este comando: /sp area 5")
            elif opcion11 == 2:
                print("1) Usan essentials")
                print("2) No usan essentials")
                opcion111 = int(input("Opcion: "))
                if opcion111 == 1:
                    radio == int(input("Dame un rango: "))
                    cmd = "/pt /sphere 0 " + radio
                    print("Coge cualquier item y ejecuta el siguiente comando: " + cmd)
                elif opcion111 == 2:
                    radio == int(input("Dame un rango: "))
                    cmd = "//sphere 0 " + radio
                    print("Ejecuta el siguiente comando: " + cmd)
                else:
                    print(Fore.CYAN + "Error: " + Fore.RED + "Por favor selecciona una opcion valida")
            else:
                print(Fore.CYAN + "Error: " + Fore.RED + "Por favor selecciona una opcion valida")
    elif opcion == 2:
        print("1) Usan essentials")
        print("2) No usan essentials")
        opcion111 = int(input("Opcion: "))
        if opcion111 == 1:
            radio == int(input("Dame un rango: "))
            cmd = "/pt /sphere minecraft:lava " + radio
            print("Coge cualquier item y ejecuta el siguiente comando: " + cmd)
        elif opcion111 == 2:
            radio == int(input("Dame un rango: "))
            cmd = "//sphere minecraft:lava " + radio
            print("Ejecuta el siguiente comando: " + cmd)
        else:
            print(Fore.CYAN + "Error: " + Fore.RED + "Por favor selecciona una opcion valida")

    else:
        print(Fore.CYAN + "Error: " + Fore.RED + "Por favor selecciona una opcion valida")

def findStaff_es():
    print("Comandos:")
    print("1) /baltop")
    print("2) /staff")
    print("3) /staffs")
    print("4) Busca el nombre del servidor (hasta que encuentres una red social, un foro, una tienda, etc)")
    print("5) /buy")
    print("6) /foro")
    print("7) /forum")



def grief_main_en():
    print("1) Announce/spam messages")
    print("2) Remove blocks / create lava spheres")
    print("3) Find staff")
    print("4) Exit")
    opcion = int(input("Option: "))
    if opcion == 1:
        grief_broadcast_en()
    elif opcion == 2:
        rmBlock_en()
    elif opcion == 3:
        findStaff_en()
    elif opcion == 4:
        sys.exit()
    else:
        print(Fore.CYAN + "Error: " + Fore.RED + "Please select a valid option")
def grief_broadcast_en():
    print("1) They use essentials")
    print("2) They don't use essentials")
    essentials_check = int(input("Option: "))
    if essentials_check == 1:
        bc = input("Provide the message you want to appear: ")
        cmd = "/pt bc " + bc
        os.system("cls || clear")
        print("Pick an item and execute the following command: " + cmd)
    elif essentials_check == 2:
        bc = input("Provide the message you want to appear: ")
        cmd = "/minecraft:say " + bc
        print("Execute this command all the times you want to make the announce: " + cmd)
    else:
        print(Fore.CYAN + "Error: " + Fore.RED + "Please select a valid option")

def rmBlock_en():
    print("1) They use WorldEdit")
    print("2) They don't use WorldEdit")
    opcion = int(input("Option: "))
    if opcion == 1:
        print("1) Destroy blocks")
        print("2) Spawn lava spheres")
        opcion1 = int(input("Option: "))
        if opcion1 == 1:
            print("1) 5 blocks radio")
            print("2) More than 5 blocks radio")
            opcion11 == int(input("Option: "))
            if opcion11 == 1:
                print("Pick a pickaxe and execute this command: /sp area 5")
            elif opcion11 == 2:
                print("1) They use essentials")
                print("2) They don't use essentials")
                opcion111 = int(input("Option: "))
                if opcion111 == 1:
                    radio == int(input("Give me a range: "))
                    cmd = "/pt /sphere 0 " + radio
                    print("Pick whatever item and execute the following command: " + cmd)
                elif opcion111 == 2:
                    radio == int(input("Give me a range: "))
                    cmd = "//sphere 0 " + radio
                    print("Execute the following command: " + cmd)
                else:
                    print(Fore.CYAN + "Error: " + Fore.RED + "Please select a valid option")
            else:
                print(Fore.CYAN + "Error: " + Fore.RED + "Please select a valid option")
    elif opcion == 2:
        print("1) They use essentials")
        print("2) They don't use essentials")
        opcion111 = int(input("Option: "))
        if opcion111 == 1:
            radio == int(input("Give me a range: "))
            cmd = "/pt /sphere minecraft:lava " + radio
            print("Pick whatever item and execute the following command: " + cmd)
        elif opcion111 == 2:
            radio == int(input("Give me a range: "))
            cmd = "//sphere minecraft:lava " + radio
            print("Execute the following command: " + cmd)
        else:
            print(Fore.CYAN + "Error: " + Fore.RED + "Please select a valid option")

    else:
        print(Fore.CYAN + "Error: " + Fore.RED + "Please select a valid option")

def findStaff_en():
    print("Commands:")
    print("1) /baltop")
    print("2) /staff")
    print("3) /staffs")
    print("4) Search the server's name (until you find a social media, a forum, a shop, etc)")
    print("5) /buy")
    print("6) /foro")
    print("7) /forum")


def grief_main_fr():
    print("1) Annoncer/spammer des messages")
    print("2) Detruire des blocks / creer des spheres de lave")
    print("3) Trouver des staff")
    print("4) Sortir")
    opcion = int(input("Option: "))
    if opcion == 1:
        grief_broadcast_en()
    elif opcion == 2:
        rmBlock_en()
    elif opcion == 3:
        findStaff_en()
    elif opcion == 4:
        sys.exit()
    else:
        print(Fore.CYAN + "Erreur: " + Fore.RED + "S'il te plait choisis un option valide")
def grief_broadcast_fr():
    print("1) Ils utilisent essentials")
    print("2) Ils n'utilisent pas essentials")
    essentials_check = int(input("Option: "))
    if essentials_check == 1:
        bc = input("Donne le message que tu veut qui apparaisse: ")
        cmd = "/pt bc " + bc
        os.system("cls || clear")
        print("Prend un item puis execute cette commande: " + cmd)
    elif essentials_check == 2:
        bc = input("Donne le message que tu veut qui apparaisse: ")
        cmd = "/minecraft:say " + bc
        print("Execute cette commande toutes les fois que tu veut pour faire les annonces: " + cmd)
    else:
        print(Fore.CYAN + "Erreur: " + Fore.RED + "S'il te plait choisis un option valide")

def rmBlock_fr():
    print("1) Ils utilisent WorldEdit")
    print("2) Ils n'utilisent pas WorldEdit")
    opcion = int(input("Option: "))
    if opcion == 1:
        print("1) Detruire des blocks")
        print("2) Spawner des spheres de lave")
        opcion1 = int(input("Option: "))
        if opcion1 == 1:
            print("1) Un rang de 5 blocks")
            print("2) Un rang superieur a 5 blocks")
            opcion11 == int(input("Option: "))
            if opcion11 == 1:
                print("Prend une pioche puis execute cette commande: /sp area 5")
            elif opcion11 == 2:
                print("1) Ils utilisent essentials")
                print("2) Ils n'utilisent pas essentials")
                opcion111 = int(input("Option: "))
                if opcion111 == 1:
                    radio == int(input("Donne moi un rang: "))
                    cmd = "/pt /sphere 0 " + radio
                    print("Prend n'importe quel item puis execute cette commande: " + cmd)
                elif opcion111 == 2:
                    radio == int(input("Donne moi un rang: "))
                    cmd = "//sphere 0 " + radio
                    print("Execute cette commande: " + cmd)
                else:
                    print(Fore.CYAN + "Erreur: " + Fore.RED + "S'il te plait choisis un option valide")
            else:
                print(Fore.CYAN + "Erreur: " + Fore.RED + "S'il te plait choisis un option valide")
    elif opcion == 2:
        print("1) Ils utilisent essentials")
        print("2) Ils n'utilisent pas essentials")
        opcion111 = int(input("Option: "))
        if opcion111 == 1:
            radio == int(input("Donne moi un rang: "))
            cmd = "/pt /sphere minecraft:lava " + radio
            print("Prend n'importe quel item puis execute cette commande: " + cmd)
        elif opcion111 == 2:
            radio == int(input("Donne moi un rang: "))
            cmd = "//sphere minecraft:lava " + radio
            print("Execute cette commande: " + cmd)
        else:
            print(Fore.CYAN + "Erreur: " + Fore.RED + "S'il te plait choisis un option valide")

    else:
        print(Fore.CYAN + "Erreur: " + Fore.RED + "S'il te plait choisis un option valide")

def findStaff_fr():
    print("Commandes:")
    print("1) /baltop")
    print("2) /staff")
    print("3) /staffs")
    print("4) Recherche le nom du serveur (jusqu'a trouver un reseau social, un forum, un shop, etc)")
    print("5) /buy")
    print("6) /foro")
    print("7) /forum")
