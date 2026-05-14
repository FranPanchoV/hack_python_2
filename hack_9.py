"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}

    if "foo" in s:
        # Obtener el string
        text = s["foo"]  # "fookziman"

        # Quitar la 'k' (está entre 'o' y 'z')
        # Opción 1: replace
        text = text.replace("k", "")

        # Opción 2: slicing (si siempre está en la misma posición)
        # text = text[:3] + text[4:]  # "foo" + "ziman"

        # Capitalizar primera letra
        text = text.capitalize()  # "Fooziman"

        result["Foo"] = text

    return result

print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))
