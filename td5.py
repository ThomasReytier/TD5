def nb_moyenne(tab):
    somme = 0
    moyenne = 0
    nb_val_sup = 0
    nb_val_inf = 0
    for i in range(len(tab)):
        somme += tab[i]
    moyenne = somme/len(tab)
    for i in range(len(tab)):
        if tab[i] > moyenne:
            nb_val_sup += 1
    for i in range(len(tab)):
        if tab[i] < moyenne:
            nb_val_inf += 1
    return moyenne, nb_val_sup, nb_val_inf

