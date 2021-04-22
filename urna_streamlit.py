import numpy as np
from scipy.stats import bernoulli
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from clase_urna import polyas_urn, n_sim_polyas_urn
from PIL import Image


text_file = open('texto.txt', 'r')
text = text_file.read()

# Parámetros para gráficos
plt.style.use('seaborn-darkgrid')

plt.rcParams.update({'font.size': 25})      
plt.rc('axes', labelsize=20)
plt.rc('legend', fontsize=18)  
plt.rc('xtick', labelsize=20) 
plt.rc('ytick', labelsize=20) 
plt.rcParams['axes.titlesize'] = 25
plt.rcParams["figure.figsize"] = (15,6)


st.title('Simulaciones y Conductas Limites')
st.header('La Urna de Polya')
st.write("Simulación de la Urna de Polya para el curso MA3403-1")
st.write(text)
st.write('En la siguiente sección podrá simular la urna de polya segun los parametros iniciales que se elijan')

st.header('Simulación')
st.write('Selecciona los valores iniciales de la simulación moviendo las perillas')

n_w = st.slider('Número inicial de bolas blancas', min_value = 1, max_value = 10)
n_b = st.slider('Número inicial de bolas negras', min_value = 1, max_value = 10)

N = st.slider('Cantidad de iteraciones por simulación', min_value = 20, max_value = 200)
n_sims = st.slider('Número de simulaciones', min_value = 5, max_value = 100)

st.write('Haga click en correr simulacion')

if (st.button('Correr Simulación')):
    sim_polya = n_sim_polyas_urn(n_sims, N, n_w, n_b)
    sim_polya.run_sim()

    st.write(f'''A continuacion se muestran la proporción de las bolas negras para cada una de las {sim_polya.n_sim} simulaciones con {N} iteraciones. Se consideran un numero de bolas inicial de {n_b} negras y {n_w} blancas ''')
    
    fig, ax = plt.subplots()
    for i in range(sim_polya.n_sim):
        ax.plot(range(1,N+1),sim_polya.sims[i].results['porc_1'][sim_polya.n_init_balls:])
    
    ax.set_title('Proporción de bolas negras por iteración\n Todas las simulaciones')
    ax.set_ylabel('Proporción de bolas negras')
    ax.set_xlabel('Iteración')
    ax.set_ylim(0,1)
    
    st.pyplot(fig)


st.header('Conductas Limites')
st.write('El modelo va mas alla de una simple urna. Si consideramos a $X_i$ una variable aleatoria tal que $X_i=1$ si es que la bola en la iteracion $i$ es negra y $X_i=0$ si es que es blanca, la proporción de bolas negras en la iteracion $n$ viene dada por')
st.latex('Y_n = \dfrac{n_b+\sum\limits_{i=1}^{n}X_i}{n_b+n_w+n}')
st.write('Se demuestra que cuando la cantidad $n$ de iteraciones tiene al infinito, la proporcion $Y_n$ converge a una variable aleatoria continua con distribucion $Beta(n_b, n_w)$ la cual tiene como funcion de densidad:')
st.latex('f(x) = \dfrac{\Gamma(n_b+n_w)}{\Gamma (n_b) \Gamma (n_w)} x^{n_b-1}(1-x)^{n_w-1}, \quad x\in[0,1] ')
st.write('donde $\Gamma(\cdot)$ denota la función Gamma. Esta distribución modela la proporcion de dos poblaciones. Esto se verá después en el curso.')
st.write('Un caso especial es cuando $n_w =n_b=1$, en este caso la proporcion $Y_n$ converge a una $Beta(1,1)$, la cual recupera a una distribucion uniforme en $[0,1]$. Realizando una simulacion para observar esto, se simula 200 veces el modelo con 500 iteraciones cada uno. Los resultados son los siguientes:')

image = Image.open('graficos/grafico_uniforme.png')
st.image(image, caption='Grafico primer caso',use_column_width= 'always')

st.write('En lo anterior se observa que en la iteracion 500 las proporciones obtenidas cubren todo el intervalo $densamente$, no notando ninguna tendencia a concentrarse en algún punto del intervalo $[0,1]$. Para notar mejor el fenómeno anterior se realiza el siguiente histograma:')

image_2 = Image.open('graficos/aprox_uniforme.png')
st.image(image_2, caption='Histograma, primer caso',use_column_width= 'always')
st.write('En el gráfico se observa el histograma de la proporción de las bolas negras en la última iteración para todas las simulaciones. Se tiene que no existe tendencia a concentrarse en ningún punto, otorgando igual peso a todo el intervalo. Se grafica la densidad real de una $Uniforme(0,1)$ para comparar.')

st.write('Para estudiar un comportamiento distinto de la distribucion Beta, se seleccionan otros valores iniciales. Se selecciona un numero inicial de 10 bolas negras y 1 blanca. Se realizan 200 simulaciones con 500 iteraciones')
image = Image.open('graficos/grafico_caso.png')

st.image(image, caption='Grafico segundo caso',use_column_width= 'always')
st.write('del grafico anterior notamos una tendencia de tener una mayor proporcion de bolas negras. Se tiene que el histograma obtenido de la proporcion de las bolas negras en la ultima iteracion es el siguiente:')
image = Image.open('graficos/aprox_caso.png')
st.image(image, caption='Histograma, segundo caso',use_column_width= 'always')
st.write('En el gráfico anterior se observa el histograma obtenido del porcentaje de bolas negras en la última iteración para cada simulación. Es posible notar que existe efectivamente una tendencia a tener valores altos de porcentaje de bolas negras en la densidad empírica, lo cual se condice con la densidad real de la $Beta(10,1)$.')


st.header('Referencias')

st.markdown(
    """
Algunas referencias para entender mejor lo expuesto en esta aplicacion:
- La Urna de Polya:
    - [Sobre la intuicion y usos](https://dayinlab.com/2017/09/05/la-urna-de-polya-por-que-la-gente-bebe-coca-cola/)
    - [Sobre la teoría](https://www.randomservices.org/random/urn/Polya.html)
    - [Mas teoria, avanzada](http://individual.utoronto.ca/normand/Documents/MATH5501/Project-2/Polya_urn_general_distr.pdf)
- La distribución Beta:
    - [Intucion](https://towardsdatascience.com/beta-distribution-intuition-examples-and-derivation-cf00f4db57af)
    - [Teoria](https://en.wikipedia.org/wiki/Beta_distribution)
""")


st.header('Notas')
st.markdown(
    """
- Creador de la app: Francisco Vasquez Leiva
- Mail: fvasquez at dim.uchile.cl
""")

st.write('Las tildes fueron eliminadas a proposito')

