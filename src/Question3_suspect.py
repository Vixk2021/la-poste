# Lire les adresses IPs warning et construction de la liste. 

fichier_warning = "input\warning.txt"
connexion_suspect = [] 

with open (fichier_warning, "r", encoding='utf-8') as f:
    contenu = f.read().splitlines()
    print (contenu, "Fichier warning")
    for line in f:
        connexion_suspect.append(line.strip())
        print (connexion_suspect, "liste de connexion suspect")

#Comparaison avec le fichier connexionLog pour identification des suspects. (PAS REUSSI SNIF) 

with open ("input/connexionlog.txt", "r") as connexion, open("out/suspect.txt","w") as suspect:
    connexionlog = connexion.read().splitlines()
    #print(connexionlog, "")
    for log in connexionlog:   
        fichier_suspect = "suspect.txt"
        ip = log.split(";")[0]
        suspect.write(ip)
        #print(ip, "Ip des connexions log")
        for element in connexion_suspect:
            if ip == element:
                print("suspect trouvé")