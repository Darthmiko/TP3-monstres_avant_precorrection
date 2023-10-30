# créé par mikolai Szychowski
# cree le 18 octobre 2023
# TP3 combat de monstres
import random     #fonction definit
import time
def jeu():

    niveau_vie = 20
    victoire = 0
    défaite = 0

    numero_adversaire = 1
    numero_combat = 1
    nb_victoire = 0
    nb_défaite = 0
    nb_victoire_consecutive = 0
    print('Bonjour, bienvenu dans ce jeu ou vous combattrez des monstres')
    nom=str(input('Quelle sera votre nom?'))   #nom de l avatar
    print('Bonne chance',nom,'.')

    while True:

        time.sleep(1)

        print('Vous tombez face a face avec un adversaire')  # menu
        print('Vous avez quatres options')
        print('1:Combattre le monstres')
        print('2:Contourner le monstres et perdre une vie')
        print('3:Afficher les regles du jeu')
        print('4:Quitter la partie')
        if nb_victoire % 3 == 0:
            force_adversaire = random.randint(1,11)
            time.sleep(1)
        else:
            force_adversaire = random.randint(1,11)
            print('Vous tombez face a face avec un adversaire de difficulté',force_adversaire,'.')
        time.sleep(2)


        time.sleep(2)
        choix=int(input('Que désirez vous faire?'))

        if choix == 1:
            print(' ')
            print('',nom,'')
            time.sleep(2)
            print('Adversaire:',numero_adversaire,'')
            print('Force de l adversaire:',force_adversaire,'')
            print('Niveau de vie:',niveau_vie,'')
            print('Combat',numero_combat,':',nb_victoire,'victoires contre',nb_défaite,'défaites')

            premier_dé = random.randint(1,6)
            deuxieme_dé = random.randint(1,6)
            score_dé = premier_dé + deuxieme_dé
            time.sleep(3)
            print('Premier dé:', premier_dé,'')
            time.sleep(1)
            print('Deuxieme dé:', deuxieme_dé,'')
            time.sleep(1)
            print('Total:', score_dé,'')
            time.sleep(1)

            if score_dé > force_adversaire:
                print('Victoire!')
                niveau_vie = niveau_vie + force_adversaire
                nb_victoire = nb_victoire + 1
                numero_combat = numero_combat + 1
                numero_adversaire = numero_adversaire + 1
                nb_victoire_consecutive = nb_victoire_consecutive + 1

                time.sleep(2)
                print(' ')
                print('',nom,' \n Niveau de vie:', niveau_vie,' \n Nombre de victoire consécutives:',nb_victoire_consecutive,'')
                print(' ')
                time.sleep(2)

            elif  score_dé <= force_adversaire:
                time.sleep(2)
                print('Défaite.')
                print(' ',force_adversaire,'points de vie')
                print(' ')
                niveau_vie = niveau_vie - force_adversaire

            if niveau_vie <= 0:
                print('Niveau de vie:',niveau_vie,'')
                print('La partie est terminée, vous avez perdu.')
                print('Vous avez vaincu',nb_victoire,'monstre(s).')
                break

            else:
                combat_statut = défaite
                nb_défaite =  nb_défaite + 1
                numero_combat = numero_combat + 1
                numero_adversaire = numero_adversaire + 1
                nb_victoire_consecutive = 0
                True
        elif choix == 2:
            print('')
            print('Vous décidez de contourner ce monstre. \n -1 point de vie')
            print(' ')
            niveau_vie = niveau_vie - 1
            True

        elif choix == 3:
            print(''
                  '\n Regle du jeu:'
                  '\n Pour remporter un combat, il faut que la somme de vos dés soit supérieur a la force de votre adversaire.'
                  '\n dans ce cas, vos vie augmente du niveau de votre adversaire.'
                  '\n Une  défaite a lieu quand la valeur de vos dés sont inférieur au niveau de votre adversaire.'
                  '\n Dans ce cas, vos vie diminue du niveau de votre adversaire.'
                  '\n Vous pouvez choisir de combattre ou de contourner un adversaire et éviter le combat.'
                  '\n Dans ce cas, vous perdez une vie.'
                  '\n ')
            time.sleep(20)

            True

        elif choix == 4:
            time.sleep(1)
            print(' ')
            print('Merci et au revoir.')
            break

        else:    #continue en cas d erreur
            print(' ')
            print('erreur.'
                  '\n Ceci n est pas une option.')
            break

jeu()