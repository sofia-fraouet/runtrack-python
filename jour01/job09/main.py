Nom = "mermaid_tarte" 
Prix = 40
Stock = 100
print("le nom de l'article:" , Nom )
print("le prix de l'article:" , Prix ,"euros")
print("la quantité est de:" , Stock)
Stock_jour = int(input("Veuillez saisir la quantité souhaitée : "))
nouveaustock = Stock - Stock_jour
print("Nouvelle quantité :", nouveaustock)


nouveauprix = Prix * 1.1
print("Quantité :", nouveaustock)
print("Prix initial du produit :", Prix)
print("Prix après inflation (augmentation de 10%) :", nouveauprix)
