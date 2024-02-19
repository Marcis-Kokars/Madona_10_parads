 #Izveidot Python programmu, kur lietotājs ievada gar faila nosaukumu un faila formātu (paplašinājumu), un atkarībā no faila paplašinājuma tiek nolasīts faila saturs. Nolasītā informācija ir jāizdrukā terminālī. Paredzēt iespejamās kļūdas! 
def lasit_failu(fails):
    with open(fails, 'r') as f:
        saturs = f.read()
    return saturs

def main():
    fails = input("Lūdzu, ievadiet faila nosaukumu: ")
    formats = input("Lūdzu, ievadiet faila formātu (paplašinājumu, piemēram, txt vai csv): ")
    fails_ar_formats = f"{fails}.{formats}"

    try:
        if formats == "txt":
            teksts = lasit_failu(fails_ar_formats)
            print("Faila saturs:")
            print(teksts)
        elif formats == "csv":
            # Jūs varat pievienot kodu šeit, ja vēlaties apstrādāt CSV failus
            print("CSV failu apstrāde pagaidām nav atbalstīta.")
        else:
            print("Nepareizs faila formāts. Atbalstītie formāti: txt, csv")
    except FileNotFoundError:
        print("Faila nav atrasts.")

if __name__ == "__main__":
    main()
