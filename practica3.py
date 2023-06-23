num1 = int(input("Ingresa el segundo número: "))

op= input("ingrese '+' '-'  '*'  '/' : ")
num2 = int(input("Ingresa el segundo número: "))
if op == '+':
    print(f"""
============================
ejecutando operacion.......
============================     
        """)
    print(f"""
El resultado de la suma es : "{num1 + num2}
""")
elif op == '-':
    print(f"""
============================
ejecutando operacion.......
============================     
        """)
    print(f"""
El resultado de la suma es : "{num1 - num2}
""")
elif op == '*':
    print(f"""
============================
ejecutando operacion.......
============================     
        """)
    print(f"""
El resultado de la suma es : "{num1 * num2}
""")
elif op == '/':
    print(f"""
============================
ejecutando operacion.......
============================     
        """)
    print(f"""
El resultado de la suma es : "{num1 / num2}
""")
    
else:
    print(f"""
=======================================
Error al seleccionar operacion.........
=======================================
""")
    