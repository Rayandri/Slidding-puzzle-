from math import *
from random import *


# pour ce projet les notebook on été extremement utile surtout celui sur les algorithme pour le IDA*
class Taquin:
    """
    Class permetant de representer un taquin
    annectode la liste_taquin est tres peut utiliser je fais un fais plein de save partout du coup
    """

    def __init__(self, case='012345678'):
        """
        generation du taquin
        :param case :default='012345678': l'emplacement des cases
        """
        var_temp = list()
        for i in case:
            var_temp.append(i)
        self.liste_taquin = var_temp

        # on va noter la taille du taquin ( le taquin doit etre carré )
        # pour calculer sa on fais la racine carré du nombre de case
        self.taille = int(len(self.liste_taquin) ** 0.5)

        # on fais des sauvergades de l'etat sous forme de txt brut
        # sela est plus pratique pour l'affichage
        self.etat = case

    def niveau_de_melangement(self):
        """
        cette methode mesure le niveau de melange
        :return: le niveau de melange en integer
        """
        nb = 0
        self.save_etat()#je prefere self.etat a self.liste_taquin
        for i in range(len(self.etat)):
            for j in range(i+1, len(self.etat)):
                if self.etat[i] > self.etat[j]:
                    nb += 1
        self.nb_melange = nb
        return nb

    def taquin_possible(self):
        """
        un taquin est sollible si (d'apres wikipedia) et mes test l'on confirmer
        "Le problème sera soluble si la parité de la permutation est identique à la parité de la case vide."
        """
        return (self.niveau_de_melangement() % 2 == self.localisation_zero() % 2)

    def est_gagnant(self):
        ''' renvoie true si c'est gagnant '''
        return (self.etat == '012345678')  # pratique

    def localisation_zero(self):
        """
        :return: la localisation de 0
        """
        return self.liste_taquin.index('0')

    def save_etat(self):
        """ sauverarde l'etat """
        self.etat = ''
        for i in self.liste_taquin:
            self.etat += str(i)
    
    def unsave_etat(self, etat):
        """
        on passe un etat en parametre et on mets cette etat en etat actuelle
        """
        liste = [i for i in etat]
        self.liste_taquin = liste
        self.etat = etat
        


    def delpacement(self, pos1, pos2):
        """ on echange les position des deux elements a deplacer """
        var_temp1 = self.liste_taquin[pos1]
        var_temp2 = self.liste_taquin[pos2]
        self.liste_taquin[pos1] = var_temp2
        self.liste_taquin[pos2] = var_temp1
        self.save_etat()

    """
    les mouvement sont par rapport a la case vide 
    anecdote de programmeur a la base les mouvement été fais par rapport a la case que l'on souhaité deplacer 
    puis apres a voir analyser la correction du prof et avoir remarque que nos deplacement
    fesais 4* plus ligne on est passer a un deplacement via la case vide
    de plus ceci est facilement inversable sur l'interface pour que pour le client sa soit naturel 
    """

    def erreur_deplacement(self):
        print("Ce deplacement est impossible")

    def gauche(self):
        zero = self.localisation_zero()
        if zero not in (0, 3, 6):
            self.delpacement(zero, zero - 1)  # gauche correspond a -1 ( le va a la case en + 1 )
        else:
            self.erreur_deplacement()

    def droite(self):
        zero = self.localisation_zero()
        if zero not in (2, 5, 8):
            self.delpacement(zero, zero + 1) # droite +1
        else:
            self.erreur_deplacement()

    def haut(self):
        zero = self.localisation_zero()
        if zero not in (0, 1, 2):
            self.delpacement(zero, zero - 3) # haut -3
        else:
            self.erreur_deplacement()

    def bas(self):
        zero = self.localisation_zero()
        if zero not in (6, 7, 8):
            self.delpacement(zero, zero + 3) # bas +3
        else:
            self.erreur_deplacement()

    def melanger(self):
        """ le melange sera une succesion de n coup compris entre 15 et 50"""
        n = randint(15, 50)
        msg = 'je melange'  # pour suivre le melange
        self.etat = "012345678"
        while self.est_gagnant():
            print(msg)
            for i in range(n):
                deplacement = randint(0, 4)
                if deplacement == 1:
                    self.droite()
                elif deplacement == 2:
                    self.gauche()
                elif deplacement == 3:
                    self.haut()
                else:
                    self.bas()
            msg = msg.replace('me', 'reme')  # pour afficher je remelange , reremelange, ...
        self.save_etat()

    def melange2(self):
        """ melange chaotique et qui verifie si le taquin est possible """
        nombre = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        etat = ''
        for i in range(9):
            etat += str(nombre.pop(randint(0,len(nombre)-1)))
        self.liste_taquin = etat
        self.save_etat()
        if self.taquin_possible() == False:
            print('je melange une autre fois')
            self.melange2()
            
            
            
            

    def etat_possible(self):
        """
        renvoie la liste des etats possible au coup suivant  pour le taquin
        cette fonction est base sur des calcul simple
        on va utiliser les : pour parcourir la liste etat
        ce qu'elle fais c'est que on fais un echange de la case du deplacement future avec zero est on sauvergarde l'etat
        exemple :

        6 4 5
        7 2 1
        8 3 0

        l'etat suivant avec un coup haut sera

        6 4 5
        7 2 0
        8 3 1

        se qui donne mathematiquement si le zero est postioner en 8

        a b c   a b c    a b c
        d e f   d e 0 ou d e f
        g h 0   g h f    g 0 h


        :return: 
        """
        position = self.localisation_zero()
        etat_si_haut = ''
        etat_si_bas = ''
        etat_si_droite = ''
        etat_si_gauche = ''
        rendu = []

        if position == 0:
            etat_si_haut = ''
            etat_si_bas = self.etat[3] + self.etat[1:3] + self.etat[0] + self.etat[4:9] # 4 a 8 (on exclu le 9)
            etat_si_droite = self.etat[1] + self.etat[0] + self.etat[2:9]
            etat_si_droite = self.etat[1] + self.etat[0] + self.etat[2:9]
            etat_si_gauche = ''

        if position == 1:
            etat_si_haut = ''
            etat_si_bas = self.etat[0] + self.etat[4] + self.etat[2:4]+ self.etat[1] + self.etat[5:9]
            etat_si_droite = self.etat[0] + self.etat[2] + self.etat[1] + self.etat[3:9]
            etat_si_gauche = self.etat[1] + self.etat[0] + self.etat[2:9]

        if position == 2:
            etat_si_haut = ''
            etat_si_bas = self.etat[0:2] + self.etat[5] + self.etat[3:5] + self.etat[2] + self.etat[6:9]
            etat_si_droite = ''
            etat_si_gauche = self.etat[0] + self.etat[2] + self.etat[1] + self.etat[3:9]

        if position == 3:
            etat_si_haut = self.etat[3] + self.etat[1] + self.etat[2] + self.etat[0] + self.etat[4:9]
            etat_si_bas = self.etat[0:3] + self.etat[6] + self.etat[4:6] + self.etat[3] + self.etat[7:9]
            etat_si_droite = self.etat[0:3] + self.etat[4] + self.etat[3] + self.etat[5:9]
            etat_si_gauche = ''

        if position == 4:
            etat_si_haut = self.etat[0] + self.etat[4] + self.etat[2] + self.etat[3] + self.etat[1] + self.etat[5:9]
            etat_si_bas = self.etat[0:4] + self.etat[7] + self.etat[5:7] + self.etat[4] + self.etat[8]
            etat_si_droite = self.etat[0:4] + self.etat[5] + self.etat[4] + self.etat[6:9]
            etat_si_gauche = self.etat[0:3] + self.etat[4] + self.etat[3] + self.etat[5:9]

        if position == 5:
            etat_si_haut = self.etat[0:2] + self.etat[5] + self.etat[3:5] + self.etat[2] + self.etat[6:9]
            etat_si_bas = self.etat[0:5] + self.etat[8] + self.etat[6] + self.etat[7] + self.etat[5]
            etat_si_droite = ''
            etat_si_gauche = self.etat[0:4] + self.etat[5] + self.etat[4] + self.etat[6:9]

        if position == 6:
            etat_si_haut = self.etat[0:3] + self.etat[6] + self.etat[4:6] + self.etat[3] + self.etat[7:9]
            etat_si_bas = ''
            etat_si_droite = self.etat[0:6] + self.etat[7] + self.etat[6] + self.etat[8]
            etat_si_gauche = ''

        if position == 7:
            etat_si_haut = self.etat[0:4] + self.etat[7] + self.etat[5:7] + self.etat[4] + self.etat[8]
            etat_si_bas = ''
            etat_si_droite = self.etat[0:7] + self.etat[8] + self.etat[7]
            etat_si_gauche = self.etat[0:6] + self.etat[7] + self.etat[6] + self.etat[8]

        if position == 8:
            etat_si_haut = self.etat[0:5]+ self.etat[8] + self.etat[6] + self.etat[7] + self.etat[5]
            etat_si_bas = ''
            etat_si_droite = ''
            etat_si_gauche = self.etat[0:7] + self.etat[8] + self.etat[7]

        if etat_si_haut != '':
            rendu.append(etat_si_haut)
        if etat_si_bas != '':
            rendu.append(etat_si_bas)
        if etat_si_gauche != '':
            rendu.append(etat_si_gauche)
        if etat_si_droite != '':
            rendu.append(etat_si_droite)
        return (rendu)

    def __str__(self):
        """
        cette fonction est un casi copier coller de la fonction de notre chere prof
        etant donné que nous avant une interface elle est casi inutile (elle servira juste pour mes test )

        OUI il y a une barre en position 3
        :return: l'affichage en txt
        """
        aff = ""
        for i in range(0, self.taille):  # ligne 1 (0-2)
            aff += str(self.etat[i]) + ' | '
        aff += '\n'
        for i in range(self.taille, self.taille * 2):  # ligne 2 (3-5)
            aff += f'{self.etat[i]} | '
        aff += '\n'
        for i in range(self.taille * 2, self.taille * 3):  # ligne 3 (6-8)
            aff += f'{self.etat[i]} | '
        aff += '\n'
        return aff


