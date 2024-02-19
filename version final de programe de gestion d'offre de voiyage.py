#declaration des classes et leur methodes

#---------------------------------------------------------------------------------------------
class Date:
    def __init__(self,jour,mois,anne):
        self.jour =jour
        self.mois =mois
        self.anne =anne
    def saisir_date(self):
      
      while True:
            
            self.jour = int(input("saisir le jour:"))
            if self.jour > 31 or self.jour <= 0:
                print("Répétez à nouveau et veuillez entrer le jour  correctement !!!\n")
                continue

            self.mois = int(input("saisir le mois :"))
            if self.mois > 12 or self.mois <= 0:
                print("Répétez à nouveau et veuillez entrer le mois  correctement !!!\n")
                continue

            self.anne = int(input("Vsaisir l'année :"))
            if len(str(self.anne)) != 4 :
                print("Répétez à nouveau et veuillez entrer l'année  correctement  (contient 4 nombre)!!!\n")
                continue
            
            if self.anne<2020:
                print("vous ne pouvez pas declarer un offre avant de l'anne 2020,repeter de nouveau")
                continue
            if self.anne>2050:
                print("vous ne pouvez pas declarer un offre apres  l'anne 2050,repeter de nouveau")
                continue
            break
      
      
    def afficher_date(self):
            d_of= f"{self.jour}/{self.mois}/{self.anne}"
            return d_of
    
   #ensemble de methode que j'ai les inclut pour permetre la comparaison des date 
    def __eq__(self, other):
        if isinstance(other, Date):
            return (self.anne, self.mois, self.jour) == (other.anne, other.mois, other.jour)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Date):
            return (self.anne, self.mois, self.jour) < (other.anne, other.mois, other.jour)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Date):
            return (self.anne, self.mois, self.jour) <= (other.anne, other.mois, other.jour)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Date):
            return (self.anne, self.mois, self.jour) > (other.anne, other.mois, other.jour)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Date):
            return (self.anne, self.mois, self.jour) >= (other.anne, other.mois, other.jour)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Date):
            return (self.anne, self.mois, self.jour) != (other.anne, other.mois, other.jour)
        return NotImplemented



#--------------------------------------------------------------------------------------------------------------------------------------------
class Offre_voiyage:
    def __init__(self,Ref_Offre,Ville_de_depart,Ville_d_arrivee,date_offre):
        self.Ville_de_depart=Ville_de_depart
        self.Ville_d_arrivee=Ref_Offre
        self.Ref_Offre=Ville_d_arrivee
        self.date_offre=Date("","","")
    def declaration_offre(self):
        
        while True:
            try:
                f=open("offre.txt","r")
                contenu=f.readlines()
                nbr=str(len(contenu))
                self.Ref_Offre=nbr
                self.Ville_de_depart=str(input(" la ville de depart:"))
                self.Ville_d_arrivee=str(input(" la ville d'arriver:"))
                print(">>saisir la date de depart:<<")
                self.date_offre.saisir_date()
                
            except ValueError :
                print("Erreur de saisie. Veuillez entrer des valeurs correctes.")
            else:
                break
    def afficher_offre_info(self):
       info=f">la reference:{self.Ref_Offre}\t\t>la ville de depart:{self.Ville_de_depart}\t\t>la ville d'arriver:{self.Ville_d_arrivee}\t\t>la date de depart:{self.date_offre.afficher_date()}\t\t"   #  la date de d'experation d'offre:{self.date_offre1.afficher_date()}"
       return info
    
    

#-------------------------------------------------------------------------------------------------------------------------------------
class Transport_Aller_Simple(Offre_voiyage):
    def __init__(self,Ref_Offre,Ville_de_depart,Ville_d_arrivee,date_offre,prix_a_simple):
        super().__init__(Ref_Offre,Ville_de_depart,Ville_d_arrivee,date_offre)
        self.prix_a_simple=prix_a_simple
        self.type_="aller simple"
        self.statut="debloquer"
        
    def decla_offre_aller_simple(self):
        print(f">>>declaration d'offre de voiyage de type: {self.type_}<<<<")
        super().declaration_offre()
        while True:
            try:
                prix_input=float(input("le prix d'offre:"))
                self.prix_a_simple=round(prix_input,2) 
            except ValueError:
                print("le prix doit etre de type float!!,vueillez  le saisir de nouveau: ")
            else:
                break
    def affichage_offre_aller_simple(self):
        info=super().afficher_offre_info()
        return f"le type d'offre:{self.type_}\t\t{info}\t\t>>le prix:{self.prix_a_simple}"
    def aller_simple_dico(self):# rendre les information d'offre en format dictionaire pour permetre les stoques
        dico={
              "reference":self.Ref_Offre,
              "type d'offre":self.type_,
              "statut d'offre":self.statut,
              "ville de depart":self.Ville_de_depart,
              "Ville d'arriver":self.Ville_d_arrivee,
              "la date de depart":self.date_offre.afficher_date(),
              "le prix ":self.prix_a_simple
             }
        return dico
 
    
 
#----------------------------------------------------------------------------------------------------------------
class Transport_Aller_Retour(Transport_Aller_Simple):
    def __init__(self,Ref_Offre,Ville_de_depart,Ville_d_arrivee,date_offre,prix_a_simple,date_arriver):
         super().__init__(Ref_Offre,Ville_de_depart,Ville_d_arrivee,date_offre,prix_a_simple)
         self.prix_a_simple=prix_a_simple
         self.date_arriver=Date("","","")
         self.type_="Transpor aller/retour"
         self.statut="debloquer"
    def decla_offre_aller_retour(self):
         
         super().decla_offre_aller_simple()
         print(">>sasir la date d'ariver:<<")
         self.date_arriver.saisir_date()
    def affichage_offre_aller_retour(self):
        info=super().affichage_offre_aller_simple()
        return f"{info}\t\t>>la date d'arriver:{self.date_arriver.afficher_date()}\t\t"
    def aller_retour_dico(self):
        dico={
              "reference":self.Ref_Offre,
              "type d'offre":self.type_,
              "statut d'offre":self.statut,
              "ville de depart":self.Ville_de_depart,
              "Ville d'arriver":self.Ville_d_arrivee,
              "la date de depart":self.date_offre.afficher_date(),
              "la date d'arriver":self.date_arriver.afficher_date(),
              "le prix ":self.prix_a_simple
             }
        return dico
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------
class Hebergement(Offre_voiyage):
    def __init__(self,Ref_Offre,date_offre,ville_de_depart,Ville_d_arrivee):
        super().__init__(Ref_Offre,ville_de_depart,Ville_d_arrivee,date_offre)
        self.nombre_de_nuit=0
        self.type_offre ="hebergement"
        self.type=""
        self.prix_par_nuit=0
        self.statut="debloquer"
        self.prix_total=0
    def declaration_hebergement(self):
        print(">>>declaration d'offre de voiyage de type:hebergement<<<<")
        super().declaration_offre()
    def declaration_des_prpriete(self):#declaration des propriete de l'hebergement
        while True:
            try:
                prix_input=float(input("le prix par nuit  ( float):"))
                self.prix_par_nuit=round(prix_input,2)
                self.nombre_de_nuit=int(input("le nombre de nuit (entier):"))
                self.prix_total=self.prix_par_nuit*self.nombre_de_nuit
                
                choix=int(input("preciser le type d'ebergement parmi les choix  :\n1:déjeuner\n:demi-pension\n3:pension complète\nchoix:"))
                if choix==1:
                    self.type="dejeuner"
                elif choix==2:
                    self.type="demi-pension"
                elif choix==3:
                    self.type="pension complete"
                else :
                    print("Ereur de saisie!! le choix doit etre soit (1),(2)ou(3),veuilez renter les information de nouveau")
                    continue
            except ValueError:
                print("Ereur de saisie veuillez respecter la forme de saisie!!")
            else:
                break
    def affichage_offre_hebergement_info(self):
        info=super().afficher_offre_info()
        return f"le type d'offre:{self.type_offre}\t\t{info}\t\ttype d'ebergement:{self.type}\t\tnombre de nuits:{self.nombre_de_nuit}\t\tprix par nuit:{self.prix_par_nuit}\t\t"
    
    def affichage_hebergement_prpriete(self):
        return f"type d'ebergement:{self.type}\t\tnombre de nuits:{self.nombre_de_nuit}\t\tprix par nuit:{self.prix_par_nuit}\t\t"
    def dico_hebergement(self):
        dico={ 
                "reference":self.Ref_Offre,
                "type d'offre":self.type_offre,
                "statut d'offre":self.statut,
                "ville de depart":self.Ville_de_depart,
                "Ville d'arriver":self.Ville_d_arrivee,
                'la date de depart':self.date_offre.afficher_date(),
                "type d'ebrgement":self.type,
                "nombre de nuit":self.nombre_de_nuit,
                "le prix par nuit":self.prix_par_nuit,
                "le prix ":self.prix_total
            }
        return dico
    
    
