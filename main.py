

from model.banco import Banco
from model.cliente import Cliente
from model.conta import ContaCorrente, ContaPoupanca


banco = Banco()

cliente1 = Cliente('Leonardo',37)
cliente2 = Cliente('Jessica',29)
cliente3 = Cliente('Paulo',29)



conta1 = ContaPoupanca(1111,254136, 100)
conta2 = ContaCorrente(2222,985415, 300)
conta3 = ContaPoupanca(1212,685471, 150)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autorizado')

print('#'*20)
if banco.autenticar(cliente2):
    cliente2.conta.depositar(40)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autorizado')
print('#'*20)
