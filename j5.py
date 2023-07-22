a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

d = input("amalni kiriting: ")
s=""
match d:
    case '+':
        s=a + b
    case '-':
        s=a - b
    case '*':
        s=a * b
    case '/':
        s=a / b
    case _:
        
        s="amal notug`ri kiritildi"
print("Natija: ",s)
