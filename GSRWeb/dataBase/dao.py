# # -*- coding: utf-8 -*-
# from django.db import connection
#
#
# class Dao:
#     def __init__(self):
#         """ Constructeur par défaut"""
#
#     def executeQuery(self, query):
#         """ Fonction permet d'effectuer une requête et d'en retourner
#         le résultat avec la description des colonnes
#
#         Paramètres :
#         stringQuery -- String de la requête à exécuter
#         """
#         cursor = connection.cursor()
#         cursor.execute(query)
#         row = cursor.fetchall()
#         return row
#
#     def executeQueryWithDescription(self, query):
#         """ Fonction permet d'effectuer une requête et d'en retourner
#         le résultat avec la description des colonnes
#
#         Paramètres :
#         stringQuery -- String de la requête à exécuter
#         """
#         cursor = connection.cursor()
#         cursor.execute(query)
#         row = cursor.fetchall()
#         return row, cursor.description
#
#     def retrieveDataRows(self, cursor, choiceDataList=[1, 2]):
#         """ Fonction qui permet d'obtenir les informations des colonnes de la requête
#
#         Paramètres :
#         cursor -- Curseur de la requête
#         choiceDataList = Liste qui permet de choisir quelles informations nous voulons des colonnes (PEP 249)
#         """
#         # numberNeededData = len(choiceDataList)
#         # mainList = list()
#
#     def databaseDescription(self):
#         """ Fonction qui permet d'avoir les informations concernant les tables de la base de données
#         courante et ses colonnes
#
#         """
#         queryTables = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name != '{0}' AND table_name != '{1}' AND table_name != '{2}'".format(
#             "geometry_columns", "spatial_ref_sys", "geography_columns")
#         cursor = connection.cursor()
#         cursor.execute(queryTables)
#         resultTables = cursor.fetchall()
#         dictionnaryTables = {}
#         for tables in resultTables:
#             for nameTable in tables:
#                 queryColumns = "SELECT column_name, data_type FROM information_schema.columns WHERE table_name ='{0}'".format(
#                     nameTable)
#                 cursor.execute(queryColumns)
#                 resultColumns = cursor.fetchall()
#                 dictionnaryTables[nameTable] = resultColumns
#         return dictionnaryTables
#
#     def geometryAsKML(self, binaryData):
#         """ Fonction permettant de transformer des données binaires en données KML grâce à la fonction ST_AsKML de
#         postGis
#
#         Paramètres :
#         binaryData -- Données binaires à retourner en KML
#         """
#
#         return self.executeQuery("SELECT ST_AsKML('{0}');".format(binaryData))
#
#     def dataToDisplay(self):
#         """ Permet de récupérer les données à afficher dans les formulaires en se concentrant sur les données
#         importantes de la BDD (on enlève les données redondantes telles que route, plo_debut, plo_fin, etc. et des tables)
#         Certaines colonnes à ne pas afficher sont spécifiques à des tables.
#         """
#
#         listColumnsNotDisplay = ["route", "plo_debut", "plo_fin", "abs_debut", "abs_fin", "cote"]
#         listTablesNotDisplay = ["geometry_columns", "spatial_ref_sys", "plos", "plos_sections", "sections",
#                                 "sections_suivantes", "routes", "geography_columns"]
#         queryTables = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
#         for table in listTablesNotDisplay:
#             queryTables += " AND table_name != '" + table + "'"
#         cursor = connection.cursor()
#         cursor.execute(queryTables)
#         resultTables = cursor.fetchall()
#         dictionnaryTables = {}
#         for tables in resultTables:
#             for nameTable in tables:
#                 queryColumns = "SELECT column_name FROM information_schema.columns WHERE table_name ='{0}'".format(
#                     nameTable)
#                 for column in listColumnsNotDisplay:
#                     queryColumns += " AND column_name != '{0}'".format(column)
#                 cursor.execute(queryColumns)
#                 resultColumns = cursor.fetchall()
#                 dictionnaryTables[nameTable] = resultColumns
#         return dictionnaryTables