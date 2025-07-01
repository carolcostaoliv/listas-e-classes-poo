#1
import random

class Bingo:
    def __init__(self, quantidade_bolas):
        self.__quantidade_bolas = quantidade_bolas
        self.__bolas_sorteadas = []

    def sortear(self):
        if len(self.__bolas_sorteadas) == self.__quantidade_bolas:
            return -1
        while True:
            numero_sorteado = random.randint(1, self.__quantidade_bolas)
            if numero_sorteado not in self.__bolas_sorteadas:
                self.__bolas_sorteadas.append(numero_sorteado)
                return numero_sorteado

    def get_bolas_sorteadas(self):
        return self.__bolas_sorteadas

class BingoUI:
    __jogo_bingo = None

    @classmethod
    def menu(cls):
        return int(input("1 - Iniciar jogo, 2 - Sortear, 3 - Sorteados, 4 - Fim\nInforme uma opção: "))

    @classmethod
    def main(cls):
        opcao = 0
        while opcao != 4:
            opcao = cls.menu()
            match opcao:
                case 1: cls.iniciar_jogo()
                case 2: cls.sortear_bola()
                case 3: cls.mostrar_sorteados()

    @classmethod
    def iniciar_jogo(cls):
        total_bolas = int(input("Digite o número de bolas que o jogo terá: "))
        cls.__jogo_bingo = Bingo(total_bolas)
        print(f"O jogo está sendo iniciado com {total_bolas} bolas")

    @classmethod
    def sortear_bola(cls):
        if cls.__jogo_bingo is None:
            print("Inicie o jogo primeiro")
        else:
            bola = cls.__jogo_bingo.sortear()
            if bola == -1:
                print("Todas as bolas já foram sorteadas")
            else:
                print(f"O número sorteado foi {bola}")

    @classmethod
    def mostrar_sorteados(cls):
        if cls.__jogo_bingo is None:
            print("Inicie o jogo primeiro")
        else:
            print("As bolas sorteadas foram:", *cls.__jogo_bingo.get_bolas_sorteadas())

BingoUI.main()

#2
class Contato:
    def __init__(self, codigo, nome, email, telefone):
        self.__codigo = codigo
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_nome(self):
        return self.__nome

    def set_email(self, novo_email):
        self.__email = novo_email

    def set_telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    def __str__(self):
        return f"{self.__codigo} - {self.__nome} - {self.__email} - {self.__telefone}"

class ContatoUI:
    __lista_contatos = []

    @classmethod
    def main(cls):
        opcao = 0
        while opcao != 6:
            opcao = cls.menu()
            if opcao == 1: cls.inserir_contato()
            elif opcao == 2: cls.listar_contatos()
            elif opcao == 3: cls.atualizar_contato()
            elif opcao == 4: cls.excluir_contato()
            elif opcao == 5: cls.pesquisar_contato()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def inserir_contato(cls):
        codigo = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        telefone = input("Informe o telefone: ")
        novo_contato = Contato(codigo, nome, email, telefone)
        cls.__lista_contatos.append(novo_contato)

    @classmethod
    def listar_contatos(cls):
        for contato in cls.__lista_contatos:
            print(contato)

    @classmethod
    def atualizar_contato(cls):
        nome_antigo = input("Informe o nome do contato que deseja atualizar: ")
        for contato in cls.__lista_contatos:
            if contato.get_nome() == nome_antigo:
                nome_novo = input("Novo nome: ")
                email_novo = input("Novo email: ")
                telefone_novo = input("Novo telefone: ")
                contato.set_nome(nome_novo)
                contato.set_email(email_novo)
                contato.set_telefone(telefone_novo)
                print("Contato atualizado")

    @classmethod
    def excluir_contato(cls):
        nome_para_excluir = input("Informe o nome do contato que deseja excluir: ")
        for contato in cls.__lista_contatos:
            if contato.get_nome() == nome_para_excluir:
                cls.__lista_contatos.remove(contato)
                print("Contato excluído")

    @classmethod
    def pesquisar_contato(cls):
        termo = input("Informe o nome do contato: ")
        for contato in cls.__lista_contatos:
            if contato.get_nome().startswith(termo):
                print(contato)

ContatoUI.main()

#3
class Pais:
    def __init__(self, codigo, nome, populacao, area_km2):
        self.__codigo = codigo
        self.__nome = nome
        self.__populacao = populacao
        self.__area_km2 = area_km2

    def get_nome(self):
        return self.__nome

    def set_populacao(self, nova_populacao):
        self.__populacao = nova_populacao

    def get_populacao(self):
        return self.__populacao

    def set_area(self, nova_area):
        self.__area_km2 = nova_area

    def calcular_densidade(self):
        return self.__populacao / self.__area_km2

    def __str__(self):
        return f"{self.__codigo} - {self.__nome} - {self.__populacao} - {self.__area_km2}"

class PaisUI:
    __lista_paises = []

    @classmethod
    def main(cls):
        opcao = 0
        while opcao != 7:
            opcao = cls.menu()
            if opcao == 1: cls.inserir_pais()
            elif opcao == 2: cls.listar_paises()
            elif opcao == 3: cls.atualizar_pais()
            elif opcao == 4: cls.excluir_pais()
            elif opcao == 5: cls.pais_mais_populoso()
            elif opcao == 6: cls.pais_mais_povoado()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Mais Populoso, 6-Mais Povoado, 7-Fim")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir_pais(cls):
        codigo = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        populacao = int(input("Informe a população: "))
        area = float(input("Informe a área: "))
        novo_pais = Pais(codigo, nome, populacao, area)
        cls.__lista_paises.append(novo_pais)

    @classmethod
    def listar_paises(cls):
        for pais in cls.__lista_paises:
            print(pais)

    @classmethod
    def atualizar_pais(cls):
        nome_pesquisa = input("Informe o nome do país que deseja atualizar: ")
        for pais in cls.__lista_paises:
            if pais.get_nome() == nome_pesquisa:
                nova_pop = int(input("Nova população: "))
                nova_area = float(input("Nova área: "))
                pais.set_populacao(nova_pop)
                pais.set_area(nova_area)
                print("País atualizado")
                return
        print("País não cadastrado")

    @classmethod
    def excluir_pais(cls):
        nome_exclusao = input("Informe o nome do país a ser excluído: ")
        for pais in cls.__lista_paises:
            if pais.get_nome() == nome_exclusao:
                cls.__lista_paises.remove(pais)
                print("País excluído")
                return
        print("País não cadastrado")

    @classmethod
    def pais_mais_populoso(cls):
        if not cls.__lista_paises:
            print("Nenhum país cadastrado")
        else:
            mais_populoso = max(cls.__lista_paises, key=lambda p: p.get_populacao())
            print(f"País mais populoso: {mais_populoso}")

    @classmethod
    def pais_mais_povoado(cls):
        if not cls.__lista_paises:
            print("Nenhum país cadastrado")
        else:
            mais_povoado = max(cls.__lista_paises, key=lambda p: p.calcular_densidade())
            print(f"País mais povoado: {mais_povoado}")

PaisUI.main()
