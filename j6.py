a = int(input("sonni kiriting: "))

d = input("Uzunlik birligini kiriting: ")
s=""
match d:
    case "dm":
        s=a * 10
    case 'sm':
        s=a * 100
    case 'mm':
        s=a * 1000
   
    case _:
        
        s="notug`ri kiritildi"
print("Natija: ",s,"m")