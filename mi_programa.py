#este es un programaque pregunta tu nombre, edad, direccion, fecha de nacimiento
# correo electronico y telefono. Ademas debe sumar la edad y año de nacimiento.
print("Hola! por favor, dime tu nombre")
nombre_persona = input()
print(f"Es un gusto conocerte, {nombre_persona}")
print(f"{nombre_persona} me podrias indicar tu apellido?")
apellido_persona = input()
print(f"Perfecto, {nombre_persona} {apellido_persona} ahora, necesito que me digas tu edad y fecha de nacimiento")
edad_persona = int(input())
fecha_nacimiento = input()
print(f"Gracias {nombre_persona}, indicame tu dirección por favor")
direccion_persona = input()
print("Por último, necesito la siguiente información, tu email y número de telefono")
email_persona = input()
telefono_persona = input()
print(f"Muchas gracias {nombre_persona}! ahora, revisa la información para ver si está correcta")
print(f"Tu nombre es {nombre_persona} {apellido_persona}, tienes {edad_persona} años y naciste el {fecha_nacimiento}, vives en {direccion_persona}, tu email es {email_persona} y tu telefono es el {telefono_persona}, esta información es correcta?")
respuesta1 = input()
print(f"{respuesta1}, muy bien!, muchas gracias {nombre_persona}.")
print("Por favor, indicame tu año de nacimiento")
year = int(input())

#a continuación sumaré el año de nacimiento con la edad.

resultado = edad_persona + year

print(f"La suma de tu edad y tu año de nacimiento es: {resultado}.")

print(f"Gracias {nombre_persona}, fue un gusto conocerte.")


