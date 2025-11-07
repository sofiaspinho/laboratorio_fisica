import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

angulo_incid = [10,15,18,20,35,40,45,49,50,70]
angulo_reflex = [11,15.5,17.3,19.9,34,38,43,47,48,67.7]
angulo_refrac = [6,9,11,12,21,24,27,29,30,37.8]

# fonte bonita
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['font.size'] = 14

### graf1
plt.title(r'$\Theta_{r}$ em função de $\Theta_{i}$')
plt.xlabel('$\Theta_{r}$ [$\degree$]')
plt.ylabel('$\Theta_{i}$ [$\degree$]')
plt.grid(which='major', color='#CCCCCC', linestyle='-',zorder=1)
plt.grid(which='minor', color='#CCCCCC', linestyle=':',zorder=1)
plt.minorticks_on()
plt.scatter(angulo_reflex, angulo_incid, color='#4287f5', marker='o',edgecolors='#3042b3',zorder=2)
#plt.plot(angulo_reflex, angulo_incid, color='red')
plt.savefig('exp1g1-2.png')
plt.close()

### graf2
plt.title(r'$\Theta_{t}$ em função de $\Theta_{i}$')
plt.scatter(angulo_refrac, angulo_incid, color='#4287f5', marker='o',edgecolors='#3042b3',zorder=2)
plt.plot(angulo_refrac, angulo_incid, color='grey',linestyle=':',zorder=1)
plt.xlabel('$\Theta_{t}$ [$\degree$]')
plt.ylabel('$\Theta_{i}$ [$\degree$]')
plt.savefig('exp1g2.png')
plt.close()

### slope ## graf2.1
angulo_incid = np.array([10,15,18,20,35,40,45,49,50,70])
angulo_refrac = np.array([6,9,11,12,21,24,27,29,30,37.8])
seni = np.sin(np.deg2rad(angulo_incid))
senr = np.sin(np.deg2rad(angulo_refrac))
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(senr, seni)
y3 = [slope3 * xi + intercept3 for xi in senr]
plt.title(r'sen$\Theta_{t}$ em função de sen$\Theta_{i}$')
plt.scatter(senr, seni, color='#4287f5', marker='o',edgecolors='#3042b3', label='Medidas')
plt.plot(senr, y3, color='red', label='Ajuste')
plt.xlabel('sen$\Theta_{t}$ [$\degree$]')
plt.ylabel('sen$\Theta_{i}$ [$\degree$]')
print("slope 3: ",slope3,"erro padrão 3: ",std_err3)
plt.legend()
plt.savefig('grafico2-1.png')
plt.close()

'''
slope 3:  1.5007292040210787 erro padrão 3:  0.013467922956849898
'''


