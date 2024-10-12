# 3) Dada la implementación de las clases Color y Borde, y el siguiente fragmento de 
# código: 

# C1 = Color(150, 150, 150) 
# C2 = Color(150, 150, 150) 
# B1 = Borde(1,C1) 
# B2 = Borde(1,C2) 
# print(C1 == C2) 
# print(B1 == B2) 
# print(C1.esIgualQue(C2)) 
# print(B1.esIgualQue(B2)) 
 
# A. Dibuje el diagrama de objetos al terminar el bloque de asignaciones. 
# B. Muestre la salida.

print(C1 == C2) = false por que c1 no es el mismo objeto que c2

print(B1 == B2) = false por que b1 no es el mismo objeto que b2

print(C1.esIgualQue(C2)) = true por que los colores c1 y c2 son iguales

print(B1.esIgualQue(B2)) = true por que los bordes b1 y b2 son iguales


# 4) Dada la implementación de las clases Color y Borde, y el siguiente fragmento de 
# código: 

# C1 = Color(150, 150, 150) 
# C2 = Color(150, 150, 150) 
# B1 = Borde(1,C1) 
# B2 = Borde(1,C2) 
# B3 = B2.clonar() 
# B4 = Borde(B2.obtenerGrosor(), B2.obtenerColor()) 
# print( B2 == B3) 
# print( B2 == B4) 
# print(B2.esIgualQue(B1)) 
# print(B2.esIgualQue(B3)) 
# print(B2.obtenerGrosor() == B1.obtenerGrosor() and B2.obtenerColor() == B1.obtenerColor()) 
# print(B2.obtenerGrosor() == B3.obtenerGrosor() and B2.obtenerColor() == B3.obtenerColor()) 
# print(B2.obtenerGrosor() == B1.obtenerGrosor() and B2.obtenerColor().equals(B1.obtenerColor())) 
# print(B2.obtenerGrosor() == B4.obtenerGrosor() and B2.obtenerColor().equals(B4.obtenerColor()))

B3 = B2.clonar()
B3 = Borde(1,C2)

B4 = Borde(B2.obtenerGrosor(), B2.obtenerColor()) 
                B4= Borde(1,C2)
                
print( B2 == B3) = false

print(B2 == B4) = false

print(B2.esIgualQue(B1)) = ¿((1,C2) = (1, C1))? = false

print(B2.esIgualQue(B3)) = ¿((1,C2) = (1,C2))? = true

print(B2.obtenerGrosor() == B1.obtenerGrosor() and B2.obtenerColor() == B1.obtenerColor()) = 
(1, C2) == (1, C1) and (1, C2) == (1, C1) = false

print(B2.obtenerGrosor() == B3.obtenerGrosor() and B2.obtenerColor() == B3.obtenerColor()) =
(1,C2) == (1, C2) and (1, C2) == (1, C2) = true

print(B2.obtenerGrosor() == B1.obtenerGrosor() and B2.obtenerColor().equals(B1.obtenerColor())) =
(1,C2) == (1,C1)  and  (1, C2).equals(1, C1) = false por que equals no está dentro de la clase color y borde.

print(B2.obtenerGrosor() == B4.obtenerGrosor() and B2.obtenerColor().equals(B4.obtenerColor())) =

(1,C2) == (1, C2)  and  (1, C2).equals(1, C2) = false por que equals no está dentro de la clase color y borde.

# 5) Muestre la evolución del diagrama de objetos y la salida del ejercicio anterior 
# considerando que la clase Borde implementa: 
# A. clonación en profundidad, igualdad superficial 
# B. clonación superficial, igualdad en profundidad 
# C. clonación en profundidad, igualdad en profundidad