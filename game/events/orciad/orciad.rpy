init python:

    #Introduction
    #Triggered when Rowan enters the orc warband camp in Northern Rosaria for the first time.
    event('orciad_introduction', triggers='map_res_105', run_count=1, group='orciad_camp', priority=pr_map_res)
    #Camp Menu
    #should show after the intro, and every time on entering the camp after
    event('campMenu', triggers='map_res_105', conditions=("week >= 4",), depends=('orciad_introduction',), group='orciad_camp', priority=pr_map_res)





label orciad_introduction:
#Introduction
#Triggered when Rowan enters the orc warband camp in Northern Rosaria for the first time.

#orc warband CG
scene black with fade
show rowan necklace shock behind black
show andras displeased behind black

ro "Ого!"

"Спрятавшись среди деревьев и скал, выходящих на одну из многочисленных небольших долин, ответвляющихся от главной Розарианской долины, Роуэн обнаружил нечто, похожее на огромный отряд орков!"
"Он наблюдал, как несколько тысяч солдат орков толпились вокруг грубых палаток и костров. Отчет Бладмину нужно было отправить немедленно."

#fade to black and back

"Пока он ждал, он понял, что между орками, похоже, существует пропасть. То, что сначала казалось одним лагерем, на самом деле было двумя, с очевидным разрывом между ними."
"Время от времени вдоль линии границы вспыхивали бои, и человек мог видеть по крайней мере два трупа, оставшихся от предыдущих стычек."

an "Ну вот, это не обычное зрелище."

show rowan necklace neutral behind black

ro "Рад, что ты смог присоединиться ко мне, мастер."

"Человек, которого ждал Роуэн, присоединился к нему в его укрытии и наблюдал за большим лагерем внизу."
"Эта армия, которую они обнаружили, представляла бы большую ценность для Бладмина, но ее размер означал, что привести ее в лоно будет гораздо труднее, чем более мелкие племена."

if goblinRecruit == False:
    "Однако Великая армия была именно тем, что Близнецы хотели, чтобы Роуэн нашел, и он нашел ее."
    "У Андраса определенно был блеск в глазах, свидетельствовавший о том, что он тоже весьма доволен этим открытием."
    an "Кажется, ты нашел альтернативу гоблинам, отлично. Орки гораздо сильнее и жестче, чем эти маленькие слабаки."
else:
    an "Еще одна армия?  Ну, иметь две, конечно, было бы неплохо, предполагая, что ты можешь заставить их следовать за нами."
    an "Не трать свое время зря, я бы не хотел упустить что-то жизненно важное, пока ты пытаешся заставить меня целоватся с  армией орков."

"Он на мгновение опустил взгляд на лагерь, прежде чем продолжить."

an "Теперь я понимаю, почему ты не хотел, чтобы я сделал грандиозный выход. Каков твой план, слуга?"

ro "Я считаю, что первым шагом должно быть встретиться с их лидерами, выяснить, почему они здесь, и уйти оттуда."

"Роуэн на мгновение заколебался, обдумывая свои слова."

ro "Я бы и сам сделал, но быть человеком означает, что мне будет небезопасно идти одному."

"Полу-демон посмотрел на долину, с задумчивым взглядом, прежде чем ответить."

an "Я прощу тебе использование меня в качестве дипломатического щита, если ты сможешь раздобыть мне новую армию орков."

"Мужчина коснулся пальцами своего амулета и ответил"

ro "Да, хозяин."

scene bg26 with fade
show rowan necklace neutral at midleft with moveinleft
show andras displeased at edgeleft with moveinleft

"Даже когда они приблизились к лагерю, было очевидно, что дисциплина давно исчезла, если она вообще когда-либо существовала."
"Они не заметили ни разведывательных патрулей, ни даже охранников на краю лагеря."
"Пока они вдвоем шли через палатки, несколько орков подняли головы, но никто не сделал движения, чтобы остановиться или хотя бы заговорить с незваными гостями."

