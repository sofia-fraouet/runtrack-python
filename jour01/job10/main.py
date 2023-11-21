montant_initial = 10000  
taux_rendement_annuel = 5  


gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Le gain annuel initial est de {gain_annuel} euros.")


montant_initial += 5000
taux_rendement_annuel += 2


nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Après augmentation du capital et du taux, le nouveau gain annuel est de {nouveau_gain_annuel} euros.")


retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1


montant_final = montant_initial + gain_annuel
gain_annuel = (taux_rendement_annuel / 100) * montant_final
print(f"Après retrait et diminution du taux, le montant final de l'investissement est de {montant_final} euros.")
print(f"Le nouveau gain annuel est de {gain_annuel} euros.") 