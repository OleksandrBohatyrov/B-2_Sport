from random import *
def Lisa_Andmed(sportlased:list,tulemused:list):
    """Lisa sportlasi
    :param list s: sportlased 
    :param list p: tulemused 
    :rtype: list, list
    """

    n = int(input("Enter the number of athletes: "))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        tulemus=(randint(1, 100) for _ in range(3))
        result=max(tulemus)
        sportlased.append(nimi)
        tulemused.append(result)
    return sportlased, tulemused


def Soorteerimine(i:list,p:list):
    """Järjesta kasvavalt
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: int, str
    """

    n=len(p)
    for j in range(0,n-1):
        for k in range(j+1,n):
            if p[j]>p[k]:
                abi=p[j]
                p[j]=p[k]
                p[k]=abi
                abi=i[j]
                i[j]=i[k]
                i[k]=abi

    return i,p


def nimiResult(sportlased:list,tulemused:list):
    """Otsi nime järgi
    :param list s: sportlased 
    :param list p: tulemused 
    :rtype: list, list
    """
    nimi=input("Print nimi ")
    nimiList = []
    for j in range(len(sportlased)):
        if sportlased[j] == nimi:
            nimiList.append(tulemused[j])
    
    print (nimi,"result on",nimiList) 



def Kustutamine(sportlased:list,tulemused:list):
    """Eemaldage nimekirjast sportlane, kelle tulemus on alla 15
    :param list s: sportlased 
    :param list p: tulemused 
    :rtype: list, list
    """

    
    Kustutamine = [i for i, score in enumerate(tulemused) if score < 15]
    if Kustutamine:
        print("Järgmised sportlased on diskvalifitseeritud:")
        for i in reversed(Kustutamine):
            athlete_name = sportlased.pop(i)
            score = tulemused.pop(i)
            print(f"- {athlete_name}: {score}")
    else:
        print("Ühtegi sportlast ei diskvalifitseeritud.")

def Top3(sportlased:list,tulemused:list):
    """Top3
    :param list s: sportlased 
    :param list p: tulemused 
    :rtype: list, list
    """
    results = [(sportlased[i], tulemused[i]) for i in range(len(sportlased))]
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    top_results = sorted_results[:3]
    print("Top 3 results:")
    for i, (athlete, score) in enumerate(top_results):
        print(f"{i+1}. {athlete}: {score}")
    return top_results


def Vähem_Result(sportlased:list,tulemused:list):
    """Halvim tulemus
    :param list s: sportlased 
    :param list p: tulemused 
    :rtype: list, list
    """

    result=min(tulemused)
    ind=p.index(tulemused)
    nimi=sportlased[ind]

    return sportlased, tulemused