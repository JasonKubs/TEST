

label hunt_for_gits:

if delane_gifts > 39:
    scene bg26 with fade
    "Как всегда, Роуэн направился к Краугу и его оркам. Но на этот раз его ждал только один орк."
    show rowan necklace neutral at midleft with dissolve
    show wild orc neutral at edgeright with dissolve
    wo "Шеф сказал, что Делейн доволна подарками. Больше никаких рейдов."
    ro "Хм."
    "Он должен был предвидеть это. В отличие от Батри, Улькро грабил не ради забавы."
    "У него была четкая цель, и теперь, когда она была достигнута, он не станет рисковать своими лучшими людьми в дальнейшем." 
    "Как только борьба за лидерство будет завершена, Роуэн, вероятно, сможет совершать регулярные рейды с другими орками, если это будет интересно для него."  
    $ giftHuntAvailable = False
    jump campMenu

else:

    if giftHuntFirst == True:
        
        scene bg26 with fade
        "Улькро пообещал ему отряд рейдеров, и Роуэн был бы дураком, если бы не воспользовался этим. Дорогие подарки было не так легко найти."
        if jezDelaneHelp == "get":
            "Теперь, когда он подумал об этом, у Изеры, возможно, есть какие-то старые драгоценности, с которыми она захочет расстаться..."
            "Лишь бы звезды сошлись и оно стала щедрой, под их лучами. Ее помощь обходится дорого, но это был бы самый быстрый способ получить что-то хорошее для Делейн."
        else:
            pass
        if cliohnaDelaneHelp == "get":
            "В библиотеке имелся раздел, посвященный знати Розарии, который мог бы заинтересовать Делейн."
            "И он мог бы спросить Клиону, о возможности взять некоторые книги для нее."
        else:
            pass
        "Пока что, было бы лучше, если бы он воспользовался людьми Улькро."
        show rowan necklace neutral at edgeleft with dissolve
        show wild orc neutral at center with dissolve
        show orc soldier neutral at center with dissolve
        "Рейдарскаяя группа ждала его на краю лагеря. Двадцать ветеранов орков, солдаты, некоторые из которых достаточно взрослые, чтобы сражаться под Карнасом."
        "Их возглавлял крупный орк по имени Крауг, и в ближайшие дни они будут составлять компанию Роуэна."
        ro "Центральный и восточный регионы Розарии уже слишком разорены, чтобы они могли принисти нам богатую добычу. Западные земли будут принесут больше награбленного."
        "Крауг молча кивнул. Хотя формально он был во главе отряда, Роуэн должен был действовать как следопыт партии." 
        "Он сам должен был найти цели, подходящие для их набега." 
        ro "Пойдем. У нас впереди долгий путь."
        scene black with fade
        "..."
        $ giftHuntFirst = False
        jump giftRaidProper
        
    else:
        scene bg26 with fade
        "И снова Роуэн встретился с отрядом Крауга. И как всегда, его люди были готовы отправиться в любой момент."  
        scene black with fade
        "Пора было идти за подарками для Делейн."
        "..."
        jump gift_Raid_Travel
        
label gift_Raid_Travel:

