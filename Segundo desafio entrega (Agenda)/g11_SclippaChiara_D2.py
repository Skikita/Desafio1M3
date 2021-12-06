"""Diseñar un programa en Python, que usando un diccionario nos permita:
-Cargar la agenda telefónica de nuestros colegas (al menos 5)
-Nos permita buscar el teléfono de algún contacto
"""
agenda = {}

def agendaDeContactos():
    print("Bienvenido/a a la agenda de contactos de Chiara!")
    control = True
    while control :
        nombre= input("Introduzca el nombre del contacto que desea agregar/buscar: ")
        if nombre not in agenda:
            telefono=int(input("El contacto no esta agendado, introduce el telefono que desea agendar: "))
            agenda[nombre]= telefono
            print("La lista de contactos es: ",agenda) 
        else:
            print("El contacto ya esta agendado, su telefono es: ",agenda[nombre])      
        respuesta = input("¿Desea seguir agregando/buscando contactos? Responda SI/NO: ")
        if respuesta != "SI":
            control = False
    print("Usted ha finalizado la consulta en la agenda de Chiara. Sus contactos son:")
    print(agenda)
agendaDeContactos()