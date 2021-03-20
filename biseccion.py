#####################################################################
#   Autor :       Juan Carlos Quiroz Aguialar                       #
#   Fecha :       02/21                                             #
#   Descripcion:  Metodo de biseccion                               #
#                                                                   #
#####################################################################

import math as mt




################################################################################
#  Funcion hacer la biseccion una ves que se encontro un intervalo con raiz    #
#  Recibe a -> Inicio del intervalo  b-> Fin del intervalo                     #
#  Devuelve la aproximacion de la raiz                                         #
################################################################################

def biseccion(a,b):
    dif = 1
    #Esta variable controla la precision con que se quiere calcular la raiz
    #innicialmente es 1x10^(-5) = 0.00005
    #si se requiere mayor precision se puede modificar este valor
    precision = 1*(10**(-5))
    #Mientras la diferencia sea menor a la precision seguira en este ciclo
    while (dif > precision ):
        #calculamos el valor medio
        c = (a+b)/2
        d = fx(a) * fx(c)
        #si se encuentra en el primer intervalo se actualiza el limite final a el valor medio
        if(d < 0):
            b = c
        else:
            d = fx(c) * fx(b)
            #si la raiz se encuentra en el segundo intervalo se actualiza el limite inicial al valor medio
            if (d < 0):
                a = c
        dif = abs(a - b)
    return (a)




################################################################################
#  Funcion calcular el valor de x en la funcion donde buscamos la raiz         #
#  Recibe el punto x donde evaluaremos la funcion                              #
#  Devuelve el valor de la funcion en el punto x                               #
################################################################################

def fx(x):
    #se puede cambiar esta funcion, por ejemplo para usar la funcion cos(x)
    #return mt.cos(x)
    return mt.sin(x)

################################################################################
#  Funcion saber si existe una raiz en el intervalo                            #
#  Recibe a -> Inicio del intervalo  b-> Fin del intervalo                     #
#  Devuelve cierto si hay una raiz o falso si no la hay                        #
################################################################################
def busca_intervalo(a,b):
    c = fx(a) * fx(b)
    if(c < 0):
        return True
    else :
        return  False


def main():
    #Lista para guardar las raices
    raices = []

    a = float(input("ingresa el limite inferior del intervalo \n"))
    b = float(input("ingresa el limite superior del intervalo \n"))



    #Si necesitamos intervalos mas pequeños podemos cambiar esta variable
    paso = 0.1


    #Si existe una raiz en los limites del intervalo las guardamos
    if (fx(a) == 0):
        raices.append(a)
    if (fx(b) == 0):
        raices.append(b)

    i = a + paso


    #El cliclo se detiene cuando llegamos al limite superior del intervalo
    while (i <= b):
        print("Buscando en el intervalo... (",a,",",i,")")
        if(busca_intervalo(a,i)):
            print("\t\t Hay una raiz \n\t\t Haciendo la biseccion...")
            r = biseccion(a,i)
            print("**********************************************************************\n*\t\t\t La raiz es: ", r
                  , "\n**********************************************************************")
            raices.append(r)

        a = round(i,3)
        i = round(a + paso,3)


    print("Metodos de biseccion terminado, desea imprimir las raices?? \n 1->Si \n 2->No")
    res = int(input())
    if (res == 1):
        print("Raices -> ",raices)



# Ejecuta la funcion principal
if __name__ == '__main__':
    main()

