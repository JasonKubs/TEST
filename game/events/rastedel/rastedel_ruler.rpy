init python:
    
    event('rastedel_performance_review', triggers='week_end', conditions=('rastAllyChosen == True',), run_count=1, priority=pr_story)


label rastedel_performance_review:

$ rastPerformanceReview = True
$ rastActFour = True

scene bg18 with fade

show rowan necklace neutral at edgeleft with dissolve
show jezera happy at midleft with dissolve
show andras displeased at midright with dissolve

#if orciad is complete
show tarish neutral at edgeright with dissolve

#TODO - if goblin quest is complete, show goblin rep

"Роуэн вошел в комнату Изеры немного опаздав. Другие слуги уже были там, ожидая его за столом."
"Половина съеденной жареной свиньи стояла в центре. Большую часть которой ел Андрас."

je "Похоже, что наша критика в адрес нашего общего друга была немного преждевременной."
je "Она продемонстрировала достойное похвалы понимание политических рычагов влияния и способов их использования."

"Роуэн отметил, что он слышал критику в адрес Амерейны только от нее."
"Он остановился перед своим креслом, положив на спинку руки, вместо того, чтобы сесть."

ro "Она была очень полезной. С ее помощью я обеспечил важную позицию в городе для борьбы с этим злом."

"Андраш плюнул на тарелку перед собой, затем потянулся до жаркого за другой порцией."

an "Слишком много маскировки. Ожидание на обочине скучно мне."

if raeveKeepCapture == "assault":
    an "В Рэйве мы бросились к воротам. Захватили их врасплох и заставили истечь кровью. То же самое и с Астартой. "
    show jezera displeased at midleft with dissolve
    je "Ты взял Астарту без ведома."

else:
    an "Козни в Рэйве. Прокрадываться сюда. Если бы ты мог победить в Астарте, тайком прокравшись, ты бы победил."
    show jezera displeased at midleft with dissolve
    je "Ты получил знания об Астарте из-за того, что я тайком прокралась. Прояви уважение."
    
"Андрас  закатил глаза."

an "Вопрос остается открытым. Тебе повезло, что Растедель так хорошо защищен."
an "Если бы у меня было хоть чуть-чуть больше душ, я бы уже был во дворце, пил гребаное вино барона."

"Пока он говорил, горничная с опущенными глазами наливала еще вина в пустой бокал, и позволяла ему лапать свой зад."
"Роуэн видел, как она выполняла некоторые поручения Изеры раньше. Один из ее домашних животных, без сомнения."

#TODO - if goblin quest is complete

#if orciad is complete
"Тариш, которая сидела с тарелкой чуть менее заполненой, чем у Андраса, открыла рот следующей."

tar "Но ты же не можешь этого сделать, не так ли? Не трать свое племя на то, чтобы доказать что ты лучше всех, покажи лучше, какой у тебя большой член."

show jezera neutral at midleft with dissolve

ro "Мы ведь не поэтому собрались здесь сегодня, не так ли?"

"Андрас разозлился, и холодные жесткие факты надвигающегося конфликта Роуэн понял лучше всех."
"Перспектива кровопролития от Андраса не была особенно смешной. Не после его последнего показа...."

ro "Вы хотели обсудить мой выбор в союзниках, верно?"

