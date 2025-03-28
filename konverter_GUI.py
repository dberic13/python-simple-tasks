import requests # Biblioteka za rad s API-jem
import tkinter as tk # Tkinter za grafičko sučelje
from tkinter import ttk, messagebox # Napredni widgeti i poruke

API_KEY = "bd13f3d28c13cc8f9a940a9c" # API ključ
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/" # URL za dohvaćanje tečaja

def dohvatiTecaj(valuta):
    url = BASE_URL + valuta # Stvara URL za određenu valutu
    response = requests.get(url) # Šalje zahtjev API-ju

    if response.status_code == 200: # Ako je odgovor uspješan
        return response.json()["conversion_rates"] # Vraća tečajeve u JSON formatu
    else:
        messagebox.showerror("Greška", "Neuspješno dohvaćanja tečajeva!") # Prikazuje grešku
        return None # Vraća praznu vrijednost ako API ne radi

def konvertiraj():

    try:
        iznos = float(entry_iznos.get()) # Dohvaća uneseni iznos i pretvara u broj
        valuta = combo_u.get() # Dohvaća valutu iz padajućeg izbornika
        valutaKonverzija = combo_k.get() # Dohvaća ciljanju valutu iz padajućeg izbornika

        # Ako su iste valute, prikazuje upozorenja

        if valuta == valutaKonverzija:
            messagebox.showwarning("Upozorenje", "Odaberite različite valute!")
            return
        
        # Dohvaćanje tečajeva iz API-ja

        tecajevi = dohvatiTecaj(valuta)

        # Ako su podaci uspješno dohvaćeni, vrši izračun

        if tecajevi and valutaKonverzija in tecajevi:
            iznosKonverzija = iznos * tecajevi[valutaKonverzija] # Računa konverziju 
            label_rezultat.config(text=f"{iznos:.2f} {valuta} je {iznosKonverzija:.2f} {valutaKonverzija}") # Prikazuje rezultat
        else:
            messagebox.showerror("Greška", "Nevažeća valuta ili problem s API-jem.") # Ako API ne radi, prikazuje grešku
    except ValueError:
        messagebox.showerror("Greška", "Molimo unesite ispravan broj!") # Ako korisnik unese nešto što nije broj

# Postavljanje glavnog Tkinter prozora
root = tk.Tk()
root.title("Konverter valuta") # Naziv prozora
root.geometry("400x300") # Veličina prozora
    
# Unos iznosa
tk.Label(root, text="Unesite iznos:", font=("Arial", 12)).pack(pady=5) # Tekstualna oznaka
entry_iznos = tk.Entry(root, font=("Arial", 12)) # Polje za unos iznosa
entry_iznos.pack(pady=5)
    
# Padajući izbornici za valute
valute = ["EUR", "USD", "HRK", "GBP", "JPY", "AUD", "CAD", "CNY", "NZD", "RUB"] # Popis valuta

tk.Label(root, text="Iz valute:", font=("Arial", 12)).pack(pady=5) # Tekstualna oznaka za ulaznu valutu
combo_u = ttk.Combobox(root, values=valute, font=("Arial", 12)) # Padajući izbornik za ulaznu valutu
combo_u.pack()

tk.Label(root, text="U valutu:", font=("Arial", 12)).pack(pady=5) # Tekstualna oznaka za izlaznu valutu
combo_k = ttk.Combobox(root, values=valute, font=("Arial", 12)) # Padajući izbornik za izlaznu valutu
combo_k.pack()

# Gumb za konverziju
btn_konvertiraj = tk.Button(root, text="Konvertiraj", font=("Arial", 12), command=konvertiraj) # Gumb za konverziju
btn_konvertiraj.pack(pady=10)

# Prikaz rezultata
label_rezultat = tk.Label(root, text="", font=("Arial", 14, "bold")) # Tekstualna oznaka za rezultat
label_rezultat.pack(pady=10)

# Pokretanje glavnog prozora
root.mainloop()