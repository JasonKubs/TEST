init python:
    
    event('orciad_debrief', triggers='week_end', conditions=('orciad_state == 2',), run_count=1, priority=pr_story)



label orciad_debrief:

$ goal3_completed = True

$ journal.complete_quest_note('orciad', 'note32')
$ journal.complete_quest_note('orciad', 'note33')


scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

if delane_status == "free" or delane_status == "dead":
    show andras displeased at edgeright with dissolve
    show jezera displeased at midright with dissolve
    
else:
    show andras happy at edgeright with dissolve
    show jezera happy at midright with dissolve
    
je "Роуэн, подойди и встань на колени."

"Роуэн опустился на колено перед троном. Андрас сидел на троне, уверенно расставив ноги. Он не столько сидел на троне, сколько занимал его. Джезера тенью нависла над его плечом."

je "Мы приказали тебе найти союзником среди рас, которые когда-то были частью коалиций нашего предка. Орки Розарии были разумным выбором для этой миссии. Тупые. Сильные. Податливые."

if delane_status == "free" or delane_status == "dead":
    je "Это слишком плохо то, что ты потерпел неудачу в твоих усилиях, чтобы завербовать их."
    "Изера спустилась по лестнице. Через несколько мгновений она уже стояла над Роуэном и смотрела на него мрачным взглядом. Он не изменил позы."
    "На мгновение у него мелькнуло опасение, что они могут знать о том, что он сделал."
    je "Роуэн. Роуэн. Роуэн. Что мне с тобой делать?"
    an "Я знаю, что нам с ним делать."
    "Изера закатила глаза, и повернулась к Роуэну с выражением, которое совсем не соответствовало ее игривому тону."
    je "Ты пытался, я признаю это. Но все это предприятие потерпело крах. Благородная женщина сбежала, и это означает, что у нас нет племени рычагов влияния."
    "Роуэн не поднимал головы. Лучше не казаться раскаивающимся. Он уже был глубоко в яме с гадюками."
    ro "Я глубоко сожалею о своих просчетах, госпожа. Я не мог учесть все переменные, хотя это была моя обязанность."
    ro "Я предполагаю, что мы не можем привести Батри к союзу?"
    je "Батри? Я полагаю, ты слишком долго отсутствовал и не слышал новостей." 
    je "Батри мертв."
    show rowan necklace shock at midleft with dissolve
    "Роуэн застыл. Он видел Батри всего несколько дней назад. Тогда он был жив и здоров."
    show rowan necklace neutral at midleft with dissolve
    ro "Батри мертв? Кто теперь правит племенем?"
    show tarish neutral behind bg6
    tar "Я."
    hide tarish
    show tarish neutral at edgeleft with moveinleft
    "Роуэн оглянулся и увидел женскую фигуру, вышедшую из тени. Кажется, она была там все это время. Это была женщина-орк, с которой он был хорошо знаком."
    ro "Тариш?"
    $ tarish_name = 'Тариш'
    tar "Если Батри и Улькро мертвы, то кому, по-твоему, теперь принадлежит это племя? Батри вышел на охоту за той благородной девушкой, которая пропала без вести."
    if delane_status == "dead":
        tar "Он думал, что она в одном из замков твоего народа... Ходили слухи. Подошел к нему без страха. И поймал стрелу прямо в глаза."
    else:
        tar "Его парни нашли ее следы рядом с замком, принадлежащим твоим людям. Ходили слухи. Подошел к нему без страха. И поймал стрелу прямо в глаза."
        "Она засмеялась, чтобы подчеркнуть этот момент."
        an "После смерти тупого идиота племя окончательно раскололось. Но Тариш пришла сюда вовремя вместе с двумя третеми из них."
        an "В отличие от Батри или Улькро, она оказалась гораздо более готова заключить сделку."
        "Тариш бесилась, стреляя в Роуэна темным взглядом."
        tar "Я вижу, куда дует ветер. Это хорошая сделка для нас...."
        "Она наклонилась вперед и прошептала ему на ухо. Она поблекла свои слова холодным гневом."
        if tarish_path == False:
            tar "...но я не забуду о сделке, которую я предложила тебе. Ты мог привести мне девушку. У меня могло быть целое племя. Не просто забыть."
        else:
            tar "Мы договорились, хьюми. Ты нарушил слово. Это стоила мне почти половины племени да. Я не забываю такого."
        "Роуэн держался абсолютно неподвижно. Возвращение Тариш неприятно. Более того, такой ценный союзник не мог быть антагонизирован перед близнецами."
        je "Короче говоря, ты потерпел неудачу, но по чистой случайности события сложились удачно для тебя."
        je "Если бы у меня не было доказательств обратного, я бы сказалf, что тебе повезло, Роуэн." 
        je "На этот раз мы предотвратим наказание. Мы бы предпочли целое племя, но на данный момент и это подойдет."
        je "В следующий раз от тебя будет ожидаться больше. Бегство этой девушки разрушило почти все."
        an "Хотя, я думаю, ты захочешь знать условия нашей сделки, мальчик. Тариш может быть и присоединяется к нам, но мы должны были согласиться бросить ей кость."
        tar "Племя хочет рабов. Многие из них были приняты в качестве восполнения для тех, кто ушел. Нам нужно больше."
        "Роуэн сглотнул."
        an "Следующие несколько деревень, которые ты захватишь, ты отдашь Тариш. Ни какой дани и торговых сделок. Ты меня слышишь?"
        ro "Конечно, хозяин."
        "Он мысленно выругался. Склонность Тариш к жестокости не была секретом. С ней, у руля орков, означало, более жестокую и беспощадную, армию орков."
        if delane_status == "free":
            "Его сердце упало, забрав с собой всю самооценку, которую он восстановил после побега."
            "Даже его маленькие героические подвиги все еще означали страдания невинных. Ему пришлось заставить себя не хмуриться."
        else:
            "Его сердце тяжело упало. Мало того, что он не сумел спасти Леди Делейн, но еще и обеспечил себе большие страдания в результате своих действий." 
            "Сегодня был мрачный день."
        #TODO
        #Next 3 villages, forced enslavement. No reward. 
        #Max Morale reduced by 20 (from 100 to 80)


