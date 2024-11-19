import os   # IMPORTAMOS BIBLIOTECA OS PARA UTILIZARLA COMO HERRAMIENTA A LA HORA DE LIMPIAR PANTALLA 
import getpass #IMPORTAMOS BIBLIOTECA GETPASS PARA OCULTAR LOS CARACTERES A LA HORA DE INGRESAR LA CONTRASEÑA 

contadorComida = 0      #declaracion de variables globales 
contadorIndumentaria= 0
contadorPerfumeria =0
tipoUS = 'a definir'

def limpiar():    #procedimiento limpiar 
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def programainicio():  # validacion de usuario y contraseña (inicio de sesion)
	nombreUsuario = 'E' 
	claveUsuario ='1'
	contadorintentos = 1

	usuario= input('ingrese usuario: ')
	contraseña = getpass.getpass("ingrese contraseña: ")
	if nombreUsuario == usuario and claveUsuario==contraseña: 
		global tipoUS
		tipoUS = 'Administrador'
		principal()
	else:
		while contadorintentos<3:
			if usuario != nombreUsuario or claveUsuario != contraseña:
				contadorintentos=contadorintentos+1
				print(contadorintentos)
				usuario= input('ingrese usuario: ')
				contraseña = getpass.getpass("ingrese contraseña: ")
				if usuario == nombreUsuario and claveUsuario == contraseña:
					tipoUS = 'Administrador'
					contadorintentos = 0
					principal()
	if contadorintentos >= 3:
		print('NUMERO MAXIMO DE INTENTOS PERMITIDO, INTENTE MAS TARDE')	

def menuprincipal():   #INTERFACE GRAFICA DE MENU PRINCIPAL 
	limpiar()
	print('*** MENU PRINCIPAL ***')
	print('tipo de usuario' ,tipoUS )
	print('1-GESTION DE LOCALES')
	print('2-CREAR CUENTAS DE DUEÑOS DE LOCALES')
	print('3-APROBAR /DENEGAR SOLICITUD DE DESCUENTO')
	print('4-GESTION DE NOVEDADES')
	print('5-REPORTE DE UTILIZACION DE DESCUENTOS')
	print('0-SALIR')


def principal():
	opc= 1 
	while opc != '0':
		menuprincipal()
		opc= input('ingrese una opcion: ')
		if opc == '1':
			gestiondelocales()
		elif opc== '2':
			encontrstuccion()
		elif opc== '3':
			encontrstuccion()
		elif opc== '4':
			gestiondenovedades()
		elif opc== '5':
			encontrstuccion()
		else:
			if opc != '0':
				limpiar()
				print('la opcion ingresada no es valida')

def gestiondelocales(): 
	opc= 'A'
	while opc != 'D':
		limpiar()
		print('*** GESTION DE LOCALES ***')
		print('A- CREAR LOCALES')
		print('B- MODIFICAR LOCAL')
		print('C- ELIMINAR LOCAL')
		print('D- VOLVER')
		opc = input('ingrese una opcion: ').upper()
		if opc== 'A':
			crearlocales()
		elif opc == 'B':
			encontrstuccion()
		elif opc == 'C':
			encontrstuccion()
		else:
			if opc != 'D':
				print('esta opcion no es valida')