if rastAlly == "jacques":
    "Изера вздохнула."
    je "Ты выбрал... интересную... фракцию, чтобы связать свою судьбу. Полагаю, у тебя есть объяснение своему выбору."
    "Роуэн кивнул."
    ro "Нам нужен союзник, который мог бы взять власть в свои руки, но не был бы привязан к той системе, которая существует в настоящее время."
    ro "Вердена и Марианну не удалось бы убедить играть в мяч, Патрисии не хватает своего округа, барон не может привести собаку на поводке."
    ro "Жак умен, но и прагматичен. Я считаю, что если мы устроим переговоры с ним дав ему силы, то он придет к соглашению."
    "Роуэн был достаточно уверен, что сможет убедить Изеру принять его выбор."
    "Это не то, что предложила Амерайн, но Изера не чужда прагматичному компромиссу. Настоящей проблемой было бы..."
    show andras smirk at midright with dissolve
    an "Договоренность с позиции слабости, да? Интересно, говоришь ли ты там о личном опыте?"
    show andras angry at midright with dissolve
    "Андрас откинулся назад и зарычал."
    an "Не думай, что я идиот, человек. Ты правда думаешь, что твое истинное намерение ускользает от меня?"
    an "Ты пытаешься думать, как выбраться из боя, не так ли? Ты же не хочешь, чтобы твои глупые человеческие хижины были уничтожены, когда я приду туда."
    an "Мы с тобой оба прекрасно знаем, что мне не нужна сделка."
    an "Если они будут все еще сражатся друг с другом, когда появится моя армия, это будет такая же победа для меня."
    show rowan necklace concerned at edgeleft with dissolve
    "Роуэн бессознательно поставил ногу назад и крепче схватил стул."
    ro "Я искренне думаю, что Жак - наш естественный союзник среди тех, кто может разумно взять власть в свои руки. Конечно, ты видишь преимущество и в этом."
    show rowan necklace neutral at edgeleft with dissolve
    if society_type == "might":
        ro "Жак был бы естественным лидером людей, если бы они нарушили слово Солансии. Ты видишь, что он идеальный союзник?"
    #if goblin quest
    #He turned to (Goblin Representation)
    #if orciad
    "Он обратился к Тариш."
    ro "Могу представить, что только ты понимаешь мою мудрость?"
    if orciad_ally == "tarish":
        "Тариш кивнула головой с нетерпением, не упуская шанса."
        tar "Все да портится, и никто не потерял солдат. Если ты можешь выиграть так, зачем делать это по-другому? В Роуэна есть немного старой змеи. Орки поддерживают его."
        show jezera happy at midleft with dissolve
        "Изера кивнула головой в ответ на слова Тариш. Андрас, тем временем, огляделся, ищя союзника, но не нашел его."
    elif orciad_ally == "batri":
        "Тариш обдумала эту идею. Комната ждала ее ответа. Ведь без Батри любое нападение на город было бы ошибкой."
        tar "Достаточно сказать, что Батри скажет наверняка. Если бы мы поймали людей без боя, это могло бы стать скучным для скучающих воинов."
        tar "Но если ты сможешь выиграть, отправив всех его орков в мертвое логово, ты не услышишь от него никаких криков."
        "Роуэн повернулся к Андрасу. Это был не столь хороший ответ, как он хотел, но он все равно представлял собой согласие орков на его план."
    elif orciad_ally == "ulcro":
        "Тариш обдумала эту идею. Комната ждала ее ответа. В конце концов, без Улькро, любое нападение на город было бы ошибкой."
        tar "Достаточно сказать, что Улькро скажет наверняка. Если бы мы поймали людей без боя, это могло бы стать скучным для скучающих воинов."
        tar "Но если ты сможешь выиграть, отправив всех его орков в мертвое логово, ты не услышишь от него никаких криков."
        "Роуэн повернулся к Андрасу. Это был не столь хороший ответ, как он хотел, но он все равно представлял собой согласие орков на его план."
    else:
        "Тариш зарычала."
        tar "Что это за бардак? Хуми нуждается в помощи мамы?"
        "Она вздохнула, кинув хмурый взгляд. Роуэн всегда мог рассчитывать на то, что ее практичность побьет ее презрение."
        tar "Правда есть правда. У нас не миллион солдат-орков. Если, Хуми думает, что мы сможем взять Да-Сити, поговорив, стоит попробовать. Если он не может, мы просто попробуем мечи и щиты."
        "Андрас поцарапал подбородок."
    show andras displeased at midright with dissolve
    an "Вот как вы все реально думаете, да?  Хорошо. Поставь крысу во главе. Постарайся заключить сделку."
    show andras smirk at midright with dissolve
    "Он мрачно улыбнулся, показав зубы."
    an "Но если это не сработает, мы сделаем это по-моему. Слышишь меня, мальчик?"
    if avatar.corruption < 60:
        "Роуэн заерзал. Он играл здесь в азартную игру. Единственная надежда заключалась в том, что он поставил на правильного чемпиона."
    ro "Я понимаю."
    je "Тогда, похоже, мы все согласны. Выбор Роуэна приемлем."
    "Она похлопала в ладоши, как будто предлагая урегулировать этот вопрос."
    
