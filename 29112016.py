## EPN-ESFOT-ASI Programacion Avanzada 2016-B
## 29112016.py
## Versión: 1.0
## Busqueda de las palabras Harry y Potter

## Autor: Bryan España y Bryan Pilatuña
## Fecha: 29-Nov-2016
def creartxt():
    archi=open('palabra.txt','w')
    archi.close()
    
def grabartxt(h,p):
    archi=open('palabra.txt','a')
    archi.write("El documento de Harry Poter contiene la palabra")
    archi.write("\nHarry se repide: \t")
    archi.write(str(h))
    archi.write("\nY tambien la palabra Potter se repide: \t")
    archi.write(str(p))
    archi.close() 

def leertxt():
    h=0
    p=0
    a=''
    archi=open('harry.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        for i in range(len(linea)):
            if linea[i] ==" ":
                if a == 'Harry':
                    h=h+1
                elif a == 'Harry.':
                    h=h+1
                elif a == 'Potter':
                    p=p+1
                elif a == 'Potter.':
                    p=p+1
                a=''
            else:
                a=a+linea[i]
        linea=archi.readline()     
        archi.close()
    print("La palabra Harry se repide: \t")
    print(h)
    print("Y tambien la palabra Potter se repide: \t")
    print(p)
    grabartxt(h,p)
           
creartxt()       
leertxt()