#---------------------------------------------------------------------------------------------------------------------------  
class Formule_complete(Transport_Aller_Retour,Hebergement):
    def __init__(self, Ref_Offre, date_offre, Ville_de_depart, Ville_d_arrivee,
                 prix_a_simple, date_arriver, type, nombre_de_nuit, prix_par_nuit):
        super().__init__(Ref_Offre, Ville_de_depart, Ville_d_arrivee, date_offre,
                         prix_a_simple, date_arriver)
        self.typeF=''
        self.type_="Formule complete"
        self.prix_total=0
        self.statut="debloquer"
    def declaration_formule_complete(self):
        super().decla_offre_aller_retour()
        super().declaration_des_prpriete()
        self.prix_total=self.prix_a_simple+self.nombre_de_nuit*self.prix_par_nuit
        while True:
            try:
                choix=int(input("preciser le type de Formule complete parmi les choix  :\n1:week-end\n2:semaine\nchoix:"))
                if choix==1:
                    self.typef="week-end"
                elif choix==2:
                    self.typef="semaine"
                else :
                    print("Ereur de saisie!! le choix doit etre soit (1)ou(2),veuillez renter les information de nouveau:")
                    continue
            except ValueError:
                print("Ereur de saisie !! le choix ne peux pas etre une lettre")
            else:
                break
    def affichage_offre_formule_complete(self):
        info1=super().affichage_offre_aller_retour()
        info2=super().affichage_hebergement_prpriete()
        return f"le type d'offre:{self.type_}\t{info1}\t{info2}"
    def dico_Formule_complete(self):
        dico={
              "reference":self.Ref_Offre,
              "type d'offre":self.type_,
              "statut d'offre":self.statut,
              "ville de depart":self.Ville_de_depart,
              "Ville d'arriver":self.Ville_d_arrivee,
              "la date de depart":self.date_offre.afficher_date(),
              "la date d'arriver":self.date_arriver.afficher_date(),
              "type d'ebrgement":self.type,
              "type de formule complete":self.typef,
              "nombre de nuit":self.nombre_de_nuit,
              "le prix par nuit ":self.prix_par_nuit,
              "prix aller/retour ":self.prix_a_simple,
              "le prix ":self.prix_total
              
             }
        return dico
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.   
class Reservation:
        def __init__(self):
            self.Ref_reservation=""
            self.Type_Offre=""
            self.Ref_Offre=""
            self.Date_depart=""
            self.Date_de_retour=None #(obligatoire en cas A/R)
            self.Genre=''
            self.Nom=''
            self.Prenom=''
            self.Pays_org_passeport=''                                  #(Nationalité)
            self.NO_Passeport=''
            self.Etat_Reservation='en cours'                                    
            self.Total_A_Payer=0 #(- 10% de la somme prix Transport et Hébergement)
        
        
        def declaration_de_reservation(self):
            print(">> Déclaration de réservation de client")
            l=[]
            f = open("reservation.txt", "r")
            contenu=f.readlines()
            nbr = str(len(contenu))
            self.Ref_reservation = nbr
            f.close()
            f2 = open("offre.txt", "r")
            contenu_offre = f2.readlines()
            f2.close()
            ref_input = input("Précisez la référence de l'offre: ")
            for line in contenu_offre:
                if 'reference' in line :
                    dico = string_to_dico(line)
                    if dico['reference']==ref_input:
                        if dico["statut d'offre"]=='bloquer':
                            print(f"vous ne pouvez pas passer cette reservation car l'offre de reference {ref_input} est bloquer !!")
                            return 0
                        else:
                            self.Ref_Offre = ref_input 
                            pr = dico["le prix "] * 0.9
                            self.Total_A_Payer = pr
                            self.Date_depart = dico['la date de depart']
                            self.Type_Offre = dico["type d'offre"]
                            if self.Type_Offre == 'Transpor aller/retour' or self.Type_Offre == "Formule complete":
                                self.Date_de_retour = dico["la date d'arriver"]
                            else:
                                self.Date_de_retour=None
                            while True:
                                    g = input("Le genre de client (1:homme, 2:femme): ")
                                    if g == "1":
                                        self.Genre = 'homme'
                                        break
                                    elif g == "2":
                                        self.Genre = 'femme'
                                        break
                                    else:
                                        print("Choix invalide !!")
                                        continue
                                    
                            self.Nom = input("Le nom de client: ")
                            self.Prenom = input("Le prénom de client: ")
                            self.Pays_org_passeport = input("Le pays d'origine (nationalité) client: ")
                            self.NO_Passeport = input("Le numéro de passeport: ")
                            l.append(line)
                            break
                    
            if l:
                return l
            else:
                print("la reference n'existe pas")
                return 0
                
        def affichage_reservation_info(self):
            return f"les information de reservation:Ref_reservation:{self.Ref_reservation}\nType_Offre:{self.Type_Offre}\nRef_Offre:{self.Ref_Offre}\nDate_depart:{self.Date_depart}\nDate_de_retour:{self.Date_de_retour}\nGenre de client:{self.Genre}\nNom:{self.Nom}\nPrenom:{self.Prenom}\nPays_org_passeport:{self.Pays_org_passeport}\nNO_Passeport:{self.NO_Passeport}\nEtat_Reservation:{self.Etat_Reservation}\nTotal_A_Payer:{self.Total_A_Payer}"
        
        def dico_reservation(self):
            dico={ 'reference' :self.Ref_reservation,
            "Type d'offre":self.Type_Offre,
            "reference d'offre":self.Ref_Offre,
            "la date de depart":self.Date_depart,
            "date de retour":self.Date_de_retour,
            "le genre de client ":self.Genre,
            "le nom de client":self.Nom,
            "le prenom de client ":self.Prenom,
            "le pays d'origine":self.Pays_org_passeport,
            "le numero de passport":self.NO_Passeport,
            "l'etat de reservation":self.Etat_Reservation,                             
            "le prix":self.Total_A_Payer,
            }
            return dico
        