elif rastAlly == "werden":
    "Андрас осушил кубок за один приём. Молчаливая горничная поспешила наполнить его напитком."
    show andras happy at midright with dissolve
    an "На моем месте, ты бы уже убил его. Но на моем месте многое бы изменилось, да?"
    show andras angry at midright with dissolve
    an "Так какого хрена ты делаешь?"
    show jezera happy at midleft with dissolve
    "Изера улыбнулась тихо, но это была паутинная улыбка. Плохой знак."
    je "Впервые брат и сестра согласны. Твой выбор сбивает с толку. В коммюнике от нашей общей подруги и она казалась совершенно ошеломленной."
    "Андрас переменил свою позу, положив одну ногу на другую."
    an "Ну, мальчик. Продолжай. Скажи нам, почему бы нам не назвать это предательством прямо здесь и сейчас."
    #TODO - if goblin quest
    #if orciad
    "Тариш поддалась в своем кресле вперёд. Она не могла скрыть своего интереса к разбирательству."
    "Она проявила немного нерешительности, к проявлению враждебности по отношению к предмету перекрестного допроса."
    show rowan necklace angry at edgeleft with dissolve
    ro "По той же причине, по которой я объяснил нашему общему другу. Верден - ублюдок. Чисто и просто. Возможно, ни один настоящий ублюдок никогда не жил..."
    show andras smirk at midright with dissolve
    "Андрас фыркнул."
    an "Должен ли я принять это как вызов?"
    show rowan necklace neutral at edgeleft with dissolve
    ro "Но он также является невероятно разрушительным человеком. Крестьяне никогда его не примут. Протестантские первосвященники не примут его."
    ro "Но, он также является грозным лидером рыцарей. Ни один человек не обладает такой силой, чтобы раскачивать город так сильно, как он."
    ro "На самом деле, я не на его стороне. Я делаю все, что в моих силах, чтобы он проиграл."
    "Изера слегка посмеялась, привлекая внимание других."
    je "Сколько раз ты практиковался чтоб это сказать? Разрушитель? Конечно. Но, к тому же, ревностный."
    je "Я никогда не встречалf этого человека, но истории доходили до моих ушей за эти годы. Так много маленьких историй."
    je "А теперь ты ходишь вокруг него, встречаешься с ним. Может быть, даже намекаешь на то, что он может выскользнуть..."
    "Изера подняла бровь."
    je "Нельзя удивляться моему беспокойству. В конце концов, ты действительно был самым преданным слугой в прошлом?"
    show rowan necklace concerned at edgeleft with dissolve
    "У Роуэна по спине пробежал холодок. Что она имела в виду под этим?"
    #if orciad complete
    tar "Так и было, Хамми? Хочешь воткнуть нам нож в спину?"
    show rowan necklace neutral at edgeleft with dissolve
    "Андрас, размахивая рукой раздавил ужин на столе. Он выпрямился в кресле и вытер немного красного вина с губ."
    show andras angry at midright with dissolve
    an "Ты слышал, что все остальные хотели сказать. Они. Не. Доверяют. Тебе. Ты. С. Верденем."
    an "И, ты знаешь меня. Всё это интригующее дерьмо - не для меня. Если моя сестра не доверяет тебе, значит, я тоже тебе не доверяю."
    an "So, you’re going to tell us right now. In this little plan of yours. What happens to Werden?"
    "Роуэн закрыл глаза. Было так много, что он мог сделать, чтобы убедить их. Он должен был что-то сказать здесь и сейчас. Алексия..."
    ro "Он умрет."
    "Он сделал паузу, чтобы перевести дух, после его слов. Стол смотрел на него с большим восторгом."
    ro "Когда он выполнит свою задачу и все случится так, как положено, я встречусь с ним один на один, а затем убью его."
    show andras smirk at midright with dissolve
    "Андрас улыбнулся той же паутинной улыбкой, что и Изера."
    an "Вот так, парень. Это было не так уж и сложно, да? Наверное, в тебе есть немного больше меня, чем я думал."
    if rowanAndrasSex > 0:
        "Он подмигнул Роуэну, который предположил, что это была преднамеренно."
    "Потребовалось немного больше времени, но с его заявлением о намерениях убить Вердена напряжение за столом чуть чуть спало."
    "Изера все еще обдумывала, но Роуэн никогда не ожидал купить ее на эту идею. Она не была особенно доверчивой женщиной."
    
