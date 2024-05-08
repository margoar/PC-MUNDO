from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado("HP","USB")
raton1 = Raton("HP","USB")
monitor1 = Monitor("HP",15)

teclado2 = Teclado("HP","USB")
raton2 = Raton("HP","USB")
monitor2 = Monitor("HP",15)

cp1 = Computadora('HP-Monster', monitor1,teclado1,raton1)
#print(cp1)
cp2 = Computadora('HP-Junior', monitor2,teclado2,raton2)




teclado2 = Teclado("ACER","Bl")
raton2 = Raton("HP","USB")
monitor2 = Monitor("HP",15)


computadoras1 = [cp1, cp2]

orden = Orden(computadoras1)
print(orden)