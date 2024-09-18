#texto del usuario
texto=input("ingresa una cadena de texto:")

#convertir a mayuscula
texto_mayusculas=texto.upper()

#caracteristicas
longitud=len(texto)

#palabras contenidas
contiene_python="python"in texto

#resultado
print(f"texto en mayusculas:{texto_mayusculas}")
print(f"numero de caracteres:{longitud}")
print(f"contiene la palabra ´pytho´:{contiene_python}")
