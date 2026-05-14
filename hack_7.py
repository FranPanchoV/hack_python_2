"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0]
"""

def fn_hack_7(s):
    # Si la lista es [0], retornar [0]
    if s == [0]:
        return [0]

    result = []

    # Recorrer la lista por índice
    for i in range(len(s)):
        if i % 2 == 0:  # Posiciones pares (0, 2, 4...)
            result.append(str(i + 1))  # String: "1", "3", "5"
        else:  # Posiciones impares (1, 3...)
            result.append(i + 1)       # Integer: 2, 4

    return result

print(fn_hack_7(["a","b","c","d","e"]))  # => ["1",2,"3",4,"5"]
print(fn_hack_7([0]))                     # => [0]
