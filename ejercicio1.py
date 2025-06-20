#implementar una calculadoraquepida

num_1 = float(input("primer numero a consultar: "))
num_2 = float(input("segundo numero a consultar: "))
operador = input("Que operacion vas a hacer? (+,-,/,*): ")

#comoasique que switch y case?
#switch y case es una forma diferente de escribir condicionales, donde se evalua un parametro, booleano y se va a direccionar inmediatamente segun los casos definidos

match operador:
    case "+":
        print("resultado", num_1 + num_2)
    case "-":
        print("resultado", num_1 - num_2)
    case "*":
        print("resultado", num_1 * num_2)
    case "/":
        if num_2 != 0:
            print("resultado", num_1 / num_2)
        else:
            print("resultado no valido")
    case _:
        print("resultado no valido")
        