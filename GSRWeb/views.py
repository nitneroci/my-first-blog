from django.shortcuts import render
from django.http import JsonResponse
import webbrowser
import shutil
import json
import os
import fnmatch
from GSRWeb.dataBase.GSRWebDLL import GSRWebDLL
# Create your views here.

# Ici on sa connecte à la base, puis on fait le ménage dans les fichiers temporaire
accessDLL = GSRWebDLL()

cheminAcces = '/Users/Goinard/GSRWebBase/GSRWeb/temp' # Cette variable doit être modifier en fonction de l'emplacement de ce fichier

for file in os.listdir(cheminAcces):
    if fnmatch.fnmatch(file, '*.txt'):
        os.remove(cheminAcces + '/' + file)
    if fnmatch.fnmatch(file, '*.html'):
        os.remove(cheminAcces + '/' + file)

nbPage = 1;

def index(request):
    """
    Cette méthode est appeler quand l'utilisateur va sur le site, elle sert à initialisé les listes pour l'affichage
    de départ du formulaire.
    :param request: paramètre obligatoire de Django
    :return: l'affichage de la page d'accueil accompagner des valeurs des listes
    """
    context = {}

    # Appel à la DLL pour récupérer la liste des route, puis le split pour la former bien en liste
    context["listRoad"] = accessDLL.liste_des_routes().split(";")

    # Appel à la DLL pour récupérer la liste des marques, puis le split pour la former bien en liste
    context["listMarque"] = accessDLL.vehicules_marques().split(";")

    # Appel à la DLL pour récupérer la liste des marques, ...
    context["listCapteur"] = accessDLL.smartphones().split(";")

    # Appel à la DLL ...
    context["listModele"] = accessDLL.vehicules_modeles().split(";")

    # ...
    context["listImmat"] = accessDLL.vehicules_immatriculations().split(";")

    # ...
    context["listPseudo"] = accessDLL.pseudos().split(";")

    # Liste pour les emplacements

    return render(request, 'GSRWeb/index.html', context=context)

