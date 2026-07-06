import streamlit as st
from scipy.optimize import linprog

st.title("TP1 - Programación Lineal")

st.write("### Problema")
st.write("Maximizar la cobertura de antenas Wi-Fi.")

c = [-8, -5]

A = [
    [300, 180],
    [4, 2]
]

b = [1800, 24]

resultado = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

st.write("### Solución óptima")

st.write(f"**Antenas tipo A:** {resultado.x[0]:.0f}")
st.write(f"**Antenas tipo B:** {resultado.x[1]:.0f}")
st.write(f"**Cobertura máxima:** {-resultado.fun:.0f} zonas")
