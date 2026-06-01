#Generate a code to prevent the zombie enfection in a game. the amount of panzehir (mg) changes in terms of inputs: the patient's weight and the type of bite.
#rules:
#1. If the bite is type 1 (scratch), the panzehir needed is 0.5 mg per kg of the patient's weight.
#2. If the bite is type 2 (deep bite), the panzehir needed is 1 mg per kg of the patient's weight.
#3. If the bite is type 3 (zombie spit/contact), the panzehir needed is 2 mg per kg of the patient's weight.

weight=input('Enter the patient\'s weight in kg: ')
bite_type=input('Enter the bite type (1 for scratch, 2 for deep bite, 3 for zombie spit/contact): ')

weight=float(weight) 


if bite_type == '1':
    panzehir = 0.5*weight
    print('panzehir needed: ', panzehir, 'mg')
elif bite_type == '2':
    panzehir = 1*weight 
    print('panzehir needed: ', panzehir, 'mg')
elif bite_type == '3':
    panzehir = 2*weight
    print('panzehir needed: ', panzehir, 'mg')
else:
    print('Invalid bite type. Please enter 1, 2, or 3.')
    panzehir = None