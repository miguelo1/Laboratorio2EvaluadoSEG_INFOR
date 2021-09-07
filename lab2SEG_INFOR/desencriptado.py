#   Laboratorio Evaluado N°2
#   Integrantes: Ismael Solis y Miguel Orellana
#   Profesor: Manuel Alba
#   Asignatura: Seguridad Informática

import time


#Lectura de los archivos.txt
with open('mensajedeentrada.txt', 'r') as abrir_mensaje_entrada:
    mensaje_inicial=str(abrir_mensaje_entrada.read())   
    
with open('mensajeseguro.txt', 'r') as abrir_mensaje_seguro:    
    abrir_mensaje_seguro=open("mensajeseguro.txt","r")
    mensaje_final=str(abrir_mensaje_seguro.read())
    
textoencriptado=mensaje_final




def antirot5(msj):
    a="fghijklmnopqrstuvwxyzabcde"
    temp=""
    global textoencriptado
    for i in msj:
        if i in a:
            if a.index(i) <= 4:
                temp+=a[a.index(i)+21]
            else:
                temp+=a[a.index(i)-5]
        else:
            temp+= i
    textoencriptado=temp     
    print(textoencriptado)
    
def antirot18(msj):
    a="stuvwxyzabcdefghijklmnopqr"
    global textoencriptado
    temp=""
    for i in msj:
        if i in a:
            if a.index(i) < 18:
                temp+=a[a.index(i)+8]
            else:
                temp+=a[a.index(i)-18]
        else:
            temp+= i
    textoencriptado=temp
    print(textoencriptado)


for i in range(0,3):
    antirot5(textoencriptado)
time.sleep(2)
for i in range(0,10):
    antirot18(textoencriptado)



if mensaje_inicial==textoencriptado:
    print("¡Felicidades, el mensaje ha sido protegido exitosamente!")
else:
    print(" bibimos en un encriptado :(     ") #mensaje que sale cuando el texto decriptado no coincide con el mensaje inicial