#fonctions auxiliaires: #######################################################33       
def dico_to_str(d):
        chaine=str(d)
        return chaine


def sauvegarde(nomfichier,contenu):
        with open (nomfichier,"a+") as f:
            f.write(contenu+"\n")
            


def contenu_fichier(fichier):
    with open (fichier,"r") as f:
        l=f.readlines()
        return l
    

def supprimer_ligne(nom_fichier, ligne_a_supprimer):#je n'ai pas utilise cette fonction dans mon programe ,mais je l'ai garde pour d'autre programe pour le future 
    # Lire le contenu du fichier
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()

    # Supprimer la ligne cible si elle existe
    lignes_modifiees = [ligne for ligne in lignes if ligne.strip() != ligne_a_supprimer.strip()]

    # Réécrire le contenu mis à jour dans le fichier
    with open(nom_fichier, 'w') as f:
        f.writelines(lignes_modifiees)

        
import ast

def string_to_dico(chaine):
    try:
        return ast.literal_eval(chaine.strip())
    except (SyntaxError, ValueError):
        print("Error converting string to dictionary.")
        return None



def reference_achanger():
        ref=input(("enter le reference  cible :"))
        return ref

def reference_a_afficher():
    ref=input("entrer la reference d'offre que vous voullez l'afficher:")
    return ref

def nouveau_date():#j'ai utilise cette fonction comme input de nouveau date 
        print("\n>>enter le nouveau date<<\n")
        jour=input(" le jour : ")
        mois=input(" le  mois : ")
        anne=input(" le  anne : ")
        return f"{jour}/{mois}/{anne}"

def nouveau_prix_d_offre():
    while True:
        try:
            prix_input=float(input("le nouveau prix en :"))
            nouveau_prix=round(prix_input,2)
            return nouveau_prix
        except ValueError:
                print("le prix doit etre de type float!!,vueillez  le saisir de nouveau: ")
   
    
def recherche_seule(contenu,ref):
    chaine=[]
    for line in contenu:
        dico=string_to_dico(line)
        if dico['reference']==ref:
            chaine.append(line)
    if chaine:
        print("la reference existe ")
        return chaine
    else:
        print("lareference n'existe pas")
        return 0
        
def list_to_string(l):
    separator=","
    my_string=separator.join(l)
    return my_string
    



def recherche_et_supprimer_par_ref(l, ref, nom_fichier):#j'ai remplacai l'utilisation de cette fonction apres l'amelioration de mon programe avec deux fonctions (recherche_seul) et(sauvegarde)
    chaine = []

    for line in l:
        dico=string_to_dico(line)
        if dico['reference']==ref:
            chaine.append(line)
    if chaine:
        for line in chaine:
            supprimer_ligne(nom_fichier, line)
        return chaine
    else:
        print("Le reference n'existe pas")
        return 0
 
def supprimer_tout_et_recrire(fichier,contenu):
    with open (fichier,"w") as f:
        for line in contenu:
            f.write(line)

def saisie_conditionel(Liste,sujet):# j'ai ne utilise pas cette  fonction dans mon programe
    while True :
        A=input(sujet)
        if A in Liste:
            return A
        else :
            print('Valeur Incorrect \n')

def nombre_de_lignes(l):
    n=len(l)
    return n

def nombred_lig(fichier):
    contenu=contenu_fichier(fichier)
    nbr=nombre_de_lignes(contenu)
    return nbr


def menu_type():
    
    while True:
        print(">> preciser le type d'offre <<")
        print("1: aller simple")
        print("2: aller/retour")
        print("3: hebergement")
        print("4: Formule complete")
        print("0:pour quitter")
        c=input("choix:")
        if c=="1":
            type_o='aller simple'
            return type_o
        elif c=="2":
            type_o='Transpor aller/retour'
            return type_o
        elif c=="3":
            type_o='hebergement'
            return type_o
        elif c=="4":
            type_o="Formule complete"
            return type_o
        elif c=="0":
            break
        else:
             print("choix invalable !!")

def type_a_rechercher():#menu d'autre facon 
    while True :
        try:
            c=(input(" >>preciser le type d'offre<< \n tappez:\n1:aller simple\n2:Transpor aller/retour\n3:hebergement\n4:Formele complete \nchoix: "))
            if c==1:
                return "aller simple"
            elif c==2:
                return "Transpor aller/retour"
            elif c==3:
                return "hebergement"
            elif c==4:
                return "Formule complete"
            else :
                print("choix invalide enter soit 1,2,3 ou 4")
        except ValueError:
            print("veuillez entrer un entier soit 1,2,3 ou 4")
        else:
            break

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#foctions de mis ajour :
#>>>>>>>>>>>>>>>>>>>>>>.mis ajour <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
############# mis a jour de la date ################################################# :6
def mise_ajour_date_depart(fichier):
    ref = reference_achanger()
    contenu = contenu_fichier(fichier)
    a = recherche_seule(contenu, ref)
    
    if a == 0:
        pass
    else:
        for  i,line in enumerate(contenu):
            if 'reference' in line and 'la date de depart' in line:
                dico = string_to_dico(line)
                if dico['reference']==ref  :
                    nouveau_date_str = nouveau_date()
                    dico['la date de depart'] = nouveau_date_str
                    contenu[i]=dico_to_str(dico)+'\n'
                    print("Mise à jour de la date d'offre effectuée avec succès!")
                    break
        
        supprimer_tout_et_recrire(fichier, contenu)  


def mise_ajour_date_darrivee(fichier):
    ref = reference_achanger()
    contenu = contenu_fichier(fichier)
    a = recherche_seule(contenu, ref)
    
    if a == 0:
        pass
    else:
        for  i,line in enumerate(contenu):
            if 'reference' in line and  "la date d'arriver" in line:
                dico = string_to_dico(line)
                
                if dico['reference']==ref  :
                    nouveau_date_str = nouveau_date()
                    dico["la date d'arriver"] = nouveau_date_str
                    contenu[i]=dico_to_str(dico)+'\n'
                    print(f"Mise à jour de la date d'offre de reference {ref} effectuée avec succès!")
                    break
            else:
                print(f"le type d'offre de reference {ref} n'admis pas un date d'arrive !!")
                break
        supprimer_tout_et_recrire(fichier, contenu)  



def menu_mis_date(fichier):
    while True:
        print("tappez :")
        print("1:mis a jour date depart")
        print("2:mis a jour date d'arriver ")
        print("0:pour quiter cette etape")
        c=input("choix :")
        if c=="1":
            mise_ajour_date_depart(fichier)
        elif c=="2":
            mise_ajour_date_darrivee(fichier)
        elif c=="0":
            break
            
        else:
            print("choix invalable!! ressayer de nouveau")
            continue

###mis ajour de prix ############################################################### :5

