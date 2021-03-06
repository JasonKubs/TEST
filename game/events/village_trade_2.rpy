# village trade events
init python:

    #They Offer Slaves Instead
    #should be uncommon (todo)
    event('village_trade_offer_slave_instead', triggers='village_trade', run_count=1, group='village_trade', priority=pr_map_res)
    #Other Trader
    #should be uncommon (todo)
    event('village_trade_other_trader', triggers='village_trade', run_count=1, group='village_trade', priority=pr_map_res)


label village_trade_offer_slave_instead:
#They Offer Slaves Instead
#should be uncommon (todo)

"Роуэн осмотрел деревню и нашел ее крайне нуждающейся в еде. Над ними годами висела тень голода. Люди были одеты в тряпки, и у них были признаки недоедания."
"Когда он рассказал местным торговцам о возможности доставлять им грузы первой необходимости в обмен на доход деревни, у них загорелись глаза."
"Но возникла проблема, деревня, не имела средств, необходимых для оплаты доставки продовольствия."
"Местные торговцы пообещали как-то собрать необходимые деньги. Несколько часов спустя Роуэн увидел что они придумали."
"Несколько жителей деревни стояли в кандалах на обочине дороги. Они смотрели на Роуэна жалкими глазами."
"Торговцы пояснили, что, когда они все рассказали жителям деревни, некоторые мужчины и женщины, чьи дома больше всего пострадали от голода, решили продать себя в обмен на продовольствие."
"Благодаря их самопожертвованию деревня сможет позволить себе купить больше продуктов питания. Роуэн поцарапал подбородок."

menu:
    "Принять рабов в качестве альтернативной формы оплаты.":
        $ released_fix_rollback()
        "Роуэн посмотрел вниз на бедные несчастные души. Конечно, если оставить их здесь, они умрут от голода."
        "Конечно жизнь в качестве рабов в Бладмине не было тем, что Роуэн желал кому-либо, но, возможно, у них там была бы лучшая жизнь."
        "И кроме того, он зашел уже слишком далеко, чтобы мучаться вопросом  о рабстве. Теперь это была его жизнь."
        "Роуэн дал свое согласие торговцам, и рабы были погружены в вагоны, как и скот."
        "Их губы скручивались в милосердных улыбках, но их глаза были широкими от страха перед неизвестным."
        "В деревне была бы еда, и этого было достаточно."
        #Reduced income. +prisoners. + guilt.
        # TODO: reduced income
        $ change_prisoners(5)
        $ change_base_stat('g', 2)
        return

    "Отказ принять предложение о продаже рабов.":
        $ released_fix_rollback()
        "Роуэн посмотрел на них со вздохом. Эти люди были в отчаянном положении, конечно. Но, зная, кто его хозяева вряд ли он мог бы вернутся с ними в Бладмин."
        "Он старался не думать о людях-заключенных, которые уже там находятся, из-за него."
        "Поэтому, с тяжелым сердцем, он отказался от предложения и настаивал, что единственное, что он примет в оплату, это деньги. "
        "Торговцы с грустью приняли эту сделку, обменявшись взглядами с сельскими жителями, которые предложили себя в рабство."
        "Одна маленькая девочка схватила его лошадь за ногу, прося забрать ее. Она утверждала, что с ее продажей ее младший брат мог позволить себе поесть."
        "Роуэн просто оттолкнул девушку в сторону, не глядя на нее."
        #Reduced trade income.
        # TODO: reduced income
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label village_trade_other_trader:
#Other Trader
#should be uncommon (todo)

"С яркими красными фруктовыми садами, растянувшимися в аккуратных рядах, эта деревня станет хорошим торговым партнером."
"Однако, когда Роуэн прибыл в этот торговый дом, он нашел там чиновников скептически настроенных."
"Для них он был просто еще одним торговцем, пытавшимся сосать грудь их богатства."
"Роуэн сел за стол напротив них, изо всех сил стараясь не сказать им, что, если они отклонят его требования, Андрас придет и убьет их всех."
"Ценой их непримиримости может быть только смерть."
"На деревенской площади между собраниями Роуэн выглянул на улицу и обрел счастье. Маленькие дети бегают сытые и имеющие свой дом."
"Перед началом встречи к Роуэну подошел торговец. Он был таинственным человеком, одетым в одежду из прекрасного шелка."
"Торговец объяснил, что он слышал о ходе переговоров и будет более чем счастлив помоч Роуэну. Как ни странно, он ни чего не поросил взамен."
"Кем бы ни был этот человек, у него должны быть мотивы для попытки помочь."

"Роуэн пожала руку торговцу. Какими бы ни были его намерения, помогая Роуэну, он поможет ему в выполнении его миссии, а также спасет жизни жителей этого городка."
"Кроме того, продавец ничего не просил взамен. Если он предъявляет требования позже, Роуэн всегда может кинуть его."
"Вдвоем они вернулись в торговую гильдию. Новый союзник Роуэн, очевидно, знал деревенских торговцев."
"В перерывах напитками и шутками он уводит их от жесткой позиции."
"Сделка, которую Роуэн получил в результате, была, возможно, не такой масштабной, как ему бы хотелось, но все же была довольно прибыльной."
"Роуэн спросила торговца, почему он ему помог, когда они выехали из города. У торговца улыбка стала кровавой. Перед глазами Роуэна из головы торговца вырасли маленькие рога."
"Существо просто попросило Роуэна передать свои добрые пожелания леди Джезере. Затем его рога исчезли, не оставляя следов."
"Инкубус уехал, еще одна деревня на руне уже видна на расстоянии."
#Extra income from village.
$ castle.villages_income += 1
return
