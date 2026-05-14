"""
generic script

text: "fooziman" output => "fzmn"
text: "barziman" output => "brzmn"
text: "qux" output => "qx"
"""

def fn_hack_2(s):
    vocales = "aeiouAEIOU"  # vocales en minúscula y mayúscula
    result = ""
    for char in s:
        if char not in vocales:  # si no es vocal, lo conservamos
            result += char
    return result

print(fn_hack_2("fooziman"))  # fzmn
print(fn_hack_2("barziman"))  # brzmn
print(fn_hack_2("qux"))       # qx 
