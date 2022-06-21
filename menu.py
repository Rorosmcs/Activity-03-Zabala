import zabala_scpt_1 as s_1
import zabala_scpt_2 as s_2

"""
Pokemon: Blastoise
Level = 45
Nature: Water(inc. Stat in Speed, while dec. stat in Sp.Atk)
Based Stats:
Hp: 79 (iv = 34, ev = 79)
Attack: 83(iv = 34, ev = 60)
Defense: 100(iv = 7, ev = 60)
Sp. Atk: 85(iv = 23, ev = 70)
Sp.Def: 105(iv = 24, ev = 21)
Speed: 78(iv = 6, ev = 100)
"""

iv =[0,0,0,0,0,0]
ev = [0,0,0,0,0,0]
nature = [2,3,4,0,2,5,1.2]
base = [0,0,0,0,0,0]
ivcals = [0,0,0,0,0,0]
evcals = [0,0,0,0,0,0]

check_ev = 0

add_stat = [0,0,0,0,0,0]

def start():
    print("""
    Choose calculation:

    1. Stats calculation
    2. Ev calculation
    3. Exit
    """)
    opt = int(input("Choose Option: "))

    if opt ==1:
        statscalculation()
    elif opt ==2:
        while True:
            print("""
            1. EV calculation for single stats
            2. EV calculation for all stats
            3. Back
            """)
            opt = int(input("Choose Option: "))
            if opt == 1:
                singleStats()
            if opt == 2:
                allStats()
            if opt == 3:
                start()
            print("INVALID CHOICE, TRY AGAIN")
    elif opt ==3:
        exit()
    else:
        print("INVALID CHOICE, TRY AGAIN")
        start()
def statscalculation():
    print("\nPLEASE NOTE THAT IV VALUES ONLY RANGE FROM 0 - 31 AND EV VALUES TO 0 -  255 WITH A MAXIMUM OF 510 VALUES IN ALL STATS \n")
    #valuesstats
    print("\n ENTER POKEMON STAT/s: \n")
    lvl = int(input("ENTER LEVEL: "))
    hp = int(input("\nENTER BASED HP: "))
    iv[0] = int(input("ENTE IV: "))
    ev[0] = int(input("ENTE IV: "))
    print("\nOTHERS STATS\n")
    attk = int(input("ENTE ATTACK: "))
    iv[1] = int(input("ENTE IV: "))
    ev[1] = int(input("ENTE IV: "))
    defense = int(input("\nENTER DEFENSE: "))
    iv[2] = int(input("ENTE IV: "))
    ev[2] = int(input("ENTE IV: "))
    spattk = int(input("ENTER SP. ATTACK"))
    iv[3] = int(input("ENTE IV: "))
    ev[3] = int(input("ENTE IV: "))
    spdef = int(input("ENTER SP. DEFENSE"))
    iv[4] = int(input("ENTE IV: "))
    ev[4] = int(input("ENTE IV: "))
    speed = int(input("ENTER SPEED"))
    iv[5] = int(input("ENTE IV: "))
    ev[5] = int(input("ENTE IV: "))

    check_ev = ev[0] + ev[1] +ev[2]+ev[3]+ev[4]+ev[5]
    if check_ev > 510:
        print("\n EFFORT VALUE SHOULD NOT EXCEED 510 WHEN TOTALED! TRY AGAIN. ")
        statscalculation()
        
    print("\nPOKEMON STATS\n")
    print("Nature: Water(inc. Stat in Speed, while dec. stat in Sp.Atk)")
    totph = s_1.pokemonStats.hp_statsfunct(lvl,hp,iv,ev)
    print("\n HP: ", round(totph),end='\n\n')
    print("\nOTHER STATS: \n")
    str = s_1.pokemonStats.other_statsfunct(attk,defense,spattk,spdef,speed,iv,ev,lvl,nature)
    stats_name = ['ATTACK: ','Defense: ','SPECIAL ATTACK: ','SPECIAL DEFENSE: ','SPEED','']
    for x in range(len(str)):
        print(stats_name[x],round(str[x], 2))
        x = x + 1
    anothercalculation()

