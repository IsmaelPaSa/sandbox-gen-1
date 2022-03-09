import random

greek_alphabet = [
	['Α', 'α', 'Alpha', 'a'],
	['Β', 'β', 'Beta', 'b'],
	['Γ', 'γ', 'Gamma', 'g'],
        ['Δ', 'δ', 'Delta', 'd'],
        ['Ε', 'ε', 'Epsilon', 'e'],
        ['Ζ', 'ζ', 'Zeta', 'z'],
        ['Η', 'η', 'Eta', 'h'],
        ['Θ', 'θ', 'Theta', 'th'],
        ['Ι', 'ι', 'Iota', 'i'],
        ['Κ', 'κ', 'Kappa', 'k'],
        ['Λ', 'λ', 'Lambda', 'l'],
        ['Μ', 'μ', 'Mu', 'm'],
        ['Ν', 'ν', 'Nu', 'n'],
        ['Ξ', 'ξ', 'Xi', 'x'],
        ['Ο', 'ο', 'Omicron', 'o'],
        ['Π', 'π', 'Pi', 'p'],
        ['Ρ', 'ρ', 'Rho', 'r'],
        ['Σ', 'σ | ς', 'Sigma', 's'],
        ['Τ', 'τ', 'Tau', 't'],
        ['Υ', 'υ', 'Upsilon', 'u'],
        ['Φ', 'φ', 'Phi', 'ph'],
        ['Χ', 'χ', 'Chi', 'xh'],
        ['Ψ', 'ψ', 'Psi', 'ps'],
        ['Ω', 'ω', 'Omega', 'o'],
]

def greek():
	for i in range(random.randint(1, len(greek_alphabet))):
		random.shuffle(greek_alphabet)

	name = random.choice(greek_alphabet)
	print('Nombre:', name[2])
	print('Simbolos:', name[0], '|', name[1])
	print('Equivalente:', name[3].upper(), '|', name[3].lower())

greek()