def bfs(etat0):
    """
    cette algoritme effectue un parcours en largeur donc ne renvoie pas de chemin mais une profondeur
    :param etat0: un etat du taquin
    :return: la profondeur de la bonne solution

    3 1 2
    4 0 5
    6 7 8
    donc a 2 etapes on va verifier cela avec bfs

    >>> bfs("312405678")
    2

    """
    file = [etat0]  # notre liste d'état
    profondeur = 0  # on mesura la profondeur pour pouvoir renvoyer le nb d'etat avant la fin
    while file != []:
        etat_suivant = list()  # les etat suivant viennent de notre classe taquin
        for etat_verif in file:
            taquin_verif = Taquin(etat_verif)
            if taquin_verif.est_gagnant():  # taquin_verif.est_gagnant() renvoie True ou False
                return profondeur
            else:
                etat_suivant += [i for i in taquin_verif.etat_possible()]
        profondeur += 1
        file = etat_suivant




def nbcoup(etat):
    """notre heuristique pour ida qui se base sur la distance de manahatan
    on va calculer la distance de chaque piece selon leur position initiale """
    tt = 0
    rang = -1
    cord = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    for i in etat:
        rang += 1
        if i != 'O':
            valeur = int(i)
            terme1 =  int(valeur/3)
            terme2 = fmod(valeur, 3)# modulo 3
            part1 = abs(cord[rang][0] - terme1)# valeur absolue 
            part2 = abs(cord[rang][1] - terme2)
            tt += part1 + part2
    return tt