if giftRaidTravel == 1:
    scene bg3 with fade
    "Это был третий день их маленького рейда на Запад."
    "Поскольку это был их второй набег, то Роуэн обнаружил, к своему собственному удивлению, что Крауг и его люди больше бросаются на него."
    "Они стали дисциплинированными. Тихими. Организованными." 
    "Все, то чего не было у его собственных орков." 
    "Скорее всего, это был не последний их набег, и не было никаких причин продолжать держаться настороже. Он должен использовать это время более конструктивно." 
    "Он мог бы попытаться сломать лед между ним и молчаливым лидером партии, Краугом."
    "Как только Улькро приведет свое племя в замок Бладмин, его офицеры станут важными фигурами в армии близнецов."
    "Знание их сильных и слабых сторон может принести ему большую пользу в будущем." 
    "Кроме того, он мог бы потратить время на тренировки. Месяцы плена взяли свое - он знал, что уже не так силен, как в прошлом. Орки были бы хорошими спарринг-партнерами." 
    menu:
        "Познакомиться с Краугом.":
            $ released_fix_rollback()
            $ knowKraug = True
            "Приняв решение, он подошел к солдату-ветерану во время их следующего привала."
            "Будучи немногословным орком, Крауг не очень-то стремился говорить о себе, но после пары настойчивых вопросов Роуэн заставил его немного открыться." 
            "Когда-то у него был свой отряд, не больше трех десятков человек. Они совершали набеги в долине к северу от Розарии. "  
            "Это не удивило Роуэна, так как у многих орков были свои небольшие племена, прежде чем сильный вождь находил их и решал, что они станут частью его племени." 
            "Но Крауг, по-видимому, нашел Ультро по собственной воле. У старого вождя было то, чего хотел Крауг."
            show rowan necklace neutral behind bg3
            ro "И что же это было?"
            krau "Сила."
            "... Думаю, он не должен был ожидать большего от орка."
            "Он хотел еще раз спросить Крауга на эту тему, но для большого орка эта тема, должно быть, была особенно щекотливой, так как он не стал продолжать разговор." 
            "Ему придется продолжить распрос в другой раз." 
            $ giftRaidTravel = 2
            jump giftRaidProper
            
        "Тренировать бой с орками.":
            $ released_fix_rollback()
            $ giftHuntTraining = True
            "На следующем привале, когда лагерь был разбит, Роуэн подошел к оркам, которые показались ему более дружелюбными." 
            "Он объяснил им свою болезнь - что его форма атрофировалась за эти месяцы и что ему нужны надежные партнеры по тренировкам, чтобы восстановить ее."  
            "Орки пожали плечами. Для них это был такой же хороший способ скоротать время, как и любой другой." 
            "С этого момента Роуэн ввел строгий режим тренировок каждый вечер, сосредоточившись на работе ног и мастерстве владения клинком, как против одного, так и против нескольких противников." 
            "Орки оказались компетентными партнерами."
            "Как и многие из их рода, они предпочитали нападать и подавлять противника мощными атаками, но люди Улькро умели не только полагаться на свое физическое превосходство." 
            "Не в силах использовать свои обычные трюки, Роуэн счел спарринги стоящими, хотя потребуется некоторое время, чтобы увидеть ощутимые результаты." 
            $ add_exp(5)
            $ giftRaidTravel = 2
            jump giftRaidProper
            
elif giftRaidTravel == 2:
    scene bg31 with fade
    
    if knowKraug == True:
        "И снова они двинулись на Запад. И снова Роуэн нашел время, чтобы попытаться подружиться с массивным орком." 
        "Делясь элем у костра, Роуэн попытался вытянуть из Крауга побольше информации. Одна тема особенно занимала его мысли, как, несомненно, и всех остальных."  
        "Был ли у Улькро шанс против Батри?"
        "Ответом на это было коллективное, хотя и не слишком восторженное 'да', исходившее как от Крауга, так и от остальных людей Ультро."
        "Вождь был старым, опытным бойцом. Батри же восходящей звездой, но в глазах многих он был слишком юн, чтобы встать во главе племени." 
        "But apparently, if Batri were to win the upcoming bout, they would have no issue following him."
        show rowan necklace neutral behind bg31
        krau "Древнее право. Самый сильный лидер. Другой следует на отдых."
        ro "Разве ты не хотел бы отомстить за смерть Улькро? Или попытаться самому стать лидером?"
        "Хотя оба вождя были самыми сильными в лагере, многие орки обладали сравнимой доблестью с ними, служа лейтенантами и помощниками. Крауг был бы одним из них." 
        "Но большой орк сердито зарычал и покачал головой."  
        krau "Нет. Нет смысла. Все устали от Дис."
        krau "Весь бой в беспорядке. Ничего не хочу с этим делать."
        krau "Достаточно головной боли с Тариш, несущей неприятности."
        krau "... Как ты знаешь. "
        "Орк прищурил свои маленькие глазки. Возможно, было ошибкой принять приглашение Тариш, когда он впервые вошел в лагерь вместе с Андрасом."
        "Это бросало тень на все, что он делал сейчас."
        show rowan necklace angry behind bg31
        ro "Моя верность принадлежит Улькро. Ты в этом сомневаешься?"
        krau "..."
        "Атмосфера накалилась. Роуэн больше ничего не узнает от орка в этом рейде."
        $ giftRaidTravel = 3
        jump giftRaidProper
        
    else:
        "Once more on the trail with the orcs, Rowan resumed his training regimen." 
        "This time, his main sparring partner was a sly-looking orc named Vorg. Shorter and thinner than most of his comrades, he fought with two short blades and wore light, leather armor."
        "There was something stereotypically dishonest about him, from the dirty fighting style to the devious smirk he always had when he thought nobody was looking."  
        "Rowan labeled him 'Most likely to stab someone in the back', and quite honestly felt the other orcs shared his opinion here." 
        "Regardless, practice was practice. Though he made a mental note to never turn his back to the orc."   
        $ add_exp(5)
        $ giftRaidTravel = 3
        jump giftRaidProper
        
