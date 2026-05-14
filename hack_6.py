"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"]
"""

def fn_hack_6(s):
    # Si la lista está vacía, retornar ["0"]
    if not s:
        return ["0"]

    result = []

    # Recorrer la lista por índice
    for i in range(len(s)):
        if i % 2 == 0:  # Posiciones pares (0, 2, 4...)
            result.append(str(i + 1))  # 1, 3, 5...
        else:  # Posiciones impares (1, 3...)
            result.append("-")

    return result

print(fn_hack_6(["a","b","c","d","e"]))  
print(fn_hack_6([]))
