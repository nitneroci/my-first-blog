var map;
var tablePoly = [];

function executeQuery(typeForm){
    /*
    * Méthode appeler quand l'uilisateur valide de formulaire de requête
    * Prenant en paramètre : typeForm qui est une chaîne de caractère représentant le nom du formulaire de requête utilisé
    * Retournant : Rien mais fait l'affichage du tableau
    */
    console.log("Option de la requête : ");

    /*
    * On commence par récupérer chaque données du formulaire en vérifier si les champs sont rempli,
    * sinon on a une variable erreur qui est incrémenté
    */

    erreur = 0;

    for(var i = 1; i < 5; i ++){
        verif = document.getElementById("choix"+i);
        if (verif.checked){
            bande = i - 1;
        }
    }
    console.log("bande : " + bande);

    /*
    * Exemple pour la route, on récupère le nombre de route et on regarde une par une si elle sont selectionner, si c'est le cas
    * on écrit cette route à la suite des autres
    */

    s_route = "";
    nb = 0;
    selectBox = document.getElementById("route");
 
    for (i = 0; i < selectBox.length; i++) 
    {
        if (selectBox[i].selected) 
        {
            s_route = s_route + selectBox[i].value + ";";
            nb ++;
        }
    }

    // Si il n'y a aucune route de selectionner on marque une erreur de plus

    if (nb == 0) {
        erreur += 1;
    }
    else{
        // Sinon on enlève le dernier ';'

        s_route = s_route.substring(0, s_route.length-1);
    }

    // Si tout est séléctionner (autant de sélectionner qu'il y a de route dans la liste) ou met rien dans route pour la DLL

    if (nb == selectBox.length) {
        s_route = "";
    }
    console.log("s_route : " + s_route);
    
    date_debut = document.getElementById("debut").value;
    if (date_debut == ""){
        erreur += 2;
    }

    // La date au format MM/JJ/AAAA est splité par les / et donne donc :

    date_debut = date_debut.split("/");
    debut_a = date_debut[2]; // Ici AAAA pour l'année
    debut_m = date_debut[0]; // Ici MM pour le mois
    debut_j = date_debut[1]; // Ici JJ pour le jour
    console.log("debut_j-debut_m-debut_a");
    console.log(debut_j +"-"+ debut_m +"-"+ debut_a);
    
    date_fin = document.getElementById("fin").value;
    if (date_fin == ""){
        erreur += 4;
    }
    date_fin = date_fin.split("/");
    fin_a = date_fin[2];
    fin_m = date_fin[0];
    fin_j = date_fin[1];
    console.log("fin_j-fin_m-fin_a");
    console.log(fin_j +"-"+ fin_m +"-"+ fin_a);
    
    if (document.getElementById("mesures").checked) {
        affmes = 1;
    }
    else{
        affmes = 0;
    }
    console.log("affmes : " + affmes);
    
    for(i = 5; i < 8; i ++){
        verif = document.getElementById("choix"+i);
        if (verif.checked){
            sens = i - 5;
        }
    }
    console.log("sens : " + sens);
    
    s_capteurs = "";
    selectBox = document.getElementById("capteur");
 
    for (i = 0; i < selectBox.length; i++) 
    {
        if (selectBox[i].selected) 
        {
            s_capteurs = s_capteurs + selectBox[i].value + ";";
        }
    }
    if (s_capteurs == "") {
        erreur += 8;
    }
    else {s_capteurs = s_capteurs.substring(0, s_capteurs.length-1);}
    console.log("s_capteurs : " + s_capteurs);
    
    s_typeveh = "";
    selectBox = document.getElementById("typeVehicule");
 
    for (i = 0; i < selectBox.length; i++) 
    {
        if (selectBox[i].selected) 
        {
            s_typeveh = s_typeveh + selectBox[i].value + ";";
        }
    }
    if (s_typeveh == "") {
        erreur += 16;
    }
    else{s_typeveh = s_typeveh.substring(0, s_typeveh.length-1);}
    console.log("s_typeveh : " + s_typeveh);
    
    s_marque = "";
    selectBox = document.getElementById("marqueVehicule");
 
    for (i = 0; i < selectBox.length; i++) 
    {
        if (selectBox[i].selected) 
        {
            s_marque = s_marque + selectBox[i].value + ";";
        }
    }
    if (s_marque == "") {
        erreur += 32;
    }
    else{s_marque = s_marque.substring(0, s_marque.length-1);}
    console.log("s_marque : " + s_marque);
    
    s_modele = "";
    selectBox = document.getElementById("modeleVehicule");
 
    for (i = 0; i < selectBox.length; i++) 
    {
        if (selectBox[i].selected) 
        {
            s_modele = s_modele + selectBox[i].value + ";";
        }
    }
    if (s_modele == "") {
        erreur += 64;
    }
    else{s_modele = s_modele.substring(0, s_modele.length-1);}
    console.log("s_modele : " + s_modele);
    
    s_immatriculation = "";
    selectBox = document.getElementById("immatVehicule");
 
    for (i = 0; i < selectBox.length; i++) 
    {
        if (selectBox[i].selected) 
        {
            s_immatriculation = s_immatriculation + selectBox[i].value + ";";
        }
    }
    if (s_immatriculation == "") {
        erreur += 128;
    }
    else{s_immatriculation = s_immatriculation.substring(0, s_immatriculation.length-1);}
    console.log("s_immatriculation : " + s_immatriculation);
    
    s_pseudo = "";
    selectBox = document.getElementById("pseudo");
 
    for (i = 0; i < selectBox.length; i++) 
    {
        if (selectBox[i].selected) 
        {
            s_pseudo = s_pseudo + selectBox[i].value + ";";
        }
    }
    if (s_pseudo == "") {
        erreur += 256;
    }
    else{s_pseudo = s_pseudo.substring(0, s_pseudo.length-1);}
    console.log("s_pseudo : " + s_pseudo);
    
    verif = document.getElementById("filtreVitesse");
    if (verif.checked) {
        fvitesse = 1;
        vitesse = document.getElementById("vitesse").value;
    }
    else{
        fvitesse = 0;
        vitesse = 0;
    }
    console.log("fvitesse " + fvitesse +" : vitesse "+ vitesse);
    
    verif = document.getElementById("filtreStat");
    if (verif.checked) {
        fstat = 1;
    }
    else{
        fstat = 0;
    }
    console.log(fstat);
    
    ecart_moyenne = document.getElementById("ecart").value;
    console.log("ecart_moyenne : " + ecart_moyenne);
    
    if (document.getElementById("min").checked) {
        min = 1;
    }
    else{
        min = 0;
    }
    
    if (document.getElementById("max").checked) {
        max = 1;
    }
    else{
        max = 0;
    }
    
    if (document.getElementById("moy").checked) {
        moyenne = 1;
    }
    else{
        moyenne = 0;
    }
    
    if (document.getElementById("ecarttype").checked) {
        ecart = 1;
    }
    else{
        ecart = 0;
    }
    
    if (document.getElementById("fusion").checked) {
        algofusion = 1;
    }
    else{
        algofusion = 0;
    }
    console.log("min/max/moyenne/ecart/algofusion");
    console.log(min +"/"+ max +"/"+ moyenne +"/"+ecart +"/"+ algofusion);
    
    nombre = 0;
    console.log("nombre : " + nombre);

    note1 = "";
    couleur1 ="";
    note2 = "";
    couleur2 ="";
    note3 = "";
    couleur3 ="";
    note4 = "";
    couleur4 ="";
    note5 = "";
    couleur5 ="";
    
    nbSeuil = 0;

    // Cette enchaînement de 'if' sert à regarder le contenu de chaque seuil seulement s'il sont cocher

    if(document.getElementById("seuil1").checked){
        nbSeuil ++;
        note1 = document.getElementById("note1").value;
        couleur1 = document.getElementById("couleur1").value;
        console.log("note 1 : "+parseFloat(note1));
        console.log("couleur 1 : "+couleur1);
        if (note1 == "" || couleur1 == "") {
            erreur += 512;
            console.log("Erreur seuil 1");
        }
        else{
            if(document.getElementById("seuil2").checked){
                nbSeuil ++;
                note2 = document.getElementById("note2").value;
                couleur2 = document.getElementById("couleur2").value;
                console.log("note 2 : "+parseFloat(note2));
                console.log("couleur 2 : "+couleur2);
                if (note2 == "" || couleur2 == "" || parseFloat(note1) >= parseFloat(note2)) {
                    erreur += 512;
                    console.log("Erreur seuil 2");
                }
                else{
                    if(document.getElementById("seuil3").checked){
                        nbSeuil ++;
                        note3 = document.getElementById("note3").value;
                        couleur3 = document.getElementById("couleur3").value;
                        console.log("note 3 : "+parseFloat(note3));
                        console.log("couleur 3 : "+couleur3);
                        if (note3 == "" || couleur3 == "" || parseFloat(note2) >= parseFloat(note3)) {
                            erreur += 512;
                            console.log("Erreur seuil 3");
                        }
                        else{
                            if(document.getElementById("seuil4").checked){
                                nbSeuil ++;
                                note4 = document.getElementById("note4").value;
                                couleur4 = document.getElementById("couleur4").value;
                                console.log("note 4 : "+parseFloat(note4));
                                console.log("couleur 4 : "+couleur4);
                                if (note4 == "" || couleur4 == "" || parseFloat(note3) >= parseFloat(note4)) {
                                    erreur += 512;
                                    console.log("Erreur seuil 4");
                                }
                                else{
                                    if(document.getElementById("seuil5").checked){
                                        nbSeuil ++;
                                        note5 = document.getElementById("note5").value;
                                        couleur5 = document.getElementById("couleur5").value;
                                        console.log("note 5 : "+parseFloat(note5));
                                        console.log("couleur 5 : "+couleur5);
                                        if (note5 == "" || couleur5 == "" || parseFloat(note4) >= parseFloat(note5)) {
                                            erreur += 512;
                                            console.log("Erreur seuil 5");
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if (nbSeuil == 0) {
        erreur += 512;
    }

    /*
    * Tout est récupérer, si erreur est supérieur à 0 il y a eu au moins un erreur,
    * donc on affiche le message d'erreur et on arrête la fonction
    */

    if (erreur>0) {
        messageErreur(erreur);
        return;
    }

    // On affiche le chargement

    $("#loader").show();

    // On vide le tableau

    $("thead").empty();
    $("tbody").empty();

    // On fait un requête ajax qui intérroge execute query (dans views.py) avec les données récupérer

    $.ajax({
       url: '/GSRWeb/query/',
       data: {
        'bande': bande,
        'debut_a': debut_a,
        'debut_m': debut_m,
        'debut_j': debut_j,
        'fin_a': fin_a,
        'fin_m': fin_m,
        'fin_j': fin_j,
        'sens': sens,
        'fvitesse': fvitesse,
        'fstat': fstat,
        'affmes': affmes,
        'min': min,
        'max': max,
        'moyenne': moyenne,
        'ecart': ecart,
        'algofusion': algofusion,
        's_route': s_route,
        'vitesse': vitesse,
        's_capteurs': s_capteurs,
        's_typeveh': s_typeveh,
        's_marque': s_marque,
        's_modele': s_modele,
        's_immatriculation': s_immatriculation,
        's_pseudo': s_pseudo,
        'ecart_moyenne': ecart_moyenne,
        'nombre': nombre,
        'nbseuil': nbSeuil,
        'note1': note1,
        'couleur1': couleur1,
        'note2': note2,
        'couleur2': couleur2,
        'note3': note3,
        'couleur3': couleur3,
        'note4': note4,
        'couleur4': couleur4,
        'note5': note5,
        'couleur5': couleur5,
       },
       dataType: 'json',
       success: function (data){

       // Méthode appeler quand on a réussi la requête, on parcour les résultat et les ajoute au tableau

        var premier = true; // Ce booléen sert à effectuer un traitement légèrement différent à la première ligne
        for(var ligne in data){
            valeurs = data[ligne];
            if (premier) {
                $("thead").append("<tr>");

                // On crée les balises pour remplir le header du tableau

                for (var j = 0; j < valeurs.length; j ++){
                    $("thead").append("<th>"+valeurs[j]+"</th>");
                }
                $("thead").append("</tr>");
                premier = false;
            }
            else{
                $("tbody").append("<tr>");

                // On crée les balises pour remplir le contenu du tableau

                for (var k = 0; k < valeurs.length; k ++){
                    $("tbody").append("<th>"+valeurs[k]+"</th>");
                }
                $("tbody").append("</tr>");
            }
        }
        console.log("Success !");

        // On vide la map de la page d'accueil

        viderMap();
        setTimeout(function(){

            // On actualise cette map de la page d'accueil

            actualiserMap();
            setTimeout(function(){

                // On enlève le chargement

                $("#loader").hide();
            },100);
        },100);
       },
       error: function(){

       // Méthode appeler en cas d'erreur dans la réponse à ajax et on enlève juste le chargement et affiche un message générique

       messageErreur(0);
        $("#loader").hide();
       }
    });
    
    return false;
}

function messageErreur(num_erreur) {

    // Méthode appeler s'il y a au moins un erreur avec un entier en entré

    num = num_erreur; // On fait un copie, num est un entier correspondant a un code binaire permettant de savoir les entiers additionner

    message_erreur = "Vous avez oublier de remplir les champs suivant :\n"; // Le début du message

    if (num_erreur == 0) {
        message_erreur = "Erreur lors de la requête." // Cas exceptionnel ou la requête a échouer
    }
    if (num >=512) {
        message_erreur = message_erreur + "Soucis de seuil (vérifier que ces en ordre croissant)\n"; // On ajoute des ligne en fonction
        num = num - 512;
    }
    if (num >=256) {
        message_erreur = message_erreur + "Pseudo\n";
        num = num - 256;
    }
    if (num >= 128) {
        message_erreur = message_erreur + "Immat\n";
        num = num - 128;
    }
    if (num >= 64) {
        message_erreur = message_erreur + "Modele\n";
        num = num - 64;
    }
    if (num >= 32) {
        message_erreur = message_erreur + "Marque\n";
        num = num - 32;
    }
    if (num >= 16) {
        message_erreur = message_erreur + "Type\n";
        num = num - 16;
    }
    if (num >= 8) {
        message_erreur = message_erreur + "Capteur\n";
        num = num - 8;
    }
    if (num >= 4) {
        message_erreur = message_erreur + "Date de début de période\n";
        num = num - 4;
    }
    if (num >= 2) {
        message_erreur = message_erreur + "Date de fin de période\n";
        num = num - 2;
    }
    if (num == 1) {
        message_erreur = message_erreur + "Route";
        num = num - 1;
    }

    window.alert(message_erreur); // On fait une simple window.alert de ce message
}
function initMap(){

    // Méthode d'initialisation de la map, appeler quand l'on charge la page

    var ouest = {lat: 47.983221, lng: -0.962226};
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
        center: ouest
    });
}

function viderMap() {

    // Méthode vidant la map de ces tracers, faite en parcourant la liste de ces tracers

    for (var i in tablePoly) {
        tablePoly[i].setMap(null);
    }

    // On vide aussi le tableau des tracers

    tablePoly = [];
}