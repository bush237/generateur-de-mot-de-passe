import random  # Importation de la bibliothèque random pour générer des caractères aléatoires
import string  # Importation de la bibliothèque string pour utiliser des chaînes de caractères prédéfinies

def generate_password(length, uppercase, lowercase, numbers, symbols):
    characters = ""  # Chaîne de caractères qui contiendra tous les caractères possibles du mot de passe

    if uppercase:
        characters += string.ascii_uppercase  # Ajoute les lettres majuscules si spécifié
    if lowercase:
        characters += string.ascii_lowercase  # Ajoute les lettres minuscules si spécifié
    if numbers:
        characters += string.digits  # Ajoute les chiffres si spécifié
    if symbols:
        characters += "!@#§%^&*"  # Ajoute les symboles si spécifié

    if not characters:
        print("Veuillez sélectionner au moins un type de caractère.")  # Affiche un message d'erreur si aucun type de caractère n'est sélectionné
        return ""  # Retourne une chaîne vide

    # Génère le mot de passe en choisissant aléatoirement des caractères parmi ceux disponibles
    password = ''.join(random.choice(characters) for _ in range(length))
    return password  # Retourne le mot de passe généré

def main():
    # Demande à l'utilisateur d'entrer la longueur du mot de passe et convertit en entier
    length = int(input("Entrez la longueur souhaitée pour votre mot de passe : "))

    # Demande à l'utilisateur s'il veut inclure des majuscules et convertit la réponse en booléen
    uppercase = input("Inclure des majuscules ? (o/n) : ").lower() == 'o'
    
    # Demande à l'utilisateur s'il veut inclure des minuscules et convertit la réponse en booléen
    lowercase = input("Inclure des minuscules ? (o/n) : ").lower() == 'o'
    
    # Demande à l'utilisateur s'il veut inclure des chiffres et convertit la réponse en booléen
    numbers = input("Inclure des chiffres ? (o/n) : ").lower() == 'o'
    
    # Demande à l'utilisateur s'il veut inclure des symboles et convertit la réponse en booléen
    symbols = input("Inclure des symboles ? (o/n) : ").lower() == 'o'
    
    # Demande à l'utilisateur combien de mots de passe il souhaite générer
    num_passwords = int(input("Combien de mots de passe souhaitez-vous générer ? "))

    # Boucle pour générer et afficher le nombre de mots de passe demandé
    for _ in range(num_passwords):
        password = generate_password(length, uppercase, lowercase, numbers, symbols)
        if password:
            print("Vos mot de passe généré : ", password)

# Point d'entrée du programme
if __name__ == "__main__":
    main()  # Appelle la fonction main() pour exécuter le programme

# Signature personnelle
# Code écrit par [ABOLO BORIS GRAIG], [24A41FS]
