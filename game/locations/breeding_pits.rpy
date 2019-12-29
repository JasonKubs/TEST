# Breeding pits of the castle
label pit:
    
    $ _breeding_pits_menu_items = [
        ('Talk', '_operator_talk'),
        ('Monsters report', 'pits_report'),
        ]
    if rowan_draith_sex:
        $ _breeding_pits_menu_items.append(('Fuck Draith', 'draithRepeat'))

    call screen room_screen('bg25', 'draith room',
        _breeding_pits_menu_items,
        'draith')
    return


label pits_report:
    scene bg25
    'pits_report'
    jump pit
