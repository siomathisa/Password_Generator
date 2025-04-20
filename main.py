import tkinter as tk
from tkinter import messagebox, filedialog
import random

# Caractères disponibles
lettres_majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettres_minuscules = lettres_majuscules.lower()
chiffres = "0123456789"
symboles = "!?$.%*#@{}()[]"

mdp_list = []

# ---------- FONCTIONS ----------

def generer_mdp():
    try:
        longueur = int(entry_longueur.get())
        nombre = int(entry_nombre.get())

        # Création du pool de caractères
        pool = ""
        if var_maj.get():
            pool += lettres_majuscules
        if var_min.get():
            pool += lettres_minuscules
        if var_chiffres.get():
            pool += chiffres
        if var_speciaux.get():
            pool += symboles

        if not pool:
            messagebox.showwarning("Alerte", "Veuillez sélectionner au moins un type de caractère.")
            return

        resultats.delete(1.0, tk.END)
        mdp_list.clear()

        for _ in range(nombre):
            mdp = ''.join(random.choice(pool) for _ in range(longueur))
            mdp_list.append(mdp)
            resultats.insert(tk.END, mdp + '\n')

        # Lancer animation de "flash"
        flash_resultats()

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

def copier_presse_papier():
    mdps = resultats.get(1.0, tk.END).strip()
    if mdps:
        fenetre.clipboard_clear()
        fenetre.clipboard_append(mdps)
        messagebox.showinfo("Copié", "Mots de passe copiés dans le presse-papier.")

def sauvegarder_fichier():
    if not mdp_list:
        messagebox.showwarning("Alerte", "Aucun mot de passe généré.")
        return
    fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichier texte", "*.txt")])
    if fichier:
        with open(fichier, 'w') as f:
            for mdp in mdp_list:
                f.write(mdp + '\n')
        messagebox.showinfo("Sauvegardé", f"Mots de passe sauvegardés dans {fichier}")

def flash_resultats():
    # Petit effet visuel quand on génère
    def flash(i):
        if i % 2 == 0:
            resultats.config(bg="#2e2e2e")
        else:
            resultats.config(bg="#3e3e3e")
        if i < 4:
            fenetre.after(100, lambda: flash(i + 1))
    flash(0)

# ---------- INTERFACE GRAPHIQUE ----------

fenetre = tk.Tk()
fenetre.title("🖤 Générateur de mots de passe - Dark Mode")
fenetre.geometry("500x550")
fenetre.config(bg="#1e1e1e")

# Mode sombre par défaut
fenetre.config(bg="#1e1e1e")
resultats = tk.Text(fenetre, height=10, width=55, bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff", font=("Consolas", 10))
resultats.pack()

# Labels + Inputs
tk.Label(fenetre, text="Longueur du mot de passe :", bg="#1e1e1e", fg="#ffffff", font=("Segoe UI", 10)).pack(pady=5)
entry_longueur = tk.Entry(fenetre, bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff", font=("Segoe UI", 10))
entry_longueur.pack(pady=2)

tk.Label(fenetre, text="Nombre de mots de passe :", bg="#1e1e1e", fg="#ffffff", font=("Segoe UI", 10)).pack(pady=5)
entry_nombre = tk.Entry(fenetre, bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff", font=("Segoe UI", 10))
entry_nombre.pack(pady=2)

tk.Label(fenetre, text="Inclure dans le mot de passe :", bg="#1e1e1e", fg="#ffffff", font=("Segoe UI", 10)).pack(pady=10)

# Checkboxes
var_maj = tk.BooleanVar(value=True)
var_min = tk.BooleanVar(value=True)
var_chiffres = tk.BooleanVar(value=True)
var_speciaux = tk.BooleanVar()

tk.Checkbutton(fenetre, text="Lettres majuscules", variable=var_maj, bg="#1e1e1e", fg="#ffffff", selectcolor="#1e1e1e").pack()
tk.Checkbutton(fenetre, text="Lettres minuscules", variable=var_min, bg="#1e1e1e", fg="#ffffff", selectcolor="#1e1e1e").pack()
tk.Checkbutton(fenetre, text="Chiffres", variable=var_chiffres, bg="#1e1e1e", fg="#ffffff", selectcolor="#1e1e1e").pack()
tk.Checkbutton(fenetre, text="Caractères spéciaux", variable=var_speciaux, bg="#1e1e1e", fg="#ffffff", selectcolor="#1e1e1e").pack()

# Boutons
tk.Button(fenetre, text="🎲 Générer", command=generer_mdp, bg="#444444", fg="#ffffff", activebackground="#666666", activeforeground="#ffffff", relief="flat", font=("Segoe UI", 10)).pack(pady=10)
tk.Button(fenetre, text="📋 Copier", command=copier_presse_papier, bg="#444444", fg="#ffffff", activebackground="#666666", activeforeground="#ffffff", relief="flat", font=("Segoe UI", 10)).pack(pady=5)
tk.Button(fenetre, text="💾 Sauvegarder", command=sauvegarder_fichier, bg="#444444", fg="#ffffff", activebackground="#666666", activeforeground="#ffffff", relief="flat", font=("Segoe UI", 10)).pack(pady=5)

# Résultats
tk.Label(fenetre, text="Résultats :", bg="#1e1e1e", fg="#ffffff", font=("Segoe UI", 10)).pack(pady=10)

# Lancer l'app
fenetre.mainloop()
