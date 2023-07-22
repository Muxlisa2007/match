
a = int(input("Bahoni kiriting - > "))
s=""
match a:
    case 1:
        s="Yomon"
    case 2:
        s="Qoniqarsiz"
    case 3:
        s="Qoniqarli"
    case 4:
        s="Yaxshi"
    case 5:
        s="A`lo"
    case _:
        
        s="raqam notug`ri kiritildi"
print(s)