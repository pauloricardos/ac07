
class Disciplina:
    def __init__(self, nome: str, carga_horaria: int) -> None:
        self.__nome = nome
        self.__carga_horaria = carga_horaria

    def __str__(self):
        return 'Nome: ' + self.__nome + ', Carga Horária: ' + str(self.__carga_horaria)

    def get_nome(self) -> str:
        return self.__nome

    def get_carga_horaria(self) -> int:
        return self.__carga_horaria


class Pessoa:
    def __init__(self, nome: str, telefone: int, email: float) -> None:
        self._nome = nome
        self._telefone = telefone 
        self._email = email

    def __str__(self):
        return 'Nome: ' + self._nome + ', Telefone: ' + str(self._telefone) +\
            ', E-mail: ' + self._email 

    def get_nome(self) -> str:
        return self._nome

    def get_telefone(self) -> int:
        return self._telefone

    def get_email(self) -> str:
        return self._email

    def set_telefone(self, novo_telefone: int) -> None:
        if isinstance(self._telefone, int):
            self._telefone = novo_telefone
        else:
            raise TypeError    

    def set_email(self, novo_email) -> None:
        if '@' in novo_email: 
            self._email = novo_email
        else:
            raise ValueError


class Aluno(Pessoa):

    def __init__(self, nome: str, telefone: int,
                 email: str, n_matricula: int, disciplinas: list) -> None:
        super().__init__(nome, telefone, email)
        self.__n_matricula = n_matricula 
        self.__disciplinas = disciplinas

    def __str__(self):
        return 'Nome: ' + self._nome + ', Telefone: ' + str(self._telefone) +\
            ', E-mail: ' + self._email + ', Nº Matricula: ' + str(self.__n_matricula) +\
            ', Disciplinas: ' + str(self.__disciplinas)

    def get_matricula(self) -> int:
        return self.__n_matricula

    def matricular(self, disciplina: 'Disciplina') -> None:
       self.__disciplinas.append(disciplina)

    def lista_disciplinas(self) -> list:
        return self.__disciplinas


class Professor(Pessoa):
    def __init__(self, nome: str, telefone: int, email: str, disciplinas: list) -> None:
        super().__init__(nome, telefone, email)
        self.__disciplinas = disciplinas

    def __str__(self):
        return 'Nome: ' + self._nome + ', Telefone: ' + str(self._telefone) +\
            ', E-mail: ' + self._email +\
            ', Disciplinas: ' + str(self.__disciplinas)

    def ministra(self, disciplina: object) -> None:
        cargaHoraria = 0
        for item in self.__disciplinas:
            cargaHoraria += item.get_carga_horaria()

        if(cargaHoraria + disciplina.get_carga_horaria()) > 200:
            raise ValueError
        else:
            self.__disciplinas.append(disciplina)


    def lista_disciplinas(self) -> list:
        novaLista = []
        for indice in range(len(self.__disciplinas)):
            novaLista.append(self.__disciplinas)
        return novaLista

        


            

    

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




############
'''
#Instância da Classe Disciplina
ads = Disciplina('ADS', 180)
tecWeb = Disciplina('TecWeb', 120)
print(ads.__str__())


#Instância da Classe Pessoa
luci = Pessoa('Luciana', 1139796226, 'pessoa@gmail.com')
print(luci.get_nome())
print(luci.get_email())
print(luci.get_telefone())
print('################################')
luci.set_email('luciana@hotmail.com')
luci.set_telefone(11942070973)
print(luci.get_email())
print(luci.get_telefone())


#Instância da Classe Aluno
lenildo = Aluno('Lenildo', 11965333811, 'aluno@fit.com', '1802273',
                [tecWeb.get_nome()])

lenildo.__init__()
print(lenildo.get_matricula())

for l in lenildo.lista_disciplinas():
    print(l)

print('################################')

lenildo.matricular(ads.get_nome())

for l in lenildo.lista_disciplinas():
    print(l)
'''

'''
class Disciplina:
    def __init__(self, nome: str, hora: int) -> None:
        self.__nome = nome
        self.__hora = hora

    def get_nome(self):
        return self.__nome

    def get_hora(self):
        return self.__hora

class Professor:
    def __init__(self, nome: str, disciplina: list) -> None:
        self.__nome = nome
        self.__disciplina = disciplina

    def __str__(self):
        return 'Nome: ' + self.__nome + ', Disciplina: ' +\
               str(self.__disciplina)
    
    def ministra(self, disciplina):
        
        for el in disciplina:
            print(el.get_nome())
            
 

ads = Disciplina('ADS', 40)
tecWeb = Disciplina('TecWeb', 60)
lpII = Disciplina('LPII', 160)
rangel = Professor('Rangel', [ads, tecWeb])

rangel.ministra([lpII])
'''




























