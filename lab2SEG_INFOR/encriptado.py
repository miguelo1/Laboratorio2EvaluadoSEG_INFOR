#   Laboratorio Evaluado N°2
#   Integrantes: Ismael Solis y Miguel Orellana
#   Profesor: Manuel Alba
#   Asignatura: Seguridad Informática


import time


#reciclado del laboratorio 1
def rot5(msj):
    a="abcdefghijklmnopqrstuvwxyz"
    temp=""
    global textoencriptado
    for i in msj:
        if i in a:
            if a.index(i) <= 20:
                temp+=a[a.index(i)+5]
            else:
                temp+=a[a.index(i)-21]
        else:
            temp+= i
    textoencriptado=temp
    print(textoencriptado)
       
def rot18(msj):
    a="abcdefghijklmnopqrstuvwxyz"
    global textoencriptado
    temp=""
    for i in msj:
        if i in a:
            if a.index(i) < 7:
                temp+=a[a.index(i)+18]
            else:
                temp+=a[a.index(i)-8]
        else:
            temp+= i
    textoencriptado=temp
    print(textoencriptado)



#Lectura del archivo.txt inicial y escritura para el final
with open('mensajedeentrada.txt', 'r') as abrir_mensaje_entrada:
    mensaje=str(abrir_mensaje_entrada.read())    
    print(mensaje)
    textoencriptado=mensaje    

time.sleep(1)
#textoencriptado=MensajeDeEntrada
for i in range(0,10):
    rot18(textoencriptado)
time.sleep(2)   
for i in range(0,3):
    rot5(textoencriptado)


#Escritura en el archivo de mensaje seguro
with open('mensajeseguro.txt', 'w') as escribir_mensaje_seguro:
    escribicion=escribir_mensaje_seguro.write(textoencriptado)






