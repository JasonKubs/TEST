# Alexia jobs and dialogues
init python:

    event('alexia_maid', conditions=('Rowan_sc',), triggers="st_alexia_maid", group='alexia_training')
    event('alexia_tavern_wench', conditions=('Rowan_sc',), triggers="st_alexia_tavern_wench", group='alexia_training')
    event('alexia_dancer', conditions=('Rowan_sc',), triggers="st_alexia_dancer", group='alexia_training')
    event('alexia_whore', conditions=('Rowan_sc',), triggers="st_alexia_whore", group='alexia_training')
    event('alexia_rest', conditions=('Rowan_sc',), triggers="st_alexia_rest", group='alexia_training')
    event('alexia_librarian', conditions=('Rowan_sc',), triggers="st_alexia_librarian", group='alexia_training')
    event('alexia_etiquette', conditions=('Rowan_sc',), triggers="st_alexia_etiquette", group='alexia_training')
    event('alexia_obedience', conditions=('Rowan_sc',), triggers="st_alexia_obedience", group='alexia_training')
    event('alexia_slut', conditions=('Rowan_sc',), triggers="st_alexia_slut", group='alexia_training')
    event('alexia_exhibitionism', conditions=('Rowan_sc',), triggers="st_alexia_exhibitionism", group='alexia_training')


label alexia_maid:
    $ renpy.block_rollback()
    if alexia.depravity <= 30:
        scene alexia_maid_1
    else:
        scene
    if alexia.skill('maid') < 25:
        '[alexia.name] проводит неделю убирая замок, как и было указано, но, к сожалению, делает очень плохо. В следствии, [alexia.perspn] получает очень мало денег за свою работу.'
    elif alexia.skill('maid') <= 50:
        'Неделя пролетает для [alexia.name]. [alexia.posspn] делает лучше, чтобы замок был как можно более чистым.'
        'Несмотря на [alexia.posspn] eе результат средний, и [alexia.perspn] оценивают, как достойный лишь средней заработной платы.'
    elif alexia.skill('maid') <= 75:
        'К настоящему времени, [alexia.name] начала привыкать к уборке замка, а также к участкам, которые требуют наибольшей работы по уборке.'
        'Используя эти знания, [alexia.perspn] способна хорошо справиться с избавлением от большей части пыли и грязи, в результате этого [alexia.posspn] хорошо вознаграждена.'
    else:
        'Потратив так много времени на уборку замка, [alexia.name] стала экспертом в этом. Вооруженная шваброй и ведром и надежным тряпкой, [alexia.perspn] это крепкое приспособление, которое можно увидеть в замке.'
        'К тому времени [alexia.perspn] убирается безупречно, а качество оплаты соответствует качеству работы.'
    $ do_job(alexia)
    return


label alexia_librarian:
    $ renpy.block_rollback()
    if alexia.depravity <= 30:
        scene alexia_library_1
    else:
        scene
    if alexia.skill('librarian') < 25:
        '[alexia.name] работает переплетает в библиотеке. [alexia.perspn] не очень хорошо знает этот медленный и трудоемкий процесс.'
        'К концу недели на полу все еще много книг, и оплата [alexia.perspn] полученное от Клионы, отражает ее недовольство.'
    elif alexia.skill('librarian') <= 50:
        'Проведя немного времени в библиотеке, [alexia.name] научилась получать данные о местоположении ряда книг, но работа все еще идет медленно.'
        'Когда Клиона приходит, чтобы заплатить, остается еще куча дел [alexia.posspn], и, как следствие, плата [alexia.perspn] получается довольно скромной.'
    elif alexia.skill('librarian') <= 75:
        'Имея большой опыт работы с библиотеками, [alexia.name] не имеет проблем с сортировкой и хранением большинства книг, только несколько [alexia.posspn] вызывают проблемы.'
        'Когда все сказано и сделано, остается только несколько груд, и Клиона находит работу удовлетворительной, вручая подходящее количество монет для хорошо выполненной работы.'
    else:
        'Изучив много стеллажей в библиотеке, [alexia.name] может сделать работу с закрытыми глазами [alexia.posspn]. С каждым указателем и местоположением, запомненным после нескольких недель сортировки, стопки книг исчезают в мгновение ока.'
        'TБиблиотека настолько опрятна, что Клиона даже удается улыбнуться, когда она видит работу [alexia.name], и вручает довольно красивую награду как благодарность.'
    $ do_job(alexia)
    return


