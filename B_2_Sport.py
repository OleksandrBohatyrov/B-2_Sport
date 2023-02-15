from module import *


sportlased=["A","B","C"]
tulemused=[10,20,50]

print(sportlased)
print(tulemused)
while True:
    menu=int(input("n1-Lisa sportlasi\n2-Järjesta kasvavalt\n3-Otsi nime järgi\n4-Eemaldage nimekirjast sportlane, kelle tulemus on alla 15\n5-Top 3\n6-Halvim tulemus"))
    if menu==0:
        break
    elif menu==1:
        Lisa_Andmed(sportlased,tulemused)
    elif menu==2:
        Soorteerimine(sportlased,tulemused)
    elif menu==3:
        nimiResult(sportlased,tulemused)
    elif menu==4:
        Kustutamine(sportlased,tulemused)
    elif menu==5:
        Top3(sportlased,tulemused)
    elif menu==6:
        Vähem_Result(sportlased,tulemused)
    else:
        print("Error")