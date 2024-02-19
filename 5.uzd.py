#Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī. Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt"). Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas. Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu. 
def ierakstit_vardu_faila(vards, fails):
        with open(fails, 'w') as f:
            f.write(vards)
        print("Ārā aug lieli kasteņi.")


def main():
    vards = input("Kastenis ")
    fails = "lietotajs.txt"

    ierakstit_vardu_faila(vards, fails)
