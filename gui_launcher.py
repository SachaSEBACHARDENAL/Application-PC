import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import random
import string

# Fonction pour générer un mot de passe
def generate_password():
    length = 16
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Mot de passe : {password}")

# Fonction pour exécuter le script d'audit sécurité (PowerShell)
def run_audit_script():
    try:
        script_path = "audit_security.ps1"
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path], check=True)
        messagebox.showinfo("Succès", "Audit terminé. Voir la console PowerShell pour les résultats.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Fonction pour exécuter le scan réseau (Python avec nmap)
def run_network_scan():
    try:
        subprocess.run(["python", "network_scan.py"], check=True)
        messagebox.showinfo("Succès", "Scan réseau terminé. Voir la console pour les résultats.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Interface GUI
root = tk.Tk()
root.title("CyberTools Lite")
root.geometry("400x300")

tk.Label(root, text="CyberTools Lite", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="🔐 Générer un mot de passe", command=generate_password).pack(pady=5)
tk.Button(root, text="🛡️ Audit sécurité poste Windows", command=run_audit_script).pack(pady=5)
tk.Button(root, text="🌐 Scan réseau (nmap)", command=run_network_scan).pack(pady=5)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

root.mainloop()
