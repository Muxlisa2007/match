a = int(input("sonni kiriting: "))

d = input("Og`irlik birligini kiriting: ")
s=""
match d:
    case "mg":
        s=a * 1000000
    case 'g':
        s=a * 1000
    case 't':
        s=a / 1000
    case "sr":
        s = a / 100
   
    case _:
        
        s="notug`ri kiritildi"
print("Natija: ",s,"kg")