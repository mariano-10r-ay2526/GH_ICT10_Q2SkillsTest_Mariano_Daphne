from pyscript import document

def nonmetals(e):
    document.getElementById('result').innerHTML = ''
    favorite_game = document.getElementById('dictionary').value.lower().strip()

    all_nonmetals = {
        'He':'Helium, 2, 4.002602 u',
        'Kr':'Krypton, 36, 83.798 ± 0.002 u',
        'H':'Hydrogen, 1, 1.00784 u',
        'Xe':'Xenon, 54, 131.293 u',
        'Ne':'Neon, 10, 20.18 u',
        'Ar':'Argon, 18, 39.948 u',
        'Cl':'Chlorine, 17, 35.45 u',
        'I':'Iodine, 53, 126.90447 u',
        'Br':'Bromine, 35, 79.904 u',
        'Og':'Oganesson, 118, 294 u',
        'At':'Astatine, 85, 210 u',
        'Ts':'Tennessine, 117, 294 u',
        'C':'Carbon, 6, 12.011 u',
        'N':'Nitrogen, 7, 14.007 u',

    }