def mise_ajour_prix(fichier):
    ref = reference_achanger()
    contenu = contenu_fichier(fichier)
    a = recherche_seule(contenu, ref)
    
    if a == 0:
        pass
    else:
        for  i,line in enumerate(contenu):
            if 'reference' in line and 'le prix ' in line and "type d'offre" in line:
                dico = string_to_dico(line)
                if dico['reference']==ref  :
                    if dico["type d'offre"]=='hebergement':
                        print("cette offre est de type hebergement pour mettre a jour  le prix vous devez mettre ajour le prix par nuit :")
                        print(">>prix par nuit:")
                        nouveau_prix = nouveau_prix_d_offre()
                        dico['le prix par nuit']=nouveau_prix
                        n=dico['nombre de nuit']
                        dico['le prix ']= nouveau_prix*n
                        contenu[i]=dico_to_str(dico)+'\n'
                        print(f"Mise à jour de de prix d'offre de reference {ref} a ete  effectuée avec succès!")
                        break
                    elif dico["type d'offre"]=='Formule complete':
                        print("cette offre est de type Formule complete  pour mettre a jour  le prix vous devez mettre ajour le prix par nuit et le prix de transport aller/retour :")
                        print(">>prix par nuit:")
                        n_p1=nouveau_prix_d_offre()
                        dico['le prix par nuit ']=n_p1
                        print(">>prix de transport aller/retour ")
                        n_p2=nouveau_prix_d_offre()
                        dico['prix aller/retour ']=n_p2
                        n_p3=dico['nombre de nuit']
                        dico['le prix ']=n_p2 + (n_p1 * n_p3)
                        contenu[i]=dico_to_str(dico)+'\n'
                        print(f"Mise à jour de de prix d'offre de reference {ref} a ete  effectuée avec succès!")
                        break



                    else:
                        nouveau_prix = nouveau_prix_d_offre()
                        dico['le prix '] = nouveau_prix
                        contenu[i]=dico_to_str(dico)+'\n'
                        print(f"Mise à jour de de prix d'offre de reference {ref} a ete  effectuée avec succès!")
                        break
        
        supprimer_tout_et_recrire(fichier, contenu)  


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
###################bloquage ou debloquage d'un offre############################### :7
#bloquer un offre #################################################
            
def bloquer_offre(fichier):
    ref = reference_achanger()
    contenu = contenu_fichier(fichier)
    a = recherche_seule(contenu, ref)
    
    if a == 0:
        pass
    else:
        for  i,line in enumerate(contenu):
            if 'reference' in line and "statut d'offre" in line:
                dico = string_to_dico(line)
                if dico['reference']==ref  :
                    if dico["statut d'offre"] == 'debloquer':
                        dico["statut d'offre"] = 'bloquer'
                        contenu[i]=dico_to_str(dico)+'\n'
                        print("Cette offre est bloquée avec succès.")
                        break  # Pas besoin de continuer la boucle une fois que l'offre est bloquée
                    else:
                        print("Cette offre est déjà bloquée,veullez vous le debloquer : ")
                        c=input("tappez 1 pour le debloquer / n' importe quoi pour quitter: ")
                        if c=="1":
                            dico["statut d'offre"] = 'debloquer'
                            contenu[i]=dico_to_str(dico)+'\n'
                            print("Cette offre est debloquée avec succès.")
                        else:
                            break

        
        supprimer_tout_et_recrire(fichier, contenu)  


def debloquer_offre(fichier):
    ref = reference_achanger()
    contenu = contenu_fichier(fichier)
    a = recherche_seule(contenu, ref)
    
    if a == 0:
        pass
    else:
        for  i,line in enumerate(contenu):
            if 'reference' in line and "statut d'offre" in line:
                dico = string_to_dico(line)
                if dico['reference']==ref  :
                    if dico["statut d'offre"] == 'bloquer':
                        dico["statut d'offre"] = 'debloquer'
                        contenu[i]=dico_to_str(dico)+'\n'
                        print("Cette offre est debloquée avec succès.")
                        break  # Pas besoin de continuer la boucle une fois que l'offre est bloquée
                    else:
                        print("Cette offre est déjà debloquée,veullez vous le bloquer : ")
                        c=input("tappez 1 pour le bloquer / n' importe quoi pour quitter: ")
                        if c=="1":
                            dico["statut d'offre"] = 'bloquer'
                            contenu[i]=dico_to_str(dico)+'\n'
                            print("Cette offre est bloquée avec succès.")
                        else:
                            break

        
        supprimer_tout_et_recrire(fichier, contenu)



def bloquer_ou_debloquer(fichier):
    while True :
        print(">>tappez :\n1:pour bloquer un offre\n2:pour debloquer un offre \n0:pour quitter ")
        c=input("votre choix:")
        if c=="1":
            bloquer_offre(fichier)
        elif c=="2":
            debloquer_offre(fichier)
        elif c=="0":
            break
        else:
            print("choix invalable!!")
            continue

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#affichage d'offre :8 

def affichage(nom_fichier):
    ref=reference_a_afficher()
    contenu=contenu_fichier(nom_fichier)
    chaine=recherche_seule(contenu,ref)
    if chaine==0:
        pass
    else:
        string=list_to_string(chaine)
        string_pro=string.replace("{", "").replace("}", "").replace(",","\t").replace("'", "").strip()
        print(f"\n>>les information de l'offre de reference <<{ref}>>  <<<:\n{string_pro}")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#changer statut de reservation##############################     
def chager_statut_reservation(fichier):
    ref = reference_achanger()
    contenu = contenu_fichier(fichier)
    a = recherche_seule(contenu, ref)
    if a == 0:
        pass
    else:
        etat=saisie_conditionel_etat()
        for  i,line in enumerate(contenu):
            if 'reference' in line and "l'etat de reservation" in line:
                dico = string_to_dico(line)
                if dico['reference'] ==ref:
                    if dico["l'etat de reservation"] ==etat:
                        print(f"l'etat de reservation de reference << {ref} >> est deja {etat}")
                    else:
                        dico["l'etat de reservation"] =etat
                        contenu[i]=dico_to_str(dico)+'\n'
                        supprimer_tout_et_recrire(fichier, contenu)
                        print("l'etat a ete modifier avec succes!!.") 
                        
                         
        

def saisie_conditionel_etat():
    while True:
        print(">>change  d'etat de reservation<<")  
        print("tappez :")     
        print("1:pour la mettre  'encours' ")
        print("2:pour la mettre  'confirmee' ")
        print("3:pour la mettre  'annulee' ")
        print("0:pour quitter ")
        c=input("votre choix:")
        if c=="1":
            etat='en cours'
            return etat
                
        elif c=="2":
            etat='confirmee' 
            return etat 
        elif c=="3":
            etat='annulee'
            return etat
        elif c=="0":
            break
        else:
            print("choix invalable!!")
            continue

##___________________________________________________________________________________________
# fontions permetre de faire les statistics d'offre :
def filtretype_period(contenu):
    a_s=0
    a_r=0
    heb=0
    f_c=0
    for line in contenu:
        dico = string_to_dico(line)
        if "type d'offre" in dico:
            if dico["type d'offre"] == 'aller simple':
                a_s += 1
            elif dico["type d'offre"] == 'Transpor aller/retour':
                a_r += 1
            elif dico["type d'offre"] == 'hebergement':
                heb += 1
            else:
                f_c += 1
    return f">>le nombre d'offre par type et par cette peride<<\naller simple:{a_s}\tTranspor aller/retour:{a_r}\thebergement:{heb}\tFormule complete:{f_c}"  


def periode_filtre(fichier):
    l_filt=[]
    p1=Date("","","")
    p2=Date("","","")
    print("enter la premiere date:")
    p1.saisir_date()
    print("enter la deuzieme date:")
    p2.saisir_date()
    contenu=contenu_fichier(fichier)
    for line in contenu:
        dico=string_to_dico(line)
        date=dico['la date de depart']
        datelist=date.split("/")
        d=Date(int(datelist[0]),int(datelist[1]),int(datelist[2]))
        if p1<=d<=p2:
            l_filt.append(line)
    if l_filt:
        return l_filt 
    else:
         return 0

