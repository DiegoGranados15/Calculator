start = True

message = """Operaciones disponibles:
    1. suma.
    2. resta.
    3. multiplicación.
    4. división.
    5. salir."""

while start == True:
    # Enter values
    n1 = int(input("Enter the first value: "))
    n2 = int(input("Enter the second value: "))

    # Message
    print(message)

    # Operations
    operation = int(
        input("Ingresa el número de la operación que deseas realizar:"))
    if operation == 1:
        print("Resultado suma:", n1 + n2)

    elif operation == 2:
        print("Resultado resta:", n1 - n2)

    elif operation == 3:
        print("Resultado multiplicación:", n1 * n2)

    elif operation == 4:
        print("Resultado división:", n1 / n2)

    elif operation == 5:
        print("La calculadora se ha apagado.")
        start = False

    else:
        print("No se realizó su operación.")