def executeQuery(request):
    """
    Méthode appeler par le site quand on valide un formulaire pour récupérer le JSON, il récupère les données du formulaire puis
    les envoies à la DLL, il reformate ensuite ce que retourne la DLL pour pouvoir renvoyer un format JSON efficace
    :param request: paramètre obligatoire de Django
    :return: un JSON contenant le résultat de la requête
    """
    global nbPage
    # Les valeurs du formulaires sont récupérer et formater pour ensuite pouvoir être renvoyer à la DLL
    print("executeQuery")
    bande = request.GET.get('bande', None)
    debut_a = request.GET.get('debut_a', None)
    debut_m = request.GET.get('debut_m', None)
    debut_j = request.GET.get('debut_j', None)
    fin_a = request.GET.get('fin_a', None)
    fin_m = request.GET.get('fin_m', None)
    fin_j = request.GET.get('fin_j', None)
    sens = request.GET.get('sens', None)
    fvitesse = request.GET.get('fvitesse', None)
    fstat = request.GET.get('fstat', None)
    affmes = request.GET.get('affmes', None)
    min = request.GET.get('min', None)
    max = request.GET.get('max', None)
    moyenne = request.GET.get('moyenne', None)
    ecart = request.GET.get('ecart', None)
    algofusion = request.GET.get('algofusion', None)
    s_route = request.GET.get('s_route', None).replace("%3B", ";").replace("%20", " ")
    vitesse = request.GET.get('vitesse', None)
    s_capteurs = request.GET.get('s_capteurs', None).replace("%3B", ";").replace("%20", " ")
    s_typeveh = request.GET.get('s_typeveh', None).replace("%3B", ";").replace("%20", " ")
    s_marque = request.GET.get('s_marque', None).replace("%3B", ";").replace("%20", " ")
    s_modele = request.GET.get('s_modele', None).replace("%3B", ";").replace("%20", " ")
    s_immatriculation = request.GET.get('s_immatriculation', None).replace("%3B", ";").replace("%20", " ")
    s_pseudo = request.GET.get('s_pseudo', None).replace("%3B", ";").replace("%20", " ")
    ecart_moyenne = request.GET.get('ecart_moyenne', None)
    nombre = request.GET.get('nombre', None)
    nbSeuil = request.GET.get('nbseuil', None)
    note1 = request.GET.get('note1', None)
    couleur1 = request.GET.get('couleur1', None).replace("%23", "#")
    note2 = request.GET.get('note2', None)
    couleur2 = request.GET.get('couleur2', None).replace("%23", "#")
    note3 = request.GET.get('note3', None)
    couleur3 = request.GET.get('couleur3', None).replace("%23", "#")
    note4 = request.GET.get('note4', None)
    couleur4 = request.GET.get('couleur4', None).replace("%23", "#")
    note5 = request.GET.get('note5', None)
    couleur5 = request.GET.get('couleur5', None).replace("%23", "#")

    # Des valeurs pour tester

    # bande = "1"
    # debut_a = "2017"
    # debut_m = "01"
    # debut_j = "01"
    # fin_a = "2017"
    # fin_m = "04"
    # fin_j = "24"
    # sens = "2"
    # fvitesse = "0"
    # fstat = "0"
    # affmes = "1"
    # min = "0"
    # max = "0"
    # moyenne = "1"
    # ecart = "0"
    # algofusion = "0"
    # s_route = "D0012"
    # vitesse = "0"
    # s_capteurs = "SZ5"
    # s_typeveh = "VL;UTIL;PL"
    # s_marque = "Renault"
    # s_modele = "Kangoo"
    # s_immatriculation = "DL-012-TE"
    # s_pseudo = "Dunois"
    # ecart_moyenne = "1"
    # nombre = "0"

    # On appel la grosse requête de la DLL

    resultreq, texteHTML, versionTexte, texteActu = accessDLL.requete_smartphone(bande, debut_a, debut_m, debut_j, fin_a, fin_m, fin_j, sens, fvitesse, fstat, affmes, min, max, moyenne, ecart, algofusion, s_route, vitesse, s_capteurs, s_typeveh, s_marque, s_modele, s_immatriculation, s_pseudo, ecart_moyenne, nombre, nbPage, nbSeuil, note1, couleur1, note2, couleur2, note3, couleur3, note4, couleur4, note5, couleur5)

    dict = {}
    # On formate le résultat pour qu'il soit convertissable en JSON
    for ligne in resultreq:
        key, value = ligne[0],ligne[1:]
        dict[key] = value

    # Je remplie le fichier Table?, fichier téléchargeable de la table en format TXT
    y = open('GSRWeb/temp/Table' + str(nbPage) + '.txt', 'w')

    y.write(versionTexte)

    y.close()

    # Je remplie le fichier Actu?, fichier contenant les informations de base pour afficher la map

    z = open('GSRWeb/temp/Actu'+str(nbPage)+'.txt', 'w')

    z.write(texteActu)

    z.close()

    # Je remplie le fichier Temp?, fichier contenant la map propre avec les quelques options d'affichage

    x = open('GSRWeb/temp/Temp'+str(nbPage)+'.html', 'w')

    x.write(texteHTML)

    x.close()

    # J'ouvre cette map

    webbrowser.open('C:' + cheminAcces + '/Temp'+str(nbPage)+'.html')

    # On augmente le nombre de page map de 1 puisque on viens d'en ajouter une

    nbPage = nbPage + 1

    # Et on retourne le dictionnaire en format JSON

    return JsonResponse(dict)


def recupDonnee(request):
    """
    Méthode appeler par le site quand il essai d'afficher la réponse sur la page principal, en effet cette méthode renvoie
    un JSON avec les information du dosser Actu?.txt qui servent à l'affichage de la map sur la page d'accueil
    :param request: paramètre obligatoire de Django
    :return: un JSON contenant le contenu essnetiel à l'affichage de la map
    """

    # On ouvre le fichier et on récupère son contenu

    file = open('GSRWeb/temp/Actu' + str(nbPage - 1) + '.txt', 'r')
    content = file.read()

    # On traite ce qui est dans le fichier pour faire un dictionnaire en reprennant le contenu et en le découpant en fonction
    # des saut de ligne et des tabulation

    resultat = content.split("\n")
    dictionary = {}

    for i in range(len(resultat) - 1):
        dictionary[i] = resultat[i].split("\t")

    # Et on retourne le dictionnaire en format JSON

    return JsonResponse(dictionary)