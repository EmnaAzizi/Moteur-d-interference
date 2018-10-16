def basefait(bff):
     return bff;
def maximum(conflit) :
                maxi=0
                k=0
                for i in range(len(conflit)) :
                    
                   
                  premisse =conflit[i] [ conflit[i] .index("si")+3 : conflit[i] .index("alors")-1]
                  pr = premisse.split(" et ")
                  if len(pr)>maxi:
                        maxi=len(pr)
                        k=i
                return k         
def Sauvv (Sauv,bff,Regles):
    if Sauv is 1 :
        with open('C:/Users/HP/Desktop/d/trace.txt','w') as f:
             f.write("\n \n la base des faits \n\n" + str(bff)  + "\n \n Regles executees"+ str(Regles) )
        open('C:/Users/HP/Desktop/d/bf'+str(BC)+str(BF)+'.txt', 'w').close()
        with open('C:/Users/HP/Desktop/d/bf'+str(BC)+str(BF)+'.txt', 'a') as file:                
                for i in range(len(bff)):
                     file.write(bff[i]+',')
    return 0 
                     
    

    

def conf(brr):
            conflit=[]
            for i in range(len(brr)) :    
                premisse = brr[i] [ brr[i] .index("si")+3 : brr[i] .index("alors")-1]
                pr = premisse.split(" et ")
                concl = brr[i] [ brr[i] .index("alors")+6 : brr[i] .index("*")]
                co = concl.split(" et ")
                v="True"
                k=0
   
                while v=="True" and k<len(pr):
                  if pr[k] in bff :
                      k=k+1     
                  else :
                        v="False"
                        break
                if v is "True":
                        conflit.append(brr[i]);
            return conflit
        