def comtage_par_type(fichier):
    contenu=contenu_fichier(fichier)
    a_s=0
    a_r=0
    heb=0
    f_c=0
    l=[]
    for line in contenu:
        dico = string_to_dico(line)
        if "type d'offre" in dico:
            if dico["type d'offre"] == 'aller simple':
                a_s += 1
            elif dico["type d'offre"] == 'Transpor aller/retour':
                a_r += 1
            elif dico["type d'offre"] == 'hebergement':
                heb += 1
            else:
                f_c += 1
    l=[a_s,a_r,heb,f_c]
    return l 
          
def chois_de_comtage_par_type(list):
    
    while True:
        try:
            print("tappez:")
            print("1:afficher le  nombre d'offre de type aller simple: ")
            print("2:afficher  le nombre d'offre de type aller/retour: ")
            print("3:afficher le nombre d'offre de type hebergement: ")
            print("4:afficher le nombre d'offre de type Formule complete: ")
            print("0:pour quitter cette etape")
            choix=int(input(" choix:"))
            if choix==1:
                print(f"le  nombre d'offre de type aller simple :{list[0]}")
            elif choix==2:
                print(f"le  nombre d'offre de type aller/retour:{list[1]}")

            elif choix==3:
                print(f"le  nombre d'offre de type hebergement:{list[2]}")
            elif choix==4:
                print(f"le  nombre d'offre de type Formule complete :{list[3]}")
            elif choix==0:
                break
            else:
                print("le choix doit etre soit 1,2,3 ,4 ou 0 pour quiter")
        except ValueError:
            print("Ereur de format de saisie !! le choix ne peut pas etre une lettre ")   
        else:
            continue
#_________________________________________________________________________________________
## fontions permetre de faire les statistics sur les reservation :
#contage de reservation par etat :
def comtage_par_etat(fichier):
    contenu=contenu_fichier(fichier)
    conf=0
    anu=0
    enc=0
    
    c_etat=[]
    for line in contenu:
        dico = string_to_dico(line)
        if "l'etat de reservation" in dico:
            if dico["l'etat de reservation"] == 'confirmee':
                conf += 1
            elif dico["l'etat de reservation"] == 'annulee':
                anu += 1
           
            else:
                enc+=1
    

    c_etat=[conf,anu,enc]
                
    return c_etat

def chois_de_comtage_par_etat(list,fichier):
    contenu=contenu_fichier(fichier)
    while True:
        try:
            print("tappez:")
            print("1:afficher le  nombre de reservation global: ")
            print("2:afficher  le nombre de reservation confirmee: ")
            print("3:afficher le nombre de reservation annuler: ")
            print("4:afficher le nombre de reservation en cours: ")
            print("0:pour quitter cette etape")
            choix=int(input(" choix:"))
            if choix==1:
                print(f"le  nombre global des reservation :{len(contenu)}")
            elif choix==2:
                print(f"le  nombre de reservation confirmee:{list[0]}")

            elif choix==3:
                print(f"le  nombre de reservation annuler:{list[1]}")
            elif choix==4:
                print(f"le  nombre de reservation en cours :{list[2]}")
            elif choix==0:
                break
            else:
                print("le choix doit etre soit 1,2,3 ,4 ou 0 pour quiter")
        except ValueError:
            print("Ereur de format de saisie !! le choix ne peut pas etre une lettre ")   
        else:
            continue





#menu de reservation confireme par ....###################################################################################
def nombre_de_reservation_confirme_par(fichier):
    while True:
        try:
            print("tappez:")
            print("1:Nbre de réservations confirmé par période ")
            print("2:Nbre de réservations confirmé par destination ")
            print("3:Nbre de réservations confirmé par client ")
            print("4:Nbre de réservations confirmé par nationalite: ")
            print("0:pour quitter cette etape")
            choix=int(input(" choix:"))
            
            if choix==1:
                i=0
                l=periode_filtre(fichier)
                if l==0:
                    print("aucune reservation declaree dans cette period !!")
                    pass
                else:
                    for line in l:
                        if "l'etat de reservation" in line:
                            dico=string_to_dico(line)
                            if dico["l'etat de reservation"]=='confirmee':
                                i+=1
                                

                    print(f"le  nombre de réservations confirmé par cette periode :{i} ")   
                    
            elif choix==2:
                conter_reser_par_destination_resultat()
                
            elif choix==3:
                conter_reser_par_nom_resultat(fichier)
                
            elif choix==4:
                conter_reser_par_nationalite_resultat(fichier)
                
            
            elif choix==0:
                break
            else:
                print("le choix doit etre soit 1,2,3 ,4 ou 0 pour quiter")
        except ValueError:
            print("Ereur de format de saisie !! le choix ne peut pas etre une lettre ")   
        else:
            continue


#contage  reservation par destination ########################################
def extraire_destination_offre():
    contenu = contenu_fichier("offre.txt")
    ref_destinas = []
    for line in contenu:
        if "Ville d'arriver" in line and 'reference'in line  :
            dico = string_to_dico(line)
            ref_destina_key = (dico['reference'])
            distina=(dico["Ville d'arriver"])
            found = False
            for ref_destina in ref_destinas:
                if ref_destina['reference'] == ref_destina_key:
                        ref_destinas["Ville d'arriver"] =distina
                        found = True
                        break

            if not found:
                ref_destinas.append({'reference': ref_destina_key, "Ville d'arriver": distina})  
    return ref_destinas





def contage_reservations_per_reference():
    contenu = contenu_fichier("reservation.txt")
    reservations = []

    for line in contenu:
        if "reference d'offre" in line and "l'etat de reservation" in line:
            dico = string_to_dico(line)
            if dico["l'etat de reservation"]=='confirmee':
                ref_key= (dico["reference d'offre"])
                
                found = False
                for reservation in reservations:
                    if reservation["reference d'offre"] == ref_key:
                        reservation['count'] += 1
                        found = True
                        break

                if not found:
                    reservations.append({"reference d'offre": ref_key, 'count': 1})

    return reservations

def contage_reservations_per_destination_list():
    a = extraire_destination_offre()
    b = contage_reservations_per_reference()
    list_offre_reser = []
    for dico_ref in a:
        for dico_dis in b:
            if dico_ref['reference'] == dico_dis["reference d'offre"]:
                list_offre_reser.append({"distination": dico_ref["Ville d'arriver"], 'count': dico_dis['count']})

    return list_offre_reser

def contage_reservations_per_distination():
    list=contage_reservations_per_destination_list()
    destination = []

    for dico in list:
            
            
            reserv_key = (dico['distination'])
            count=dico['count']
            found = False
            for reservation in destination:
                if reservation['distination'] == reserv_key:
                    reservation['count'] +=count 
                    found = True
                    break

            if not found:
                    destination.append({'distination':reserv_key , 'count': count})

    return destination

def conter_reser_par_destination_resultat():
    result = contage_reservations_per_distination()
    c=input("preciser la distination :")
    found=False
    for entry in result:
        if entry['distination']==c:
                print(f"la distination {entry['distination']} a {entry['count']} reservations confirme.")
                found=True
                break
    if found==True:
        pass
    else:
        print(f"il n'ya aucune reservation confirme de distination {c}" )

#le nombre de reservation par client ##############################################################
def contage_reservations_per_client(fichier):
    contenu = contenu_fichier(fichier)
    reservations = []

    for line in contenu:
        if "le nom de client" in line and "le prenom de client" in line and "l'etat de reservation" in line:
            dico = string_to_dico(line)
            if dico["l'etat de reservation"]=='confirmee':
                client_key = dico['le nom de client']+" "+ dico['le prenom de client ']
                
                found = False
                for reservation in reservations:
                    if reservation['client'] == client_key:
                        reservation['count'] += 1
                        found = True
                        break

                if not found:
                    reservations.append({'client': client_key, 'count': 1})

    return reservations
