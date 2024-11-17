num = int(input("Dime un número entre el 1 y 5: "))
if num > 5 or num < 1:
    print("[ERROR]")
else:
    if num % 2==0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} es impar")