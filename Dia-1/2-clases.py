class Persona:
    # cuando una variable se define dentro de una clase pasa a llamarse ATRIBUTO
    estatura = 1.80
    peso = 80
    signo_zodiacal = 'LEO'

    def sumar(self, *args):
        # self = this en js,c#, c++
        # cuando una función se declara o se define dentro de una clase para a llamarse METODO
        #Recibir una numero ilimitado de numeros para realizar su sumatoria
        total = 0
        # args = (10,10,52,52,65,55)
        for numero in args:
            total = total + numero
        return total
    
    def saludar(self, nombre):
        return 'Hola {}'.format(nombre)
    
# cuando sacamos una 'copia' de la clase para utilizarla estamos creando una instancia
persona1 = Persona()
persona2 = Persona()

# Modifico los atributos de esa persona en particular
persona1.peso = 70
persona2.peso = 50

# todas la modificaciones que hacemos es independiente de la instancia

print(persona1.peso)
print(persona2.peso)

resultado1 = persona1.sumar(10,10,52,52,65,55)
resultado2 = persona1.sumar(12,36,25,14,25)

print(resultado1)
print(resultado2)