elif giftRaidTravel == 3:
    scene bg31 with fade
    if knowKraug == True:
        "Четвертый набег. 'Сколько их еще?' - подумал Роуэн, когда они разбили лагерь под вечер." 
        "Он увидел поблизости Крауга, который готовил костер. Их последний разговор закончился на плохой ноте, но после всех их приключений герой чувствовал, что между ними возникло некоторое товарищество." 
        "Достаточное, чтобы задать, пожалуй, самый спорный вопрос, который только можно было задать в лагере."  
        "Что Крауг думает о страстном увлечении Ультро Делейн?" 
        "Большинству орков это должно было показаться странным. Многие думали, что Улькро просто одержим ею. Если бы они знали истинную причину его действий, то, без сомнения, над ним бы посмеялись."
        "Разумеется, не в лицо, а тихо, незаметно, за кружкой эля и среди проверенных союзников."
        "Роуэн ожидал, что Крауг либо уклонится от ответа, либо даст какой-нибудь уклончивый ответ. Но вместо этого орк посмотрел ему прямо в глаза и заговорил низким рычащим голосом." 
        show rowan necklace neutral behind bg31
        krau "У меня был приятель, Роуэн. Долгое время назад."
        "В полутьме вечера Роуэн увидел, как орк стиснул зубы."
        krau "Длинный белый волос. Как зимний дух."
        krau "Готовил хорошее рагу."
        krau "…"
        krau "...и ребёнка в пути. "
        "Его выражение смягчилось, всего на мгновение..."
        krau "Я не должен был быть ее другом. Проиграл дуэль из-за нее. "
        krau "Но я ей нравился. Нравился мой дух."
        krau "Выбрал меня, а не другого."
        "... только чтобы превратиться в ненавистный хмурый взгляд."
        krau "И хьюми убил ее."
        "Орк уставился на костер, пламя которого лениво плясало в темноте."
        "Гнев и ненависть, тщательно сдерживаемые годами. Жажда мести была так сильна, что течение времени не помогло ей угаснуть."
        show rowan necklace angry behind bg31
        ro "... Тебе ведь на самом деле не нравится Улькро, не так ли?"
        "Он оскалил зубы в насмешливой улыбке."
        krau "Нет."
        krau "Но он приведет нас к твоему хозяину. Красному демону."
        krau "И этого мне достаточно."
        
        if serveChoice == 4:
            "Улькро, возможно, был одним из немногих орков, кто мог преодолеть свою ярость и желать от жизни чего-то большего, чем война и насилие." 
            "Но его солдаты были не такими. Все, чего они хотели, - это отомстить. Кровь. Убийство и изнасилование." 
            "Впрочем, это не имело значения. Это были инструменты, не более того."  
            show rowan necklace happy behind bg31
            ro "Не беспокойся. Андрас позаботится о том, чтобы вы увидели действие." 
            krau "Хорошо."
            "От таких зверей, как он, тоже была своя польза."
            
        else:
            "Роуэн промолчал. Орки, подобные Улькро, доказали, что даже существа хаоса способны перерасти свои инстинкты." 
            "Но многие другие все еще были движимы ненавистью и жаждой насилия." 
            "Он мог только надеяться, что сумеет сделать что-нибудь, чтобы помешать им поджечь мир." 
        
        show rowan necklace concerned behind bg31
        krau "Хватит болтать."
        krau "Эти разговоры занимают слишком много времени. С этого момента сосредоточься на поиске цели."
        ro "Согласен."
        "Он сомневался, что узнает от него больше. Лучше всего было покончить с этим и перейти к следующей цели."
        $ kraugCommander = True
        $ giftRaidTravel = 5
        jump giftRaidProper
        
    else:
        "Четвертый набеги. Несмотря ни на что, Роуэн начал искренне любить некоторых орков, входивших их маленькую группу."
        "Они тоже находили его дружелюбным, и некоторые из них начинали относиться к нему уже не как к ненужному грузу, а как к достойному товарищу."  
        "Один из них даже предложил ему советы по его тренировке в замке."
        "Учитывая физическую разницу между ним и орками, Роуэн был уверен, что если следовать полностью его совету, то он буквально убьет его, хотя в нем было некоторые здравое зерно." 
        "И благодаря их регулярным спаррингам Роуэн уже чувствовал, что становится сильнее. Он с нетерпением ждал их будущих тренировок." 
        "Но вместо этого." 
        krau "Роуэн, это занимает слишком много времени"
        krau "Хватит терять время. Сосредоточься на поиске хорошей цели."
        "Прошел уже месяц, и Крауг начал терять терпение. Как бы ни хотелось Роуэну использовать это время для оттачивания своих навыков, он не должен испытывать судьбу лишний раз." 
        "Той подготовки, которую он прошел до сих пор, должно быть достаточно. Пришло время покончить с этим." 
        $ add_exp(100)
        $ giftRaidTravel = 5
        jump giftRaidProper


