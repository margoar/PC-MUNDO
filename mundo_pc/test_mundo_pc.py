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

teclado3= Teclado("Gamer", 'Bluetotth')
raton3 = Raton('gamer' ,'Bluetoht')
monitor3 = Monitor ("Gamer",34)

cp1 = Computadora('HP-Monster', monitor1,teclado1,raton1)
#print(cp1)
cp2 = Computadora('HP-Junior', monitor2,teclado2,raton2)
cp3 = Computadora("Gammer",monitor3,teclado3,raton3)

computadoras1 = [cp1, cp2]
orden = Orden(computadoras1)
orden.agregar_computadora(cp3)
print(orden)

computadoras2 = [cp2,cp3]
orden2 = Orden(computadoras2)
print(orden2)