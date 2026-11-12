import sympy as sp
import streamlit as st

x = sp.symbols('x')
y = sp.symbols('y')

expression = x**2 + 2*x*y + y**2

st.write(expression)
st.write(sp.expand(expression))
st.write(sp.factor(expression))

