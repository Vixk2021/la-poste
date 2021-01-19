
with open ("input/connexionlog.txt", "r") as connexiontest, open("out/utilisateurs.txt","w") as mon_fichier:
#f = open('input\connexiontest.txt', 'r')
#g = open('out\utilisateurs.txt', "w")
    for line in connexiontest:
        nom_fichier = "utilisateurs.txt"
        nom_utilisateurs = line.split(";")[1]
        mon_fichier.write("%s\n" % nom_utilisateurs)
        #print(mon_fichier)
        print(nom_utilisateurs)

#mon_fichier.close()
#=open('Input/connexion.log','r'+)