else:
    jump giftRaidProper


label giftRaidProper:

if check_skill(12, 'survival')[0]:
    jump giftEventSelection
    
else:
    jump giftHuntFailed
    

label giftEventSelection:

$ res_roll = dice(20)

if res_roll < 15:
    
    $ res_roll = dice(3)
    
    if res_roll == 1:
    
        if meetingBanditsSeen == False:
            jump meetingBandits
        else:
            jump giftEventSelection
    
    if res_roll == 2:
        if findingMonksSeen == False:
            jump findingMonks
        else:
            jump giftEventSelection
    
    if res_roll == 3:
        if findingCaravanSeen == False:
            jump findingCaravan
        else:
            jump giftEventSelection
            
else:
    $ res_roll = dice(2)

    if res_roll == 1:
    
        if noblesHuntingSeen == False:
            jump noblesHunting
        else:
            jump giftEventSelection
    
    if res_roll == 2:
        if summerResidenceSeen == False:
            jump summerResidence
        else:
            jump giftEventSelection

                                             
label giftHuntFailed:
scene bg31 with fade

"Несмотря на все старания Роуэна, группе не удалось найти подходящую цель для рейда."  
"Герой ожидал, что Крауг обвинит его в пустой трате времени, но когда он сказал орку, что они должны прекратить эту охоту, он воспринял новость спокойно." 

krau "Понятно. Попробуем на следующей неделе."
            
"Он должен был сделать это."

return

label meetingBandits:

scene bg31 with fade

"Роуэн не нашел того, что искал, но он возьмет все, что сможет."
"На северо-западе, они наткнулись на группу бандитов. После обмена обычными оскорблениями и угрозами группа проявила готовность к переговорам."
"Имея связи в соседних городах, они предложили обмен - рабынь на подарки."
"Крауг быстро одобрил эго, не спрашивая мнения Роуэна."
" аставить Делейн принять Улькро было на данный момент главным приоритетом, и никакая цена не была слишком высокой." 

$ delane_gifts += 5
$ meetingBanditsSeen = True
return


label findingMonks:

scene bg31 with fade

"Поскольку орки близнецов в основном разоряли центральную и восточную Розарию, в западных регионах было гораздо больше торговли и больше путешественников."  
"Пара монахов, направлявшихся в одно из соседних аббатств, оказалась их целью."
"Сопровождаемые святым рыцарем и его оруженосцем, их не будут беспокоить большинство бандитов. На них не все равно не было ничего ценного."
"Кроме книг."
"Орки быстро справились с ними, добавив в библиотеку Делейн “Удобрение урожая”, “Гимны Солансии”, “Вечная Вера” и “Анналы западных династий”."
"Может быть, не самая захватывающая коллекция, но, по крайней мере, было хоть что-то."

$ delane_gifts += 5
$ findingMonksSeen = True
return

label findingCaravan:

scene bg31 with fade

"Путешествуя, Роуэн иногда встречал караваны и торговцев. Но ему редко выпадала возможность послать орков на перехват."
"Это простой вопрос логистики – если они не направлялись в сторону одного из порталов, его орки не смогли бы поймать их вовремя."
"Но теперь, когда он двигался с настоящей бандой разбойников за спиной…"
"Торговый караван, который ему удалось выследить, состоял из трех повозок и более дюжины наемников. Трудная цель для большинства бандитов."
"Крауг велел ему сидеть тихо и подготовил своих людей. Роуэн попыталась возразить, но орк не стал его слушать."
"Его группа уже давно тренируется вместе. Они знали, как работать вместе - Роуэн будет просто  мешатся под ногами." 
"Они сам разберется с караваном."

