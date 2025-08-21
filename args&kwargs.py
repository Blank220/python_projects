def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end= ' ')
    print('')
    print(f"{kwargs.get('country')}")
    print(f"{kwargs.get('house')}, {kwargs.get('street')}")
    print(f"{kwargs.get('barangay')}, {kwargs.get('municipality')} {kwargs.get('province')}")


shipping_label('Mark','Lester','Comia',
               country = 'Philippines',
               province = 'Batangas',
               municipality = 'San Juan',
               barangay = 'Tipaz',
               street = 'Blue Island',
               house = '#148'
               )