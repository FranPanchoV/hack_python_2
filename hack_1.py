"""
generic script

text: "fooziman" output => "fOozIman"
text: "qux" output => "qUx"
text: "eq" output => "eq"
"""

def fn_hack_1(s):
    result = list(s)
    # Solo aplicamos cambios si la longitud es mayor a 2
    if len(result) > 2:
        # Ponemos en mayúscula el índice 1 (segunda letra)
        if len(result) > 1:
            result[1] = result[1].upper()
        # Ponemos en mayúscula el índice 4 (quinta letra)
        if len(result) > 4:
            result[4] = result[4].upper()

    return ''.join(result)

print(fn_hack_1("fooziman"))  # fOozIman
print(fn_hack_1("qux"))       # qUx
print(fn_hack_1("eq"))        # eq
