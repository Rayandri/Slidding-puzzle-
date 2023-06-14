from classe_taquin import *

t = Taquin()
t.melange2()
t.unsave_etat(t.etat)
espace(15)
while t.est_gagnant() == False:
    print(t)
    choix = input("Z Q S D or help, chemin, solution: ")
    if choix == "z":
        t.haut()
    elif choix == "s":
        t.bas()
    elif choix == "q":
        t.gauche()
    elif choix == "d":
        t.droite()
    elif choix == 'help':
        c = ida(t.etat)
        print(f'on est a {len(c)} coups')
        
    elif choix == 'chemin':
        c = ida(t.etat)
        c.reverse()
        for i in c:
            afficher(i)
            print()
    elif choix == 'coup suivant':
        c = ida(t.etat)
        c.reverse()
        t.unsave_etat(c[0])
        
    elif choix == 'solution':
        c = ida(t.etat)
        c.reverse()
        for i in c:
            t.unsave_etat(i)
            print(t)

    elif choix == 'bfs':
        c = bfs(t.etat)
        print(c)

    elif choix == "new":
        t.melange2()
        t.unsave_etat(t.etat)
    elif choix == "test":#test avec un taquin chaotique
        for i in range(10):
            t.melange2()
            t.unsave_etat(t.etat)
            print(t)
            print("############   " + str(len(ida(t.etat))) + "      ##############")
    elif choix == "test2":#test avec un taquin "simple"
        for i in range(10):
            t.melanger()
            t.unsave_etat(t.etat)
            print(t)
            print("############   " + str(len(ida(t.etat))) + "      ##############")
    else:
        print('il faut bien taper z q s d')



print('bien jouer')