show tarish neutral at midright with moveinright

"Первый признак какого-либо порядка появился, когда небольшая группа женщин-орков догнала Роуэна и Андраса сзади, и их лидер обратился к демону."

tar "Босс демон, что привело тебя в лагерь орков?"

"Андрас вопросительно посмотрел на Роуэна, спрашивая, стоит ли ему говорить или нет."

menu:
    "Пусть Андрас сам решает.":
        $ released_fix_rollback()
        "Роуэн слегка наклонил голову и ждал, когда хозяин заговорит."
        #if player chose might society
        if society_type == 'might':
            an "Я-Андрас, повелитель Бладмина, и я пришел, чтобы заявить права на эту армию, как и положено мне. Почему ты остановила меня, женщина?"
        #else
        else:
            an "Я-Андрас, император Бладмина, и я пришел заявить права на эту армию, как и положено мне. Почему ты остановила меня, женщина?"
        #rejoin
        "Глаза орка расширились от шока при этом открытии, затем она быстро оглядела палатки, чтобы увидеть, обратил ли кто-нибудь внимание на то, что только что было сказано."
        tar "ТСС! Не говори так громко."
        "Она помахала рукой своим спутницам, которые разбежались и начали более тщательно осматривать окрестности. Андрас озадаченно смотрел на нее."
        "Роуэн решил, что ему лучше пока взять инициативу в свои руки, похоже дело принимало неожиданный оборот."
        ro "Почему? Есть ли здесь предательство или ненависть к повелителям демонов?"
        tar "Нет, здесь другая проблема. Пойдемте, поговорим наедине."

    "Говори от имени Андраса, утверждая, что ищешь солдат для новой армии.":
        $ released_fix_rollback()
        ro "Мой хозяин пришел в поисках солдат для своей армии. Ваши цифры заинтриговали его, Хотя я вижу, что вам не хватает дисциплины."
        tar "Вы хотите, чтобы орки сражались за вас? Я могла бы помочь с этим."
        "Она помахала своим спутницам, чтобы они выстроились вокруг них. Андрас посмотрел на них со смесью смущения и раздражения на лице."
        ro "Как именно ты собираешься это сделать?"

    "Говорите от имени Андраса, утверждая, что ищете лидера этой группы.":
        $ released_fix_rollback()
        ro "Мой хозяин пришел поговорить с лидером этой группы. Если вы не командуете ими, то в ваших интересах сообщить нам, где мы можем его найти."
        tar "Есть два начальника. Борьба за красивую девушку. Очень плохое дело. Надо поговорить со мной, прежде чем ты встретишься с ними."
        ro "Да? Это будет что-то, что вы не можете сказать нам здесь?"
        "Она махнула своим спутникам, чтобы они встали вокруг них. Андрас посмотрел на них со смесью смущения и раздражения на лице."
        tar "Могу пообещать хорошие разговоры боссу демона."

    "Говорите от имени Андраса, скажите, что вы намерены выяснить, откуда взялась группа.":
        $ released_fix_rollback()
        ro "Мой учитель пришел, чтобы выяснить происхождение этой группы и почему вы, просто сидите здесь."
        ro "Почему вы сражаетесь между собой вместо того, чтобы нападать на людей?"
        tar "Был набег на Пинкс, потом большой орк нашел симпатичную даму и не поделился."
        ro "Поделится ею?"
        tar "Да, пойдемте, можете сказать больше подальше от этого места."
        "Она махнула своим спутникам, чтобы они встали вокруг них. Андрас посмотрел на них со смесью смущения и раздражения на лице."
        ro "Неужели это большой секрет?"

"Женщина-орк махнула им, чтобы они следовали за ней, и направилась в другую часть лагеря."

hide tarish with moveoutright

