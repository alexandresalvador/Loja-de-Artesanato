from classes.lojaArtesanato import Cliente
from classes.lojaArtesanato import Produto
from classes.lojaArtesanato import Encomenda
from classes.lojaArtesanato import relatorio

cliente1 = Cliente('Alexandre Salvador', '4476810-2284', 'R. Lorival Tabbert, Aventureiro, Joinville, 89139848', '123.456.654-22')
print(cliente1.verificarCpf())

produto1 = Produto('Piso', 'Piso Listrado', '10 cm', '30 cm', '35 cm', '5kg', 'Preto', 120.00)
print(produto1.verificarPreco())

encomenda1 = Encomenda(2)

relatorio(cliente1, produto1, encomenda1)