def dlsplus(etatdepart, profdepart, profmax):
    """
    cette fonction se base sur une heuristique est expliquer plus haut
    pour trouver la solution
    le chemin est une variable global pour facilement le recuperer dans ida

    @rtype: list
    @param etatdepart: l'etat d'ou on recherche la solution (vue que c'est recusrive il evolue)
    @param profdepart: la prof de depart de recherche
    @param profmax: int la prof max de recherche
    @return: le chemin sous forme de liste
    """
    global mini,chemin
    if profdepart == 0:
        chemin = list()
    taquindetravail = Taquin(etatdepart)
    
    evalcoup = profdepart + nbcoup(etatdepart)
    if profdepart > 28:#normalement jamais executer mais il est la au cas ou
        print("probleme avec le taquin !!!!!!!!!!!!!!!!!!!!!!!!")#si il est executer il y a une erreur dans le melange
        print(afficher(etatdepart))
        return False

    if evalcoup > profmax:#l'heuristique matematique qui nous permet de savoir si on va depasser le nombre de coup necessaire pour trouver notre solution
        if evalcoup < mini:
            mini = evalcoup
        return False
    
    if taquindetravail.est_gagnant():
        return True

    for etatsuivant in taquindetravail.etat_possible():
        if dlsplus(etatsuivant, profdepart+1, profmax) ==  True:
            chemin.append(etatsuivant)
            return True
    return False

def ida(etatdepart):
    """
    ida se base sur une heuristique du chemin de manahantan et il permet de pouvoir resoudre la plupars des taquin en un temps raisonable
    @param etatdepart:
    @return: le chemin sous forme de liste avec la solution a la fin
    >>> ida("312405678")
    l'IDA* peut comme meme etre long   on evalue le nombre de coup a envrion ~4.0
    ['012345678', '312045678']
    """
    global mini,chemin
    m = nbcoup(etatdepart)
    
    while m!= 1000:
        mini = 1000
        print("l'IDA* peut comme meme etre long   on evalue le nombre de coup a envrion ~" +str(nbcoup(etatdepart)))#pour eviter les freeze en tinker
        if dlsplus(etatdepart, 0, m):
            return chemin
        m =  mini
    return False


def afficher(txt):
    """cette fonction sert uniquement pour afficher le taquin en solution final en console """
    print (f"{txt[0]} {'|'} {txt[1]} {'|'} {txt[2]}")
    print(f"{'---+---+---'}")
    print(f"{txt[3]} {'|'} {txt[4]} {'|'} {txt[5]}")
    print(f"{'---+---+---'}")
    print(f"{txt[6]} {'|'} {txt[7]} {'|'} {txt[8]}")
    #mon ipad ne voulais pas de un seul print


def nb_coup_restant(etat):
    """
    renvoie le nombre de coup restant formater a l'aide d'une phrase
    si il y a moins de 5 coup trouver on verifie la solution a l'aide de bfs car IDA* n'est pas tres precis sur les petite
    distance et peut trouver des chemin legerement plus long

    @param etat:
    @return:
    """
    l = len(ida(etat))
    if l < 5:
        print('on verifie avec bfs')
        l = bfs(etat)# ida peut donner des valeur fausse si il y a peu d'etat a faire
    txt = f" Il reste {l} coups"
    print(txt)
    return txt


def _test():
    import doctest
    doctest.testmod(verbose=True)

#_test()