show rowan necklace neutral at center with dissolve

"Роуэн наблюдал с безопасного расстояния, как орки устроили засаду и напали, как только торговцы оказались в нужном месте." 
"Разворачивающийся бой был немного смущающим зрелищем." 
"Роуэн привык к тому, что орки в лучшем случае проявляют умеренную компетентность, а в худшем-полное ее отсутствие."
"Но это ... это были элитные люди Улькро. Орки, которым он доверил обеспечение подарков для своей любимой Делейн."
"Они были дисциплинированными. Они молчали. И они были безжалостны."
"Наемники были убиты без особого труда." 
"Роуэн сомневался, что Батри или Тариш действительно понимают, что значит хорошо обученный солдат."

if serveChoice == 4:
    show rowan necklace happy at center with dissolve
    "Он дал задний ход своей лошади."
    
else:
    show rowan necklace concerned at center with dissolve
    "Он давал близнецам опасного союзника."

show rowan necklace neutral at center with dissolve

"Как только битва закончилась, Роуэн подошел к каравану, чтобы осмотреть его груз."

krau "Хмм. Сырье."

ro "Похоже на то."

"Железные прутья. Зерно. Семена. Вещи, которые были нужны Бладмину, но Делейн ничего не оценил бы."
"За исключением..." 

ro "Драпировка."

"Три тюка дорогих тканей, идеально подходящих для украшения палатки Делейн."
"После недолгих переговоров Крауг согласился оставить большую часть строительных материалов Роуэну."
"В то время как они забрали ткани и часть золота, спрятанного в ящиках тележки." 
"Это должно помочь с проектом восстановления."

$ change_treasury(+80)
$ delane_gifts += 10
$ findingCaravanSeen = True
return

label noblesHunting:

scene bg3 with fade

"Забравшись далеко на Запад, Роуэн повел орков к тому месту, как он знал, что было охотничьими угодьями лордов." 
"Удача улыбнулась им. Невероятная удача."
"На третий день поисков Роуэн наконец нашел то, что искал. Охотничья группа, состоящая из пары молодых лордов, четырех рыцарей ухаживающими за двумя дамами."
"У одного из них была фигура, похожая на фигуру Делейн."

show rowan necklace neutral at midleft with moveinleft

krau "What’s tha plan?"

ro "Хммм..."

"Они не смогут снять одежду с мертвых тел. Если оставить в стороне моральные последствия, смыть кровь будет ужасно трудно."
"Но они действительно значительно превосходят их числом…"

ro "Если это возможно, я не хочу злить другую благородную семью."
ro "Поэтому мы должны попытаться решить эту проблему без кровопролития."

krau "Большинство рыцарей скорее умрут с честью, чем сдадутся оркам."

"В долгой военной карьере Роуэна проблемой для него всегда было отсутствие чести у лордов. Он не мог поверить, что настанет день, когда на его пути ее будет такое изобилие."

ro "Тогда мы убедимся, что смерть 'с честью' для них не вариант."

show rowan necklace happy at midleft with dissolve

ro "Это может быть немного не обычно, просто следуй моему примеру."

scene black with fade 

scene bg3 with fade

joff "А потом сказал: 'Держи эту уголовную мразь!” и одним взмахом меча выбил топор прямо из его руки!"
joff "Свист!"

nive "О боже!"

rosa "(О Богиня, пожалуйста, прикончи меня.)"

"Леди Нив громко ахнула, прикрывая рот от изумления."
"Остальные члены свиты, в зависимости от расстояния, отделявшего их от Сэра Джоффри, либо вежливо кивали, либо закатывали глаза...."
".... либо, в случае одинокого рыцаря в самом хвосте, имитировали удар ножом в сердце своему другу."  
"Упомянутый друг, хотя и разделял его чувства по этому поводу, был слишком хорошо воспитан, чтобы предложить что-либо, кроме понимающей улыбки."

rosa "Вы, должно быть, настоящий боец, сэр Джоффри."

joff "Ну, я не люблю хвастаться..."

lysa "Никто тебя в этом не обвиняет, Джоффри."

