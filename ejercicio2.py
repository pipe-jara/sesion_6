num_1 = float(input("primer numero a consultar: "))
num_2 = float(input("segundo numero a consultar: "))
operador = input("Que operacion vas a hacer? (+,-,/,*): ")

if operador == "+":
    print("resultado", num_1 + num_2)
elif operador == "-":
    print("resultado", num_1 - num_2) 
elif operador == "*":
    print("resultado", num_1 * num_2) 
elif operador == "/":
    if num_2 != 0:
            print("resultado", num_1 / num_2)
    else:
         print("error dividiendo por cero")
else:
     print("operacion no valida ")