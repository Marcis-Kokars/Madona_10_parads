#Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā). 
def lasit_failu(fails):
    with open(fails, 'diena') as f:
        saturs = f.read()
    return saturs

def main():
    fails = input("Ārā šodien sakaista diena")
    try:
        teksts = lasit_failu(fails)
        print("Faila saturs: Saulaina, skaista, brīnišķīga")
        print(teksts)
    except FileNotFoundError:
        print("ziema")

if __name__ == "__main__":
    main()