# random map events that happen on plains
init python:

    #Brigand Slavers
    #Requires: After first warning of famine sweeping area, after Castle Raeve assault at least
    # TODO: probably switch dependence to rumor of famine
    event('brigand_slavers', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, depends=('famine_looms', 'raeve_keep_visit_goal2'),
        group='map_expl', priority=pr_map_rnd)
    #Tower Ruin
    event('tower_ruin', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label brigand_slavers:
#Brigand Slavers
#Requires: After first warning of famine sweeping area, after Castle Raeve assault at least
scene bg31 with fade

"Роуэн услышал их задолго до того, как они появились в поле зрения."
"Множество ног, маршируюших одновремено; грубый смех и ругань; грохот и звон цепей."
"С полдюжины человек, вооруженных ножами, мечами и арбалетами, конвоировали около 20 рабов в лохмотьях, связаных вместе по рукам и ногам."
"Увидев впереди на дороге Роуэна, вожак резким движением руки приказал остановиться."

if avatar.infamy < 10:
#infamy low to medium
    brig "Эй, я тебя знаю. Большой, крестьянский герой с прошлой войны, не так ли? Рейган, или что-то в этом роде. Когда-то я работал с парнями, которые маршировали под твоим началом."
    "Он бросил ленивый взгляд на людей позади себя. Двое других бандитов отвернулись, на их худых грязных лицах застыла горечь."
    brig "Ну, герой ты мой, мы с тобой не ссоримся. Это другое время, когда люди должны делать некоторые гразные дела, чтобы остаться в живых."
    brig "Думаю, что настоящий человек из народа увидит это и пойдет по своим делам, а мы пойдем по своим. Это так?"
    "Остальные бандиты внимательно следили за Роуэном, держа руки поближе к оружию. Рабы, стоявшие во главе отряда, беспомощно смотрели на Роуэна пустыми глазами."
    jump .brigmenu
#else
else:
    brig "Эй, я тебя знаю. Большой крестьянский герой с прошлой войны, не так ли? Рейган, или что-то в этом роде."
    brig "Слышал, что ты поменял свои полюса. Печальное состояние этого мира, да?"
    ro "Что ты делаешь?"
    brig "В наши дни обычным Джекам приходится прикладывать свои руки к некоторым грязным делам, чтобы выжить. Но я думаю, что такой прагматичный джентльмен, как ты, может это оценить."
    brig "Может быть, тебе будет интересно купить часть наших акций?"
    brig "Они будут дешевыми - я не могу позволить себе накормить их всех, это правда. Придется избавиться от некоторых."
    "Остальные бандиты внимательно наблюдали за Роуэном, держа руки поближе к оружию. Рабы в голове отряда беспомощно смотрели на Роуэна."
    jump .brigmenu

label .brigmenu:

menu:

    "Пропустить их.":
        $ released_fix_rollback()
        ro "Меня все это не интересует. Убирайся с моих глаз."
        "Главарь разбойников ухмыльнулся, и его компаньоны расслабились."
        brig "Я рад, что ты хоть немного соображаешь. Приятный денек, сэр Роберт, или как там тебя."
        "Он резко дернул рукой, и другие разбойники заставили невольничий поезд снова тронуться. Звон цепей и шарканье ног через некоторое время полностью исчезли из поля зрения Роуэна."
        #gain a small amount of infamy
        $ change_base_stat('f', 1)

    #low corruption only
    "Потребовать, чтобы они освободили рабов." if avatar.corruption < 10:
        $ released_fix_rollback()
        ro "Ты немедленно освободишь этих людей, или я убью тебя на месте, бестолочь."
        brig "Стыдно. Меня заставили поверить, что ты умен."
        "Один из солдат внезапно поднял арбалет и выстрелил."

        #dodge check DC12
        $ event_tmp['dodge check'] = check_skill(12, 'dodge')
        if not event_tmp['dodge check'][0]:
        #fail
            "Роуэн дернулся в сторону, но не смог остановить болт, с ошеломляющей силой врезавшийся в его броню."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Роуэн акробатически метнулся в сторону, и болт просвистел мимо его плеча."
            "Затем главарь разбойников набросился на него, вонючий и свирепый, пытаясь зацепить его острием своего кинжала."

        $ event_tmp['strength check'] = check_stat(10, 'strength')
        #strength check DC10
        if not event_tmp['strength check'][0]:
        #fail
            "Роуэн боролся изо всех сил и сумел отскочить достаточно далеко, чтобы лезвие не пронзило его внутренности, но все же получил жестокий удар по ребрам."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Роуэн боролся, как Росомаха, нанося апперкот по небритому подбородку мужчины и заставляя его вспороть своим клинком пустоту."

        if not event_tmp['strength check'][0] and not event_tmp['dodge check'][0]:
        #Failed both checks
            "Согнувшись пополам от шока, вызванного ранами, Роуэн не мог остановить зверя, который ударил его в живот и сбросил в придорожную канаву."
            "Издевательский смех и одобрительные возгласы других бандитов, перемешавшиеся с ужасными стонами рабов, сопровождали его падение."
            brig "В этом мире больше нет места для таких, как ты, герой. Прими это или умри."
            "Он резко дернул рукой, и другие разбойники заставили невольничий поезд снова тронуться. Звон цепей и шарканье ног через некоторое время полностью исчезли из поля зрения Роуэна."
            return
        else:
        #passed one check    # or two
            "Роуэн отодвинулся на достаточное расстояние, чтобы вытащить свой собственный клинок, и с силой ударил им по незащищенному горлу противника. С кровавым вздохом он рухнул в грязь."
            ro "Бегите или встретьтесь со мной, трусы."
            "Глаза остальных разбойников метнулись между телом их предводителя и Роуэном, затем один из них, а затем и остальные повернулись и убежали. Роуэн обыскал карманы трупа и нашел ключ, который подходил к кандалам рабов."
            slave "Я ... я не знаю, что мы будем делать, по правде говоря, хозяин. Мы бежали на юг от голода, когда они напали на нас. Они забрали то немногое, что у нас было. Но... все же лучше, чем быть во власти таких людей."
            slave "Мы что-нибудь придумаем. Большое вам спасибо, сэр Роуэн, - пока я жив, я буду говорить всем, кто захочет слушать, что вы последний по-настоящему благородный человек в Розарии."
            "Роуэн смотрел им вслед, сияя рыцарской гордостью."
            #gain 25 xp, lose some infamy and guilt
            $ add_exp(25)
            $ change_base_stat('f', -1)
            $ change_base_stat('g', -1)
            return

    "Купить рабов.":
        $ released_fix_rollback()

        ro "Они предлагают этих пленников дешевле, чем я мог бы за них заплатить. И даже быть во власти Андраса и Изеры лучше, чем быть брошенными на верную смерть этой бандой..."
        ro "Хорошо. Я возьму немного."
        brig "Сколько?"

        menu:
            "Не могу себе этого позволить.":
                $ released_fix_rollback()
                ro "Черт..."
                brig "Гммм. Как хорошо, что мы не пытались тебя ограбить. Такая пустая трата времени."
                "Он резко дернул рукой, и другие разбойники заставили невольничий поезд снова тронуться. Звон цепей и шарканье ног через некоторое время полностью исчезли из поля зрения Роуэна."
                #small infamy boost
                $ change_base_stat('f', 1)
                return

            #allow extra choices to buy [5], [10], [15], or [20] slaves with the following outcome
            # TODO: check for free space for prisoners?
            'Купить 5' if castle.treasury >= 5 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 5
            'Купить 10' if castle.treasury >= 10 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 10
            'Купить 15' if castle.treasury >= 15 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 15
            'Купить 20' if castle.treasury >= 20 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 20
        $ released_fix_rollback()
        "Не сводя глаз с остальных разбойников, Роуэн передал ему золото."
        #if not 20
        if event_tmp['buy slaves'] < 20:
            "Вожак достал ключ и щелкнул им, отсчитывая количество оборванных душ, которые только что купил Роуэн."
        #else
        else:
            "Разбойники вытолкнули вперед всех рабов, которые только что купил Роуэн."
        slave "Ты... ты не имеешь права так поступать! Мы просто обычные люди, как и ты..."
        brig "Прекрати тявкать, собака! Приятно иметь с вами дело, сэр Редмонд. Я надеюсь, что мы сможем сделать это снова."
        "С кристаллом Роуэну потребовалось всего несколько минут, чтобы вызвать отряд орков, которые грубо увели оборванное имущество прочь."
        "Глядя, как они уходят, Роуэн почти убедил себя, что он спас этих людей от верной смерти, либо продали еще худшим хозяевам. Почти."
        #minus gold (5 gold per prisoner) and gain prisoners equal to the number of slaves purchased, medium guilt and infamy gains
        $ change_treasury(-5 * event_tmp['buy slaves'])
        $ change_prisoners(event_tmp['buy slaves'])
        $ change_base_stat('g', 3)
        $ change_base_stat('f', 3)
        return

    #High corruption only
    "Убить их, забери рабов себе." if avatar.corruption >= 10:
        $ released_fix_rollback()
        ro "Такая грязь, как ты, не заслуживает рабов. Я думаю, что убью тебя и возьму их себе."
        brig "Ты ведь сделаешь это, правда?"
        "Один из солдат внезапно поднял арбалет и выстрелил."

        #dodge check DC12
        $ event_tmp['dodge check'] = check_skill(12, 'dodge')
        if not event_tmp['dodge check'][0]:
        #fail
            "Роуэн дернулся в сторону, но не смог остановить болт, с ошеломляющей силой врезавшийся в его броню."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Роуэн акробатически метнулся в сторону, и болт просвистел мимо его плеча."
            "Затем главарь разбойников набросился на него, вонючий и свирепый, пытаясь зацепить его острием своего кинжала."

        $ event_tmp['strength check'] = check_stat(10, 'strength')
        #strength check DC10
        if not event_tmp['strength check'][0]:
        #fail
            "Роуэн боролся изо всех сил и сумел отскочить достаточно далеко, чтобы лезвие не пронзило его внутренности, но все же получил жестокий удар по ребрам."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Роуэн боролся, как Росомаха, нанося апперкот по небритому подбородку мужчины и заставляя его вспороть своим клинком пустоту."

        if not event_tmp['strength check'][0] and not event_tmp['dodge check'][0]:
        #failed both checks
            "Согнувшись пополам от шока, вызванного ранами, Роуэн не мог остановить зверя, который ударил его в живот и сбросил в придорожную канаву."
            "Издевательский смех и одобрительные возгласы других бандитов, перемешавшиеся с ужасными стонами рабов, сопровождали его падение."
            brig "Это слишком громкие слова. В следующий раз держи их при себе."
            "Он резко дернул рукой, и другие разбойники заставили невольничий поезд снова тронуться. Звон цепей и шарканье ног через некоторое время полностью исчезли из поля зрения Роуэна."
            return
        else:
        #succeeded one or more
            "Роуэн отодвинулся на достаточное расстояние, чтобы вытащить свой собственный клинок, и с силой ударил им по незащищенному горлу противника. С кровавым вздохом он рухнул в грязь."
            "Роуэн двинулся на остальных разбойников, лицо его было бледным и страшным от жажды крови."
            "Однако еще до того, как он добрался до первого, они бежали, испуганные и ошеломленные этим живым воплощением хаоса, с которым им не повезло столкнуться."
            "Рабы отшатнулись от него, и труп задергался в грязи, пепельный ужас был написан мелом на их изможденных лицах."
            ro "Делайте в точности, как я говорю, и вы не разделите судьбу этого дурака."
            "С кристаллом Роуэну потребовалось всего несколько минут, чтобы вызвать отряд орков, которые грубо увели оборванное имущество прочь."
            "Роуэн смотрел им вслед, полностью удовлетворенный своей добычей и тем, как она была добыта."
            #gain 20 prisoners, gain 25 xp, gain a large amount of infamy
            $ change_prisoners(20)
            $ add_exp(25)
            $ change_base_stat('f', 5)
            return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label tower_ruin:
#Tower Ruin
#No requirements
scene bg31 with fade

"На вершине соседнего холма стояли развалины старой сторожевой башни - одинокий каменный палец, длиною тридцать футов от земли, остаток из другого века."
"Должно быть, это логово бандитов или обиталище привидений, предположил Роуэн. В долинах неохраняемый готовый камень редко лежал долго, его быстро присваивало крестьянство."
"Он должен был подумать, стоит ли рисковать и тратить время на изучение руин."

menu:
    "Осмотреть.":
        $ released_fix_rollback()
        "Роуэн поднялся по усыпанному щебнем холму и вошел в башню через щель в стене."
        "В воздухе чувствовался дурной привкус, ощущение злобы и отчаяния, казалось, запекшееся в самом камне, подтверждая его подозрения, что это место населено призраками."
        #stealth check DC12
        if not check_skill(12, 'move_silently')[0]:
        #fail
            "Роуэн старался вести себя как можно тише, пробираясь через камни и гниющую мебель внутри в поисках чего-нибудь ценного."
            "Но черная атмосфера сжималась вокруг него, пока он не почувствовал, что задыхается, телом и разумом."
            "Это было все равно что утонуть на дне глубокого. Где внизу, {i} голоса{/i} шептали ужасные вещи..."
            "Нервы у Роуэна не выдержали, и он, отчаянно спотыкаясь, вернулся к пролому в стене и выбежал из него, набирая полные легкие воздуха, как только снова оказался снаружи."
            "Через несколько мгновений он восстановил дыхание - но ощущение обречености, черных слов и мыслей, проникших в его сознание, осталось."
            #lose 1 move point, gain a small amount of corruption
            $ change_mp(-1)
            $ change_base_stat('c', 1)
            return
        else:
        #pass
            "Роуэн старался вести себя как можно тише, пробираясь через камни и гниющую мебель в поисках чего-нибудь ценного."
            "Зловещая угнетенность башни осталась, но Роуэн сохранял свои мысли такими же безобидными и тихими, как его шаги, и таким образом, он не тревожил души, которые скрывались в ней."
            #lose one move point
            $ change_mp(-1)

        #loot rolls
        $ event_tmp['loot rolls'] = dice(4)
        $ released_fix_rollback()

        if event_tmp['loot rolls'] == 1:
        #1/4 chance - nothing
            "К сожалению, в башне не было ничего интересного. Оказалось, призраки здесь не хранят ничего, кроме горьких воспоминаний о собственной кончине."
            "Разочарованный, Роуэн осторожно выбрался из развалин и продолжил свой путь."
            #gain 20 xp
            $ add_exp(20)
            return
        elif event_tmp['loot rolls'] == 2:
        #1/4 chance - random piece of armour
            "На полпути вверх по лестнице, которая огибала башню изнутри, Роуэн обнаружил останки скелета, стрела пронзила его оскаленный череп."
            "В руках он сжимал броню - возможно, что воин не успел натянуть ее вовремя. Защищенная от стихии, он все еще была в хорошем состоянии."
            "Роуэн осторожно забрал ее из костлявых, покрытых плесенью рук бывшего владельца и пошел обратно, радуясь возможности спуститься с холма с добычей и оставить руины далеко позади."
            #gain one random piece of armour, gain 20 xp
            $ add_exp(20)
            $ get_rnd_item(0, 500, 'armour')
            return
        elif event_tmp['loot rolls'] == 3:
        #1/4 chance - money
            "На нижнем уровне башни Роуэн нашел складское помещение, которое выглядело так, будто его уже обыскали."
            "Внутри которого множество людей встретило неприятные последствия, сюдя по количеству скелетов, которые он должен был обойти."
            "В небольшом углублении у дальней стены он нашел небольшой сундучок, наполненный толстыми монетами. Древняя сокровищница, мягко поблескивающая золотом."
            "Сундук не был спрятан. Почему его не забрали? Проклят?"
            "Казалось, ничего плохого не случилось, когда Роуэн осторожно потрогал монеты, а затем переложил их в свой кошель и покинул башню."
            "Довольный своей добычей и еще более довольный тем, что оставил позади призрачные руины, он спустился с холма и продолжил свой путь."
            #gain one hundred gold for the treasury, gain 20 xp
            $ change_treasury(100)
            $ add_exp(20)
            return
        else:
            #1/4 chance military information
            "В башне не было ничего ценного, все это было потеряно из-за какой-то катастрофы, постигшей это место, когда оно еще знало живых обитателей."
            "Однако в главном зале Роуэн нашел большую карту, прибитую к стене, потрескавшуюся, но все еще хорошо сохранившуюся."
            "На ней были изображены горы, реки, крепости и арсеналы, передвижения войск, узкие места на местности, где во время войны должны были ставится заслоны."
            "Она явно устарела, но по собственным сведениям Роуэн понял, что это была карта Розарии, ее основных поселений и складов, не изменившихся за это время."
            "Он подумал, что эта информация вполне может позволить ему догадаться, как и где силы барона, выстроятся, если дело дойдет до прямых столкновений."
            "Он тщательно переписал детали карты, а затем покинул башню, радуясь, что проклятое место осталось позади."
            #todo - Rosaria loses military points
            #gain 20 xp
            $ add_exp(20)
            return

    "Оставить башню в покое.":
        $ released_fix_rollback()
        "Пусть, башня спит, решил Роуэн. Он продолжил свой путь, быстро оставив руины позади."
        return