joff "...Но мой дядя, лорд Полиньяк, говорит, что уже двадцать лет не видел такого воина, как я!"

nive "ООО!"

rosa "Очень внушительно."

lysa "Очень впечатляет."

rosa "О тогда, вы просто обязаны рассказать нам больше."

"Как Леди Нив купилась все это дерьмо, было выше понимания леди Розалии."
"Если повезет, ее подруга скоро преодолеет свою влюбленность, и она освободится от присутствия этого шута."
"По крайней мере, сэр Лизандер был более подходящей компанией."

joff "Ну, если ты настаиваешь..."

rkn "Подождите."

"Рыцарь впереди поднял руку, его голос был напряжен."

rkn "… Что-то не так."

harry "Точная оценка, мой осторожный друг!"

"Из-за дерева перед ними появился человек в маске. Одетый в кожу, он держал в руке палаш и кусок ткани, закрывавший его лицо."

harry "Ужасный Гарри к вашим услугам."
harry "И это ограбление."

"Сэр Джоффри расхохотался."

joff "Ха, ты,  что..."

lysa "...это банда."

"Орки вышли из своих укрытий вокруг них."

rosa "(Как же мы их не заметили?!)"

lysa "… Ваши орки весьма искусны, сэр Гарри."

harry "Спасибо мисс, мы “ужасный Гарри и его отвратительные негодяи.”"

"..."

harry "Я не мог придумать ничего, что начиналось бы с 'Х'."

nive "... Хулиганы?"

harry "..."

orcb "Бля, это лучше."
orcb "Эх."

"Розали в панике огляделась. Почему эти люди так непринужденно болтают? Их же собирались убить!"
"Она наклонилась к стоявшему рядом рыцарю и сердито прошептала:"

rosa "Сделай что-нибудь!"

"Образцовое руководство. Рыцарь на мгновение заколебался, затем осторожно потянулся за мечом..."

harry "А...аа....а.. "

"... но ужасный Гарри тут же заметил его движение и угрожающе погрозил пальцем."

harry "Я бы не советовал этого делать. Мы все хорошо вооружены, окружили вас и превосходим числом в два раза."

harry "Где то трое на одного, так как милые дамы формально не воюют."
harry "… Но я прослежу, чтобы они были превратились в 'заложниц', если вы откажетесь сотрудничать."

joff "Ублюдок!"

harry "Спасибо. А теперь, как насчет того, чтобы вы сняли все свое золото и драгоценности, и мы покончим с этим ..."
harry "Несчастным для вас и очень удачным для меня, фиаско, без единой капли пролитой крови?"

joff "Если вы думаете..."

lysa "Джоффри, дамы."

"Предупреждающий тон его подруги, должно быть, дошел до вспыльчивого аристократа."
"Джоффри закрыл рот и после некоторого колебания бросил бандиту мешочек с монетами, висевший у него на поясе." 
"Рыцари последовали его примеру. Быть ограбленным бандитами было унизительно, но действовать опрометчиво и рисковать жизнями своих подопечных было намного хуже."  
"Вскоре перед человеком в маске лежала небольшая кучка сокровищ. Ужасный Гарри одобрительно кивнул."  

harry "Хорошо, хорошо, мы все на пути к очень счастливому концу, по сравнению с некоторыми другими вариантами. И еще кое-что."
harry "Юная леди, могу я узнать ваше имя?"

"Бандит повернулся к Розали. Она изумленно уставился на него в удивлении."

harry "Ваше имя?"

rosa "… Розали. Леди Розали Доллоуэй."

harry "Очень приятно познакомиться. Доллоуэй, знатное имя...."
harry "Итак, леди Розали...."
harry "Мне нравилось ваше платье. Раздеватесь."

"Розали покраснела."

rosa "Чт... Да как ты смеешь!"

harry "С полной безнаказанностью.  Хватит болтать. Раздевайтесь. Прыгай!"

"Розали вытаращила глаза, не понимая, что происходит. Она огляделась вокруг, надеясь хоть как-то спастись от этого безумия." 
"Никто из рыцарей не встретился с ней взглядом. Они нервно схватились за мечи, но еще не успели вытащить их. "
"Кроме одного."

joff "… нет."

"Сэр Джоффри спрыгнул с лошади, обнажил меч и повернулся лицом к бандиту."

