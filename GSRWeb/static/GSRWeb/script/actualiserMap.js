function actualiserMap() {

    // Méthode récupérant le contenu de Actu?.txt et en affiche un map, par le biai d'une requête ajax

    $.ajax({
       url: '/GSRWeb/recup/',
       dataType: 'json',
       success: function (data){

            // En cas de réussite on va parcourir le tableau des résultats et affichage chaque tracer

            total_x = 0; // Variable contenant l'addition de tout les 'x' (coordonnée)
            total_y = 0; // Variable contenant l'addition de tout les 'y' (coordonnée)
            nbxy = 0; // Nombre de x et de y
            for (var i in data) {
                localisation = []; // Tableau contenant les coordonnées du tracer
                for (var j in data[i]) {

                    // Pour chaque valeur d'une ligne, on récupère les deux valeurs (x,y)

                    valeurs = data[i][j].split(",");
                    if (valeurs.length == 2) { // S'il y a deux valeurs le x et le y
                        localisation.push(new google.maps.LatLng(valeurs[0], valeurs[1])); // On ajoute au tableau

                        // On fait les addition pour le calcul plus tard

                        total_x = total_x + parseFloat(valeurs[0]);
                        total_y += parseFloat(valeurs[1]);
                        nbxy ++;
                    }
                }

                // Pour charque tracer on le crée avec les coordonnée récupérer et la couleur qui lui est lié
                tablePoly[i] = new google.maps.Polyline({
                    path: localisation, // Coordonnée
                    strokeColor: data[i][1], // Couleur
                    strokeOpacity: 1.0,
                    strokeWeight: 4
                    });
                tablePoly[i].setMap(map); // On le lie à la map
            }
            moyenne_x = total_x/nbxy; // Calcul de la moyenne des x

            moyenne_y = total_y/nbxy; // Calcul la moyenne de y

            map.setCenter(new google.maps.LatLng(moyenne_x,moyenne_y)); // Cente à la moyenne de x et moyenne de y

            map.setZoom(9); // Valeur de zoom la plus approprié
       }
    });
}