def conter_reser_par_nom_resultat(fichier):
    result = contage_reservations_per_client(fichier)
    
    nom=str(input("preciser le nom  de client:"))
    prenom=str(input("preciser le prenom  de client:"))
    p=nom+" "+prenom
    
    found=False
    for entry in result:
        if entry['client']==p:
            print(f"Client {entry['client']} a {entry['count']} reservations confirme.")
            found=True
            break
    if found==True:
        pass
    else:
        print(f"il n'ya aucune reservation confirme  sous le nom de client {p}  ")

#nombre de reservation par nationalite##################################################################
def contage_reservations_per_nationalite(fichier):
    contenu = contenu_fichier(fichier)
    reservations = []

    for line in contenu:
        if "le pays d'origine" in line  and "l'etat de reservation" in line:
            dico = string_to_dico(line)
            if dico["l'etat de reservation"]=='confirmee':
                nation_key = (dico["le pays d'origine"])
                
                found = False
                for reservation in reservations:
                    if reservation["le pays d'origine"] == nation_key:
                        reservation['count'] += 1
                        found = True
                        break

                if not found:
                    reservations.append({"le pays d'origine": nation_key, 'count': 1})

    return reservations

def conter_reser_par_nationalite_resultat(fichier):
    result = contage_reservations_per_nationalite(fichier)
    c=input("preciser la nationalite :")
    found=False
    for entry in result:
        if entry["le pays d'origine"]==c:
            print(f"la nationalite {entry["le pays d'origine"]} a {entry['count']} reservations confirme.")
            found=True
            break
    if found==True:
        pass
    else:
        print(f"il n'ya aucune reservation confirme de nationalite {c}" )


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## fontions permetre de faire les statistics sur le chiffre d'affaire : 
#chiffre d'affaire global_________________________________________________
def chiffre_d_affaire_global(fichier):
    contenu=contenu_fichier(fichier)
    chifr_aff=0
    for line in contenu:
        if 'le prix' in line and "l'etat de reservation" in line:
            dico=string_to_dico(line)
            if dico["l'etat de reservation"]=='confirmee':
                chifr_aff=chifr_aff+float(dico['le prix'])
            
    return f"le chiffre d'affaire global :{chifr_aff } DH"
#___________________________________________________________________________


#menu de chiffre d'affaire par......##########################################################################################
def chiffre_affaire_par(fichier):
    
    while True:
        try:
            print("tappez:")
            print("1:calculer le  chiffre d'affaire par période: ")
            print("2:calculer  le chiffre d'affaire par type: ")
            print("3:calculer le chiffre d'affaire par destination: ")
            print("4:calculer le chiffre d'affaire par nationalite: ")
            print("5:calculer le chiffre d'affaire par période ,par type,par destination et par nationalite:")
            print("0:pour quitter cette etape")
            choix=int(input(" choix:"))
            chifr_aff=0
            if choix==1:
                l=periode_filtre(fichier)
                if l==0:
                    
                    pass 
                else:
                    for line in l:
                        if 'le prix' in line and "l'etat de reservation" in line:
                            dico=string_to_dico(line)
                            if dico["l'etat de reservation"]=='confirmee':
                                chifr_aff=chifr_aff+float(dico['le prix'])
                                

                    print(f"le chiffre d'affaire par cette période est :{chifr_aff } DH")   
                    
            elif choix==2:
                l=comtage_par_type_chiffre_d_affaire(fichier)
                
                chois_de_calculer_chiffre_d_affaire_par_type(l)
            elif choix==3:
                chiffre_d_affaire_par_destination_resultat()
            elif choix==4:
                chif_par_nationalite_resultat(fichier)
            
            elif choix==5:
                chiffre_d_affaire_par_tout_resultat()
            elif choix==0:
                break
            else:
                print("le choix doit etre soit 1,2,3 ,4,5 ou 0 pour quiter")
        except ValueError:
            print("Ereur de format de saisie !! le choix ne peut pas etre une lettre ")   
        else:
            continue


##chiffre d'affaire par type   #######################################################################



def comtage_par_type_chiffre_d_affaire(fichier):
    contenu=contenu_fichier(fichier)
    a_s=0
    a_r=0
    heb=0
    f_c=0
    
    for line in contenu:
        
        if "Type d'offre" in line and 'le prix' in line and "l'etat de reservation" in line :
            
            dico = string_to_dico(line)
            if dico["l'etat de reservation"]=='confirmee':
                
                if dico["Type d'offre"] == 'aller simple':
                    
                    
                    a_s+=float(dico['le prix'])
                    
                elif dico["Type d'offre"] == 'Transpor aller/retour':
                    a_r+=float(dico['le prix'])
                elif dico["Type d'offre"] == 'hebergement':
                    heb+=float(dico['le prix'])
                else:
                    f_c+=float(dico['le prix'])
    
    return [a_s,a_r,heb,f_c]





def chois_de_calculer_chiffre_d_affaire_par_type(list):
    
    while True:
        try:
            print("tappez:")
            print("1:calculer le chiffre d'affaire d'offre de type aller simple: ")
            print("2:calculer le chiffre d'affaire d'offre de type aller/retour: ")
            print("3:calculer le chiffre d'affaire d'offre de type hebergement: ")
            print("4:calculer le chiffre d'affaire d'offre de type Formule complete: ")
            print("0:pour quitter cette etape")
            choix=int(input(" choix:"))
            if choix==1:
                print(f"le chiffre d'affaire d'offre de type aller simple :{list[0]} DH")
            elif choix==2:
                print(f"le chiffre d'affaire d'offre de type aller/retour:{list[1]} DH")

            elif choix==3:
                print(f"le chiffre d'affaire d'offre de type hebergement:{list[2]} DH")
            elif choix==4:
                print(f"le chiffre d'affaire d'offre de type Formule complete :{list[3]} DH")
            elif choix==0:
                break
            else:
                print("le choix doit etre soit 1,2,3 ,4 ou 0 pour quiter")
        except ValueError:
            print("Ereur de format de saisie !! le choix ne peut pas etre une lettre ")   
        else:
            continue 

#######################################################################################
#chiffre d'affaire par destination 
        
def chiffre_d_affire_reservations_per_reference():
    contenu = contenu_fichier("reservation.txt")
    reservations = []

    for line in contenu:
        if "reference d'offre" in line  and "l'etat de reservation" in line and 'le prix' in line:
            dico = string_to_dico(line)
            if dico["l'etat de reservation"]=='confirmee':
                ref_key= (dico["reference d'offre"])
                prix=dico['le prix']
                found = False
                for reservation in reservations:
                    if reservation["reference d'offre"] == ref_key:
                        reservation['le prix'] +=prix
                        found = True
                        break

                if not found:
                    reservations.append({"reference d'offre": ref_key, 'le prix': prix})

    return reservations 



def chiffre_d_affaire_reservations_per_destination_list():
    a = extraire_destination_offre()
    b = chiffre_d_affire_reservations_per_reference()
    list_offre_reser = []
    for dico_ref in a:
        for dico_dis in b:
            if dico_ref['reference'] == dico_dis["reference d'offre"]:
                list_offre_reser.append({"distination": dico_ref["Ville d'arriver"], 'le prix': dico_dis['le prix']})
    
    return list_offre_reser


def chiffre_d_affaire_reservations_per_distination(list):
    
    destination = []

    for dico in list:
            
            
            reserv_key = (dico['distination'])
            prix=dico['le prix']
            found = False
            for reservation in destination:
                if reservation['distination'] == reserv_key:
                    reservation['le prix'] +=prix 
                    found = True
                    break

            if not found:
                    destination.append({'distination':reserv_key , 'le prix': prix})
    print(destination)
    return destination


def chiffre_d_affaire_par_destination_resultat():
    list1=chiffre_d_affaire_reservations_per_destination_list()
    
    result = chiffre_d_affaire_reservations_per_distination(list1)
    
    c=input("preciser la distination :")
    found=False
    for entry in result:
        if entry['distination']==c:
            print(f"le chiffre d'affaire de destination   {entry['distination']} est : {entry['le prix']} DH.")
            found=True
            break
    if found==True:
        pass
    else:
        print(f"il n'ya aucune reservation confirme de distination {c}" )  

#chiffre d'affiare par nationalite##################################################

def chiffre_d_affaire_per_nationalite(fichier):
    contenu = contenu_fichier(fichier)
    reservations = []

    for line in contenu:
        if "le pays d'origine" in line  and "l'etat de reservation" in line and 'le prix' in line:
            dico = string_to_dico(line)
            if dico["l'etat de reservation"]=='confirmee':
                nation_key = (dico["le pays d'origine"])
                prix=dico['le prix']
                
                found = False
                for reservation in reservations:
                    if reservation["le pays d'origine"] == nation_key:
                        reservation['chiffre d affaire'] +=prix
                        found = True
                        break

                if not found:
                    reservations.append({"le pays d'origine": nation_key, 'chiffre d affaire': prix})

    return reservations  
 
def chif_par_nationalite_resultat(fichier):
    result = chiffre_d_affaire_per_nationalite(fichier)
    c=input("preciser la nationalite :")
    found=False
    for entry in result:
        if entry["le pays d'origine"]==c:
            print(f"le chiffre d affaire de nationalite: {entry["le pays d'origine"]} est {entry['chiffre d affaire']} DH .")
            found=True
            break
    if found==True:
        pass
    else:
        print(f"il n'ya aucune reservation confirme de nationalite : {c}" )     

#chiffre daffaire par tout #######################################################################################
def type_et_period(list1):
    
    type_o = menu_type()
    l = []

    for line in list1:
        if "Type d'offre" in line and "le pays d'origine" in line and "reference d'offre" in line and 'le prix' in line and 'reference':
            dico = string_to_dico(line)

            if dico["Type d'offre"] == type_o and dico["l'etat de reservation"] == 'confirmee':
                ref=dico['reference']
                ref_o = dico["reference d'offre"]
                origin = dico["le pays d'origine"]
                prix = dico['le prix']

                found = False

                for r in l:
                    if  r['reference']==ref:
                        r["reference d'offre"] == ref_o
                        r["le pays d'origine"] = origin
                        r['le prix'] = prix
                        found = True
                        break

                if not found:
                    l.append({'reference':ref,"reference d'offre": ref_o, "le pays d'origine": origin, 'le prix': prix})

    
    
    if l:
        return l
    else:
        return 0
def preciser_pays_do(list2):
    c = input("preciser la nationalite (pays d'origine):")
    l = []

    for dico in list2:
        if "reference d'offre" in dico and "le pays d'origine" in dico and 'le prix' in dico:
            if dico["le pays d'origine"] == c:
                prix = dico['le prix']
                ref = dico["reference d'offre"]
                found = False

                for r in l:
                    if r["reference d'offre"] == ref:
                        r['le prix'] += prix
                        found = True
                        break

                if not found:
                    l.append({"reference d'offre": ref, 'le prix': prix})

    

    if l:
        return l
    else:
        return 0
                
        
def chiffre_par_list(a,b):
    
    list_offre_reser = []
    for dico_ref in a:
        for dico_dis in b:
            if dico_ref['reference'] == dico_dis["reference d'offre"]:
                list_offre_reser.append({"distination": dico_ref["Ville d'arriver"], 'le prix': dico_dis['le prix']})
    
    return list_offre_reser


def chiffre_d_affaire_par_tout_resultat():
    list1=periode_filtre("reservation.txt")
    if list1==0:
         print("il n'ya aucune reservation confirme declaree dans cette priod")
         pass
    else:
        list2=type_et_period(list1)
        if list2==0:
             print("il n'ya aucune reservation confirme declarer   de ce type d'offre dans cette period ")
             pass
        else:
            list3=preciser_pays_do(list2)
            if list3==0:
                 print("il n'ya aucune reservation confirme declarer  de cette nationalite  de ce type d'offre dans cette period ")
                 pass
            else:
                a=extraire_destination_offre()
                list4=chiffre_par_list(a,list3)
                
                if list4:
                    result = chiffre_d_affaire_reservations_per_distination(list4)
                    c=input("preciser la distination:")
                    found=False
                    for entry in result:
                        if entry['distination']==c:
                            print(f"le chiffre d'affaire de destination   {entry['distination']} est : {entry['le prix']} DH.")
                            found=True
                            break
                    if found==True:
                        pass
                    else:
                        print(f"il n'ya aucune reservation confirme dans cette period de ce type de cette nationalite de distination {c}")
                else:
                    pass 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#fonctions auxiliaires: #######################################################33       
def dico_to_str(d):
        chaine=str(d)
        return chaine


def sauvegarde(nomfichier,contenu):
        with open (nomfichier,"a+") as f:
            f.write(contenu+"\n")
            


def contenu_fichier(fichier):
    with open (fichier,"r") as f:
        l=f.readlines()
        return l
    

def supprimer_ligne(nom_fichier, ligne_a_supprimer):#je n'ai pas utilise cette fonction dans mon programe ,mais je l'ai garde pour d'autre programe pour le future 
    # Lire le contenu du fichier
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()

    # Supprimer la ligne cible si elle existe
    lignes_modifiees = [ligne for ligne in lignes if ligne.strip() != ligne_a_supprimer.strip()]

    # Réécrire le contenu mis à jour dans le fichier
    with open(nom_fichier, 'w') as f:
        f.writelines(lignes_modifiees)

        
import ast

def string_to_dico(chaine):
    try:
        return ast.literal_eval(chaine.strip())
    except (SyntaxError, ValueError):
        print("Error converting string to dictionary.")
        return None



def reference_achanger():
        ref=input(("enter le reference  cible :"))
        return ref

def reference_a_afficher():
    ref=input("entrer la reference d'offre que vous voullez l'afficher:")
    return ref

def nouveau_date():#j'ai utilise cette fonction comme input de nouveau date 
        print("\n>>enter le nouveau date<<\n")
        jour=input(" le jour : ")
        mois=input(" le  mois : ")
        anne=input(" le  anne : ")
        return f"{jour}/{mois}/{anne}"

def nouveau_prix_d_offre():
    while True:
        try:
            prix_input=float(input("le nouveau prix en :"))
            nouveau_prix=round(prix_input,2)
            return nouveau_prix
        except ValueError:
                print("le prix doit etre de type float!!,vueillez  le saisir de nouveau: ")
   
    
def recherche_seule(contenu,ref):
    chaine=[]
    for line in contenu:
        dico=string_to_dico(line)
        if dico['reference']==ref:
            chaine.append(line)
    if chaine:
        print("la reference existe ")
        return chaine
    else:
        print("lareference n'existe pas")
        return 0
        
def list_to_string(l):
    separator=","
    my_string=separator.join(l)
    return my_string
    



def recherche_et_supprimer_par_ref(l, ref, nom_fichier):#j'ai remplacai l'utilisation de cette fonction apres l'amelioration de mon programe avec deux fonctions (recherche_seul) et(sauvegarde)
    chaine = []

    for line in l:
        dico=string_to_dico(line)
        if dico['reference']==ref:
            chaine.append(line)
    if chaine:
        for line in chaine:
            supprimer_ligne(nom_fichier, line)
        return chaine
    else:
        print("Le reference n'existe pas")
        return 0
 
def supprimer_tout_et_recrire(fichier,contenu):
    with open (fichier,"w") as f:
        for line in contenu:
            f.write(line)

def saisie_conditionel(Liste,sujet):# j'ai ne utilise pas cette  fonction dans mon programe
    while True :
        A=input(sujet)
        if A in Liste:
            return A
        else :
            print('Valeur Incorrect \n')

def nombre_de_lignes(l):
    n=len(l)
    return n

def nombred_lig(fichier):
    contenu=contenu_fichier(fichier)
    nbr=nombre_de_lignes(contenu)
    return nbr


def menu_type():
    
    while True:
        print(">> preciser le type d'offre <<")
        print("1: aller simple")
        print("2: aller/retour")
        print("3: hebergement")
        print("4: Formule complete")
        print("0:pour quitter")
        c=input("choix:")
        if c=="1":
            type_o='aller simple'
            return type_o
        elif c=="2":
            type_o='Transpor aller/retour'
            return type_o
        elif c=="3":
            type_o='hebergement'
            return type_o
        elif c=="4":
            type_o="Formule complete"
            return type_o
        elif c=="0":
            break
        else:
             print("choix invalable !!")

def type_a_rechercher():#menu d'autre facon 
    while True :
        try:
            c=(input(" >>preciser le type d'offre<< \n tappez:\n1:aller simple\n2:Transpor aller/retour\n3:hebergement\n4:Formele complete \nchoix: "))
            if c==1:
                return "aller simple"
            elif c==2:
                return "Transpor aller/retour"
            elif c==3:
                return "hebergement"
            elif c==4:
                return "Formule complete"
            else :
                print("choix invalide enter soit 1,2,3 ou 4")
        except ValueError:
            print("veuillez entrer un entier soit 1,2,3 ou 4")
        else:
            break
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#menu de programe principal#########################################################
def Menu():
    print(">>Menu de gestion <<\n")
    print("1:declare un offre d'aller simple")
    print("2:declarer offre aller retour")
    print("3:declarer offre d'bergement")
    print("4:declarer offre Formule complete")
    print("5:mettre ajour le prix d'un un offre")
    print("6:mettre ajour la date d'un offre")
    print("7:bloquer un offre")
    print("8:afficher une offre")
    print("9:nombre d'offre total  et par une periode precie")
    print("10:nombre d'offre par type et par une periode precie")
    print("11:declarer une reservation")
    print("12:Modifier le statut d'une reservation")
    print("13:Nbre de réservations annulé, confirmé ou Global")
    print("14:Nbre de réservations confirmé par période, par destination, par client ou par nationalité")
    print("15:Chiffre d'affaires global")
    print("16:Chiffre d'affaires global par période, par type, pardestination et/ou par nationalité")


    print("\n0:quiter le programe")
    choix=input("choix:")
    
    return choix 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#programe pricipal##########################################################################################################################
def principal(): 
    while True:
        try:
            choix=int(Menu())
            if choix==1:
                
                s=Transport_Aller_Simple("Ref_Offre", "Ville_de_depart", "Ville_d_arrivee"," date_offre", "prix_a_simple") 
                s.decla_offre_aller_simple()
                print(s.affichage_offre_aller_simple())
                d=s.aller_simple_dico()
                contenu=dico_to_str(d)
                sauvegarde("offre.txt", contenu)

            elif choix==2:
               ar=Transport_Aller_Retour("Ref_Offre"," Ville_de_depart"," Ville_d_arrivee", "date_offre"," prix_a_simple", "date_arriver")
               ar.decla_offre_aller_retour()
               print(ar.affichage_offre_aller_retour())
               d=ar.aller_retour_dico()
               contenu=dico_to_str(d)
               sauvegarde("offre.txt", contenu)
               
            elif choix==3:
                h=Hebergement("Ref_Offre", "date_offre", "ville_de_depart", "Ville_d_arrivee")
                h.declaration_hebergement()
                h.declaration_des_prpriete()
                print(h.affichage_offre_hebergement_info())
                print(h.affichage_hebergement_prpriete())
                
                d=h.dico_hebergement()
                contenu=dico_to_str(d)
                sauvegarde( "offre.txt",contenu)
            elif choix==4:
                f=Formule_complete('Ref_Offre', 'date_offre', 'Ville_de_depart',' Ville_d_arrivee', 'prix_a_simple', 'date_arriver',' type',' nombre_de_nuit', 'prix_par_nuit')
                f.declaration_formule_complete()
                print(f.affichage_offre_formule_complete())
                d=f.dico_Formule_complete()
                contenu=dico_to_str(d)
                sauvegarde( "offre.txt",contenu)
                
                
                
            elif choix==5:
                
                mise_ajour_prix("offre.txt")
            elif choix==6:
                menu_mis_date("offre.txt")
                
                
                
            elif choix==7:
                bloquer_ou_debloquer("offre.txt")
            elif choix==8:
                affichage("offre.txt")
                
            elif choix==9:
                n=nombred_lig("offre.txt")
                print(f"le nombre d'offres total est :{n}")
                c=input("voullez vous preciser une periode tappez (1) pour continue (autre que 1) pour sauter cette etape:")
                if c=="1":
                    l=periode_filtre("offre.txt")
                    print(f"le nombre d'offre total par ette period est :{len(l)}")
                    
                else:
                    pass
            elif choix==10:
                l=comtage_par_type("offre.txt")
                chois_de_comtage_par_type(l)
                c=input("voullez vous preciser une periode tappez (1) pour continue (autre que 1) pour sauter cette etape:")
                if c=="1":
                    l=periode_filtre("offre.txt")
                    if l==0:
                        print("aucun offre declaree dans cette period !!")
                        pass
                    else:
                        f_t_p=filtretype_period(l)
                        print(f_t_p)
                    
                else:
                    pass
                
            elif choix==11:
                res=Reservation()
                r=res.declaration_de_reservation()
                if r==0:
                    continue
                else: 
                    print(res.affichage_reservation_info())
                    d=res.dico_reservation()
                    contenu=dico_to_str(d)
                    sauvegarde( "reservation.txt",contenu)
            
            elif choix==12:
                chager_statut_reservation("reservation.txt")
                

            elif choix==13:
                l=comtage_par_etat("reservation.txt")
                chois_de_comtage_par_etat(l,"reservation.txt")

            elif choix==14:
                nombre_de_reservation_confirme_par("reservation.txt")
                
            elif choix==15:
                print(chiffre_d_affaire_global("reservation.txt"))

                
            elif choix==16:
                chiffre_affaire_par("reservation.txt")
            
            elif choix==0:  
                print("<<<< FIN DE PROGRAME >>>")
                break
            
            else:
                print("veuilez enter soit (0),(1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15) ou (16):")  
                continue
            
        except ValueError:
            print("le choix doit etre un entier!!!!")  
        
            
if __name__=="__main__":
    principal()         