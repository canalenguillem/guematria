from googletrans import Translator


# Diccionario de valores de guematría para cada letra hebrea
valores_guematria = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
    'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
    'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40,
    'נ': 50, 'ן': 50, 'ס': 60, 'ע': 70, 'פ': 80,
    'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200,
    'ש': 300, 'ת': 400
}

# Función para calcular el valor de guematría de una palabra
def calcular_guematria(palabra_hebreo):
    valor_total = 0
    for letra in palabra_hebreo:
        if letra in valores_guematria:
            valor_total += valores_guematria[letra]
        else:
            print(f"Letra {letra} no reconocida en la guematría.")
    return valor_total


if __name__ == "__main__":
    # Ejemplo de uso
    palabra_en_hebreo = "שלום"  # Esto significa "paz"
    valor_guematria = calcular_guematria(palabra_en_hebreo)


    print(f"El valor de guematría de '{palabra_en_hebreo}' es: {valor_guematria}")