else:
    show jezera happy at midleft with dissolve
    je "Действительно. Я была рада услышать, что ты согласился с рекомендацией нашего общего друга. "
    "Изера подняла золотую ложку и повернула ее перед собой."
    je "Ты веришь, что он может быть испорчен с нашей точки зрения?"
    "Роуэн кивнул головой. Он не очень волновался, когда услышал, что Изера хотела эту встречу."
    "В конце концов, он выбрал союзника, который, скорее всего, доставит ей удовольствие."
    ro "Да. Она разочарована своим положением и жаждет большего."
    ro "Если мы сможем убедить ее в том, что, действуя бок о бок с нами, она получит то, что хочет, то ее можно обратить."
    if avatar.corruption < 31:
        show rowan necklace concerned at edgeleft with dissolve
        "Рука Роуэна немного сжалась. Это была неприятная тема для разговора...."
    else:
        show rowan necklace happy at edgeleft with dissolve
        "Роуэн дал Изере мрачную улыбку."
        ro "Вы научили меня госпожа, что у каждого есть своя цена."
        "Изера посмеялась  и выпила из своего бокала достаточно много напитка, чтобы соответствовать своему брату."
        je "Должна ли я гордиться или бояться?"
    show rowan necklace neutral at edgeleft with dissolve
    an "Итак, мальчик, как ты собираешься это сделать? Надеюсь, ты не собираешься просто подойти к этой суке и расказать наши планы."
    je "Отличная мысль, дорогой брат. Существует ряд подходов, которые необходимо использовать. Ты хочешь подогреть ее амбиции, да?"
    if orciad_ally == "batri":
        je "Возможно, нанять шпиона, замаскированного под тебя.... В прошлый раз это сработало неплохо. Хотя, может быть, это будет слишком сложно...."
        "Изера замолчала, несомненно, несколько конкурирующих идей уже сформировались в ее мозгу."
    ro "По правде говоря, я пока не совсем уверен. Моя нынешняя идея - просто стать ближе к ней и найти чего она хочет. Или слабость."
    "Он на секунду замолчал."
    ro "Хотя, конечно, если у вас есть совет, я с удовольствием им воспользуюсь. Я новичок, когда дело доходит до таких усилий."
    "Прежде чем Андрас смог ответить, Изера щелкнула пальцами и взволнованно захихикала."
    je "Конечно! Подожди секунду, у меня тут кое-что есть."
    "Изера бросилась к шкафу рядом с кроватью. За ней последовали глаза всех, кто сидел за столом. Она открыла его жестом руки и быстрой вспышкой синего света."
    "Потом она вернулась, держа в руках шкатулку с драгоценностями."
    ro "Что это?"
    je "Помощь для операции. Когда носишь, то получается ритуал. Что-то вроде привязанности души. Наш общий друг знает, как это работает."
    je "Но если консультант его наденет, это свяжет ее с нами и обеспечит полную лояльность. Очень полезный инструмент для подрывной деятельности в городе."
    "Роуэн поднял коробку."
    ro "У тебя есть очарование, чтобы обеспечить лояльность...?"
    "Изера хихикала и опустилась обратно в кресло."
    je "Интересно, почему ты его не носишь, а?"
    "По правде говоря, Роуэн задавался вопросом о возможности того, что его собственный разум несколько раз контролировался."
    "Но, если бы он находился под контролем, было бы невозможно выяснить, а если бы он не был тогда невозможно опровергнуть. Он бы никогда не узнал так или иначе."
    "Все это было естественным соображением, когда заставляли работать на демонов."
    je "Увы, такая безделушка, хотя иногда и весьма ценна, но имеет ограниченную применимость."
    je "Сложно производить, и для этого нужна душа в состоянии хотя бы частичной готовности."
    je "Вторая проблема заключается в воздействии на пользователя. Если вашим желанием является послушание и испорченность, то это прекрасный инструмент."
    je "Однако она менее эффективна для поддержания дееспособных подчиненных в долгосрочной перспективе. Хорошо для губернаторов, плохо для генералов."
    je "Это обмен волшебство на ум, к сожалению."
    show rowan necklace concerned at edgeleft with dissolve
    "Роуэн посмотрел на коробку. Он стал тяжелее, хоть и не прибавил в весе."
    je "Отдайте его нашей общей подруге как настанет время обеспечить ее лояльность. Его использование не так уж и сложно, но она понимает очарование лучше, чем ты."
    je "Просто будь в комнате, когда она использует его. Она должна будет назвать имя того, кому надо служить."
    je "Если она скажет имя, отличное от имени моего или моего брата, я буду зла. Ты должен убедиться, что она верна своему слову."
    if avatar.corruption < 31:
        "“Поддержание дееспособных подчиненных”. Эта фраза застряла в голове Роуэна. Неважно, что имела в виду Изера, это было нехорошо. Она собирается сделать что-то ужасное с этой женщиной?"
        "...У него был выбор?"
    else:
        "Свержение коррумпированной розарианской системы было одной вещью. Другое обидеть людей. Было уже слишком поздно отступать."
        "Но это означало, что с женщиной случится что-то плохое. Что было неясно."
    show rowan necklace neutral at edgeleft with dissolve
    ro "Я прослежу, чтобы это было сделано."
    "Изера обратилась к остальным."
    je "Надеюсь, эта идея не вызывает возражений с остальной части стола?"
    "Андрас откусил ветчину и ответил с едой во рту."
    an "Нет. Мне в основном интересно, как она выглядит. Она привлекательна?"
    ro "Это зависит от того, что ты думаешь о пожилых женщинах."
    "Андрас поперхнулся."
    an "Кхе. Я сам посмотрю, что будет после того, как дело будет сделано."
    #if orciad
    "Тариш зевнула."
    tar "Как хочешь. Если весь твой яммерин означает меньше мертвых орков, я тебя не остановлю."
    "Изера хлопнула в знак признательности."
    je "Похоже, стол в согласии, маленький герой. У тебя есть овечка, чтобы подчинить ее."
    
