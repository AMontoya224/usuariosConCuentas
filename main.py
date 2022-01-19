from usuario import Usuario

# NOTA: Enviar nombre, el número de cuentas que desea abrir, valor por defecto incluido y la tasa de interés
lopez = Usuario("Guido Lopez", 2)
monty = Usuario("Ricardo Monty", 4, 0.03)
reyes = Usuario("Anibal Reyes", 3, 0.05)

# NOTA: El número de cuentas por convención empieza desde el 1
lopez.hacer_depósito(100, 1).hacer_depósito(150, 2).mostrar_balance_usuario()
reyes.hacer_depósito(25, 1).hacer_depósito(142, 2).mostrar_balance_usuario()
monty.hacer_depósito(250, 3).hacer_depósito(50, 4).hacer_retiro(20, 3).hacer_retiro(10, 2).mostrar_balance_usuario()

lopez.transferir_dinero(100, 2, monty, 3).mostrar_balance_usuario()
monty.mostrar_balance_usuario()

reyes.hacer_retiro(120, 2).generar_interes(2).mostrar_balance_usuario()
monty.generar_interes(1).mostrar_balance_usuario()