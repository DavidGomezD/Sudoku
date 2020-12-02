arreglo=["n7_f7",
    "n8_f7",
    "n9_f7",
    "n7_f8",
    "n8_f8",
    "n9_f8",
    "n7_f9",
    "n8_f9",
    "n9_f9"]

n = 72
c = 0
while c <= 8:
    print("""{% set mostrar_"""+str(n)+""" = aleatorio_"""+str(n)+""" %}
{% if mostrar_"""+str(n)+""" == 0 %}
<input class="w-full pl-8 justify-self-center bg-black text-white" type="number" name=" """+str(arreglo[c])+"""" min="1" max="9">
{% else %}
<input class="w-full pl-8 justify-self-center bg-black" type="number" name=" """+str(arreglo[c])+""" " value="{{  """+str(arreglo[c])+"""  }}" readonly="readonly">
{% endif %}""")
    c += 1
    n += 1
