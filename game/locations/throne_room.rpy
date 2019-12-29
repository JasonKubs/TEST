# Throne room of the castle
label throne_room:
       
    $ _throne_room_menu_items = [
        ('Hints', '_operator_talk'),
        ('Realm reports', 'realm_reports'),
        ('Review goal', 'review_goal'),
        ]
    if can_summon_Liurial:
        $ _throne_room_menu_items.append(('Summon Liurial', 'summon_liurial'))
        
    if get_jez_potion == True and delane_status == "tent":
        $ _throne_room_menu_items.append(("Ask Jezera for help with Tarish's plan", 'tarishQuestJez'))
        
    if jezDelaneHelp == "get" and delane_status == "tent":
        $ _throne_room_menu_items.append(('Ask Jezera for help with gifts for Delane', 'jezeraDelaneHelp'))

    call screen room_screen('images/Backgrounds/throne room.jpg', None,
        _throne_room_menu_items,
        'rowan_empty_throne_room')
    return


label review_goal:
    call screen review_goal_screen
#~     'review goal'
    jump throne_room


label realm_reports:
    call screen realms_report_screen
#~     'realm reports'
    jump throne_room

