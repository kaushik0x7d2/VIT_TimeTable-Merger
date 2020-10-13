names =[]
contents = []
while True:
    
    a=input("Press ENTER to continue")
    if a=="":
        name=input("Input Name: ")
        names.append(name)
        table=[]
        print("Enter/Paste your content. Ctrl-D to save it.")
        
        while True:
            try:
                line = input()
            except EOFError:
                break
            contents.append(line)
        slots = ['A1', 'TA1', 'TAA1', 'B1', 'TB1', 'C1', 'TC1', 'TCC1', 'D1', 'TD1', 'E1', 'TE1', 'F1', 'TF1', 'G1', 'TG1',
                 'A2', 'TA2', 'TAA2', 'B2', 'TB2', 'TBB2', 'C2', 'TC2', 'TCC2', 'D2', 'TD2', 'TDD2', 'E2', 'TE2', 'F2', 'TF2', 'G2', 'TG2',
                 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11']

        lab_slots = ['L'+ f'{i}' for i in range(1, 95,2)]
        for i in lab_slots:
            slots.append(i)
        for slot in slots:
            exec("%s = %d" % (slot,0))
        for j in slots:
            for k in contents:
                if j+"-" in k:
                    exec("%s = %d" % (j,1))
        for slot in slots:
            table.append(vars()[slot])
        name=name+" = table"
        exec(name)
        for slot in slots:
            exec("%s = %d" % (slot,0))
    elif a=="exit":
        

        y = -1
        for slot in slots:
            check = []
            y = y + 1
            for z in names:
                print(z)
                print(y)
                if vars()[z][y] == 0:
                    check.append(z)
            print(f'Free people in slot {slot} : ', check)
                
        break
