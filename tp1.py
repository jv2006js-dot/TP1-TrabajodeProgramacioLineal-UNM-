from scipy.optimize import linprog

# Función objetivo (maximizar cobertura)
c = [-8, -5]

# Restricciones
A = [
    [300, 180],  # Presupuesto
    [4, 2]       # Energía
]

b = [
    1800,
    24
]

# Resolver el problema
resultado = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

# Mostrar resultados
print("=== SOLUCIÓN ÓPTIMA ===")
print("Antenas tipo A:", resultado.x[0])
print("Antenas tipo B:", resultado.x[1])
print("Cobertura máxima:", -resultado.fun)
