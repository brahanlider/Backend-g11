def saludar(nombre):
    saludo = 'Hola {}'.format(nombre)
    print(saludo)


saludar('Brahan')


def saludar_varios(*args):
  # cuando nosotros colocamos es un parametro el '*' significa que no hay limitesde ese parametro, este parametro debe de ir al ultimo
  # todos los valores que le pasemos a este parametro se almacenaran en una tupla
  # NOTA: las tuplas, a diferencia de los arreglos, no se pueden modificar osea una vez creadas sus valores no pueden cambiar
    print(args)
    for nombre in args:
        saludo = 'Hola {}'.format(nombre)
        print(saludo)


saludar_varios('Roxana', 'Rox', 'Juan', 'Martin')
saludar_varios('Pedro', 'Luis')
saludar_varios()
saludar_varios('Brahan', 19, True, 1.67)

def informacion_usuario(**kwargs):
    # kwargs > keyboards argument o se le pasan parametros por llaves
    print(kwargs)
    # .get ('llaves') > devolver el valor si es que existe la llave, sino existe entonces devolvera None
  # None o el segundo parametro que le colocaremos (opcional)
    print(kwargs.get('estatura','NOOOOOO HAAAAAAY'))
    try:
        print(kwargs['estatura'])
    except:
        print('No existe la llave estatura')

informacion_usuario(nombre='Brahan', edad= 19, esta_civil='soltero', estatura= 1.67)
informacion_usuario(nombre='Fernado', apellido= 'Juarez', nacionalidad='Colombiano', fecha_nacimiento= '31/05/1999')


# recibir dos valores y hacer la division (dividendo / divisor) y retornar su resultado
def dividir(dividendo, divisor):
    # si la división da un error entonces retornar un mensaje que diga 'Division incorrecta'
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        # aqui ingresara cuando la division sea entre 0
        return 'no puede ver division entre 0'
    
    except TypeError:
        # ingresa si la división tiene algun caracter
        return 'Las divisiones solamente pueden ser entre dos numeros'
    
    except:
        #ingresara si no es ninguno de los dos errores anteriores
        return 'error desconocido'

valor = dividir(10,5)
print(valor)

valor = dividir(10,0)
print(valor)

valor = dividir('a','h')
print(valor)

try:
    valor = dividir(5,)
    print(valor)
except TypeError:
    print('Estuvo mal llamar asi la funcion')



