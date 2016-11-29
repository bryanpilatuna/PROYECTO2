import math
def triangulo(fig):
    print("\tMenu ",fig)
    print("1.Triángulo Equilátero")
    print("2.Triángulo Isósceles")
    print("3.Triángulo Escaleno")
    sel=input("Ingrese el numero de la opcion que deseea: ")
    if sel == '1':
        print("1.-Triángulo Equilátero")
        b=int(input("Ingrese ls medida de uno de los lados: "))
        h=math.sqrt(3*b)/2
        a=(math.sqrt(3)*b**2)/4
        p=(3*b)
        imprimir(a,p)
        def creartxt():
                archi=open('equilatero.txt','w')
                archi.close()
        def grabartxt(a,p):
                archi=open('equilatero.txt','a')
                archi.write('El area del Triángulo Equilátero es: \t')
                archi.write(str(a))  
                archi.write('\nEl perimetro del Triángulo Equilátero es: \t')
                archi.write(str(p))
                archi.close()
        creartxt()
        grabartxt(a,p)
    elif sel == '2':
        print("2.-Triángulo Isósceles")
        b=int(input("Ingrese la base: "))
        l=int(input("Ingrese la medida de un lado: "))
        h=math.sqrt(l**2-(b**2/4))
        a=(b*math.sqrt(l**2-(b**2/4)))/2
        p=(2*l+b)
        imprimir(a,p)
        def creartxt():
                archi=open('isosceles.txt','w')
                archi.close()
        def grabartxt(a,p):
                archi=open('isosceles.txt','a')
                archi.write('El area del Triángulo Isósceles es: \t')
                archi.write(str(a))  
                archi.write('\nEl perimetro del Triángulo Isósceles es: \t')
                archi.write(str(p))
                archi.close()
        creartxt()
        grabartxt(a,p)
    elif sel == '3':
        print("3.-Triángulo Escaleno")
        b=int(input("Ingrese la base: ")) 
        h=int(input("Ingrese la altura: "))
        l=int(input("Ingrese la medida de un lado: "))
        l2=int(input("Ingrese la medida de del otro lado: "))
        a=(b*h)/2
        p=(b+l+l2)
        imprimir(a,p)
        def creartxt():
                archi=open('escaleno.txt','w')
                archi.close()
        def grabartxt(a,p):
                archi=open('escaleno.txt','a')
                archi.write('El area del Triángulo Isósceles es: \t')
                archi.write(str(a))  
                archi.write('\nEl perimetro del Triángulo Isósceles es: \t')
                archi.write(str(p))
                archi.close()
        creartxt()
        grabartxt(a,p)
    else:
        print("El numero no se encuentra en el rango del menu ")

def poligono(fig,lad):
    print("\t",fig)
    l=float(input("Ingrese la medida de un lado: "))
    apo=float(input("Ingrese el apotema: "))
    n=lad
    p=l*n
    a=(p*apo)/2
    imprimir(a,p)
    def creartxt():
                archi=open('poligono.txt','w')
                archi.close()
    def grabartxt(a,p):
                archi=open('poligono.txt','a')
                archi.write('El area del Poligono es: \t')
                archi.write(str(a))  
                archi.write('\nEl perimetro del Poligono es: \t')
                archi.write(str(p))
                archi.close()
    creartxt()
    grabartxt(a,p)

def imprimir(a,p):
    print("El area de la figura es: ",a)
    print("El perimetro de la figura es: ",p)

def menu():
    print("\tMenu")
    print("3.-Tringulo")
    print("4.-Cuadrado")
    print("5.-Pentagono")
    print("6.-Hexagono")
    print("7.-Heptagono")
    print("8.-Octogono")
    print("9.-Eneagono")
    print("10.-Decagono")

def main():
    res='si'
    while res[0] in ['s','S']:
        menu()
        sel=input("Ingrese el numero de la opcion que deseea: ")
        if sel == '3':
            triangulo("Triangulo")
        elif sel == '4':
            def creartxt():
                archi=open('impares.txt','w')
                archi.close()
            def grabartxt(areacua,pericua):
                archi=open('impares.txt','a')
                archi.write('El area del cuadrado es: \t')
                archi.write(str(areacua))  
                archi.write('\nEl perimetro del cuadrado es: \t')
                archi.write(str(pericua))
                archi.close() 
            print ("AREA Y PERIMETRO DEL CUADRADO")
            lado = float(input("Ingrese el lado del cuadrado: "))
            pericua = lado+lado+lado+lado
            areacua = lado*lado
            print ("El Area del Cuadrado es:\n")
            print (areacua)
            print ("\nEl perimetro del Cuadrado es: \n ")
            print (pericua)
            grabartxt(areacua,pericua)
        elif sel =='5':
            poligono("Pentagono",5)
        elif sel== '6':
            def creartxt():
                archi=open('hexagono.txt','w')
                archi.close()
            def grabartxt(areahexa,perihexa):
                archi=open('hexagono.txt','a')
                archi.write('El area del hexagono es: \t')
                archi.write(str(areahexa))  
                archi.write('\nEl perimetro del hexagono es: \t')
                archi.write(str(perihexa))
                archi.close() 
            print ("AREA Y PERIMETRO DEL HEXAGONO\n")
            ladohexa = float(input("Ingrese el lado del Hexagono"))
            apotema = float (input("Ingrese la apotema del Hexagono"))
            perihexa = (6* ladohexa)
            areahexa= (perihexa*apotema)
            print ("El Area del Hexagono es:\n")
            print (areahexa)
            print ("\nEl perimetro del Hexagono es: \n ")
            print (perihexa)
            grabartxt(areahexa,perihexa)
        elif sel =='7':
            poligono("Heptagono",7)
        elif sel== '8':
            def creartxt():
                archi=open('octogono.txt','w')
                archi.close()
            def grabartxt(areaocto,periocto):
                archi=open('octogono.txt','a')
                archi.write('El area del octogono es: \t')
                archi.write(str(areaocto))  
                archi.write('\nEl perimetro del octogono es: \t')
                archi.write(str(periocto))
                archi.close() 
            print ("AREA Y PERIMETRO DEL OCTOGONO\n")
            ladoct = float(input("Ingrese el lado del Octogono"))
            apotemaoct = float (input("Ingrese la apotema del Octogono"))
            periocto = (8*ladoct)
            areaocto= (periocto*apotemaoct)
            print ("El Area del Octogono es:\n")
            print (areaocto)
            print ("\nEl perimetro del Octogono es: \n ")
            print (periocto)
            grabartxt(areaocto,periocto)
        elif sel =='9':
            poligono("Eneagono",9)
        elif sel== '10':
            def creartxt():
                archi=open('decagono.txt','w')
                archi.close()
            def grabartxt(areadeca,perideca):
                archi=open('decagono.txt','a')
                archi.write('El area del decagono es: \t')
                archi.write(str(areadeca))  
                archi.write('\nEl perimetro del decagono es: \t')
                archi.write(str(perideca))
                archi.close() 
            print ("AREA Y PERIMETRO DEL DECAGONO\n")
            ladodeca = float(input("Ingrese el lado del Decagono"))
            apotemadeca = float (input("Ingrese la apotema del Decagono"))
            perideca = (10* ladodeca)
            areadeca= (perideca*apotemadeca)
            print ("El Area del Decagono es:\n")
            print (areadeca)
            print ("\nEl perimetro del Decagono es: \n ")
            print (perideca)
            grabartxt(areadeca,perideca)
        else:
             print("El numero no se encuentra en el rango del menu")
        res=input("Deseea calcular otra area y perimetro: ")
            
main()
