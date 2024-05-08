class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca

    @property
    def tipo_marca(self):
        return self._tipo_entrada