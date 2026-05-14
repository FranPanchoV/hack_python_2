"""
generic script

text: "fooziman" output => "oozima"
text: "barziman" output => "arzima"
text: "qux" output => "qux"
"""

def fn_hack_4(s):
    # Verificamos si la longitud es mayor a 3
    if len(s) > 3:
        # Usamos "slicing" para saltar el índice 0 y excluir el último
        result = s[1:-1]
    else:
        # Si tiene 3 letras o menos, no se toca
        result = s
    return result

print(fn_hack_4("fooziman"))
print(fn_hack_4("barziman"))
print(fn_hack_4("qux"))
