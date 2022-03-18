def calc_moyenne(tab):
        somme = 0
        moyenne = 0
        for i in range(len(tab)):
                somme += tab[i]
        moyenne = somme/len(tab)
        return moyenne


def calc_val_sup(tab,val):
        nb_val_sup = 0
        for i in range(len(tab)):
                if tab[i] > val:
                        nb_val_sup += 1
        return nb_val_sup

def calc_val_inf(tab,val):
        nb_val_inf = 0
        for i in range(len(tab)):
                if tab[i] < val:
                        nb_val_inf += 1
        return nb_val_inf