v="true"
while v=="true":
 bff=[]
 brr=[]
 s=0

 while s==0:
        print("Choisir votre base des connaissances \n tapez \n 1: pour la base de connaissance N°1 BC1 \n 2: pour la base de connaissance N°2 BC2 ");
        BC = input()
        print "Vous avez choisi la base de connaissance N°"+str(BC)+" ayant les regles et faits suivant : \n \n \n LES REGLES : \n\n"
        
        
        if BC is 1:

                with open("C:/Users/HP/Desktop/d/regle1.txt") as R:
                   rr1 = R.read()
                   brr= rr1.split("\n")
                   print rr1 
                print "\n\n LES FAITS : \n\n"    
                with open("C:/Users/HP/Desktop/d/bf11.txt") as bf11:
                 data1 = bf11.read()
                 print " BF1 : "+data1+"\n\n"
                with open("C:/Users/HP/Desktop/d/bf12.txt") as bf22:
                 data2 = bf22.read()
                 print " BF2 : "+data2+"\n\n"
                with open("C:/Users/HP/Desktop/d/bf13.txt") as bf33:
                 data3 = bf33.read()
                 print " BF3 : "+data3+"\n\n"
                with open("C:/Users/HP/Desktop/d/bf14.txt") as bf44:
                 data4 = bf44.read()
                 print " BF4 : "+data4+"\n\n" 
                print "Choisisser votre base des faits \n tapez \n 1: pour la base des faits N°1 BF1 \n 2: pour la base des faits N°2 BF2  \n 3: pour la base des faits N°2 BF3  \n 4: pour la base des faits N°2 BF4" 
                BF= input()
                if BF is 1 :
                  bf1 = data1.split(",")
                  bff=bf1
                  print "Vous avez choisi BF1 "
                  print bff
                  s=1
                elif BF is 2:
                 bf2= data2.split(",")
                 print "Vous avez choisi BF2 "
                 print bf2
                 bff=bf2
                 s=1
                elif BF is 3:
                 bf3= data3.split(",")
                 print "Vous avez choisi BF3 "
                 print bf3
                 bff=bf3
                 s=1
                elif BF is 4:
                 bf4= data4.split(",")
                 print "Vous avez choisi BF4 "
                 print bf4
                 bff=bf4
                 s=1   
                else :
                        print "Choix incorrect , Retapez votre choix "
        elif BC is 2:
                with open("C:/Users/HP/Desktop/d/regle2.txt") as R:
                   rr1 = R.read()
                   brr= rr1.split("\n")
                   
                   print rr1 
                print "\n\n LES FAITS : \n\n"    
                with open("C:/Users/HP/Desktop/d/bf21.txt") as bf11:
                 data1 = bf11.read()
                 print " BF1 : "+data1+"\n\n"
                with open("C:/Users/HP/Desktop/d/bf22.txt") as bf22:
                 data2 = bf22.read()
                 print " BF2 : "+data2+"\n\n"
                with open("C:/Users/HP/Desktop/d/bf23.txt") as bf33:
                 data3 = bf33.read()
                 print " BF3 : "+data3+"\n\n"
                with open("C:/Users/HP/Desktop/d/bf24.txt") as bf44:
                 data4 = bf44.read()
                 print " BF2 : "+data4+"\n\n" 
                print "Choisisser votre base des faits \n tapez \n 1: pour la base des faits N°1 BF1 \n 2: pour la base des faits N°2 BF2  \n 3: pour la base des faits N°2 BF3  \n 4: pour la base des faits N°2 BF4" 
                BF= input()
                if BF is 1 :
                  bf1 = data1.split(",")
                  bff=bf1
                  print "Vous avez choisi BF1 "
                  s=1
                elif BF is 2:
                 bf2= data2.split(",")
                 bff=bf2
                 print "Vous avez choisi BF2 "
                 print bff
                 s=1
                elif BF is 3:
                 bf3= data3.split(",")
                 bff=bf3
                 print "Vous avez choisi BF3 "
                 print bff
                 s=1
                elif BF is 4:
                 bf4= data2.split(",")
                 bff=bf4
                 print "Vous avez choisi BF4 "
                 print bff
                 s=1
        else :
                print "Choix incorrect , Retapez votre choix"

 print ("Choisir votre mode de raisonnement \n tapez \n 1: pour le mode de raisonnement avec conflit  \n 2: pour le mode de raisonnement sans conflit");
 RS= input()
 print (" Tapez \n 1 : Pour saturer la base de faits \n 2: Pour S'arrêter si un but est précisé");
 ST=input()
 if ST is 2 :
     print("Tapez le BUT")
     but = raw_input()
 if ST is 1:
        but="..."
     
 Regles=""

 if RS is 1 :
        if but in bff :
                "But Atteint"
        if len(conf(brr))==0 :
                print "aucune regle declenchable"
        while len(conf(brr))>0 :
          conflit=conf(brr)           
          print"Pour le chainage avant avec conflit \n tapez \n 1 : Sélection de la première règle \n 2:  Sélection de la règle ayant le plus de prémisses.";
          CH=input();
          if CH is 1 :
                print "vous avez choisi la 1 ere regle"
                print conflit [0]
                Regles=Regles+"\n"+conflit [0]
                concl = conflit[0] [conflit[0].index("alors")+6 : conflit[0] .index("*")]
                brr.remove(conflit[0])
                chaine="non"+" "+ concl;
                if ( chaine in bff) :
                    print ("ERROR : NOT CONCLUSION EXISTE DANS LA BASE DES FAITS")
                    break; break;
                else :
                        bff.append(concl)
                        if concl==but:
                          print "BUT atteint"
          if CH is 2 :
                k=maximum(conflit)
                concl = conflit[k] [conflit[k].index("alors")+6 : conflit[k] .index("*")]
                print "vous avez choisi la regle ayant le plus de premisses :"
                print conflit[k]
                Regles=Regles+"\n"+conflit [k]

                brr.remove(conflit[k])
                
                chaine="non"+" "+ concl;
                if ( chaine in bff) :
                            print ("ERROR : NOT CONCLUSION EXISTE DANS LA BASE DES FAITS")
                            break;
                else :
                        bff.append(concl)
                        if but==concl:
                                 print" BUT Atteint "
                                 


              
 elif RS is 2 :
       bfff=basefait(bff);
       
       
       
       if but in bff :
                "But Atteint"
               
       w=0
      
       while w==0 and len(brr)!=0 :
             
             i=0
             
             while  i <len(brr) :
               
                
                   
                premisse = brr[i] [ brr[i] .index("si")+3 : brr[i] .index("alors")-1]
                pr = premisse.split(" et ")
                concl = brr[i] [ brr[i] .index("alors")+6 : brr[i] .index("*")]
                co = concl.split(" et ")
                
                v="True"
                k=0
   
                while v=="True" and k<len(pr):
                  if pr[k] in bfff :
                      k=k+1
                  else :
                        v="False"
                        break
               
                   
                if v is "True":
                        Regles=Regles+"\n"+brr[i]
                        print brr[i]

                        brr.remove(brr[i])
                        
                        for j in range(len(co)):
                            chaine="non"+" "+ co[j];
                            if ( chaine in bfff) :
                                print ("ERROR : NOT CONCLUSION EXISTE DANS LA BASE DES FAITS")
                                break; break; break;
                            bfff.append(co[j])
                            if (co[j]==but) :
                                w=1
                                print " ***********************But atteint************************* "
                              
                                
                i=i+1
             
             
             if (bfff==bff):
                 if (but!="..."):
                     print " \n \n ****************But non atteint******************** ";
                     break
                 else   :
                     
                   print ("\n \n --------Saturation de la base des faits : pas de regles declenchables----------- ")
                   break
             bff=bfff   

                           

       
                                                        
                                  
 print "\n \n les regles exécutées sont : \n"
 print Regles
 print "\n"
 print "Votre nouvelle base des faits \n"
 print bff
 print "voulez vous sauvegarder la trace ? Tapez 1: OUI 2: NON"
 Sauv=input()
 Sauvv(Sauv,bff,Regles)        

    
        
