import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# fonte bonita
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['font.size'] = 14

### rede de difração
# P0Pm em função de m
P0Pm = np.array([1.5, 3.0, 4.5,6.0,7.6,9.2])
m = np.array([1,2,3,4,5,6])

coef = np.polyfit(m,P0Pm,1)
poly1d_fn = np.poly1d(coef)
plt.scatter(m,P0Pm, color='#4287f5', marker='o',edgecolors='#3042b3', \
label='Medidas',alpha=0.8,zorder=2)
plt.plot(m, poly1d_fn(m), color='red',label='Ajuste',zorder=1)
plt.xlabel('m')
plt.ylabel('P$_{0}$P$_{m}$')
plt.title(r'P$_{0}$P$_{m}$ em função de m')
print("coef: ",coef)
plt.legend()
plt.savefig('exp3_redededifr-polyfit.png')
plt.close()

'''
coef = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(coef) 
plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k') 
'''

### curva de calibração
lbd_esperado = np.array([365,405,436,546,579,610])
lbd_medido =  np.array([380.5,422.3,455.2,564.3,604.3,641.1]) # a = 1.04 - 3

# comprimento de onda determinado a partir da medida vs esperado
plt.title(r'$\lambda$ medido em função de $\lambda$ esperado')
coef = np.polyfit(lbd_esperado, lbd_medido,1)
poly1d_fn = np.poly1d(coef)
plt.scatter(lbd_esperado, lbd_medido, color='#4287f5', marker='o',edgecolors='#3042b3', label='Medidas',zorder=2)
#plt.plot(lbd_esperado, poly1d_fn(lbd_esperado), color='red', \
#label='Ajuste',zorder=1)
plt.xlabel('$\lambda$ medido [nm]')
plt.ylabel('$\lambda$ esperado [nm]')
print("coef: ",coef)
plt.legend()
plt.savefig('exp3_lambdas-polyfit.png')
plt.close()