else:
    "Андрас громко рассмеялся и присоединился к ним."
    an "Ты продолжаешь удивлять меня. Я ожидал, что ты сбежишь следом за кучей гоблинов. Но ты пошел и взял быка за рога."
    je "Мы поддержали контакт с руководством племени, и они согласились не только поддержать нас, но и послать военных вождей в другие кланы, чтобы собрать больше сил."
    je "Благодаря их присутствию мы сможем начать выставлять реальную армию на поле боя."
    
    if orciad_ally == "tarish":
        show andras displeased at edgeright with dissolve
        an "Хотя я не знаю, как много пользы получим от них с пауком во главе. Отравители и заговорщики не подходят для руководства армией рейдеров и убийц."
        "Изера помахала ему рукой."
        je "Мы обсуждали это в последнее время. Как видишь, брат не очень доволен выбором союзника. Но я признаю твою мудрость в этой ситуации."
        je "В отличие от мужчин, у нее голова на плечах, а не между ног. Все они сражаются на дуэли из-за размера члена."
        je "Она намного проницательнее. С Таришем во главе, мы не будем бояться, что они попадут в какую-нибудь ловушку."
        "Андрас закатил глаза, но не стал настаивать. Роуэн молча обновил свои данные."
        "До тех пор, Изера ручалась за нее, он сомневался, что Андрас будет высказывать свое раздражение при выборе лидера при Роуэне."
        
        if avatar.corruption > 39:
            "И, возможно, при этом поставит во главе племени человека, преданным ему лично...."
            
        else:
            pass
    
    if orciad_ally == "ulcro":
        an "Улькро - старая рука. Он воевал на последней войне. Но с его новой наложницей, у него какой-то пожар в животе."
        an "Мне бы пригодился кто-нибудь  с дикарем в нем, но я могу утешить себя, что их возглавляет настоящий солдат."
        je "Он странный зверь. Он слишком похож на человека. Но я вижу мудрость в твоем выборе, герой."
        je "У любого другого кандидата было бы больше собственной воли. Сороки говорят мне, что им управляет его новая человеческая женщина."
        je "Ты веришь, что эта леди Делейн будет твоим другом?"
        "Роуэн мягко кивнул."
        ro "Я нашел ее вполне поддающейся убеждению. Она любит секс и власть, и воображает себя интеллектуалкой."
        ro "Ухаживайте за ней и заставляйте ее чувствовать себя важной персоной, и она гарантирует, что Улькро выполнит вашу просьбу."
        "Улыбка Изеры выросла больше."
        je "В тебе больше плаща и кинжала, чем я ожидала вначале. Ты действительно очень интересная игрушка, Роуэн."
        "У Роуэна не было ответа на этот вопрос. Он держал голову опущенной, а рот закрытым."
        
    if orciad_ally == "batri":
        an "Вы сделали правильный выбор, кого поддержать. Этот Батри-боец. С ним во главе нашего орочьего отряда мы отправим Розарийцев назад за их стены."
        je "Не слишком радуйся, брат. Батри жесток, но он-тупое оружие. Его воля может сделать его разочаровывающим союзником."
        je "Более того, я сомневаюсь, что мы можем ожидать от него много коварства."
        je "Будет  ли это выражатся, в некомпетеном тактике, или это будет означать, что его будет легко контролировать...что ж, посмотрим. Наверное, все это."
        "Изера повернулась к Роуэну, приподняв бровь."
        show jezera neutral at midright with dissolve
        je "Меня удивило то, что ты вообще выбрал его. Самый жестокий из всех возможных. Возможно, наш маленький герой имеет намного больше Андраса в нем, чем мы думали."
        "У Роуэна не было ответа на этот вопрос. Он держал голову опущенной, а рот закрытым."
    
show andras displeased at edgeright with dissolve
show jezera neutral at midright with dissolve

if rastedelFirstVisit == False:
    je "Не забудьте посетить твою дорогую столицу. Мне не терпится увидеть, чем обернется твое долгожданное возвращение."
    "Она издала игривый смешок."
    
else:
    pass
    
"Роуэн кивнул и поднялся, чтобы уйти. Когда он вышел из зала, его мысли обратились к более важным вопросам. Силы под командованием близнецов значительно выросли."
"До сих пор это были стычки, теперь настоящая война только начиналась."

if avatar.corruption > 39:
    "И все же, почему эта перспектива звучала почти...интересно?"
    
else:
    pass
    
return


