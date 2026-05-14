"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    counter = 1

    for item in s:
        new_dict = {}
        for key, value in item.items():
            # Convertir clave y valor a números incrementales
            new_dict[str(counter)] = str(counter + 1)
            counter += 2
        result.append(new_dict)

    return result

# Prueba
print(fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}]))
# => [{'1': '2'}, {'3': '4'}, {'5': '6'}]
