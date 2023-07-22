y = input("Harfni kiriting (s,j,sh,g`): ")
k = input("Raqamni kiriting(0,1,2): ")
s = ""
match y:
    case "s":
        s = "shimol"
    case "j":
        s = "janub"
    case "sh":
        s = "sharq"
    case "g`":
        s = "g`arb"
      
    case _:
        
        s="Notug`ri kiritildi"
print(s)


match k:
    case "0":
        s = "Harakatni davom ettir: "
    case "1":
        s = "Chapga buril"
    case "2":
        s = "O`ngga buril"
    case _:

        s="Notug`ri kiritildi"
print(s)