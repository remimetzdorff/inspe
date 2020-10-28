import matplotlib.pyplot as plt
import numpy as np

file = np.loadtxt("donnees-planetes.csv", skiprows=4, delimiter=";")
x_M = file[ : ,0]
y_M = file[ : ,1]
x_V = file[ : ,2]
y_V = file[ : ,3]

######################################
# changements d'échelle pour les axes
######################################
# limites du graphe
plt.xlim(-1, 1)
plt.ylim(-1, 1)

#######################
# parametres de l'etude
#######################

# Combien de jours doit durer l'observation ? (max=416)
nb_jours = 400

# Combien d'heures entre deux positions ? (nombre pair (2 ou 4 ou 6 ou 8 ou....))
delta_t = 400

#######################################
# limitation du nombre de jours d'étude
#######################################
X_M, Y_M, X_V, Y_V =[],[],[],[]

for i in range(nb_jours*12) :
    X_M.append(x_M[i]) ; Y_M.append(y_M[i])
    X_V.append(x_V[i]) ; Y_V.append(y_V[i])
x_M = X_M ; y_M = Y_M
x_V = X_V ; y_V = Y_V

########################################################
# gestion de l'intervalle de temps entre chaque position
########################################################

# creation des listes des positions pour Mercure et Venus
X_M, Y_M, X_V, Y_V =[],[],[],[]

for i in range(len(x_M)) :
    if i % (delta_t/2) == 0 :
        X_M.append(x_M[i]) ; Y_M.append(y_M[i])
        X_V.append(x_V[i]) ; Y_V.append(y_V[i])

# listes pour Mercure : X_M (abscisses) et Y_M (ordonnees)
# listes pour Venus : X_V (abscisses) et Y_V (ordonnees)

###################################
# tracé des positions sur le graphe
###################################

# le Soleil
plt.scatter(0,0, marker = "*", s = 600, color = "orange", label = "Soleil")

# Mercure
plt.plot(X_M,Y_M, color = "blue", marker = ".", markersize = 8, linestyle="", label = "positions de Mercure")

# Venus
plt.plot(X_V,Y_V, color = "red", marker = ".", markersize = 8, linestyle="", label = "positions de Venus")


##############################
# Titre, nom des axes, legende
##############################
plt.title("Positions des planètes Mercure et Vénus au cours du temps")
plt.xlabel("distance au soleil en unités astronomiques (1 u.a. = $1,5\\times 10^{11}$ m)")
plt.ylabel("distance au soleil en unités astronomiques (1 u.a. = $1,5\\times 10^{11}$ m)")
plt.legend(loc = "upper left", title = "légende", ncol=2, columnspacing = 3.0, shadow=True)
plt.show()