label alexia_tavern_wench:
    $ renpy.block_rollback()
    scene
    'Алексия работает в таверне.'
    $ do_job(alexia)
    return


label alexia_dancer:
    $ renpy.block_rollback()
    scene
    'Алексия танцует в таверне, развлекая посетителей.'
    $ do_job(alexia)
    return


label alexia_whore:
    $ renpy.block_rollback()
    scene
    'Алексия работает в замковом борделе.'
    $ do_job(alexia)
    return


label alexia_rest:
    $ renpy.block_rollback()
    scene
    'Алексия отдыхает.'
    $ alexia.energy = 100
    return


label alexia_etiquette:
    $ renpy.block_rollback()
    scene
    if alexia.depravity < 20:
        'Изера проводит каждый день, пытаясь обучить сексуально подавленную [alexia.name] без особого успеха.'
        'Когда неделя подходит к концу, [alexia.perspn] кажется становится более восприимчивым к образу мыслей Изеры.'
    elif alexia.depravity < 40:
        'Обучив [alexia.name] быть более открытой, Изера продолжает свои уроки по выявлению в ней внутренней шлюхи.'
        'Несмотря на сопротивление, демон замечает, что ее ежедневные занятия, безусловно, дают желаемый эффект.'
    elif alexia.depravity < 60:
        'Изера ухмыляется, наблюдая, как далеко [alexia.name] упала с тех пор [alexia.perspn] начала свое обучение.'
        'После еще одной недели специального обучения, [alexia.name] сделала еще один шаг по пути к полной порочности.'
    $ do_job(alexia)
    return


label alexia_obedience:
    $ renpy.block_rollback()
    scene
    # TODO: these texts rely on obedience stat, not on training level. It is more reliable to use training levels directly
    if alexia.obedience < 20:
        'Изера изо всех сил старается научить Алексию основам подчинения, но девушка бесполезна, что делает ее очень хорошей любовницей.'
        'По крайней мере, к концу недели она стала более управляема, чем была в начале.'
    elif alexia.obedience < 40:
        'Теперь, когда Алексия начала понимать свое место, Изера продолжает свои уроки, чтобы разрушить то, что осталось от ее воли.'
        'После нескольких дней, демон, передающего свои уроки с помощью силы, она видит немного сопротивления в девушке, когда ей приказывают.'
    elif alexia.obedience < 60:
        'Теперь уроки прочно овладели Алексией, и теперь она без колебаний действует, чтобы выполнить любую просьбу, Изеры.'
        'Демон ухмыляется, заметив, что подчинение начало укореняться в девушке, и она радуется жизни в качестве рабыни.'
    $ do_job(alexia)
    return


label alexia_slut:
    $ renpy.block_rollback()
    scene
    'Тренировка Алексии как шлюхи'
    $ do_job(alexia)
    return


label alexia_exhibitionism:
    $ renpy.block_rollback()
    scene
    'Тренинг для Алексии по эксгибиционизму '
    $ do_job(alexia)
    return


# TODO: maybe move following dialogues to separate file
label alexia_confirm_self_title:
    $ renpy.block_rollback()
    scene
    al 'Да [alexia.player_title], отныне я буду называть себя [alexia.self_title].'
    jump train_alexia


label alexia_confirm_player_title:
    $ renpy.block_rollback()
    scene
    al 'Хорошо, теперь я буду звать тебя [alexia.player_title].'
    jump train_alexia
