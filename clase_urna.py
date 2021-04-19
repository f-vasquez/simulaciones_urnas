import numpy as np
from scipy.stats import bernoulli
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class polyas_urn:
    def __init__(self, N, n_w, n_b, c = 1):
        self.stages = N
        self.n_whites = n_w
        self.n_blacks = n_b
        self.plus_n = c
        self.simulations= {}
    
    def simulate(self):
        self.balls = [1]*self.n_blacks + [0]*self.n_whites
#         random.shuffle(self.balls)
        
        for i in range(self.stages):
            p = np.sum(self.balls)/(len(self.balls))
            bern = bernoulli(p)
            bern_r = bern.rvs()
            
            if bern_r == 1:
                self.balls += [1]*self.plus_n
            else:
                self.balls += [0]*self.plus_n 
    
    def get_results(self):
        df_1 = pd.DataFrame(self.balls, columns = ['Occ'])

        df_1['oc_1'] = (df_1['Occ']==1).astype(int)
        df_1['oc_2'] = (df_1['Occ']==0).astype(int)

        df_1['sum_oc_1'] = df_1['oc_1'].cumsum()
        df_1['sum_oc_2'] = df_1['oc_2'].cumsum()

        df_1['sum'] = df_1.index+1

        df_1['porc_1'] = df_1['sum_oc_1']/df_1['sum']
        df_1['porc_2'] = df_1['sum_oc_2']/df_1['sum']
        
        self.results = df_1

class n_sim_polyas_urn:
    def __init__(self,n_sim, N, n_w, n_b, c = 1):
        self.sims = {i:polyas_urn(N, n_w, n_b) for i in range(n_sim)}
        self.n_sim = n_sim
        self.n_init_balls = n_w+n_b
    
    def run_sim(self):
        for i in range(self.n_sim):
            self.sims[i].simulate()
            self.sims[i].get_results()