joff "Я сказал - Нет. Вы можете взять наши драгоценности, наше золото.... "
joff "Но вы не отнимете у нас чести! Я не позволю вам унижать Леди Розали ради вашего больного удовольствия! "

"Воздух стал напряженным. Почему-то казалось, что бандит в маске больше не улыбается под маской."

harry "Мальчик, я не думаю, что ты понимаешь, в каком положении ты находишься здесь…"

joff "Не смей называть меня мальчиком!"
joff "Я сэр Джоффри Роули, оруженосец Себастьяна Кумбса! И я не позволю какому-то простому бандиту так обращаться с благородной леди!"
joff "Мне плевать, что вы нас окружили! Честь требует, чтобы я встал на ее защиту!"
joff "Хотя я сомневаюсь, что ты понимаешь, что значит сохранять свои идеалы перед лицом невзгод."

if avatar.corruption > 80:
    "В бандите произошла едва заметная перемена. Розали не понравилось выражение его глаз."
    rosa "Джоффри...."
    harry "Очень хорошо. Я принимаю твой вызов."
    "Холодный голос Гарри прервал ее: бандит поднял руку и сделал знак сэру Джоффри подойти к нему." 
    "Мгновение спустя оба бойца оказались лицом к лицу. Джоффри со своим вооруженным мечом, бандит со своим собственным, ублюдочным клинком."
    "У него было преимущество длины меча, но Джоффри тренировался с детства."
    "Может быть, у него есть шанс?"
    harry "Леди Розали, не могли бы вы подать нам сигнал?"
    rosa " Я не..."
    harry "Не заставляйте меня повторять, Леди Розали."
    "Она тяжело сглотнула. Она не хотела этого делать. Но она должна была это сделать."
    rosa "Бой!"
    "Все произошло в одно мгновение.  Джоффри бросился на бандита..." 
    show bg3 with sshake
    "Ужасный Гарри одним ударом отбил его меч и пошел в контратаку."
    show bg3 with sshake
    show bg3 with redflash
    joff "Ааааа!"
    "Молодой оруженосец взвыл от боли, когда меч бандита ударил его в лицо. Он упал на землю, схватившись за правую сторону лица."
    joff "Мой глаз! Ты забрал мой ... -"
    "Бандит ударил его рукоятью в лицо, и он потерял сознание."
    harry "Но я пощадил твою жизнь. Считай, что тебе повезло."
    "Его глаза обратились к дворянке. Дрожь пробежала вниз по ее позвоночнику."
    harry "Итак, Леди Розали…"
    harry "Платье, если можно."
    scene black with fade
    scene bg31 with fade
    show rowan necklace neutral at edgeright with dissolve
    show wild orc neutral at center with dissolve
    show orc soldier neutral at center with dissolve
    "Платье для Делейн. Ювелирные украшения. Немного золота. Прекрасная добыча, по мнению Роуэна."
    wo "Хех, это очень весело."
    ro "Заткнись."
    "Это не была победа для него."
    $ delane_gifts += 15
    $ change_base_stat('g', +3)   
    $ noblesHuntingSeen = True
    return
    
else:
    "В бандите произошла едва заметная перемена. Розали никак не могла понять, в чем дело. Это была ... печаль?"
    
    harry "Очень хорошо. Я принимаю твой вызов. Готовься."
    "Бандит поднял руку и сделал знак сэру Джоффри подойти к нему."
    "Мгновение спустя оба бойца оказались лицом к лицу. Джоффри со своим вооруженным мечом, бандит со своим собственным, ублюдочным клинком."
    "У него было преимущество по длине меча, но Джоффри тренировался с детства. Может быть, у него есть шанс?"
    harry "Леди Розали, не могли бы вы подать нам сигнал?"
    "Она тихо вздохнула. В какой-то степени она чувствовала, что это плохо кончится."
    rosa "Бой!"
    "Все произошло в одно мгновение. Джоффри бросился на бандита. Ужасный Гарри отбил его меч одним ударом."
    scene bg3 with sshake
    "И вырубил его рукоятью меча."
    nive "Сэр Джоффри!"
    "Молодой сквайр упал на землю, без сознания. Слишком много было хвастовства."
    harry "Я восхищаюсь его галантностью, правда. Но это его убьет."
    harry "Никогда не следует выбрасывать свою жизнь напрасно."
    "Его глаза вернулись к благородной женщине."
    harry "Итак, леди Розали...."
    harry "Платье, если можно."
    scene black with fade
    scene bg31 with fade
    show rowan necklace happy at edgeright with dissolve
    show wild orc neutral at center with dissolve
    show orc soldier neutral at edgeleft with dissolve
    "Платье для Делейн. Изящные украшения. Немного золота. Прекрасная добыча, в целом."
    wo "Хех, это очень весело."
    os "Имя отстойное."
    wo "Да. Но мне оно не отвратительно."
    show rowan necklace neutral at edgeright with dissolve
    "Роуэн закатил глаза."
    ro "У вас у всех была возможность придумать что-нибудь. Все критики...."
    "Им повезло, что они не стали уродливыми."
    "И с тем, как все пошло наперекосяк, Роуэн сомневался, что кто-то сможет связать 'Ужасного Гарри и его отвратительных разбойников' с лагерем орков на севере Розарии."
    show rowan necklace happy at edgeright with dissolve
    "В общем, отличная работа."
    $ delane_gifts += 15
    $ change_base_stat('c', -3)   
    $ noblesHuntingSeen = True
    return


