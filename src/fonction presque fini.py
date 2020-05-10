import random
import math
moustiques=1500000
humains=6900000
humainsMalades=200000
jours=1

def liste_moustiques_jour (nM,j):
#liste des jours de naissance de nM moustiques
    L=[]
    for i in range (0,nM):
        L.append(j)
    return L

def liste_moustiques_adulte (nM):
#liste de nM moustiques
#False pour peut pas encore piquer et True peut piquer
    L=[]
    for i in range (0,nM):
        L.append(True)
    return L

def liste_humains_jour (nH,j):
#liste de nH humains (jour de l'etat)
#S (pour Susceptible)
#M (pour Malade)
#I (pour Immunisée)
    L=[]
    for i in range (0,nH):
        L.append(j)
    return L

def liste_humains_etat (L,nH,etat):
#liste de nH humains (etat)
#S (pour Susceptible)
#M (pour Malade)
#I (pour Immunisée)
    for i in range (0,nH):
        L.append(etat)
    return L

def esperance_moustique (jour_de_naissance,j):
    return (jour_de_naissance+19+15==j)

def natalite_moustique_jour (j,listeM):
#12 larves/moustique/jour
    for i in range (0,12):
        listeM.append(j)
    return listeM

def natalite_moustique_adulte (listeM):
#12 larves/moustique/jour
    for i in range (0,12):
        listeM.append(False)
    return listeM

def nb_pique (listeM):
    res=0
    for adulte in listeM:
        if (adulte):
            res=res+1
    return res

def surmortalite_jour (listeMj,listeMa,nM):
    M=math.floor(0.80*nM)
    for i in range (0,len(listeMj)):
        if(listeMa[i]) and (M!=0):
            listeMj[i]=1010
            M=M-1
    return listeMj

def surmortalite_adulte (listeMj,listeMa,nM):
    M=math.floor(0.80*nM)
    for i in range (0,len(listeMj)):
        if(listeMj[i]==1010) and (M!=0):
            listeMa[i]=False
            M=M-1
    return listeMa

def malade_jour (listeHj,listeHe,nbPiqure,j):
    n=0
    for i in range (0,len(listeHj)):
        if (n!=nbPiqure) and (listeHe[i]=="S"):
            listeHj[i]=j
        n=n+1
    return listeHj

def malade_etat (listeHj,listeHe,nbPiqure,j):
    n=0
    for i in range (0,len(listeHe)):
        if (n!=nbPiqure) and (listeHe[i]=="S"):
            listeHe[i]="M"
        n=n+1
    return listeHe

def immunite(j,jour_de_letat):
#guérison: 3 à 5 jours
    a=random.randint(3,5)
    return (j-jour_de_letat==a)

def plus_immunise(j,jour_de_letat):
    return (j-jour_de_letat==1)

def fonction():
    LMJ=liste_moustiques_jour(moustiques,1)
    LMA=liste_moustiques_adulte(moustiques)
    LHJ=liste_humains_jour(humains,1)
    LHE=[]
    LHE=liste_humains_etat(LHE,humains-humainsMalades,"S")
    LHE=liste_humains_etat(LHE,humainsMalades,"M")

    for jour in range (1,jours+1):

        for i in range (0,len(LMJ)):
            #transformation
            if (LMJ[i]+19==jour):
                LMA[i]=True

            #natalite
            if (LMA[i]):
                LMA=natalite_moustique_adulte(LMA)
                LMJ=natalite_moustique_jour(jour,LMJ)

            #esperance
            if (esperance_moustique(LMJ[i],jour)):
                LMJ[i]=999
                LMA[i]=False

        #surmortalite
        LMJ=surmortalite_jour(LMJ,LMA,len(LMJ))
        LMA=surmortalite_adulte(LMJ,LMA,len(LMJ))

        #nbPiqure
        piqure=nb_pique(LMA)
        if (piqure!=0):
            #infection
            n=0
            for i in range (0,len(LHJ)):
                if (n!=piqure) and (LHE[i]=="S"):
                    LHE[i]="M"
                    LHJ[i]=jour
                n=n+1

                #immunite
                if (immunite(jour,LHJ[i])):
                    LHE[i]="I"
                    LHJ[i]=jour

                #plus_immunise
                if (plus_immunise(jour,LHJ[i])):
                    LHE[i]="S"
                    LHJ[i]=jour
        else:
            return []

    return LHE

def main():
    if (fonction()==[]):
        print("!!! ERADICATE !!!")
    #else: print(fonction())
main()
