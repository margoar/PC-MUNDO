class Monitor:
    contador_monitores =0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self._marca = marca
        self._tamanio = tamanio
        self._id_monitor = Monitor.contador_monitores

    def __str__(self):
        return f'id: {self._id_monitor} , Marca: {self._marca}, Tamano : {self._tamanio} '

if __name__ == '__main__':
    monitor1 = Monitor('HP', 15)
    print(monitor1)
    monitor2 = Monitor('ACER', 27)
    print(monitor2)