def singleStats():
    basestat = [0,0,0,0,0,0]
    while True:
        print("""
        1. Hp
        2. Attack
        3. Defense
        4. Sp.Attack
        5. Sp.Defense
        6. Speed
        """)
        opt = int(input("CHOOSE OPTION: "))
        if opt == 1:
            stat_type = "hp"
            print("\nENTER POKEMON STAT/s: \n")
            lvl = int(input("ENTER LEVEL: "))
            basestat[0] = int(input("ENTER BASE HP: "))
            iv[0] = int(input("ENTER IV: "))
            if iv[0] > 31:
                print("\nIV SHOULD RANGE FROM 0 TO 31. TRY AGAIN! ")
                singleStats()
            ev[0] = int(input("ENTER IV: "))
            if iv[0] > 255:
                print("\n EV SHOULD RANGE FROM 0 TO 255. TRY AGAIN!")
                singleStats()
            stat = int(input("DESIRED INCREASED IN HP: "))
        
            ev_needed = s_2.pokemonEv.singlesStatsFunct(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("POKEMON'S Nature: Water(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nTHE EVS NEEDED TO INCREASE THE", stat_type,":",round(ev_needed, 2))

            while True:
                print("""
                1. PERFORM ANOTHER EVS CALCULATION
                2. BACK 
                """)
                opt = int(input("CHOOSE OPTION: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anothercalculation()
                print("INVALID CHOICE, TRY AGAIN")        
        if opt == 2:
            stat_type = 'attack'
            print("\nENTER POKEMON STAT: \n")
            lvl = int(input("ENTER LEVEL: "))
            basestat[1] = int(input("ENTER ATTACK: "))
            iv[1] = int(input("ENTER IV: "))
            ev[1] = int(input("ENTER EV: "))
            stat = int(input("DESIRED INCREASED IN ATTACK: "))

            ev_needed = s_2.pokemonEv.singlesStatsFunct(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("POKEMON'S Nature: Water(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nTHE EVS NEEDED TO INCREASE THE", stat_type,":",round(ev_needed, 2))

            while True:
                print("""
                1. PERFORM ANOTHER EVS CALCULATION
                2. BACK 
                """)
                opt = int(input("CHOOSE OPTION: "))
                if opt == 1:
                    singleStats();
                if opt == 2:
                    anothercalculation()
                print("INVALID CHOICE, TRY AGAIN") 
        if opt == 3:
            stat_type = 'defense'
            print("\nENTER POKEMON STAT: \n")
            lvl = int(input("ENTER LEVEL: "))
            basestat[2] = int(input("ENTER BASE DEFENSE: "))
            iv[2] = int(input("ENTER IV: "))
            ev[2] = int(input("ENTER EV: "))
            stat = int(input("DESIRED INCREASED IN DEFENSE: "))

            ev_needed = s_2.pokemonEv.singlesStatsFunct(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("POKEMON'S Nature: Water(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nTHE EVS NEEDED TO INCREASE THE", stat_type,":",round(ev_needed, 2))

            while True:
                print("""
                1. PERFORM ANOTHER EVS CALCULATION
                2. BACK 
                """)
                opt = int(input("CHOOSE OPTION: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anothercalculation()
                print("INVALID CHOICE, TRY AGAIN")
        if opt == 4:
            stat_type = 'special attack'
            print("\nENTER POKEMON STAT: \n")
            lvl = int(input("ENTER LEVEL: "))
            basestat[3] = int(input("ENTER SP.ATTACK: "))
            iv[3] = int(input("ENTER IV: "))
            ev[3] = int(input("ENTER EV: "))
            stat = int(input("DESIRED INCREASED IN SP.ATTACK: "))

            ev_needed = s_2.pokemonEv.singlesStatsFunct(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("POKEMON'S Nature: Water(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nTHE EVS NEEDED TO INCREASE THE", stat_type,":",round(ev_needed, 2))

            while True:
                print("""
                1. PERFORM ANOTHER EVS CALCULATION
                2. BACK 
                """)
                opt = int(input("CHOOSE OPTION: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anothercalculation()
                print("INVALID CHOICE, TRY AGAIN") 
        if opt == 5:
            stat_type = 'special defense'
            print("\nENTER POKEMON STAT: \n")
            lvl = int(input("ENTER LEVEL: "))
            basestat[4] = int(input("ENTER SP.ATTACK: "))
            iv[4] = int(input("ENTER IV: "))
            ev[4] = int(input("ENTER EV: "))
            stat = int(input("DESIRED INCREASED IN SP.DEFENSE: "))

            ev_needed = s_2.pokemonEv.singlesStatsFunct(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("POKEMON'S Nature: Water(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nTHE EVS NEEDED TO INCREASE THE", stat_type,":",round(ev_needed, 2))

            while True:
                print("""
                1. PERFORM ANOTHER EVS CALCULATION
                2. BACK 
                """)
                opt = int(input("CHOOSE OPTION: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anothercalculation()
                print("INVALID CHOICE, TRY AGAIN") 
        if opt == 6:
            stat_type = 'speed'
            print("\nENTER POKEMON STAT: \n")
            lvl = int(input("ENTER LEVEL: "))
            basestat[6] = int(input("ENTER SPEED: "))
            iv[6] = int(input("ENTER IV: "))
            ev[6] = int(input("ENTER EV: "))
            stat = int(input("DESIRED INCREASED IN SPEED: "))

            ev_needed = s_2.pokemonEv.singlesStatsFunct(stat_type,basestat,lvl,iv,ev,stat,nature)

            print("POKEMON'S Nature: Water(inc. Stat in Speed, while dec. stat in Sp.Atk)")
            print("\nTHE EVS NEEDED TO INCREASE THE", stat_type,":",round(ev_needed, 2))

            while True:
                print("""
                1. PERFORM ANOTHER EVS CALCULATION
                2. BACK 
                """)
                opt = int(input("CHOOSE OPTION: "))
                if opt == 1:
                    singleStats()
                if opt == 2:
                    anothercalculation()
                print("INVALID CHOICE, TRY AGAIN")
        print("INVALID CHOICE, TRY AGAIN") 

def allStats():
    stat_type = ['hp','attack','defense','special attack','special defense','speed',]
    print("\ENTER POKEMON STATS: \n")
    lvl = int(input("ENTER LEVEL: "))
    for x in range(len(stat_type)):
        base[x] = int(input("ENTER BASE" + stat_type[x] + ": "))
        ivcals[x] = int(input("ENTER IV: "))
        if ivcals[x] > 31:
            print("\nIV SHOULD RANGE FROM 0 TO 31. TRY AGAIN!")
            allStats()
        evcals[x] = int(input("ENTER EV: "))
        if evcals[x]>255:
            print("\nEV SHOULD RANGE FROM 0 TO 31. TRY AGAIN!")
            allStats()
        add_stat[x] = int(input("DESIRED INCREASED IN" + stat_type[x] +": "))
        x = x + 1
                        
    check_ev = ev[0] + ev[1] + ev[2] + ev[3] + ev[4] + ev[5]
    if check_ev >510:
        print("\nEFFORT VALUE SHOULD NOT EXCEED 510 WHEN TOTABLED! TRY AGAIN.")
        allStats()

    ev_needed = s_2.pokemonEv.allStatsFunct(lvl,base,ivcals,evcals,add_stat,nature)

    print("POKEMON'S Nature: Water(inc. Stat in Speed, while dec. stat in Sp.Atk)")
    print("\nTHE EVS NEEDED TO INCREASE THE")

    for s  in range(len(stat_type)):
        print(stat_type[s], ": ",round(ev_needed[s], 2))
        s = s + 1

    anothercalculation()

def anothercalculation():
    while True:
        print("""
        1. PERFORM ANOTHER CALCULATION
        2. END
        """)
        opt = int(input("CHOOSE OPTION: "))
        if opt == 1:
            start()
        if opt == 2:
            exit()
        print("INVALID CHOICE, TRY AGAIN")
start()