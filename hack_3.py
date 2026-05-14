"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N"
text: "barziman" output => "B@rz¡m@N"
text: "3q" output => "3Q"
text: "qu" output => "Qv"
text: "qux" output => "QvX"
"""

def fn_hack_3(s):
    # Definimos los reemplazos tal cual los pide el script genérico
    replacements = {
        'a': '@', 'e': '3', 'i': '¡', 'o': '0', 'u': 'v'
    }

    n = len(s)
    result = []

    for i in range(n):
        char = s[i]

        # Lógica de mayúsculas: Primera y última posición siempre mayúsculas
        # (Si no son letras, upper() simplemente no hace nada)
        if i == 0 or i == n - 1:
            char = char.upper()

        # Aplicar reemplazo solo si el carácter (en minúscula) está en nuestro mapa
        # Usamos .lower() para buscar en el diccionario pero mantenemos la intención original
        res_char = replacements.get(char.lower(), char)

        result.append(res_char)

    return "".join(result)

print(fn_hack_3("fooziman"))  # F00z¡m@N
print(fn_hack_3("barziman"))  # B@rz¡m@N
print(fn_hack_3("3q"))        # 3Q
print(fn_hack_3("qu"))        # Qv
print(fn_hack_3("qux"))       # QvX
