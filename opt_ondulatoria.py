import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

# fonte bonita
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['font.size'] = 14

# os graficos são:

# P0Pn em func de n - fenda retangular
## slope ## graf1 
P0Pn = np.array([0.60, 1.30, 1.80, 2.40, 3.00, 3.70])
n = np.array([1,2,3,4,5,6])
plt.figure()
plt.title(r'P0P$_{n}$ em função de n')
slope1, intercept, r_value, p_value, std_err1 = stats.linregress(n,P0Pn)
y_pred = [slope1 * xi + intercept for xi in n]
plt.xlabel('n')
plt.ylabel('P0P$_{n}$ [cm]')
plt.plot(n, y_pred, color='red', label='Ajuste')
plt.scatter(n, P0Pn, color='#4287f5', label='Medidas', marker='o',edgecolors='#3042b3')
plt.legend()
print("slope 1: ",slope1,"erro padrão 1: ",std_err1)
plt.savefig('exp2_g1.png')
plt.close()

'''
slope 1:  0.6057142857142858 erro padrão 1:  0.013502330360721534
slope 2:  0.55 erro padrão 2:  0.0

'''
# P0Pm em func de m - fenda dupla retangular
P0Pm = np.array([0.50, 1.05, 1.60])
m = np.array([1,2,3])
plt.figure()
plt.title(r'P0P$_{m}$ em função de m')
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(m,P0Pm)
y_pred2 = [slope2 * xi2 + intercept2 for xi2 in m]
plt.xlabel('m')
plt.ylabel('P0P$_{m}$ [cm]')
plt.plot(m, y_pred2, color='red', label='Ajuste')
plt.scatter(m, P0Pm, color='#4287f5', label='Medidas', marker='o',edgecolors='#3042b3')
plt.legend()
print("slope 2: ",slope2,"erro padrão 2: ",std_err2)
plt.savefig('exp2_g2.png')
plt.close()

# é isso?
# np.sin(np.deg2rad(angulo_incid))

'''
IGNORAR ISSO 

########## EXPERIMENTO 2
medidas = [0.3, 0.5, 0.3, 0.6, 0.4]
medidas = np.array(medidas)
media = (medidas.sum())/len(medidas)
soma = []
for i in range(len(angulo_crit)):
	soma.append((medidas[i]-media)**2)
soma = np.array(soma); soma = soma.sum()
incerteza_A = np.sqrt((soma)/(len(medidas)*(len(medidas)-1))) 


angulo_crit = [47, 49, 49, 49, 50]
angulo_crit = np.array(angulo_crit)
n1 - nacrílico
n2 - na = 1
indice_refrac = 1/np.sen(48.8)*np.pi/180

# grafico angulo_reflex vs angulo_incid
plt.title(r'$\Theta_{r}$ em função de $\Theta_{i}$')
plt.plot(angulo_reflex, angulo_incid, color='red')
plt.xlabel('$\Theta_{r}$ [$\degree$]')
plt.ylabel('$\Theta_{i}$ [$\degree$]')
plt.savefig('grafico1.png')
plt.close()
#plt.show()

# grafico angulo_refrac vs angulo_incid
plt.title(r'$\Theta_{t}$ em função de $\Theta_{i}$')
plt.plot(angulo_refrac, angulo_incid, color='red')
plt.xlabel('$\Theta_{t}$ [$\degree$]')
plt.ylabel('$\Theta_{i}$ [$\degree$]')
plt.savefig('grafico2.png')
plt.close()
#plt.show()


angulo_crit = [47, 49, 49, 49, 50]
angulo_crit = np.array(angulo_crit)
x_medio = (angulo_crit.sum())/len(angulo_crit)
soma = []
for i in range(len(angulo_crit)):
	soma.append((angulo_crit[i]-x_medio)**2)
soma = np.array(soma); soma = soma.sum()
incerteza_A = np.sqrt((soma)/(len(angulo_crit)*(len(angulo_crit)-1))) 
incerteza_B = 0.5
incerteza_C = np.sqrt((incerteza_A**2) + (incerteza_B**2))
'''

