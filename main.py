import random

# Listes de caractères utilisables
lettre = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffre = "0123456789"
symbole = "!?$.%*#@{}()[]"
caractere = lettre + lettre.lower() + chiffre + symbole
caractere_sans_symbole = lettre + lettre.lower() + chiffre

while True:
    # Demander la longueur du mot de passe et le nombre de mots de passe à générer
    longueurMdp = int(input("Entrez la longueur du mot de passe : "))
    nombreDeMdp = int(input("Entrez le nombre de mots de passe : "))
    
    # Demander si l'utilisateur veut des caractères spéciaux
    caractere_speciaux = input("Voulez-vous des caractères spéciaux (oui/non) ? : ").lower()
    
    if caractere_speciaux == 'oui':
        for i in range(nombreDeMdp):
            mdp = ""
            # Générer un mot de passe avec des caractères spéciaux
            for j in range(longueurMdp):
                caracteremdp = random.choice(caractere)
                mdp += caracteremdp
            print("Votre mot de passe est : ", mdp)
    elif caractere_speciaux == 'non':
        for i in range(nombreDeMdp):
            mdp = ""
            # Générer un mot de passe sans caractères spéciaux
            for j in range(longueurMdp):
                caracteremdp = random.choice(caractere_sans_symbole)
                mdp += caracteremdp
            print("Votre mot de passe est : ", mdp)
    else:
        print("Veuillez répondre par oui ou non")
        continue  # Recommence la boucle si l'utilisateur n'a pas répondu correctement
    
    # Demander si l'utilisateur souhaite continuer
    continuer = input("Voulez-vous générer d'autres mots de passe (oui/non) ? : ").lower()
    if continuer != 'oui':
        print("Fin du programme.")
        break