show rowan necklace neutral at edgeleft with dissolve
show jezera neutral at midleft with dissolve
show andras displeased at midright with dissolve

"Когда дела, казалось бы, были закончены и остальные стали подниматься со стульев. Роуэн, сказал."
    
ro "Есть еще кое-что, о чем я хотел поговорить, пока мы здесь."

if avatar.corruption < 60:
    ro "Если план будет успешным и армия придет к выводу, что город уже не в состоянии защитить себя, что вы планируете делать после победы?"
    je "Стратегически? Ну, это зависит от того..."
    ro "Нет. Я имею в виду, для жителей города. Что с ними будет?"
    show andras smirk at midright with dissolve
    "Андраш засмеялся."
    an "Интересно, отпущу ли я своих солдат с поводка?"
    show rowan necklace concerned at edgeleft with dissolve
    "Роуэн застыл на месте. Он не хотел быть столь откровенным в этом вопросе, но, было трудно не заметить намерения заданного им вопроса."
    ro "Что-то вроде этого."
    "Андрас повернулся к своей сестре."
    an "Что скажешь? Пустая столица была бы неплоха, не так ли?"
    show jezera displeased at midleft with dissolve
    "Изера закатила глаза. На нее, по крайней мере, можно было рассчитывать, когда речь шла о том, чтобы не убивать людей на улицах без причины."
    je "Ну же, милый герой. Ты не можешь же поверить, что наши войска просто войдут в Растдейль, и мы все вместе поужинаем. "
    je "Война не так работает."
    je "Уверена, ты из первых рук сможешь рассказать, какие прекрасные вещи делались с захваченными солдатами и поселениями под знаменем моего отца."
    show rowan necklace neutral at edgeleft with dissolve
    "Роуэн держался. Если и было место, где он не должен был отступать, то это здесь."
    ro "Не все победы похожи. Например, иногда под игом можно найти и освободить великую силу."
    ro "Иногда... меньше."
    "Он не мог не взглянуть на Андраса, после этих слов. Естественно, Андраса это не очень беспокоило."
    an "Оу, все еще плачешь по моему веселью после последней битвы?"
    an "Я всегда могу дать тебе еще повод немного поплакать."
    "Изера встала с кресла и подняла руки вверх, останавливая их."
    je "Роуэн, не ссорся с Андрасом. Ты не настолько глуп."
    je "Это не тебе решать. Ты приведёшь город в наши объятия любви. То, что случится после этого, не твое дело."
    je "Ты понимаешь, что получаешь за свои услуги."
    show rowan necklace concerned at edgeleft with dissolve
    "Она указала на амулет на его шее. Роуэн опустил голову. Он рисковал многим здесь...."
    show rowan necklace neutral at edgeleft with dissolve
    ro "Я не могу стоять здесь. Я должен знать твой ответ."
    ro "Это единственная битва, которую я не могу обойти стороной. Я должен знать, что вы планируете сделать с Растеделем и его людьми, когда битва закончится."
    show andras angry at midright with dissolve
    "Андрас наклонился в сторону в кресле, просто глядя на Роуэна. Комната вновь опогрузилась в тихую напряженность."
    an "..."
    ro "..."
    an "Хммм."
    show andras displeased at midright with dissolve
    an "Хорошо."
    an "Если ты отдашь город в мои руки без какого-либо реального сопротивления, то я воздержусь от его разрушения."
    an "Уничтожить его очень плохо. Орков довольно сложно контролировать, когда их кровь вскипает."
    "Изера застонала."
    je "Вот, у тебя есть дар, Роуэн. Тебе есть что сказать?"
    "Роуэн покачал головой. У него сердце билось в груди, но он сделал это. Андрас согласился ограничить себя."
    ro "Нет. Это все, что меня действительно волновало."
    "Он дал глубокий поклон."
    ro "Хозяин. Госпожа."
    #if goblins TODO
    #if orciad
    ro "Леди Тариш."
    "Он повернулся, чтобы выйти из комнаты, но был остановлен голосом, обращенный к нему. Грубый тон Андраса."
    show andras angry at midright with dissolve
    an "Это не стандартное одолжение, мальчик. Это целый город. Ты можешь просить что-нибудь подобное один раз, слышишь меня? Один раз"
    ro "Я понимаю."
    scene bg14 with fade
    show rowan necklace concerned at midleft with dissolve
    "Когда он уезжал, мысли о том, что он сделал, все еще бились в его по мозгу. Если бы Андрас этого не сделал, как бы сильно он настаивал?"
    "Он бы умер за это? Он бы позволил Алексии умереть за это?"
    ro "..."
    ro "Герой Розарии."
    show rowan necklace happy at midleft with dissolve
    ro "Хех."
    return
    
