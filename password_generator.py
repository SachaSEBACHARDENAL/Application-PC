import tkinter as tk
import random
import string

# Fonction pour générer un mot de passe
def generate_password():
    length = int(password_length.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_display.delete(0, tk.END)
    password_display.insert(0, password)

# Fonction pour copier le mot de passe dans le presse-papiers
def copy_password():
    root.clipboard_clear()  # Efface le presse-papiers
    root.clipboard_append(password_display.get())  # Ajoute le mot de passe au presse-papiers
    root.update()  # Met à jour l'interface

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de mot de passe")

# Configuration de la taille de la fenêtre
root.geometry("450x250")
root.config(bg="#f0f0f0")

# Titre de l'application
title_label = tk.Label(root, text="Générateur de Mot de Passe", font=("Helvetica", 16), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# Label pour la longueur du mot de passe
label_length = tk.Label(root, text="Longueur du mot de passe : ", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
label_length.pack(pady=5)

# Entrée pour spécifier la longueur du mot de passe
password_length = tk.Entry(root, font=("Helvetica", 12), width=10, justify="center")
password_length.pack(pady=5)

# Champ de texte pour afficher le mot de passe généré
password_display = tk.Entry(root, font=("Helvetica", 12), width=40, justify="center", bd=2, relief="sunken")
password_display.pack(pady=15)

# Bouton pour générer le mot de passe
generate_button = tk.Button(root, text="Générer", font=("Helvetica", 12), command=generate_password, bg="#4CAF50", fg="white", bd=0, relief="raised", width=15)
generate_button.pack(pady=10)

# Bouton pour copier le mot de passe
copy_button = tk.Button(root, text="Copier", font=("Helvetica", 12), command=copy_password, bg="#008CBA", fg="white", bd=0, relief="raised", width=15)
copy_button.pack(pady=10)

# Lancer l'application
root.mainloop()
