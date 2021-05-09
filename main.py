
def kerulet_sikidomok():
    print('===========================')
    print('Kerület számítás:')
    adott_input = input('Írj egy "N"-t négyzetért, "H"-t a háromszögért. Írj egy "0"-t, ha ki szeretnél lépni a programból: ').capitalize()
    kerulet: int = 0
    if adott_input == "N":
        oldalak_hosszusaga = int(input('Add meg a négyzet oldalának hosszát cm-ben: '))
        kerulet = oldalak_hosszusaga * 4
        print(f'A háromszög kerülete: {kerulet}cm')
    elif adott_input == "H":
        elso_oldal = int(input('Add meg az első oldal hosszát cm-ben: '))
        masodik_oldal = int(input('Add meg a második oldal hosszát cm-ben: '))
        harmadik_oldal = int(input('Add meg a harmadik oldal hosszát cm-ben: '))
        if elso_oldal < masodik_oldal + harmadik_oldal and masodik_oldal < elso_oldal + harmadik_oldal and harmadik_oldal < elso_oldal + masodik_oldal or elso_oldal == masodik_oldal and elso_oldal == harmadik_oldal:
            kerulet = elso_oldal + masodik_oldal + harmadik_oldal
            print(f'A háromszög kerülete: {kerulet}cm')
            pass
        else:
            print('Az általad megadott háromszög nem létezik!')
    elif adott_input == "0":
        print('Program leállítása...')
        quit()
    else:
        print('Az általad megadott opció nem létezik!')
        print('===========================')


def main() -> None:
    kerulet_sikidomok()
    while True:
        valasztas = int(input('A program újboli lefuttatásához írj egy "1"-est: '))
        if valasztas == 1:
            kerulet_sikidomok()
        else:
            print("Program leállítása...")
            quit()


if __name__ == "__main__":
    main()
