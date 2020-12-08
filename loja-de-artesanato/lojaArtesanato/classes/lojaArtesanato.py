
class Cliente():

    nome= ""
    telefone= ""
    endereco= ""
    cpf= ""



    def __init__ (self, nome, telefone, endereco, cpf):

        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cpf = cpf



    def verificarCpf(self):

        primeiro_ponto = self.cpf.find('.')
        segundo_ponto = self.cpf.find ('.', (primeiro_ponto + 1))
        hifen = self.cpf.find ('-', segundo_ponto)

        if((len(self.cpf) == 14) and (primeiro_ponto == 3) and (segundo_ponto == 7) and (hifen == 11)):
            primeira_parte = self.cpf[0:2]
            segunda_parte = self.cpf[4:6]
            terceira_parte = self.cpf[8:10]
            ultima_parte = self.cpf [12:13]

        if(primeira_parte.isdigit() and segunda_parte.isdigit() and terceira_parte.isdigit() and ultima_parte.isdigit()):
            return True
        else:
            return False



class Produto():
    nome = ""
    descricao = ""
    largura = ""
    comprimento = ""
    altura = ""
    peso = ""
    cor = ""
    vlunitario = 0



    def __init__ (self, nome, descricao, largura, comprimento, altura, peso, cor, vlunitario):

        self.nome = nome
        self.descricao = descricao
        self.largura = largura
        self.comprimento = comprimento
        self.altura = altura
        self.peso = peso
        self.cor = cor
        self.vlunitario = vlunitario



    def verificarPreco(self):
        if(type (self.vlunitario) == str):
            return 'O valor unitário tem que ser um número: '

class Encomenda():

    info = Cliente
    objeto = Produto
    quantidade = 0


    def __init__ (self, quantidade):
        self.quantidade = quantidade



def relatorio(Cliente, Produto, Encomenda):

    print('\nCliente: ', Cliente.nome.upper(), '\nTelefone: ', Cliente.telefone, '\nEndereço: ',Cliente.endereco, '\nCPF: ',Cliente.cpf)
    print('Produto: ',Produto.nome, '\nDescrição: ',Produto.descricao, '\nLargura: ',Produto.largura, '\nComprimento: ',Produto.comprimento, '\nAltura: ',Produto.altura, '\nPeso: ',Produto.peso, '\nCor: ',Produto.cor, '\nValor Unitário: ',Produto.vlunitario)
    print('Quantidade: ',Encomenda.quantidade, '\nValor Total: ',Produto.vlunitario * Encomenda.quantidade)