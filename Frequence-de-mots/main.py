# Un programme qui lit un fichier texte 
# et affiche les 5 mots les plus fréquents

# 1. Ouvrir le fichier
#2. Lire le contenu
#3. Nettoyer le texte (minuscules + ponctuation)
#4. Découper en mots
#5. Compter les occurrences avec un dictionnaire
#6. Trier le dictionnaire par valeurs décroissantes
#7. Prendre les 5 premiers
#8. Afficher le résultat 


import re
from collections import  Counter

def frequencedemot(file, nbre_mots=5):
    try:
        with open(file, "r", encoding="utf-8")     as f:
            contenu = f.read()
            
            if not contenu.strip():
                print("Le fichier est vide")
                return
            
            # Nettoyer le texte
            nettoyer_text = re.sub(r"[^\w\s]", " ", contenu.lower())
            mots = nettoyer_text.split()
             
             # Mots vides
            mots_vides = {"l", "le", "la", "les", "a", "des", "un", "une", "de", "d", "du", "au", "en", "et", "est", "à", "par", "pour", "sur", "avec"}   
            mots_filtres = [mot for mot in mots if mot not in mots_vides and len(mot) > 1]   
            
            if not mots_filtres:
                print("Aucun mot valide trouvé")
                 
            frequence = Counter(mots_filtres)
            #mots_tries = sorted(frequence.items(), key=lambda x : x[1], reverse=True)
            
            #print("== FREQUENCES DES MOTS ==\n")
#            for mot, count in mots_tries:
#                print(f"{mot}: {count}")  
            
            print(f"\n== LES {nbre_mots} MOTS LES PLUS FREQUENTS ==\n")  
            #top_5 = mots_tries[:5]
#            for mot_5, count_5 in top_5:
#                print(f"{mot_5}: {count_5}")
            top_mots = frequence.most_common(nbre_mots)
            for key, value in top_mots :  
                print(f"{key}: {value}")
                 
    except FileNotFoundError:
        print("File Not Found")
    except Exception as e:
        print(f"Erreur: {e}")


frequencedemot("./file/text.txt", 10)