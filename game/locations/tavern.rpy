# Castle tavern
label tavern:
    call screen room_screen('bg21', 'indarah room',
        (('Talk', '_operator_talk'),
        ('Rumours', 'tavern_rumours'),
        ),
        'indarah')
    return


label tavern_ransom:
    scene bg21
    'tavern ransom'
    jump tavern


label tavern_rumours:
    scene bg21
    'tavern rumours'
    jump tavern

