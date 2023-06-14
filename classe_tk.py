# -*- coding: utf-8 -*-

#%% import
from tkinter import *
from random import *
import logging  # la gestion d'erreur
from tkinter.font import *  # les polices
from tkinter.messagebox import * # les popup
import sys  # le system pour sys.exit()
from time import sleep
import os
from classe_taquin import *
import subprocess # pour ouvrir le fichier index html a l'aide de python sans passer par os si l'invite de commande est desactiver

try:  # ce try  est juste pour rayan
    from fonction_recurante import *  # dans le pythonpath ou dans le dossier envoyer
except:
    sys.path.append("C:\\10 rayan\\NSI\\fonction")
    from fonction_recurante import *

    print('importé via sys')

logging.basicConfig(format='line=%(lineno)s %(message)s')  # pour la gestion d'érreur

# %% debut du code


t = Taquin() # la classe ne peut etre initialiser dans notre main
t.melanger() # car on utilise t dans la class


class Fenetre:
    """
    Cette Class sert a la gestion de l'interface graphique en tkinter
    tous ce qui est print n'est pas lu par l'utlisateur mais pas le dev il sert donc a debugoger le jeux
    l'interface du taquin commence a la methode init_taquin le reste sert juste a l'interface de base
    """




    def __init__(self):
        """
        on renvoie a init par convention et pour tinker si il veut s'auto debuger avec le debuger tinker et les init separer sont plus utile au debugage
        """
        self.init()

    def init(self):
        """
        initialise notre fenetre avec nos couleur et la resolution ainsi que le pleine écran et d'autre chose
        :return:
        """
        self.epi = False  # mode epileptic (esteregg)
        self.root = Tk()
        self.bg = "#1e1f29"
        self.root['bg'] = self.bg
        self.root.title("Taquin")
        self.resolution(
            mode='auto')  # fonction qui mets la resolution automatiquement en fonction de la resolution de l'ecran 1
        self.root.attributes('-fullscreen', False)
        self.top_verif = False  # si nous souhaiton utiliser des toplevel permet de savoir si ils sont activer ou pas (chez nous non normalement)
        Button(self.root, height=0, relief=FLAT, width=0, highlightthickness=0, command=self.f_epi, bg=self.bg).place(
            x=0, y=0)  # ester egg

        self.bu_fermer = Button(self.root, bg='red', width=10, height=0, relief=FLAT,
                                command=self.root.destroy)
        self.bu_fermer.place(relx=0.988, rely=0.0001)
        self.police_ttg = Font(size=30)
        self.init_taquin()

    def init_top(self):
        """
        initialise un top level ( cette fonction n'est pas forcement utiliser)
        :return:
        """
        self.top = Toplevel(self.root)
        self.top['bg'] = 'white'
        self.top.title("Top")
        self.top.geometry('1920x1080')
        self.top_verif = True
        full_screen(self.top)
        self.bu_fermer = Button(self.top, bg='red', width=10, highlightthickness=0, height=0, relief=FLAT,
                                command=self.root.destroy).place(relx=0.988, rely=0.0001)

    def affichage(self, top=0):
        """
        Affiche le root
        ou le top si il est souhaitez
        :param top:
        :return:
        """
        if top == 0:
            self.root.mainloop()
        else:
            self.top.mainloop()

    def rename(self, nom, top=0):
        """
        pour rename les fenêtres
        :param nom:
        :return:
        """
        if top == False:
            self.root.title(nom)
        elif top == True:
            self.top.title(nom)

    def screen_shot(self, nom, extension=".png"):
        """
        effectue un screen shot
        :param nom:
        :return:
        """
        PIL.ImageGrap.grab().sabe(nom + extension)

    def open_image(self, nom):
        """

        :param nom: avec l'extension
        :return:
        """
        photo = PhotoImage(file=nom)

        return photo

    def fond(self, couleur='0', methode=False, top=False, renvoie=False):

        """
        change la couleur du fond
        inutile de lire cette fonction elle permet juste de gérer plein de chose pour l'ester egg
        :param couleur: la couleur souhaiter ou zero pour random
        :param methode: la methode utilisé dans couleur_random()
        :param top: si on veux modifier la couleur du top
        :return: nothing
        """
        if not renvoie:
            if not top:
                if couleur != '0':
                    self.root['bg'] = couleur
                elif methode != 0:
                    self.root['bg'] = couleur_random(methode)
                else:
                    try:
                        self.root['bg'] = couleur
                    except:
                        print('erreur sur le changement de fond couleur')
            elif top:
                if couleur != '0':
                    self.top['bg'] = couleur
                elif methode != 0:
                    self.top['bg'] = couleur_random(methode)
                else:
                    try:
                        self.top['bg'] = couleur
                    except:
                        print('erreur sur le changement de fond couleur')
        else:
            self.couleur_bu = couleur_random(methode)

    def resolution(self, taille='1920x1080', top=False, mode='manuel'):
        """
        change la resolution
        :param mode: manuel or auto
        :param taille: 1920x1080
        :param top: type bool
        :return: nothing
         si le mode est auto cela change la resolution automatiquement par rapport a la resolution de l'écran
        """
        if mode == 'auto':
            x = self.root.winfo_screenwidth()
            y = self.root.winfo_screenheight()
            taille = str(x) + 'x' + str(y)
        if top == False:
            self.root.geometry(taille)
        else:
            self.top.geometry(taille)

    def actualisation(self):
        """
        gere actualisation de la fenetre et s'auto appelle au bout de 50ms
        sert pour le moment au ester egg
        :return:
        """
        if self.epi:
            self.fond(methode=4)
            self.fond(methode=3, renvoie=True)

        self.root.after(50, self.actualisation)

    def f_epi(self):
        """
        ester egg sur le mode épileptique
        :return:
        """

        self.epi = True
        self.actualisation()

    ##############################################################################################################################
    # %%spyderonly debut de la zone du Taquin
    ###############################################################################################################################

    def init_taquin(self):
        """
        oui je pourais tous mettre dans le init mais pas soucis
        se simpliciter et modulatirer je prefere separer chaque initialisation
        """
        self.root.iconbitmap('taquin.ico')
        self.couleur_bg = "#404256"
        self.couleur_fg = 'white'
        self.couleur_predefinis = False
        self.couleur_rond()
        self.police = Font(size=15, family='High Tower text')  # normalement inclus avec office sinon mettez Times news roman
        self.afficher_nb_coup_var = False
        self.nb_coup_SV = StringVar() # SV sera string var
        self.inv_depla = False
        self.resolution("1000x800")
        self.init_canevas()
        self.init_bouton()
        self.maj_taquin()

    def init_canevas(self):
        """initalise le cannevas de jeu """
        self.can = Canvas(self.root, width=500, height=500, bd=1, relief=SUNKEN, bg=self.bg)
        self.can.place(anchor=CENTER, relx=0.4, rely=0.4)

        self.root.bind('<Key>', self.clavier )# pour jouer avec zqsd ou les fleches du clavier

    def init_bouton(self):
        """nos 100 000 bouton et label"""
        self.aide_nb_coup = Button(self.root, text="Nombre de coup", bg=self.couleur_bg, fg=self.couleur_fg,
                            font=self.police, width=15, height=2, command=self.afficher_nb_coup)
        self.aide_nb_coup.place(anchor=CENTER, relx=0.2, rely=0.85)
        self.label_nb_coup = Label(self.root, textvariable=self.nb_coup_SV, bg=self.couleur_bg, fg=self.couleur_fg, bd=2,
                            font=self.police, width=17, height=2)
        self.aide_coup_s = Button(self.root, text="Coup suivant", bg=self.couleur_bg, fg=self.couleur_fg, bd=2,
                            font=self.police, width=15, height=2, command=self.coup_suivant)
        self.aide_coup_s.place(anchor=CENTER, relx=0.5, rely=0.85)
        self.aide_solu = Button(self.root, text="Solution", bg=self.couleur_bg, fg=self.couleur_fg, bd=2,
                            font=self.police, width=15, height=2, command=self.solution)
        self.aide_solu.place(anchor=CENTER, relx=0.8, rely=0.85)

        self.new_eazy = Button(self.root, text="Nouvelle partie\n Difficulté simple ", bg=self.couleur_bg, fg=self.couleur_fg, bd=2,
                            font=self.police, width=15, height=4, command=self.n_eazy_fu)
        self.new_eazy.place(anchor = CENTER, relx=0.8, rely=0.3)

        self.new_hard = Button(self.root, text="Nouvelle partie\n Difficulté hard ", bg=self.couleur_bg,
                               fg=self.couleur_fg, bd=2,
                               font=self.police, width=15, height=4, command=self.n_hard_fu)
        self.new_hard.place(anchor=CENTER, relx=0.8, rely=0.55)

        Button(self.root, text="Couleur\nRandom", bg=self.couleur_bg,
                               fg=self.couleur_fg, bd=2, width=6, height=3, command=self.couleur_rond_r).place(relx=0.85, rely=0.15, anchor = CENTER)
        Button(self.root, text="Couleur\nSimple", bg=self.couleur_bg,
               fg=self.couleur_fg, bd=2, width=6, height=3, command=self.couleur_rond_p).place(relx=0.75, rely=0.15, anchor = CENTER)
        Button(self.root, text="Regle du jeux", bg=self.couleur_bg,
               fg=self.couleur_fg, bd=2, width=10, height=3, command=self.rule).place(relx=0.01, rely=0.01)
        Button(self.root, text="Inverser les touches", bg=self.couleur_bg,
               fg=self.couleur_fg, bd=2, width=15, height=2, command=self.inverse_deplacement).place(relx=0.4, rely=0.04, anchor = CENTER)

    def rule(self):
        """ ouvre dans le navigateur index.html"""

        try:
            import webbrowser
            import psutil
            url = 'index.html'
            if psutil.LINUX:
                # Linux
                print('unix')
                chrome_path = '/usr/bin/google-chrome %s'
                webbrowser.get(chrome_path).open(url)
            elif psutil.WINDOWS:
                # Windows
                print('windows')
                try:
                    os.startfile('index.html')  # windows
                    print('enfin')
                except:
                    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                    webbrowser.get(chrome_path).open(url)
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'#windows serveur et veille version
                    webbrowser.get(chrome_path).open(url)

            elif psutil.MACOS:
                print('macos')
                # MacOS
                chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
                webbrowser.get(chrome_path).open(url)
        except:#google n'est pas installer
            try:
                os.startfile('index.html') # windows
                print('enfin')
            except:# lamenais (cmd bloque)
                print('#################################################\n il faut lancer a la main le fichier index.html \n #############################')


    def n_eazy_fu(self):
        """
        cette fonction cree une nouvelle partie avec un melange dis simple
        le melange fais des coups aleatoire
        """
        t.melanger()
        t.save_etat()
        print(t)
        if self.afficher_nb_coup_var: # pour masquer l'affichage du nombre de coup
            self.afficher_nb_coup()
        self.couleur_rond()
        self.maj_taquin()

    def n_hard_fu(self):
        """
        cette fonction fais un melange chaotique
        """
        t.melange2()
        t.unsave_etat(t.etat)
        print(t)
        if self.afficher_nb_coup_var: #pour masquer l'affichage du nombre de coup
            self.afficher_nb_coup()
        self.couleur_rond()
        self.maj_taquin()

    def afficher_nb_coup(self):
        """savoir si on affiche ou cache le nombre de coup """
        if not self.afficher_nb_coup_var:
            self.afficher_nb_coup_var = True
            self.label_nb_coup.place(anchor=CENTER, relx=0.2, rely=0.95)
            self.maj_nb_coup()
        else:
            self.afficher_nb_coup_var = False
            self.label_nb_coup.place_forget()

    def maj_nb_coup(self):
        """mets a jour la viable (string var tk) qui affiche le nombre de coup restant"""
        t.save_etat()
        self.nb_coup_SV.set(nb_coup_restant(t.etat))


    def coup_suivant(self):
        """  les save_etats se font souvent par precaution
         unsave permet de mettre le taquin a la sauvegarde donée en parametre """
        t.save_etat()
        c = ida(t.etat)
        t.unsave_etat(c[-1])
        self.maj_taquin()

    def solution(self):
        """
        en tinker le sleep freeze la fenetre donc faut improviser
        """
        self.chemin = ida(t.etat)
        self.chemin.reverse()# la liste est a l'envers
        self.root.after(200, self.solution_sleep)

    def solution_sleep(self):
        ''' pour avoir un affichage de la solution dynamique toute les 300ms'''
        if not self.chemin:
            return False
        t.unsave_etat(self.chemin[0])
        print(t)#j'aime bien avoir une console qui affiche plein de truc pour debuger ( vue que il y a un Interface c'est pas derangant)
        self.maj_taquin()
        self.chemin.pop(0)#0 car ca finis par la solution donc je fais comme avec une file
        self.root.after(300, self.solution_sleep)#300ms

    def inverse_deplacement(self):
        """inverse les deplacement (on deplace en fonction de la case et non du zero)"""
        self.inv_depla = not self.inv_depla

    def maj_taquin(self):
        '''
        fonction qui mets a jour l'affichage du taquin
        elle est sale puisque elle supprime chaque element du taquin et le replace a ca nouvelle position
        on fais des boules (ronds) car c'est plus jolie
        '''
        self.sup_all()#vide le canevas (c'est sale)
        x = 100
        y = 100
        r = 70 # pour avoir un peu d'espace
        for i in t.liste_taquin:#pour une fois que j'utilise t.liste_taquin
            if i != "0":
                self.can.create_oval(x-r, y-r, x+r, y+r, fill=self.dico_couleur[int(i)], outline=self.dico_couleur[int(i)])
                self.can.create_text(x, y, text=i, fill='white', font=self.police_ttg, anchor=CENTER)
            else:
                self.can.create_oval(x-r, y-r, x+r, y+r, fill='#323445', outline='#1e1f29') # rond vide
            x += 150
            if x > 400:
                x = 100
                y += 150
        if t.est_gagnant():
            print('gggg')
            showinfo("Victoire", "Bien Joué" , parent=self.can)# parent permet de faire apparaitre au dessus d'un element mais ca marche pas vraiment :)
            t.melanger()
            self.maj_taquin()

    def sup_all(self):
        """ cette fonction vide le canevas
        c'est sale mais fonctionel"""
        for i in self.can.find_all():#parcours tous les elements du canevas
            self.can.delete(i)

    def couleur_rond_r(self):
        """ r pour random cette fonction est appeler par le bouton"""
        self.couleur_predefinis = False
        self.couleur_rond()
        self.maj_taquin()

    def couleur_rond_p(self):
        """ p pour predefinis cette fonction est appeler par le bouton"""
        self.couleur_predefinis = True
        self.couleur_rond()
        self.maj_taquin()

    def couleur_rond(self):
        """ cette fonction choisis les couleur des ronds
        soit via des couleur predefinis soit via des couleur au hasard qui se base sur une fonction de fonction recurante """
        self.dico_couleur = {}
        if self.couleur_predefinis:
            liste_couleur_predefinis = ["#FF5500", "#FFAA00", "#AAFF00", "#55FF00", "#00FF00", "#00FF55", "#00FFAA", "#00FFFF"]
            for i in range(1, 9):
                self.dico_couleur[i] = liste_couleur_predefinis.pop(randint(0, len(liste_couleur_predefinis)-1)) #pour prendre une couleur au hasard
        else:
            for i in range(9):
                self.dico_couleur[i] = couleur_random(methode = 6)

    def clavier(self, event):
        """ detecte les touches du clavier """
        touche = event.keysym
        if not self.inv_depla:#si on deplace le zero
            if touche == "Up" or touche == "z":
                t.haut()
            elif touche == "Down" or touche == "s":
                t.bas()
            elif touche == "Right" or touche == "d":
                t.droite()
            elif touche == "Left" or touche == "q":
                t.gauche()
        else:#si on deplace pas le zero
            if touche == "Up" or touche == "z":
                t.bas()
            elif touche == "Down" or touche == "s":
                t.haut()
            elif touche == "Right" or touche == "d":
                t.gauche()
            elif touche == "Left" or touche == "q":
                t.droite()

        if self.afficher_nb_coup_var:# si on affiche le nombre de coup
            self.maj_nb_coup()
        print(t)# pour debuger
        self.maj_taquin()


