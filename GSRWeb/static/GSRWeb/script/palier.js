function tree(tablePoly, tablePaliers, nbSeuil) {

    // Méthode associant les évènement au chaque checkbox de la page avec juste la map

    console.log(tablePoly);
    console.log(tablePaliers);
    console.log(nbSeuil);

    // Le tout en fonction du nombre de seuil

    if (nbSeuil >= 1) {

        // S'il y a au moins un seuil, ou ajoute une fonction quand on click sur le checkbox

        document.getElementById('palier1').onclick=function(){

            // Méthode qui, si on coche la case, rend tout les tracer correspondant au seuil 1 visible sinon les rend invisible

            if (document.getElementById('palier1').checked == true) {
                for (var i = 0; i < tablePaliers[0]-1; i++) {
                    tablePoly[i].setVisible(true);
                }
            }
            else{
               for (var j = 0; j < tablePaliers[0]-1; j++) {
                    tablePoly[j].setVisible(false);
                } 
            }
        }
    }

    // De même pour les autres si le seuil est existant

    if (nbSeuil >= 2) {
        document.getElementById('palier2').onclick=function(){
            fin = tablePaliers[1]+tablePaliers[0]-2;
            if (document.getElementById('palier2').checked == true) {
                for (var i = tablePaliers[0]-1; i < fin; i++) {
                    tablePoly[i].setVisible(true);
                }
            }
            else{
               for (var j = tablePaliers[0]-1; j < fin; j++) {
                    tablePoly[j].setVisible(false);
                } 
            }
        }
    }
    
    if (nbSeuil >= 3) {
        document.getElementById('palier3').onclick=function(){
            debut = tablePaliers[1]+tablePaliers[0]-2;
            fin = tablePaliers[1]+tablePaliers[0]+tablePaliers[2]-3;
            if (document.getElementById('palier3').checked == true) {
                for (var i = debut; i < fin; i++) {
                    tablePoly[i].setVisible(true);
                }
            }
            else{
               for (var j = debut; j < fin; j++) {
                    tablePoly[j].setVisible(false);
                } 
            }
        }
    }
    
    if (nbSeuil >= 4) {
        document.getElementById('palier4').onclick=function(){
            debut = tablePaliers[1]+tablePaliers[0]+tablePaliers[2]-3;
            fin = tablePaliers[1]+tablePaliers[0]+tablePaliers[2]+tablePaliers[3]-4;
            if (document.getElementById('palier4').checked == true) {
                for (var i = debut; i < fin; i++) {
                    tablePoly[i].setVisible(true);
                }
            }
            else{
               for (var j = debut; j < fin; j++) {
                    tablePoly[j].setVisible(false);
                } 
            }
        }
    }
    
    if (nbSeuil == 5) {
        document.getElementById('palier5').onclick=function(){
            debut = tablePaliers[1]+tablePaliers[0]+tablePaliers[2]+tablePaliers[3]-4;
            fin = tablePaliers[1]+tablePaliers[0]+tablePaliers[2]+tablePaliers[3]+tablePaliers[4]-5;
            if (document.getElementById('palier5').checked == true) {
                for (var i = debut; i < fin; i++) {
                    tablePoly[i].setVisible(true);
                }
            }
            else{
               for (var j = debut; j < fin; j++) {
                    tablePoly[j].setVisible(false);
                } 
            }
        }
    }
}