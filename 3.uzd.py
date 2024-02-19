#Izveidot Python programmu, kas nolasītu un izdrukātu trešās un ceturtās teksta faila rindas saturu. 
def lasit_rindas(fails):
    ar_failu = open(fails, 'r')
    rindas = ar_failu.readlines()
    ar_failu.close()
    return rindas

def main():
    fails = input("Lūdzu, ievadiet teksta faila nosaukumu ar paplašinājumu (piemēram, fails.txt): ")
    try:
        rindas = lasit_rindas(fails)
        tresa_rinda = rindas[2] if len(rindas) > 2 else "Nav tresās rindas"
        ceturta_rinda = rindas[3] if len(rindas) > 3 else "Nav ceturtās rindas"

        print("Trešās rindas saturs:", tresa_rinda)
        print("Ceturtās rindas saturs:", ceturta_rinda)
    except FileNotFoundError:
        print("Faila nav atrasts.")

if __name__ == "__main__":
    main()