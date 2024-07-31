class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def subir(self):
        if self.atualAndar < self.totalAndar - 1:
            self.atualAndar += 1
            print("Subindo")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print("Descendo")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print("Entrando uma pessoa")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print("Saindo uma pessoa")
        else:
            print("NÃO TEM NINGUÉM")

def menu():
    elevador = Elevador(totalCapacidade=5, totalAndar=10)

    while True:
        print("\nMenu:")
        print("1. Subir")
        print("2. Descer")
        print("3. Entrar")
        print("4. Sair")
        print("5. Sair do Programa")
        
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            elevador.subir()
        elif opcao == '2':
            elevador.descer()
        elif opcao == '3':
            elevador.entrar()
        elif opcao == '4':
            elevador.sair()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")

if __name__ == "__main__":
    menu()