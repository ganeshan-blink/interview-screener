# AC: Return the lowest priced medication in dollars given a list of medication attributes subject to:
# Matching drug class: All medications with the same drug class number are equivalent
# Prefer generics over brand on equivalent price
# Don't dispense medication if max quantity is exceeed  

medications = [
    {
       'name': 'losartan',
       'type': 'generic',
       'class_number': 1,
       'price': 14,
       'currency': 'pound',
       'unit_type': 'tablet',
       'max_quantity': 90

    },
    {
       'name': 'cozaar',
       'type': 'brand',
       'class_number': 1,
       'price': 34,
       'currency': 'dollar',
       'unit_type': 'tablet',
       'max_quantity': 25

    },
    {
       'name': 'Amaryl',
       'type': 'brand',
       'class_number': 2,
       'price': 24,
       'currency': 'dollar',
       'unit_type': 'tablet',
       'max_quantity': 16

    },
    {
       'name': 'Glucotrol',
       'type': 'brand',
       'class_number': 2,
       'price': 40,
       'currency': 'euro',
       'unit_type': 'tablet',
       'max_quantity': 10
    }
    ,
    {
       'name': 'Micronase',
       'type': 'brand',
       'class_number': 2,
       'currency': 'rouble',
       'price': 3900,
       'unit_type': 'tablet',
       'max_quantity': 30
    },
    {
       'name': 'Glimepiride',
       'type': 'generic',
       'class_number': 2,
       'price': 24,
       'currency': 'dollar',
       'unit_type': 'tablet',
       'max_quantity':16
    }
]


def find_cheap_med(cnum, qty):
    for med in medications:
        if med['class_number'] == cnum:
            fnd = []
            fnd.append(med)
    lp = 0
    res = None
    for med in fnd:
        if qty * get_dollar_price(med) >= lp:
            lp = qty * get_dollar_price(med)
            res = med

    if res['max_quantity'] <= qty:
        return 0
    return res, get_dollar_price(res)
    

def get_dollar_price(med):
    if med['currency'] == 'dollar':
        return med['price']
    elif med['currency'] == 'euro':
        return med['price'] / 0.84 # 0.84 euro = 1 dollar
    elif med['currency'] == 'rouble':
        return med['price'] * 73 # 73 rouble = 1 dollar
    elif med['currency'] == 'pound':
        return med['price'] / 0.72 # 0.72 lb = 1 dollar
    else:
        return med['price']
    
res, price = find_cheap_med(2,15)
print("Best med for " + str(res) + " is " + str(price))