"Полудемон повернулся к своему спутнику с насмешливым выражением лица."
"Роуэн только пожал плечами, женщина-орк не дала ему ничего, чтобы уйти, и он сомневался, что она может причинить им много неприятностей, так что не было ничего плохого, чтобы последовать за ней."
"Андрас принял решение и последовал за женщиной-орком, Роуэн послушно потрусил за ним."

hide rowan with moveoutright
hide andras with moveoutright

scene black with fade
scene bg26 with fade
show tarish neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve
show andras displeased at edgeleft with dissolve

"Очевидно, эта женщина занимала довольно высокое положение в оркской иерархии, у нее был свой собственный, хотя и гораздо меньший, чем у двух других, лагерь, который Роуэн незаметил раньше."
"Она привела их сюда и теперь сидела с ними наедине, с хорошо приготовленным жареным поросенком между ними."
"В то время как Роуэн не решался пробывать оркскую кухню, Андрас не испытывал такой проблемы и съел большую часть жаркого целиком."
"У него было выше по званию, чем у женщина-орка, но она, в отличии рт него ела только мясо."

ro "Ну, я думаю, вам лучше рассказать нам, почему вы хотели встретиться с нами здесь."

an "Да, с вашей стороны было довольно самонадеянно настаивать, чтобы мы следовали за вами. Чего хочет от правителя Бладмина женщина-орк с некоторым положением, но не истинным лидерством?"

"Она некоторое время ковыряла в зубах, прежде чем ответить.  Роуэн сразу же заметил тик, если он не ошибся, похоже, она нервничала."

tar "Ам Тариш, воин сокровищницы Улькро. Это то, что осталось от сокровищ Улькро после войны."

"Она широко развела руками, имея в виду лагерь, который находился снаружи."

tar "Мы бежим на север, от розовых которые ездят верхом на зверях и прикрываются тяжелыми доспехами."

ro "Легионы Протеи."

"Андрас кивнул."

tar "Месяц назад воин Батри вернулся из рейда с очень красивой розовой девушкой в красивом платье. Улькро забрал ее, разозлил Батри."
tar "Он бросил вызов за правление, но Улькро не будет бороться с ним. Лагерь разделился надвое. Теперь мы сидим здесь и ждем, когда розовые прийдут и убьют нас."

an "Все из-за женщины?"

tar "Парни тупые, думают членами. Если бы они оба ушли, я бы стал шефом орды, сделав красивую девушку общей шлюхой, как должны были бы быть розовые девушки."
tar "Подпустите моих девочек поближе к Батри и Улькро, дайте мне да розовую девушку, и мы будем убивать любого."
tar "Мы снова пойдем в рейд и сделаем любую работу для босса."

scene black with fade
scene bg26 with fade
show rowan necklace neutral at midleft with dissolve
show andras displeased at edgeleft with dissolve

"Час спустя..."

an "Даже оркские женщины - заговорщики.... Что ты думаешь об этом?"

ro "Ну, Улькро был очень успешным генералом во время войны, было бы в наших интересах завербовать его, если бы мы могли."
ro "Однако, судя по тому, что я слышал от других присутствующих здесь женщин, Батри также весьма искусен и имеет преимущество в молодости."

an "Не поклонник плана Тариш убить их обоих?"

ro "Это не кажется очень.... орков? Это больше похоже на то, что придумала бы твоя сестра."
ro "Тариш-трусиха, она не стала бы драться с Ультро и Батри за место вождя, вот почему она хочет, чтобы мы сделали за нее грязную работу. Это не совсем  по оркски."

an "Есть ли хоть какая-то причина, по которой мы должны рассмотреть ее предложение?"

ro "Она будет у нас в долгу, и мы сможем использовать ее всю оставшуюся жизнь. К тому же, получить вождя орков в подчинение довольно редко."
ro "Я просто не уверен, что она стоит того, чтобы отказаться от двух других."
ro "Я должен поговорить с другими вождями и с той женщиной, которая им так нравится. Узнайте больше прежде, чем мы примем решение."
ro "Если ты убедишь Тариш дать мне свободный проход через лагерь, я смогу решить, каким должен быть наш выбор, а затем позаботиться об этом."

