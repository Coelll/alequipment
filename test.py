def Cargo_func(item):
    print(f'{item}')

def AA_func(item):
    print(f'{item}')

def ASW_func(item):
    print(f'{item}')

def Aux_func(item):
    print(f'{item}')

def BB_func(item):
    print(f'{item}')

def DD_func(item):
    print(f'{item}')

def DiveB_func(item):
    print(f'{item}')

def Fighters_func(item):
    print(f'{item}')

def HeavyC_func(item):
    print(f'{item}')

def LargeC_func(item):
    print(f'{item}')

def LightC_func(item):
    print(f'{item}')

def Seaplanes_func(item):
    print(f'{item}')

def SubTorps_func(item):
    print(f'{item}')

def TorpBomb_func(item):
    print(f'{item}')

def Torpedoes_func(item):
    print(f'{item}')

#   Table names defined in a dictionary
table_names = {'Cargo': Cargo_func,
                'AA Guns' : AA_func,
                'ASW': ASW_func,
                'Auxilary': Aux_func,
                'BB guns': BB_func,
                'DD guns': DD_func,
                'Dive bombers' : DiveB_func,
                'Fighters' : Fighters_func,
                'Heavy Cruiser guns': HeavyC_func,
                'Large Cruiser guns': LargeC_func,
                'Light Cruiser guns' : LightC_func,
                'Seaplanes' : Seaplanes_func,
                'Sub torpedoes' : SubTorps_func,
                'Torpedo bombers': TorpBomb_func,
                'Torpedoes': Torpedoes_func}

user_input = input("")
table_names.get(user_input)(user_input)