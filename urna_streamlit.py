import numpy as np
from scipy.stats import bernoulli
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from clase_urna import polyas_urn, n_sim_polyas_urn


st.title('Urnas')
st.write("Algunas simulaciones\n")
st.header('Urna de Polya')

n_w = st.slider('Número inicial de bolas blancas', min_value = 1, max_value = 10)
n_b = st.slider('Número inicial de bolas negras', min_value = 1, max_value = 10)

N = st.slider('Cantidad de iteraciones por simulación', min_value = 20, max_value = 200)
n_sims = st.slider('Número de simulaciones', min_value = 5, max_value = 100)

if (st.button('Correr Simulación')):
    sim_polya = n_sim_polyas_urn(n_sims, N, n_w, n_b)
    sim_polya.run_sim()
    
    fig, ax = plt.subplots()
    for i in range(sim_polya.n_sim):
        ax.plot(sim_polya.sims[i].results['porc_1'][sim_polya.n_init_balls:])

    ax.set_title('Proporción de bolas negras por cada iteración\n número de iteraciones {}'.format(sim_polya.n_sim))
    ax.set_ylabel('Proporción de bolas negras')
    ax.set_xlabel('Iteración')
    
    st.pyplot(fig)