an "Ты уверен, что не надеешся спасти хорошенькую леди самостоятельно?"

ro "Получение орков для вашей армии - моя первая задача."

an "Ради твоего же блага, я надеюсь."

#Add Orc-iad quest to journal.  Add Orc-iad note1 to journal.
$ journal.start_quest('orciad')
$ journal.add_quest_note('orciad', 'note1')
$ orciad_state = 1
jump campMenu

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label campMenu:

if orciad_ban == True:
    scene bg26 with fade
    show rowan necklace neutral behind bg26
    ro "Мне следует избегать лагеря после последнего разговора с Батри."
    return
    
else:
    pass


if seen_delane_bad_end == True:
    jump delaneBadEnd2
    
else:
    pass


#Camp Menu
#should show after the intro, and every time on entering the camp after
$ prevent_tile_exploration()

if orciad_state != 2:

    if rowan_met_batri == 'met' and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.complete_quest_note('orciad', 'note1')

    if castle.buildings["brothel"].lvl == 0 and rowan_met_batri == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note10')

    if castle.buildings["brothel"].lvl >= 1:
        $ journal.complete_quest_note('orciad', 'note10')

    if castle.buildings["brothel"].lvl >= 1 and rowan_met_batri == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note11')

    if castle.buildings["brothel"].lvl >= 1 and rowan_met_batri == 'met' and met_with_delane == True and delane_corruption == True:
        $ journal.complete_quest_note('orciad', 'note11')
        
    if rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note14')

    if rowan_met_ulcro == 'met' and met_with_delane == True and ulcro_path == 3:
        $ journal.complete_quest_note('orciad', 'note14')

    if delane_gifts < 40 and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note15')
        
    if delane_gifts > 39 and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.complete_quest_note('orciad', 'note15')
        $ journal.complete_quest_note('orciad', 'note18')
        
    if delane_gifts > 39 and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note16')

    if delane_gifts > 39 and rowan_met_ulcro == 'met' and met_with_delane == True and ulcro_path == 3:
        $ journal.complete_quest_note('orciad', 'note16')

    if rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note17')

    if rowan_met_ulcro == 'met' and met_with_delane == True and cliohnaDelaneHelp == "got":
        $ journal.complete_quest_note('orciad', 'note17')

    if delane_gifts > 39 and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.complete_quest_note('orciad', 'note17')


    if met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note19')

    if delane_trust == 3:
        $ journal.complete_quest_note('orciad', 'note19')
        $ journal.add_quest_note('orciad', 'note20')
        
    if met_with_delane == True and delane_corruption == True:
        $ journal.complete_quest_note('orciad', 'note20')
        
    if tarish_path == True and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note21')
        $ journal.add_quest_note('orciad', 'note22')
        
    if got_jez_potion == True:
        $ journal.complete_quest_note('orciad', 'note21')
        
    if got_cla_poison == True:
        $ journal.complete_quest_note('orciad', 'note22')
        
    if met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note23')
        
    if delane_plan == True:
        $ journal.complete_quest_note('orciad', 'note23')
        
    if delane_corrupt == True and batri_power > 10:
        $ journal.add_quest_note('orciad', 'note26')
        
    if delane_status == "batri":
        $ journal.complete_quest_note('orciad', 'note26')
        
    if delane_trust == 3 and got_jez_potion == True and got_cla_poison == True:
        $ journal.add_quest_note('orciad', 'note29')
        
    if delane_status == "tent" and delane_plan == True and delaneDistraction == True and delane_trust > 2 and delaneEscapePerimeter > 0:
        $ journal.add_quest_note('orciad', 'note31')

scene bg26

