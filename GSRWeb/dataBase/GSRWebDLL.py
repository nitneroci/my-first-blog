# -*- coding: utf-8 -*-
from ctypes import *
import os


class GSRWebDLL:
    """
    Cette classe donne l'accès à la DLL de GSR Base
    
    Ces fonctions reprènnent les fonctions de la DLL avec une modification du type pour adapté au langage C
    """

    def __init__(self):
        """
        Initialisation de la base, avec la configuration des variables et l'ouvertur du serveur puis de la base
        """

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..\static\GSRWeb\librairies\DLL_GSR_Base.dll")
        print(path)
        self.libraryBase = CDLL(r"C:\Users\Goinard\GSRWebBase\GSRWeb\static\GSRWeb\librairies\DLL_GSR_Base.dll")
        # Variables temporaires
        self.ipServ = "137.121.74.93"
        self.pwdServer = "ifsttar2012!"
        self.user = "postgres"
        self.port = "5432"

        # Ouverture du serveur

        self.ouvrir_serveur(self.ipServ, self.pwdServer, self.user, self.port)
        try:

            # Ouverture de la base

            self.ouvrir_base("CD28")
        except Exception as exceptError:
            print(exceptError)

    def ouvrir_serveur(self, ipServer, pwdServer, user, port):
        """
        Méthode permettant d'ouvrir le serveur, en transfèrant des informations à la DLL
        :param ipServer: l'ip du serveur
        :param pwdServer: le mot de passe du serveur
        :param user: le nom d'utilisateur
        :param port: le port de connexion
        :return: retourne 0 s'il y a une erreur
        """

        # Puisque les données en entrée d'une méthode de la DLL doivent être en type C, je les traduits

        ipServer_b = ipServer.encode('utf-8')
        pwdServer_b = pwdServer.encode('utf-8')
        user_b = user.encode('utf-8')
        port_b = port.encode('utf-8')

        # Voici le déroulement de l'appel d'une méthode de la DLL pour chaque appel de méthode :

        # On associe la méthode que l'on appel (ici ouvrir_serveur)
        DLLFunction = self.libraryBase.ouvrir_serveur

        # On marque le type des élement en entrer (c_char_p est un pointeur veur un chaîne de caractère)
        DLLFunction.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p]

        # On donne le type de retour
        DLLFunction.restype = c_short

        # On effectue la fonction (ici le retour est renvoyer dans le returne)
        return DLLFunction(ipServer_b, pwdServer_b, user_b, port_b)

    def ouvrir_base(self, databaseName):
        """
        Méthode permettant d'ouvrir la base, en transfèrant des informations à la DLL
        :param databaseName: Nom de la base à ouvrir
        :return: retourne 0 s'il y a une erreur
        """
        databaseName_b = databaseName.encode('utf-8')
        DLLFunction = self.libraryBase.ouvrir_base
        DLLFunction.argtypes = [c_char_p]
        DLLFunction.restype = c_short
        return DLLFunction(databaseName_b)

    def fermer_base(self):
        """
        Méthode permettant de fermer la base
        :return: retourne vrai si tous c'est bien passer, faux sinon
        """

        DLLFunction = self.libraryBase.fermer_base
        DLLFunction.restype = c_bool
        return DLLFunction()

    def vehicules_marques(self):
        """
        Méthode donnant la liste des marques de vehicule de la base
        :return: la liste des marques séparer par un ';'
        """

        DLLFunction = self.libraryBase.vehicules_marques
        DLLFunction.restype =c_char_p
        result = DLLFunction()
        return result.decode()

    def liste_des_routes(self):
        """
        Méthode donnant la liste des routes de la base
        :return: la liste des routes séparer par un ';'
        """

        DLLFunction = self.libraryBase.liste_des_routes
        DLLFunction.restype = c_char_p
        result = DLLFunction()
        return result.decode()

    def smartphones(self):
        """
        Méthode donnant la liste des smartphone (ou capteurs) de la base
        :return: la liste des capteurs séparer par un ';'
        """

        DLLFunction = self.libraryBase.smartphones
        DLLFunction.restype = c_char_p
        result = DLLFunction()
        return result.decode()

    def pseudos(self):
        """
        Méthode donnant la liste des pseudos de la base
        :return: la liste des pseudos séparer par un ';'
        """

        DLLFunction = self.libraryBase.pseudos
        DLLFunction.restype = c_char_p
        result = DLLFunction()
        return result.decode()

    def vehicules_modeles(self):
        """
        Méthode donnant la liste des modeles de vehicule de la base
        :return: la liste des modeles séparer par un ';'
        """

        DLLFunction = self.libraryBase.vehicules_modeles
        DLLFunction.restype = c_char_p
        result = DLLFunction()
        return result.decode()

    def vehicules_immatriculations(self):
        """
        Méthode donnant la liste des immatriculation de la base
        :return: la liste des immatriculation séparer par un ';'
        """

        DLLFunction = self.libraryBase.vehicules_immatriculations
        DLLFunction.restype = c_char_p
        result = DLLFunction()
        return result.decode()

    def requete_smartphone2(self, bande, debut_a, debut_m, debut_j, fin_a, fin_m, fin_j, sens, fvitesse, fstat, affmes,
                           min, max, moyenne, ecart, algofusion, s_route, vitesse, s_capteurs, s_typeveh, s_marque,
                           s_modele, s_immatriculation, s_pseudo, ecart_moyenne, nombre):
        """ Permet de faire la requete smarphone avec tout les paramètre qu'elle demande

        Paramètres :
        Les même que pour la DLL, suivre ce qui est écrit sur la fiche de la DLL

        Renvoie
        """
        bande_b = int(bande)
        print(bande_b)
        debut_a = int(debut_a)
        debut_m = int(debut_m)
        debut_j = int(debut_j)
        fin_a = int(fin_a)
        fin_m = int(fin_m)
        fin_j = int(fin_j)
        sens_b = int(sens)
        fvitesse_b = int(fvitesse)
        fstat_b = int(fstat)
        affmes_b = int(affmes)
        min_b = int(min)
        max_b = int(max)
        moyenne_b = int(moyenne)
        ecart_b = int(ecart)
        algofusion_b = int(algofusion)
        s_route_b = s_route.encode('utf-8')
        vitesse = float(vitesse)
        s_capteurs_b = s_capteurs.encode('utf-8')
        s_typeveh_b = s_typeveh.encode('utf-8')
        s_marque_b = s_marque.encode('utf-8')
        s_modele_b = s_modele.encode('utf-8')
        s_immatriculation_b = s_immatriculation.encode('utf-8')
        s_pseudo_b = s_pseudo.encode('utf-8')
        ecart_moyenne = float(ecart_moyenne)
        nombre_b = int(nombre)
        print("c1")
        DLLFunction = self.libraryBase.requete_smartphone
        print("c2")
        DLLFunction.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int,
                                c_int, c_int, c_int, c_int, c_int, c_char_p, c_float, c_char_p, c_char_p, c_char_p,
                                c_char_p, c_char_p, c_char_p, c_float, c_int]
        print("c3")
        DLLFunction.restype = c_bool
        print("c4")
        resultFunction = DLLFunction(bande_b, debut_a, debut_m, debut_j, fin_a, fin_m, fin_j, sens_b, fvitesse_b, fstat_b, affmes_b, min_b, max_b, moyenne_b, ecart_b, algofusion_b, s_route_b, vitesse, s_capteurs_b, s_typeveh_b, s_marque_b, s_modele_b, s_immatriculation_b, s_pseudo_b, ecart_moyenne, nombre_b)
            
        return resultFunction

    def requete_smartphone(self, bande, debut_a, debut_m, debut_j, fin_a, fin_m, fin_j, sens, fvitesse, fstat, affmes, min, max, moyenne, ecart, algofusion, s_route, vitesse, s_capteurs, s_typeveh, s_marque, s_modele, s_immatriculation, s_pseudo, ecart_moyenne, nombre, nbPage, nbSeuil, note1, couleur1, note2, couleur2, note3, couleur3, note4, couleur4, note5, couleur5):
        """
        Méthode très complète prenant tout les paramètre d'une requête smartphone et renvoyant différente texte ainsi qu'un tableau
        représentant la répond à la requête
        :param bande: type de bande, 0 pour PO, 1 pour MO, 2 pour GO, 3 pour IRI
        :param debut_a: année de la date de début
        :param debut_m: mois de la date de début
        :param debut_j: jour de la date de début
        :param fin_a: année de la date de fin
        :param fin_m: mois de la date de fin
        :param fin_j: jour de la date de fin
        :param sens: le sens du la zone a analysé, 0 pour positif, 1 pour négatif, 2 pour les deux sens
        :param fvitesse: 'booléen' à 1 si on active le filtre de vitesse
        :param fstat: 'booléen' à 1 si on active le filtre de statistique
        :param affmes: 'booléen' à 1 si on affiche les mesures
        :param min: 'booléen' à 1 si on affiche le maximum
        :param max: 'booléen' à 1 si on affiche le minimum
        :param moyenne: 'booléen' à 1 si on affiche la moyenne
        :param ecart: 'booléen' à 1 si on affiche l'écart-type
        :param algofusion: 'booléen' à 1 si on fait la fusion
        :param s_route: les routes à analyser séparer pas un ';' (si la liste est vide, toute les routes sont prise en compte)
        :param vitesse: le seuil de vitesse minimal (utile si fvitesse est à 1)
        :param s_capteurs: les capteurs à analyser séparer pas un ';'
        :param s_typeveh: les type de vehicule à analyser séparer pas un ';'
        :param s_marque: les marque des vehicule à analyser séparer pas un ';'
        :param s_modele: les modele des vehicule à analyser séparer pas un ';'
        :param s_immatriculation: les immatriculation des vehicule à analyser séparer pas un ';'
        :param s_pseudo: les pseudo qui ont capturer les données à analyser séparer pas un ';'
        :param ecart_moyenne: ecart à la moyenne à partir duquel on ignore la valeur
        :param nombre: 'booléen' à 1 si on affiche le nombre de valeurs que l'on a conversé pour calculer (en général ce paramètre est à 0)
        :param nbPage: le numéro de la requête (1 si c'est la première, etc ...)
        :param nbSeuil: le nombre de seuils (en fonction de ce qu'a cocher l'utilisateur)
        :param note1: la note en dessous de laquelle on est dans le seuil 1
        :param couleur1: la couleur des tracers du seuil 1
        :param note2: la note en dessous de laquelle on est dans le seuil 2
        :param couleur2: la couleur des tracers du seuil 2
        :param note3: la note en dessous de laquelle on est dans le seuil 3
        :param couleur3: la couleur des tracers du seuil 3
        :param note4: la note en dessous de laquelle on est dans le seuil 4
        :param couleur4: la couleur des tracers du seuil 4
        :param note5: la note en dessous de laquelle on est dans le seuil 5
        :param couleur5: la couleur des tracers du seuil 5
        :return resultat : une 'matrice' contenant les valeurs de la requête de la forme : [[val1ligne1,val2ligne1, ...],[val1ligne2,val2ligne2, ...], ...]
        :return texteRequete : le code HTML/JS de la page à ouvrir dans un nouvel onglet contenant la map et des options d'affichage
        :return versionTexte : la version texte de resultat que l'utilisateur pourra télécharger s'il en vois l'utilité
        :return texteActu : un texte contenant les données important pour l'actualisation de la map de la page d'accueil (ce texte sera ensuite converti en JSON)
        """

        # On passe les paramètre d'entrée en paramètre typé pour C

        bande_b = int(bande)
        debut_a = int(debut_a)
        debut_m = int(debut_m)
        debut_j = int(debut_j)
        fin_a = int(fin_a)
        fin_m = int(fin_m)
        fin_j = int(fin_j)
        sens_b = int(sens)
        fvitesse_b = int(fvitesse)
        fstat_b = int(fstat)
        affmes_b = int(affmes)
        min_b = int(min)
        max_b = int(max)
        moyenne_b = int(moyenne)
        ecart_b = int(ecart)
        algofusion_b = int(algofusion)
        s_route_b = s_route.encode('utf-8')
        vitesse = float(vitesse)
        s_capteurs_b = s_capteurs.encode('utf-8')
        s_typeveh_b = s_typeveh.encode('utf-8')
        s_marque_b = s_marque.encode('utf-8')
        s_modele_b = s_modele.encode('utf-8')
        s_immatriculation_b = s_immatriculation.encode('utf-8')
        s_pseudo_b = s_pseudo.encode('utf-8')
        ecart_moyenne = float(ecart_moyenne)
        nombre_b = int(nombre)

        #On calcule l'indice de la moyenne, cette indice est sa position sur un ligne de la requête (il dépend de min et max)

        indiceMoyenne = 9
        if min == 1 : indiceMoyenne += 1
        if max == 1 : indiceMoyenne += 1

        nbSeuil = int(nbSeuil)

        # On crée un tableau de seuils de taille 10 (5 note de seuil et 5 couleurs)

        seuils = [note1, note2, note3, note4, note5, couleur1, couleur2, couleur3, couleur4, couleur5]

        # On préparer la requête pour la DLL et on l'envoie

        DLLFunction = self.libraryBase.requete_smartphone
        DLLFunction.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int,
                                c_int, c_int, c_int, c_int, c_int, c_char_p, c_float, c_char_p, c_char_p, c_char_p,
                                c_char_p, c_char_p, c_char_p, c_float, c_int]
        DLLFunction.restype = c_bool
        resultFunction = DLLFunction(bande_b, debut_a, debut_m, debut_j, fin_a, fin_m, fin_j, sens_b, fvitesse_b, fstat_b, affmes_b, min_b, max_b, moyenne_b, ecart_b, algofusion_b, s_route_b, vitesse, s_capteurs_b, s_typeveh_b, s_marque_b, s_modele_b, s_immatriculation_b, s_pseudo_b, ecart_moyenne, nombre_b)

        #On initialise nos 3 variables de retour, elle représente :

        versionTexte = "" # Les résultats dans une version TXT
        texteActu = "" # Les données importantes pour actualise la map de la page d'acceuil

        # Et le contenu de la page HTML avec une grande map qui apparait dans un nouvel onglet

        texteRequete="""
        <!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">
    <title>Requête """ + str(nbPage) + """</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&key=AIzaSyBL6L84tc4Ecq_9hpmlqvDlh6qlkMyQK00"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.13.0/moment.min.js"></script>
    <link rel="stylesheet" type="text/css" href="../static/GSRWeb/checkbox.css" />
    <link rel="stylesheet" type="text/css" href="../static/GSRWeb/style.css" />
    <script src="../static/GSRWeb/script/palier.js"></script>
    <style type="text/css">
      html, body {
       margin: 0;
       padding: 0;
      }
      #map-canvas {
       margin: 0;
       padding: 0;
       position: absolute;
       width: calc(100% - 300px);
       display: inline-block;
       height : 100%;
      }
      #tree {
        margin-top: 10px;
        width: 300px;
        height: calc(100% - 10px);
        display: inline-block;
    }
    </style>
   <script type="text/javascript">
   var map;
   var tablePoly;
   var nbPalier1;
   var nbPalier2;
   var nbPalier3;
   var nbPalier4;
   var nbPalier5;
   var nbSeuil
   function initialize() {
  var mapOptions = {
    zoom: 9,
    center: new google.maps.LatLng(48.446777,1.487460),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
					zoomControl: true,
					zoomControlOptions: {
						position: google.maps.ControlPosition.LEFT_TOP,
						style : google.maps.ZoomControlStyle.LARGE
                  }
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);
  
var infoWindow = new google.maps.InfoWindow({
    content: "ok"
});
        """

        # On initialise d'autre variable utile

        nbPaliers = [1, 1, 1, 1 ,1] # Ne nombre de valeurs répondant au critère (du palier 1 pour la 1e valeur, pâlier 2 pour la 2e valeur ...
        total_x = 0 # L'addition des x de chaque tracer
        total_y = 0 # L'addition des y de chaque tracer
        total_points = 0 # Le nombre total de point

        if resultFunction: # Se 'if' veut dire : Si la requete_smartphone de la DLL a fonctionner ...
            resultat = [] # Cette variable sera retourner aussi, c'est un tableau qui devra être de la forme [[val1ligne1,val2ligne1, ...],[val1ligne2,val2ligne2, ...], ...]
            nbchamps = self.nombre_de_champs_requete() # On récupère le nombre de champs de la requête que l'on viens d'effectuer
            resultat.append([])

            # On commence à remplir resultat avec la première ligne contenant le nom des champs (on va aussi les écire de la version textuelle

            resultat[0].append(0)

            versionTexte += "0\t"
            for i in range(nbchamps):
                resultat[0].append(self.nom_champ_requete(i))
                versionTexte += self.nom_champ_requete(i) + "\t"
            nbligne = self.nombre_de_valeurs_requete()
            versionTexte += "\n"

            # On va ensuite commencer le traitement pour chaque ligne de la requête

            for j in range(nbligne):

                # On prépare les variable :

                resultat.append([])
                ligne = self.ligne_requete(j) # récupère la ligne à l'indice j avec les données séparer par un ';'
                valeurs = ligne.split(";") # On découpe en fonction de ce ';'

                # On ajoute à la version texte et au résultat le numéro de la ligne pour s'y retrouver plus facilement

                resultat[j + 1].append(j+1)
                versionTexte += str(j+1) + "\t"

                # On fait une boucle pour parcourir chacune des valeurs de la ligne et les ajouter au resultat et à la version texte

                for k in range(len(valeurs)):
                    resultat[j+1].append(valeurs[k])
                    versionTexte += valeurs[k] + "\t"
                versionTexte += "\n" # Sans oublier le saut de ligne à la fin de la ligne

                # Cette boucle ne sert qu'à remplir resultat avec des valeurs "vide" si cette ligne a moins de valeurs qu'il y a de colone

                if len(valeurs) < nbchamps:
                    for l in range(len(valeurs), nbchamps) :
                        resultat[j+1].append("")

                # On retrouve le nombre de tronçons

                nbtroncon = self.geometrie_requete(resultat[j+1][1], resultat[j+1][2], resultat[j+1][5], resultat[j+1][8], "2", "1")

                # On effectue un boucle parcourant chaque tronçon

                for m in range(nbtroncon):

                    # On initialise les variables dont nous aurons besoin par la suite

                    data = ""
                    trouver = False
                    tour = 1

                    # Boucle parcourant chaque seuil (en fonction du nombre de seuil que l'utilisateur a cocher)
                    while tour <= nbSeuil and not trouver:
                        if float(seuils[tour-1]) >= float(resultat[j + 1][indiceMoyenne]): # Si la note du seuil est >= à la moyenne des note de la ligne ...

                            # On crée alors une chaîne de caractère de la forme data_numeroduseuil_numerodepassage
                            # Exemple data_1_54 la 54e ligne du seuil 1

                            data = "data_"+str(tour)+"_"+str(nbPaliers[tour-1])

                            nbPaliers[tour - 1] += 1 # On incrémente le nombre de ligne lié à un palier puisque on en a ajouter une
                            trouver = True # Et on dit qu'on a trouver le palier correspondant
                        tour += 1 # On incrémente le numéro du tour (surtout si le if n'est pas respecter)
                    if data == "" : # Si la valeur de data n'a pas changer ...
                        continue # On passe au tour de boucle suivant (au tronçon suivant)

                    # Rappel : si on est rendu ici c'est qu'on a trouver le bon seuil pour cette ligne et que tour = numéro du seuil + 1

                    texteRequete += "var "+data+"_xy = [\n" # On commence à créer le tableau des coordonnées de chaque tracer (en JS)
                    texteActu += data+"\t"+seuils[tour + 3] # On ajoute data et la couleur lié au seuil dans texteActu
                    nbpointstroncon = self.nombre_points_trace(m) # On récupère le nombre de point pour tracer ce tronçon

                    # On parcour tous ces points

                    for n in range(nbpointstroncon):

                        # On récupère les coordonnée x et y de ce point (qu'on ajoute au total au passe et on incrémente le total de point

                        x = self.x_trace(m, n)
                        total_x += x
                        y = self.y_trace(m, n)
                        total_y += y
                        total_points += 1
                        texteRequete += "new google.maps.LatLng("+str(y)+","+str(x)+"),\n" # En JS : on créer des coordonnée google maps
                        texteActu += "\t"+str(y)+","+str(x) # On ajoute un tabulation pour x et y à texteActu sous la forme :   x,y


                    # On sort alors de la boucle

                    texteRequete += "];\n" # On ferme le tableau ouvert ligne 417
                    texteRequete += "var "+data+"_Path = new google.maps.Polyline({\n" \
                                         "path: "+data+"_xy,\n" # Et on commence à créer le Polyline (toujours du google map en JS)

                    texteActu += "\n" # On passe à la ligne suivant sur texte Actu

                    # On initialise des variable pour la boucle suivante, cette boucle parcour une fois de plus les seuils mais
                    # quand elle a trouver le seuil correspondant elle ajoute à texteRequete le JS correspondant à l'ajout de la
                    # couleur du seuil

                    trouver2 = False
                    tour2 = 1
                    while tour2 <= nbSeuil and not trouver2:
                        if float(seuils[tour2 - 1]) >= float(resultat[j + 1][indiceMoyenne]):
                            texteRequete += "strokeColor: '"+seuils[tour2+4]+"',\n"
                            trouver2 = True
                        tour2 += 1

                    # On fini d'ajoute les option du Polyline et on crée un data_nb_nb_valeur contenant une texte avec des informations
                    # On ajoute ensuite un evenement quand l'utilisateur survol un Polyline qui informe sur le tronçon où est la souris

                    texteRequete += "strokeOpacity: 1.0,\n" \
                             "strokeWeight: 4\n" \
                             "});\n" \
                             ""+data+"_Path.setMap(map);\n" \
                                     "var "+data+"_valeur = '"+resultat[j+1][1]+" ("+resultat[j+1][3]+"+"+resultat[j+1][4]+" - "+resultat[j+1][6]+"+"+resultat[j+1][7]+") : "+resultat[j + 1][indiceMoyenne]+"';\n"
                    texteRequete += """google.maps.event.addListener("""+data+"""_Path, 'mouseover', function(){
        document.getElementById("informationCurseur").innerHTML = """+data+"""_valeur;
        console.log('"""+data+"""');
        });
    """

        else : # Si requete_smartphone a échoué
            print("Pas de résultat")

        # On se sert de total_x/y et du total de point pour calculer la moyenne des x et des y puis on centre la map sur ces moyennes

        moyenne_y = total_y / total_points
        moyenne_x = total_x / total_points
        texteRequete += "map.setCenter(new google.maps.LatLng("+str(moyenne_y)+","+str(moyenne_x)+"));\n"

        # On associe des valeurs à des variables JS pour les utilisers par la suite

        texteRequete += "tablePoly = [];\n"
        texteRequete += "nbPalier1 = " + str(nbPaliers[0]) + ";\n"
        texteRequete += "nbPalier2 = " + str(nbPaliers[1]) + ";\n"
        texteRequete += "nbPalier3 = " + str(nbPaliers[2]) + ";\n"
        texteRequete += "nbPalier4 = " + str(nbPaliers[3]) + ";\n"
        texteRequete += "nbPalier5 = " + str(nbPaliers[4]) + ";\n"
        texteRequete += "nbSeuil = " + str(nbSeuil) + ";\n"

        # nbtotalPalier est un entier avec le nombre de valeurs tout seuil confondu

        nbtotalPalier = nbPaliers[0] + nbPaliers[1] + nbPaliers[2] + nbPaliers[3] + nbPaliers[4] - 5;

        # Pour chacune de ces valeurs

        for indice in range(nbtotalPalier) :
            trouver3 = False
            tour3 = 1
            while tour3 <= nbSeuil and not trouver3:

                # On va faire un enchaînement de if qui a pour seul but de trouve le seuil de la valeur où nous sommes rendu
                # et de faire le data correspondant bien

                if tour3 == 1:
                    if (indice + 1)<nbPaliers[0]:
                        data = "data_1_"+ str(indice + 1)
                        trouver3 = True
                elif tour3 == 2:
                    if ((indice + 2) - nbPaliers[0]) < nbPaliers[1]:
                        data = "data_2_"+ str((indice + 2) - nbPaliers[0])
                        trouver3 = True
                elif tour3 == 3:
                    if ((indice + 3) - nbPaliers[0] - nbPaliers[1]) < nbPaliers[2]:
                        data = "data_3_"+ str((indice + 3) - nbPaliers[0] - nbPaliers[1])
                        trouver3 = True
                elif tour3 == 4:
                    if ((indice + 4) - nbPaliers[0] - nbPaliers[1] - nbPaliers[2]) < nbPaliers[3]:
                        data = "data_4_"+ str((indice + 4) - nbPaliers[0] - nbPaliers[1] - nbPaliers[2])
                        trouver3 = True
                elif tour3 == 5:
                    if ((indice + 5) - nbPaliers[0] - nbPaliers[1] - nbPaliers[2] - nbPaliers[3]) < nbPaliers[4]:
                        data = "data_5_"+ str((indice + 5) - nbPaliers[0] - nbPaliers[1] - nbPaliers[2] - nbPaliers[3])
                        trouver3 = True
                tour3 += 1

            texteRequete += "tablePoly["+str(indice)+"] = "+data+"_Path;\n" # On utilise ce data pour aller chercher la variable du Polyline

        # On termine le script en JS

        texteRequete += """
            tree(tablePoly, [nbPalier1, nbPalier2, nbPalier3, nbPalier4, nbPalier5], nbSeuil);
        }
google.maps.event.addDomListener(window, 'load', initialize);
        </script>
  </head>
  <body>
    <div id="tree">"""

        # On boucle pour chaque seuil on créer le bouton à cocher pour afficher ou cacher

        for a in range(nbSeuil):
            texteRequete += """<div class="col-lg-12">
        <div class="form-group">"""
            texteRequete += '<input type="checkbox" name="palier'+str(a+1)+'" id="palier'+str(a+1)+'" autocomplete="off" CHECKED/>\n'
            texteRequete += '<div class="[ btn-group ]">\n'
            texteRequete += '<label for="palier'+str(a+1)+'" class="[ btn btn-primary ]">\n'
            texteRequete += """ <span class="[ glyphicon glyphicon-ok ]"></span>
                <span> </span>
            </label>"""
            texteRequete += ' <label for="palier'+str(a+1)+'" class="[ btn btn-default active ]">\n'
            texteRequete += 'Seuil '+str(a+1)+' (inf. à '+str(seuils[a])+')'
            texteRequete += """</label>
        </div>
        </div>
    </div>"""

        # Puis on fini le fichier HTML

        texteRequete +="""
        <div class="col-lg-12">
			<div class="input-group">
				<div class="input-group-addon">
					Télécharge la table : 
				</div>
				<div class="input-group-btn">
					<button class="btn btn-primary" onclick="window.open('Table"""+str(nbPage)+""".txt', '_blank_', false);"><span class="glyphicon glyphicon-save"></span></button>
				</div>
			</div>
		</div>
    </div>
    <div id="map-canvas"></div>
    <div id="informationCurseur"></div>
  </body>
</html>
        """

        print("fini")

        # On renvoi tous ces texte ainsi que le tableau

        return resultat, texteRequete, versionTexte, texteActu

    def x_trace(self, trace ,n):
        """
        Méthode renvoyer le x d'un point correspondant à trace et n
        :param trace: numéro du tronçon
        :param n: numéro du point dans ce tronçon
        :return: une chaîne de caractère représentant un double avec le x correspondant
        """

        DLLFunction = self.libraryBase.x_trace
        DLLFunction.argtypes = [c_int, c_int]
        DLLFunction.restype = c_double
        result = DLLFunction(trace, n)
        return result

    def y_trace(self, trace, n):
        """
        Méthode renvoyer le y d'un point correspondant à trace et n
        :param trace: numéro du tronçon
        :param n: numéro du point dans ce tronçon
        :return: une chaîne de caractère représentant un double avec le y correspondant
        """

        DLLFunction = self.libraryBase.y_trace
        DLLFunction.argtypes = [c_int, c_int]
        DLLFunction.restype = c_double
        result = DLLFunction(trace, n)
        return result

    def nombre_de_champs_requete(self):
        """
        Méthode renvoyant le nombre de champs dans la dernière requête effectuer
        :return: un entier désignant le nombre de champs
        """

        DLLFunction = self.libraryBase.nombre_de_champs_requete
        DLLFunction.restype = c_int
        result = DLLFunction()
        return result

    def nombre_de_valeurs_requete(self):
        """
        Méthode renvoyant le nombre de valeurs qu'il y a dans la requête (nombre de ligne)
        :return: un entier désignant le nombre de valeurs
        """

        DLLFunction = self.libraryBase.nombre_de_valeurs_requete
        DLLFunction.restype = c_int
        result = DLLFunction()
        return result

    def nom_champ_requete(self, n):
        """
        Méthode renvoyer le nom du champ de la requête positionner en n
        :param n: position du champ chercher
        :return: chaîne de caractère représentant le champ
        """

        DLLFunction = self.libraryBase.nom_champ_requete
        DLLFunction.argtypes = [c_int]
        DLLFunction.restype = c_char_p
        result = DLLFunction(n)
        return result.decode(encoding="unicode_escape")

    def ligne_requete(self, n):
        """
        Méthode renvoyant un ligne entière de la requête
        :param n: l'indice de cette ligne
        :return: la ligne avec chaque valeurs séparer par un ';'
        """

        DLLFunction = self.libraryBase.ligne_requete
        DLLFunction.argtypes = [c_int]
        DLLFunction.restype = c_char_p
        result = DLLFunction(n)
        return result.decode()

    def geometrie_requete(self, route, ch, distd, distf, type, continu):
        """
        Méthode renvoyant le nombre de tronçon
        :param route: la route
        :param ch: le numéro de chaussé
        :param distd: la distance du début
        :param distf: la distance de la fin
        :param type: le type de route (toujours 2)
        :param continu: si elle est continu (toujours 1)
        :return: un entier désignant le nombre de tronçon
        """

        route_b = route.encode('utf-8')
        ch_b = ch.encode('utf-8')
        distd_d = float(distd)
        distf_d = float(distf)
        type_b = type.encode(encoding="unicode_escape")
        continu_b = continu.encode(encoding="unicode_escape")
        DLLFunction = self.libraryBase.geometrie_requete
        DLLFunction.argtypes = [c_char_p, c_char_p, c_double, c_double, c_char, c_char]
        DLLFunction.restype = c_int
        result = DLLFunction(route_b, ch_b, distd_d, distf_d, type_b, continu_b)
        return result

    def nombre_points_trace(self, n):
        """
        Méthode renvoyant le nombre de point au tronçon indiquer
        :param n: le numéro du tronçon
        :return: un entier désignant le nombre de point pour tracer ce tronçon
        """
        DLLFunction = self.libraryBase.nombre_points_trace
        DLLFunction.argtypes = [c_int]
        DLLFunction.restype = c_int
        result = DLLFunction(n)
        return result