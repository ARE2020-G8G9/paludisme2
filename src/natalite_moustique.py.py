def natalite_moustique (nbMoustiques,j):
#12,3 larves/moustique/jour
#environ 20 jours pour passer de larve à adulte
    totM=nbMoustiques
    for jour in range (1,j):
        if (jour%20==0):
            totM=totM+totM*12,3
        i=i+1
    return totM
