#Izveidot Python programmu, kas nolasītu un izdrukātu tikai ceturtās kolonnas datus no CSV faila. 
import csv

def lasit_ceturtas_kolonnas(fails):
    ceturtas_kolonnas_dati = []
    with open(fails, 'r') as csvfile:
        csv_lasitajs = csv.reader(csvfile)
        for rinda in csv_lasitajs:
            if len(rinda) >= 4:  #Vai rīndā ir pietiekami daudz kollonu

return ceturtas_kolonnas_dati

def main():
    fails = input("Lūdzu, ievadiet CSV faila nosaukumu ar paplašinājumu (piemēram, fails.csv): ")
    try:
        ceturtas_kolonnas = lasit_ceturtas_kolonnas(fails)
        print("Ceturtās kolonnas dati:")
        for dati in ceturtas_kolonnas:
            print(dati)
    except FileNotFoundError:
        print("Faila nav atrasts.")

if __name__ == "__main__":
    main()