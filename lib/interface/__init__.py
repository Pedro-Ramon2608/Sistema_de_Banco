def cor(cores=0):
    tab = ['\033[m', # 0 - without color
             '\033[91m', # 1 - red
             '\033[92m', # 2 - green
             '\033[93m', # 3 - yellow
             '\033[94m', # 4 - blue
             '\033[95m', # 5 - purple
             '\033[96m', # 6 - cyan
             '\033[97m', # 7 - white
             ]
    return tab[cores]

def lin(tam=40):
    return f'{cor(7)}-' * tam

def cabeçalho(msg):
    print(lin())
    print(msg.center(40))
    print(lin())
