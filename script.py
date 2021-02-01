# Ce script gère les intéractions avec l'utilisateur

from prettytable.prettytable import PrettyTable
import calcul as ca
import pip

# Installe les packages requis pour faire fonctionner les scripts
def import_or_install(packages):
    for package in packages:
        try:
            __import__(package)
            print("Found Package", package, "!")
        except ImportError:
            pip.main(['install', package])

packages = ["prettytable","pyautogui"]
liste_valeurs = []

import_or_install(packages)

valeur = "ohayo gozaimasu"

while True:
    valeur = input("Entrez une valeur à ajouter à la liste. (Entrez un charactère/mot pour arrêter) : ")
    try:
        valeur = float(valeur)
        liste_valeurs.append(valeur)
        print(liste_valeurs)
    except:
        break

etendue = ca.calcEtendue(liste_valeurs)
nbDeClasse = ca.calcNbClasse(liste_valeurs)
amplitude = ca.calcAmplitude(etendue, nbDeClasse)
print("Étendue : ", etendue)
print("Nombre de classe : ", nbDeClasse)
print("Amplitude : ", amplitude)
print("Total des valeurs : ", ca.calcTotalValeurs(liste_valeurs))

dist_table = PrettyTable()
effectif = ca.creerEffectifs(nbDeClasse, liste_valeurs, amplitude)
freq_relative = ca.creerFreqRel(effectif, len(liste_valeurs))
freq_rel_comm = ca.creerFreqRelComm(freq_relative)
dist_table.add_column("Classes", ca.creerClasses(nbDeClasse, liste_valeurs, amplitude))
dist_table.add_column("Effectif", effectif)
dist_table.add_column("Fréquence relative (%)", freq_relative)
dist_table.add_column("Fréq. Rel. Commune", freq_rel_comm)

dist_table.add_row(["","","",""])
dist_table.add_row(["Total: ", sum(effectif), sum(freq_relative), "-"])
print(dist_table)