label summerResidence:

#wineryCG
scene black with fade
show rowan necklace neutral behind black

ro "Джекпот."

"Они с Краугом стояли на холме, откуда открывался вид на небольшую  резиденцию."
"Летнее убежище аристократа, в данный момент охраняемое лишь символическим гарнизоном."
"Все, что нужно, чтобы Делейн чувствовала себя комфортно прямо у них под носом."  

krau "Мы ударим в полночь. Будь готовым."

"Большую часть времени оркам не хватало дисциплины, чтобы держать рот на замке достаточно долго, чтобы не скомпрометировать свое положение."
"Но Улькро управлял крепким кораблем. Роуэн дал им несколько советов, но они и сами знали, как оставаться незамеченными."
"Наступила ночь, а местные стражники так ничего и не узнали об их присутствии."

if check_skill(6, 'move_silently')[0]:
    "Они нанесли быстрый и беспощадный удар, убив охранников и захватили резеденцию."
    if avatar.corruption > 50:
        "Роуэн приказал связать их и заковать в цепи. Замок Бладмин нужно больше рабов, и он знал, что Крауг и его люди следят за ним."
        "Даже если бы он захотел, он не смог бы проявить милосердие. Его поведение повлияло бы на то, что Улькро подумает о близнецах."
        $ change_prisoners(5)
    else:
        "Роуэн приказал освободить их. Охота на рабов не была их целью. Он увидел, что Крауг прищурился, но ему было все равно."
        $ change_base_stat('g', -3)   
        "Как они и ожидали, резиденция была богата высококачественными предметами. Не было дорогих вещей – не было ни украшений, ни редких книг, ни картин."
        "Но в резиденции были хорошо сделанные столовые приборы, ткани, которые можно было использовать для вышивания, и прекрасная коллекция вин." 
        "Мелочи, которые делали жизнь комфортной, на которые дворяне никогда не обращали внимания, пока их не забирали у них."
        "Делейн, несомненно, будет рада увидеть, как ее уровень жизни хотя бы частично поднимется."
        $ delane_gifts += 15
        $ summerResidenceSeen = True
        return
        
else:
    "По крайней мере, так они думали."
    "Они били безжалостно, но стражники были готовы к этому. Двое воинов Улькро упали от первого залпа стрел, еще один-от второго. Недостаточно, чтобы остановить их. Не так уж и много."
    "И защитники знали это слишком хорошо."
    krau "Нет!"
    "Роуэн не знал, было ли то, что последовало за этим, тем, что владелец резиденции сказал им делать в подобных случаях, или защитники сделали это назло."
    "Не желая, чтобы резиденция была разграблена, они подожгли здание."
    krau "Не дайте никому сбежать! Я хочу их видеть смерть их всех!"
    "Роуэн мог только громко выругаться, наблюдая, как огонь разгорается все сильнее. Теперь уже не было никакой возможности спасти деревянное здание." 
    "Орки быстро захватили убегающий гарнизон и предали их всех мечу, но он не нашел в этом утешения. Их набег не удался." 
    "Утром они будут рыться в развалинах и грабить то, что еще чего-то стоит. В основном столовые приборы."
    "Это было не то, чего ожидал Роуэн, но, по крайней мере, хоть что-то."
    $ delane_gifts += 5
    $ summerResidenceSeen = True
    return






    