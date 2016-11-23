import math
a=float(input("Ingresar el valor de a"))
b=float(input("Ingresar el valor de b"))
c=float(input("Ingresar el valor de c"))
if a==0:
    print ("No existe division para cero")
elif a<=0:
    print ("El valor de A debe ser mayor a cero")
    
x1=(-b+(math.sqrt(b**2 -4*a*c)))/(2*a)
x2=(-b-(math.sqrt(b**2 -4*a*c)))/(2*a)
print(x1)
print(x2)
def creartxt():
    archi=open('datos2.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos2.txt','a')
    archi.write('BRYAN PILATUÑA\n')
    archi.write('BRYAN ESPAÑA\n')
    archi.write('EL PRIMER VALOR DE X1 ES: \t')
    archi.write(str(x1))
    archi.write('\n')
    archi.write('EL SEGUNDO VALOR DE X1 ES: \t')
    archi.write(str(x2))
    
    archi.close() 
creartxt()
grabartxt()