def crearlocales(): 
	opc2 = '1'
	opc= 'S'
	limpiar()
	print('*** CREAR LOCALES ***')
	while opc != 'N':
		opc= input('¿Desea crear un nuevo local S/N?').upper()
		if opc== 'S':
			limpiar()
			nombreLocal= str(input('ingrese nombre del local: '))
			ubicacionLocal=str(input('ingrese ubicacion del local: '))
			rubroLocal = str(input('ingrese el rubro del local: ')).lower()
			while rubroLocal != 'comida' and rubroLocal != 'indumentaria' and rubroLocal != 'perfumeria':
				rubroLocal= str(input('opcion incorrecta, intente nuevamente. Los rubros permitidos son: perfumeria, indumentaria o comida ')).lower()
			if rubroLocal == 'comida':
				global contadorComida
				contadorComida = contadorComida +1
				limpiar()
				print('el local', nombreLocal, 'fue cargado con exito')				
			elif rubroLocal == 'indumentaria':
				global contadorIndumentaria
				contadorIndumentaria = contadorIndumentaria+1
				limpiar()
				print('el local', nombreLocal, 'fue cargado con exito')
			elif rubroLocal == 'perfumeria':
				global contadorPerfumeria
				contadorPerfumeria= contadorPerfumeria+1
				limpiar()
				print('el local', nombreLocal, 'fue cargado con exito')
		else:
			if opc != 'N':
				limpiar()
				print('opcion incorrecta')
	while opc2 != '0':
		limpiar()
		if contadorComida == 0 and contadorIndumentaria == 0 and contadorPerfumeria == 0: #CUANDO NO SE INGRESA NINGUN LOCAL (POR SI SE ENTRA EN EL SUB MENU POR ACCIDENTE)
			print('no hay locales cargados')
			opc2 = input('ingrese 0 para volver')   
		else:
			limpiar()
			if contadorComida != 0 and contadorComida == contadorIndumentaria and contadorComida == contadorPerfumeria:  #PROCEDIMIENTOS IDENTIFICAR EL RUBRO CON MAYOR CANTIDAD DE LOCALES CARGADOS 
				print('todos los rubros tienen ', contadorComida, ' local/es cargados')
			if contadorComida > contadorIndumentaria and contadorComida> contadorPerfumeria:
				print('el rubro con mas locales es el de comida, con:', contadorComida, 'local/es cargados')
			elif contadorIndumentaria > contadorComida and contadorIndumentaria>contadorPerfumeria:
				print('el rubro con mas locales es el de indumentaria, con:', contadorIndumentaria, 'local/es cargados')
			elif contadorPerfumeria > contadorComida and contadorPerfumeria > contadorIndumentaria:
				print('el rubro con mas locales es el de perfumeria, con:', contadorPerfumeria,  'local/es cargados')      

			if contadorComida == contadorIndumentaria and contadorComida > contadorPerfumeria:   #PROCEDIMIENTOS PARA IDENTIFICAR RUBROS CON LA MISMA CANTIDAD DE LOCALES CARGADOS (MAYORES)
				print('los rubros con mas locales son comida con:', contadorComida, 'local/es cargados e indumentaria con: ', contadorIndumentaria, ' local/es cargados')
			elif contadorIndumentaria == contadorPerfumeria and contadorIndumentaria > contadorComida:
				print('los rubros con mas locales son perfumeria con:', contadorPerfumeria	, 'local/es cargados e indumentaria con: ', contadorIndumentaria, ' local/es cargados')
			elif contadorPerfumeria == contadorComida and contadorPerfumeria > contadorIndumentaria:
				print('los rubros con mas locales son perfumeria con:', contadorPerfumeria	, 'local/es cargados y comida con: ', contadorComida	, ' local/es cargados')


			if contadorComida == contadorIndumentaria and contadorComida < contadorPerfumeria: #PROCEDIMIENTOS PARA IDENTIFICAR RUBROS CON LA MISMA CANTIDAD DE LOCALES CARGADOS (MENORES)
				print('los rubros con menos locales son comida con:', contadorComida, 'local/es cargados e indumentaria con: ', contadorIndumentaria, ' local/es cargados')
			elif contadorIndumentaria == contadorPerfumeria and contadorIndumentaria < contadorComida:
				print('los rubros con menos locales son perfumeria con:', contadorPerfumeria	, 'local/es cargados e indumentaria con: ', contadorIndumentaria, ' local/es cargados')
			elif contadorPerfumeria == contadorComida and contadorPerfumeria < contadorIndumentaria:
				print('los rubros con menos locales son perfumeria con:', contadorPerfumeria	, 'local/es cargados y comida con: ', contadorComida	, ' local/es cargados')


			if contadorComida < contadorIndumentaria and contadorComida < contadorPerfumeria: #PROCEDIMIENTOS PARA INDENTIFICAR EL RUBRO CON MENOR CANTIDAD DE LOCALES CARGADOS 
				print('el rubro con menos locales es el de comida, con:', contadorComida, 'local/es cargados')
			elif contadorIndumentaria < contadorComida and contadorIndumentaria<contadorPerfumeria:
				print('el rubro con menos locales es el de indumentaria, con:', contadorIndumentaria, 'local/es cargados')
			elif contadorPerfumeria < contadorComida and contadorPerfumeria < contadorIndumentaria:
				print('el rubro con menos locales es el de perfumeria, con:', contadorPerfumeria,  'local/es cargados')

			opc2= input('ingrese 0 para volver')
	while opc2 != '0':
		opc2= input('ingrese 0 para volver')

def gestiondenovedades(): 
	opc= 'A'
	while opc != 'E':
		limpiar()
		print('GESTION DE NOVEDADES')
		print('A- CREAR NOVEDADES')
		print('B- MODIFICAR NOVEDAD')
		print('C- ELIMINAR NOVEDAD')
		print('D- VER REPORTE DE NOVEDADES')
		print('E- VOLVER')
		opc = input('ingrese una opcion').upper()
		if opc== 'A':
			encontrstuccion()
		elif opc == 'B':
			encontrstuccion()
		elif opc == 'C':
			encontrstuccion()
		elif opc== 'D':
			encontrstuccion()
		else:
			if opc != 'E':
				print('esta opcion no es valida')


def encontrstuccion(): 

	opc= 1
	while opc!='0':
		limpiar()
		print('Esta seccion esta en construccion')
		opc= input('ingrese 0 para volver')

programainicio()

