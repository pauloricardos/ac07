# -*- coding: utf-8 -*-
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
        if isinstance(novo_telefone, int):
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
            ', Disciplinas: ' + self.__disciplinas

    def get_matricula(self) -> int:
        return self.__n_matricula

    def matricular(self, disciplina: 'Disciplina') -> None:
       self.__disciplinas.append(disciplina)

    def lista_disciplinas(self) -> list:
        return self.__disciplinas


class Professor(Pessoa):
    def __init__(self, nome: str, telefone: int, email: str) -> None:
        super().__init__(nome, telefone, email)
        self.__disciplinas = []

    def __str__(self):
        return 'Nome: ' + self._nome + ', Telefone: ' + str(self._telefone) +\
            ', E-mail: ' + self._email +\
            ', Disciplinas: ' + self.__disciplinas

    def ministra(self, disciplina: object) -> None:
        cargaHoraria = 0
        for item in self.__disciplinas:
            cargaHoraria += item.get_carga_horaria()
            
        if cargaHoraria + disciplina.get_carga_horaria() > 200:
            raise ValueError
        else:
            self.__disciplinas.append(disciplina)


    def lista_disciplinas(self) -> list:
        return self.__disciplinas