menu:
    "Исследовать лагерь." if avatar.mp > 0:
        # (costs x movement point(s))
        # movement cost is applied in each event separately
        $ choose_and_insert_next_event('orciad_explore')
        $ orciad_explore += 1
        return
        
    "Отправлится в рейд." if (rowan_joined_batri_s_raiders == True) and (avatar.mp > 0):
        $ released_fix_rollback()
        $ change_mp(-5)
        $ batri_raid_count += 1
        jump orcRaid

    "Посетить Тариш, могущественную женщину-орка." if (tarish_angered == False) and (delane_status == "tent") and delane_corrupt == False:
        $ released_fix_rollback()
        jump visitTarish

    "Посетить Батри, соперника вождя." if delane_status == "tent":
        $ released_fix_rollback()
        $ choose_and_insert_next_event('orciad_batri')
        return

    "Посетить вождя Улькро." if delane_status == "tent" and delane_corrupt == False:
        $ released_fix_rollback()
        $ choose_and_insert_next_event('orciad_ulcro')
        return

    "Найти подарки для Делейн." if delane_status == "tent" and giftHuntAvailable == True:
        $ change_mp(-10)
        $ released_fix_rollback()
        jump hunt_for_gits
        
    
    #Sneak in to meet with [noblewoman/Lady Delane] (costs y movement point(s), can only attempt once each week)
    "Прокрасться на встречу с дворянкой" if (last_delane_visit_attempt < 1) and found_delane_tent and delane_status == "tent" and delane_corruption == False:
        $ released_fix_rollback()
        $ last_delane_visit_attempt += 1
        #Sneak in to meet with Lady Delane, the captured noblewoman
        #Selecting this option triggers a sneaking check (DC15), which Rowan can only attempt once per week.  There is no time cost to attempting this.  There should be some indication in game that tells the player they need to wait a week before trying to meet with Delane again.
        if check_skill(7, 'move_silently')[0]:
            #Success
            # TODO: not an event for now
            jump eleanorFirstVisit
        else:
            "Как ни старался Роуэн проскользнуть в темницу аристократки, он никак не мог пробраться мимо стражников."
            "Его попытка привлекла внимание охранников, так что ему придется подождать до следующей недели, чтобы попытаться снова."
            jump campMenu

    "Подчинить Делейн (требуется наличие шпиона)" if (rowan_met_batri) and (met_with_delane) and (delane_status == "tent") and delane_corruption == False:
        $ released_fix_rollback()
        if get_spies('idle'):
            jump corrupt_delane
        else:
            "Роуэн нуждается в доступном шпионе, чтобы сделать это."
            jump campMenu

    "Планировать спасение Делейн." if delane_status == "tent" and delane_trust == 3:
        $ released_fix_rollback()
        $ journal.complete_quest_note('orciad', 'note23')
        $ journal.add_quest_note('orciad', 'note24')
        $ journal.add_quest_note('orciad', 'note25')
        jump delaneRescuePlan
    
    "Покинуть лагерь орков.":
        #exit to map
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


#visit Tarish
label visitTarish:

if (met_with_delane == True) and (tarish_path == False):
    jump tarishQuest

elif (met_with_delane == True) and (tarish_path == True) and (get_cla_poison == False):
    jump tarishQuestReturn

elif (met_with_delane == True) and (tarish_path == True) and (get_jez_potion == False):
    jump tarishQuestReturn

elif (met_with_delane == True) and (got_jez_potion == True) and (got_jez_potion == True):
    jump tarishQuestComplete

else:
    pass


scene bg30 with fade
show rowan necklace neutral at midleft with dissolve
show tarish neutral at midright with dissolve

tar "Розовый демон."

ro "Тариш."

tar "Нам нужна хорошенькая розовая леди, прежде чем я стану шефом. Найди ее, заставь думать, что ты друг, и приведи сюда."
tar "Сделай все это, и я служу твоему Хозяину."

jump campMenu
