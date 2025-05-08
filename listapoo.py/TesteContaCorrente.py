from contaCorrente import ContaCorrente

novaConta = ContaCorrente("Paulo", 1000)

print(f"{novaConta.cliente} - Saldo: R${novaConta.saldo:.2f}")

novaConta.sacar(500)
print(f"{novaConta.cliente} - Saldo após saque de 500: R${novaConta.saldo:.2f}")

novaConta.sacar(500)
print(f"{novaConta.cliente} - Saldo após segundo saque de 500: R${novaConta.saldo:.2f}")

novaConta.depositar(50)
print(f"{novaConta.cliente} - Saldo após depósito de 50: R${novaConta.saldo:.2f}")

sucesso = novaConta.sacar(500)
if not sucesso:
    print(f"{novaConta.cliente} - Saque de 500 não realizado (saldo insuficiente). Saldo atual: R${novaConta.saldo:.2f}")
else:
    print(f"{novaConta.cliente} - Saldo após saque de 500: R${novaConta.saldo:.2f}")
