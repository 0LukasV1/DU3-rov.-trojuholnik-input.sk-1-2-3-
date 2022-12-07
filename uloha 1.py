#prva uloha - hviezdicky

def troj(riad):
    for x in range(riad):
        for a in range(riad-x-1):
            print(end=' ' )
        for a in range(x+1):
            print("*",end=" ")
        print()

troj(8)