else:
    ro "У нас должен быть план, как обойтись с городом Растедель, как только он окажется в ваших руках."
    "Изера слегка наклонила голову."
    je "Объясните мне."
    ro "Я имею в виду, когда город падет. Что будет с людьми, живущими там? Что будет со зданиями?"
    show andras smirk at midright with dissolve
    "Андрас засмеялся."
    an "Он хочет знать, планируем ли мы уничтожить этот проклятый город до основания и помочиться на его пепел."
    ro "Что-то вроде этого."
    "Этот вопрос беспокоил его. Жертвы войны неизбежны. В конце концов, какая разница между несколькими мертвыми крестьянами?"
    "Тем не менее, было что-то, что заставило его беспокоиться о полном разрушении города. Ненависть к напрасной трате ресурсов?"
    "Может быть, немного героического порока, который все еще бродит по нему с прошлых лет?"
    ro "Мне нужен план. Мы должны быть уверены, что не уничтожим город и не убьем слишком много людей."
    an "Почему? Какая разница, отдам ли я мечу весь город?"
    show rowan necklace angry at edgeleft with dissolve
    ro "Потому что это самый ценный опорный пункт в регионе, и в нем больше рекрутов и больше производственного потенциала, чем где-либо еще под вашим знаменем."
    ro "Будет ли еще война, после Растеделя или нет."
    an "А еще больше там бесполезных ртов."
    "Он слегка покачивался, как будто они на дуэли. Для Андраса это была почти игра."
    ro "Вы думаете, что посреди общего разбоя, ты сможешь уследить за тем, кого убили?"
    ro "В розарской армии, мы так и не смогли сохранить дисциплину, когда врывались в поселение. А это была более упорядоченная армия, чем та, что у нас есть."
    "Андрас прислонился к стулу."
    an "Тогда, может быть, вообще не грабить город. Подождать несколько дней. Построить всех в очередь и спросить об их работе. Это должно решить проблему, не так ли?"
    show jezera displeased at midleft with dissolve
    je "Андрас, ты собираешься играть с ним весь день?"
    an "Я получаю удовольствие."
    "Она вздохнула и положила руки на голову."
    je "Мы услышали твой совет, Роуэн."
    je "Если ты действительно считаешь нецелесообразным сжигать город после того, как мы его возьмем, то мы примем во внимание твой совет."
    show rowan necklace neutral at edgeleft with dissolve
    "Роуэн дал глубокий поклон."
    ro "Спасибо, что выслушали его. Вы очень щедры."
    "Изера отмахнулась от него."
    je "Да, да, да. Великолепно. Невероятно. Все эти вещи. Собрание закрыто."
    scene bg14 with fade
    show rowan necklace happy at midleft with dissolve
    "Когда Роуэн вернулся в свои покои, он тихо засмеялся. Как будто в воздухе была шутка, и никто не мог ее услышать, кроме него."
    ro "Хех."
    ro "Герой Розарии..."
    return



