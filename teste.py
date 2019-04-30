class Teste():
    def __init__(self, a: list):
        self.__a = []
    
    def lista(self, b):
        return self.__a.append(b)


#Instância da Classe Disciplina
ads = Disciplina('ADS', 50)
tecWeb = Disciplina('TecWeb', 50)
LPII = Disciplina('LPII', 101)
SQL = Disciplina('SQL', 100)

#Instância da Classe Professor
rangel = Professor('Alexandre Rangel', 11965333811, 'rangel@fitprofessor.com',
                   [ads, LPII])

print(rangel.lista_disciplinas())
rangel.lista_disciplinas()

#print(rangel.lista_disciplinas())


#print(rangel.lista_disciplinas())
