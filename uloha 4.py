# pyramida zo slov

def riad(a, t=''):
    b=len(t)+1
    if t=="":
        print(x * "*")
    else:
        c=((x - len(t)) / 2)
        c=int(c)
        if 25 > len(t) > 14:
            print((c - 1) * "*", t, (c - 1) * "*")
        else:
            print((c - 1) * "*", t, c * "*")

x = 40
riad(x)
riad(x, 'jan botto')
riad(x, 'zlta lalija')
riad(x, '-')
riad(x, 'stoji stoji mohyla')
riad(x, 'na mohyle zla chvila')
riad(x, 'na mohyle trnie chrastie')
riad(x, "a v tom trni chrasti rastie")
riad(x)