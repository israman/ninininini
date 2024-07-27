conjuntoVocales = {
    'minus' : 'aeiou',
    'aguminus' : 'áéíóú',
    'graminus' : 'àèìòù',
    'dieminus' : 'äëïöü',
    'mayus' : 'AEIOU',
    'agumayus' : 'ÁÉÍÓÚ',
    'gravmayus' : 'ÀÈÌÒÙ',
    'diemayus' : 'ÄËÏÖÜ',
}

def main():
    nini = input("TEXTO A NININEAR: \n")
    for vocales in conjuntoVocales.keys():
        nini = replace(nini,vocales)
    print(nini)

def replace(text,replace):
    newText = ''
    for char in text:
        for vowel in conjuntoVocales[replace]:
            if vowel == char:
                char = conjuntoVocales[replace][2]
        newText += char
    return newText 

if __name__ == "__main__":
    main()