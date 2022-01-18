from Cuenta import Cuenta

usuario = Cuenta(500)
usuario1= Cuenta(700)

usuario.Deposito(50).Deposito(10).Deposito(20).Retiro(100).Intereses().imprimirBalance()
usuario1.Deposito(20).Retiro(10).Retiro(20).Retiro(100).Intereses().imprimirBalance()

Cuenta.imprimirtodoslosBalance()