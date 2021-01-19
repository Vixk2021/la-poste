with open ("input\connexionlog.txt", "r") as connexiontest, open("out\heure_connexion.txt","w") as mon_fichier:
#f = open('input\connexiontest.txt', 'r')
#g = open('out\utilisateurs.txt', "w")
    for line in connexiontest:
        #separateurs = " ", " : "
        nom_fichier = "heure_connexion.txt"
        heure_connexion = line.split(" ")[1]
        utilisateur = line.split(";")[1]
        ip = line.split(";")[0]
        #connexion, date_heure = line.split(";")[0]
        mon_fichier.write("%s" % heure_connexion)
       # print(heure_connexion)
        if heure_connexion < "08:00":
            print (ip, utilisateur, heure_connexion.strip(), "connexion avant 8h00")
        elif heure_connexion > "19:00":
            print(ip, utilisateur, heure_connexion.strip(), "connexion après 19H00")
        #else: 
         #   print(heure_connexion.strip(), "else")
#mon_fichier.close()

