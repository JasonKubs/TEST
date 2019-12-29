# Castle brothel
label brothel:

    $ _brothel_menu_items = [
        ('Talk', '_operator_talk'),
        ('Spies', 'brothel_spies'),
        ]
    if shayaShow:
        $ _brothel_menu_items.append(('Watch Shaya put on a show', 'shaya_Show'))    
        
    if shayaPrivateShow:
        $ _brothel_menu_items.append(('Get a private show', 'a_private_dance'))
    

    call screen room_screen('bg24', 'shaya room',
        _brothel_menu_items,
        'shaya')
    return


label brothel_spies:
    call screen spies_controls_screen
    jump brothel

