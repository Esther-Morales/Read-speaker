from tkinter import *
from tkinter import font
from gtts import gTTS
from playsound import playsound
from os import remove
 
# Esto me describe las funciones, primero el mensaje entra de lo que nosotros escribamos 
#y convierte el mensaje en voz, y crea un archivo mp3 que posteriormente el usuario puede eliminar


def Texto_a_voz():
    message = entry_field.get()
    speech = gTTS(text= message, lang = 'es')
   
    speech.save("ArchivoAudio.mp3")
    playsound("ArchivoAudio.mp3")
    remove ("ArchivoAudio.mp3")

#Funcion de Salir 
def salir():
    root.destroy()

#Funcion Borrar y estos 3 comando es lo que agrege a mis botones 
def Borrar():
    Msg.set("")



#Esto pertenece a la imagen de textovoz


root = Tk()
root.geometry ("950x500")
root.configure(bg = "gray")
root.title("CONVERTIDOR DE TEXTO A vOZ ")

imagenE= PhotoImage(file = "2e.pgm")
imagenE = imagenE.subsample(1)
lblimagen=Label(root, image= imagenE).place(x=550, y=55)
 
#cajas de mensajes
Label(root, text=("TEXTO A VOZ"), font=("Derive Unicode", 25 ), bg="white smoke").pack()
Label(root,text="Esther", font=("Arial", 20), bg="white smoke").pack(side=BOTTOM)
Label(root, text="Ingresa el Texto", font=("Derive Unicode",20), bg="white smoke").place(x=20, y=150)

# se introduce un mensaje y se lee por medio de un mensaje
Msg = StringVar()
entry_field= Entry(root, textvariable=Msg, width="65")
entry_field.place(x=20, y=235, height=30)

#Botones y sus repectivas funciones 

Button(root,text="Play", font=("Derive Unicode", 25), command=Texto_a_voz).place(x=25, y= 325)
Button(root,text="Exit", font=("Derive Unicode", 25), command=salir, bg="orangeRed1").place(x=165, y= 325)
Button(root,text="Delete", font=("Derive Unicode", 25), command=Borrar).place(x=300, y= 325)


root.mainloop()

