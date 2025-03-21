import json

fichier = "contacts.json"

def charger_contacts():
    try:
        with open(fichier, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def sauvegarder_contact(contacts):
    with open(fichier, "w") as f:
        json.dump(contacts, f, indent=4)    

def ajouter_contact():
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    age = input("Age : ")
    ville = input("Ville : ")

    contacts.append({"nom": nom, "prenom": prenom, "age": age, "ville": ville})
    sauvegarder_contact(contacts)
    print("Contact ajouté !")

def afficher_contacts():
    if not contacts:
        print("Aucun contact enregistré.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['nom']} {contact['prenom']} - {contact['age']} - {contact['ville']}")

def supprimer_contact():
    afficher_contacts()
    try: 
        index = int(input("Numéro du contact à supprimer : ")) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            sauvegarder_contact(contacts)
            print("Contact supprimé!")
        else:
            print("Numéro ivalide")
    except ValueError:
        print("Entrée invalide")        

def menu():
    while True:
        print("\n--- Gestionnaire de Contacts ---")
        print("1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Supprimer un contact")
        print("4. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            supprimer_contact()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Exécution du programme
contacts = charger_contacts()
menu()        

    
