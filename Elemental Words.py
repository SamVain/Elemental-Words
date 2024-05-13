ELEMENTS = {
    'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be': 'Beryllium', 'B': 'Boron',
    'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen', 'F': 'Fluorine', 'Ne': 'Neon',
    'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminum', 'Si': 'Silicon', 'P': 'Phosphorus',
    'S': 'Sulfur', 'Cl': 'Chlorine', 'Ar': 'Argon', 'K': 'Potassium', 'Ca': 'Calcium',
    'Sc': 'Scandium', 'Ti': 'Titanium', 'V': 'Vanadium', 'Cr': 'Chromium', 'Mn': 'Manganese',
    'Fe': 'Iron', 'Co': 'Cobalt', 'Ni': 'Nickel', 'Cu': 'Copper', 'Zn': 'Zinc',
    'Ga': 'Gallium', 'Ge': 'Germanium', 'As': 'Arsenic', 'Se': 'Selenium', 'Br': 'Bromine',
    'Kr': 'Krypton', 'Rb': 'Rubidium', 'Sr': 'Strontium', 'Y': 'Yttrium', 'Zr': 'Zirconium',
    'Nb': 'Niobium', 'Mo': 'Molybdenum', 'Tc': 'Technetium', 'Ru': 'Ruthenium', 'Rh': 'Rhodium',
    'Pd': 'Palladium', 'Ag': 'Silver', 'Cd': 'Cadmium', 'In': 'Indium', 'Sn': 'Tin',
    'Sb': 'Antimony', 'Te': 'Tellurium', 'I': 'Iodine', 'Xe': 'Xenon', 'Cs': 'Cesium',
    'Ba': 'Barium', 'La': 'Lanthanum', 'Ce': 'Cerium', 'Pr': 'Praseodymium', 'Nd': 'Neodymium',
    'Pm': 'Promethium', 'Sm': 'Samarium', 'Eu': 'Europium', 'Gd': 'Gadolinium', 'Tb': 'Terbium',
    'Dy': 'Dysprosium', 'Ho': 'Holmium', 'Er': 'Erbium', 'Tm': 'Thulium', 'Yb': 'Ytterbium',
    'Lu': 'Lutetium', 'Hf': 'Hafnium', 'Ta': 'Tantalum', 'W': 'Tungsten', 'Re': 'Rhenium',
    'Os': 'Osmium', 'Ir': 'Iridium', 'Pt': 'Platinum', 'Au': 'Gold', 'Hg': 'Mercury',
    'Tl': 'Thallium', 'Pb': 'Lead', 'Bi': 'Bismuth', 'Po': 'Polonium', 'At': 'Astatine',
    'Rn': 'Radon', 'Fr': 'Francium', 'Ra': 'Radium', 'Ac': 'Actinium', 'Th': 'Thorium',
    'Pa': 'Protactinium', 'U': 'Uranium', 'Np': 'Neptunium', 'Pu': 'Plutonium', 'Am': 'Americium',
    'Cm': 'Curium', 'Bk': 'Berkelium', 'Cf': 'Californium', 'Es': 'Einsteinium', 'Fm': 'Fermium',
    'Md': 'Mendelevium', 'No': 'Nobelium', 'Lr': 'Lawrencium', 'Rf': 'Rutherfordium',
    'Db': 'Dubnium', 'Sg': 'Seaborgium', 'Bh': 'Bohrium', 'Hs': 'Hassium', 'Mt': 'Meitnerium',
    'Ds': 'Darmstadtium', 'Rg': 'Roentgenium', 'Cn': 'Copernicium', 'Nh': 'Nihonium',
    'Fl': 'Flerovium', 'Mc': 'Moscovium', 'Lv': 'Livermorium', 'Ts': 'Tennessine',
    'Og': 'Oganesson'
}


"""
The elementalForms function takes a string 'word' as input and returns an array containing all possible combinations
of element symbols from the periodic table that can form the given word.

It uses a recursive approach to generate all possible combinations of element symbols that can form the word. 
The function iterates over the word, starting from each character, and checks if the substring (symbol) from 
the current character to the end is a valid element symbol. If it is, it adds the corresponding element name 
and symbol to the path and recursively explores further. When it reaches the end of the word, it appends the 
current path (representing a valid combination of element symbols) to the forms list.

The ELEMENTS dictionary contains mappings from element symbols to their corresponding full names. 
Before comparing symbols, the function converts them to capitalize to ensure a case-insensitive comparison.

Test cases are provided to validate the implementation.
"""

def elementalForms(word):
    def find_forms(word, start, path, forms):
        if start == len(word):
            forms.append(path[:])  # Add a copy of the current path to the forms list
            return
        
        for i in range(start, len(word)):
            symbol = word[start:i + 1].capitalize()  # Convert the symbol to capitalize
            if symbol in ELEMENTS:
                path.append(f"{ELEMENTS[symbol]} ({symbol})")
                find_forms(word, i + 1, path, forms)
                path.pop()  # Backtrack

    forms = []
    find_forms(word.lower(), 0, [], forms)
    return forms

# Test cases
print(elementalForms('snack'))
print(elementalForms('beach'))
print(elementalForms('BEACH'))

