import numpy as np

lista_nombres = ["Sofía", "Mateo", "Isabella", "Lucas", "Valentina", "Alejandro", "Emma", 
 "Santiago", "Martina", "Sebastián", "Camila", "Nicolás", "Valeria", "Gabriel", 
 "Antonella", "Daniel", "Lucía", "Andrés", "Renata", "Adrián", "Sara", "Diego",
 "Julieta", "Joaquín", "Paula", "Leonardo", "Victoria", "Benjamín", "María", 
 "Samuel", "Amelia", "David", "Elena", "Maximiliano", "Montserrat", "Ángel",
 "Regina", "Tomás", "Jimena", "Cristóbal", "Fernanda", "Bruno", "Ana", "Ricardo", 
 "Ximena", "Gael", "Andrea", "Matías", "Carolina", "Thiago", "Daniela", "Emilio", 
 "Alicia", "Jerónimo", "Natalia", "Dylan", "Claudia", "Iker", "Patricia", "Iván",
 "Alejandra", "Alan", "Laura", "Franco", "Gabriela", "Jesús", "Mariana", "Rodrigo",
 "Lorena", "Martín", "Melissa", "Juan", "Paola", "Carlos", "Diana", "Pedro", "Carmen", 
 "Miguel", "Rosa", "Jorge", "Gloria", "Luis", "Silvia", "Antonio", "Isabel", "José",
 "Esther", "Manuel", "Beatriz", "Francisco", "Raquel", "Javier", "Susana", "Raúl",
 "Pilar", "Alberto", "Eva", "Enrique", "Dolores", "Sergio", "Mercedes", "Óscar", 
 "Cristina", "Julio", "Rosario"]

dict_users = {}

for i_name in lista_nombres:
    dict_users[i_name.lower() ] = [ np.random.randint(10000, 500000), f'{i_name.lower()}_1']

print(dict_users)

#dict_users = { i:np.randon.randint(10000, 50000 for i in lista_nombres }
str_nombre = ''
    
for enu, i_name in enumerate(lista_nombres):
    str_nombre = str_nombre + f'\n{enu}: ' + i_name
    
print("i-name")
print("valor")

               
                
                
                
                
                
                
                
                
