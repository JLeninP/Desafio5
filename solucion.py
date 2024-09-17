import sys
import sympy as sp

# Variables simbolicas para SymPy
B = sp.symbols('B', real = True)
H = sp.symbols('H', real = True)
S = sp.symbols('S', real = True)
n = sp.symbols('n', real = True)

# Cálculo del flujo
Q = (B*H)**(5/3)*sp.sqrt(S)/(n*(B + 2*H)**(2/3)) # Funcion Q(B, H, S, n)

# Derivadas parciales
dQ_dn = sp.diff(Q, n)
dQ_dS = sp.diff(Q, S)


# Parámetros del canal
Bi = 20  # Ancho (m)
Hi = 0.3  # Profundidad (m)
ni = 0.03  # Coeficiente de rugosidad
Si = 0.0003  # Pendiente
 
# Errores en los parámetros
en = 0.003  # Error en n
eS = 0.00003  # Error en S

# Cálculo del error en el flujo
eQ = abs(dQ_dn) * en + abs(dQ_dS) * eS # Error estimado de Q

# Reemplazando los valores en Q(B, H, S, n) y Delta_Q(B, H, S, n).
Q_eval: float = sp.N(Q.subs({B:Bi, H:Hi, S:Si, n:ni}))
eQ_eval: float = sp.N(eQ.subs({B:Bi, H:Hi, S:Si, n:ni}))
 
# Imprimir resultados
sys.stdout.write('\n=============SOLUCIÓN=============')
sys.stdout.write(f'\nQ = {Q_eval}')
sys.stdout.write(f'\neQ = {eQ_eval}')
sys.stdout.write(f'\nQ - eQ = {Q_eval - eQ_eval}')
sys.stdout.write(f'\nQ + eQ = {Q_eval + eQ_eval}')
sys.stdout.write('\n===========FIN PROGRAMA===========\n')