# Contient plusieurs fonctions de maths
import math
from prettytable import PrettyTable

# Trouve l'étendue
def calcEtendue(liste_valeurs):
    valMin = min(liste_valeurs)
    valMax = max(liste_valeurs)

    if(valMin > valMax):
        raise Exception("La valeur de max est plus petite que c'elle de min")
    
    return valMax - valMin;

# Calcule le nombre de classes avec la regle de Sturges
def calcNbClasse(liste_valeurs):
    total = len(liste_valeurs)

    reponse = 1 + (math.log(total,2))
    reponse = round(reponse)
    return reponse

# Trouve l'amplitude
def calcAmplitude(etendue, nbClasse):
    return round(etendue / nbClasse)

# Trouve le nombre total de valeurs dans une liste
def calcTotalValeurs(valeurs):
    total = 0
    if(isinstance(valeurs, list)):
        for values in valeurs:
            total = total + values
    else:
        raise Exception("Le parametre entrée n'est pas une liste.")
    return total

# Créer une liste en fonciton des classes données.
def creerClasses(nbDeClasse, valeurs, amplitude):
    classes = []
    val_min = min(valeurs)

    for classe in range(0, nbDeClasse, 1):
        ligne = "["
        ligne = ligne + str(math.trunc(val_min + (classe * amplitude)))
        ligne = ligne + ", " + str((math.trunc(val_min + (amplitude * (classe + 1))))) + "["
        classes.append(ligne)
    
    return classes

# Créer une liste qui contient les effectifs 
def creerEffectifs(nbDeClasse, valeurs, amplitude):
    effectifs = []
    valDebut= min(valeurs)

    for classe in range(0, nbDeClasse, 1):
        val_min = math.trunc(valDebut + (classe * amplitude))
        val_max = math.trunc(valDebut + (amplitude * (classe + 1)))
        compteur = 0
        for valeur in valeurs:
            if(valeur < val_max):
                if(valeur >= val_min):
                    compteur += 1
        effectifs.append(compteur)

    return effectifs

# Créer la fréquence relative
def creerFreqRel(effectifs, total):
    frequence = []
    for effectif in effectifs:
        freq = effectif / total * 100
        frequence.append(freq)
    
    return frequence

# Créer la fréquence relative commune
def creerFreqRelComm(freqs_rel):
    frequence = []
    total_actuel = 0
    for freq_rel in freqs_rel:
        total_actuel += freq_rel
        frequence.append(total_actuel)
    
    return frequence