from app.utils import saluer
import sys 

valeurGlobale = 1

def ma_fonction():
    valeur_locale = 2
    print(valeur_locale)

def main():
    
    print("Début d'exécution du programme....")
    saluer("Alphonse")
    if len(sys.argv) > 1:
        print(f"Arguments de la ligne de commande: {sys.argv[0:]}")
    else:
        print("Aucun argument de la ligne de commande fourni.")
        
    print(valeurGlobale)
    ma_fonction()
    age = 25
    print("Alice a", age, "ans")
    print(f"Alice a {age} ans")
    
    #Formatage avancé
    print("Alice a {} ans et Bob a {} ans".format(age, age +5))
    
    
    stat_result = (7802 + 4752)/12700
    print("la stat finale est: ",stat_result)
    print(f"la stat finale est: {stat_result: .2f}")
    print(f"la stat finale est: {stat_result: 3f}.")
    print(f"la stat finale est: {stat_result: .0f}")
    
    print(f"{10:->8d}")

    entier = 2
    print(f"le type de {entier} est {type(entier)}")
    
    # list tableau que l'on peut modifier
    fruits = ["pomme", "banane", "cerise"]
    print(f"le type de {fruits} est {type(fruits)}")
    
    # tuple tableau immuable
    coordonnees = (10.0, 20.0)
    print(f"le type de {coordonnees} est {type(coordonnees)}")
    
    #range (over utilisé), pratique pour boucler
    nombres = range(5)
    print(f"le type de {nombres} est {type(nombres)}")
    
    #dictionary
    etudiant = {"nom": "Alice", "age": 25}
    print(f"le type de {etudiant} est {type(etudiant)}")
    
    #bool
    est_vrai = True
    est_faux = False
    print(f"le type de {est_vrai} est {type(est_vrai)}")
    print(f"le type de {est_faux} est {type(est_faux)}")
    
    #None
    rien = None
    print(f"le type de {rien} est {type(rien)}")
    
    print(f"{int("125")}") # fonction de transtypage : type(ce qu'il faut transtyper)
    
    #operateurs
    print(f"{5//6}")
    
    

if __name__ == "__main__":
    main()