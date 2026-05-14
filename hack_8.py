"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(s):
    result = []
    n = len(s)

    # Recorrer la lista en orden inverso
    for i in range(n-1, -1, -1):
        if n % 2 == 0:  # Si la longitud es par
            result.append(str(i + 1))
        else:  # Si la longitud es impar
            result.append(f"{s[i]}-{i+1}")

    return result

# Pruebas
print(fn_hack_8(["a","b","c","d","e"]))
print(fn_hack_8(["a","b","c"]))
print(fn_hack_8(["a","b","c","d"]))
print(fn_hack_8(["a","b"]))              
