from numpy import array


class Empleado(object):

    def __init__(self, n, d):
        self.nombre = n
        self.division = d

    def getName(self):
        return self.nombre

    def print(self):
        print("Nombre: " + self.nombre + "Division: " + self.division)


class Division(object):

    def __init__(self):
        self.list = []
        self.numero = 0
        self.nombreDivision = ""

    def Division(self, n):
        self.nombreDivision = n

    def getName(self):
        return self.nombreDivision

    def add(self, nombre):
        e = Empleado(nombre, self.nombreDivision)
        self.list.append(e)

    def DivisionIterator(self):
        return DivisionIterator(self.list)


class DivisionIterator(object):

    def __init__(self):
        self.empleado = []
        self.location = 0
        self.myIter = iter(Empleado)

    def next(self):
        return next(self.myIter)
