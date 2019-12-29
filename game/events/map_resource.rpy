# events for specific resources on map

init python:

    # tutorial village
    event('first_village_captured', triggers='map_res_100', run_count=1, priority=pr_map_res)
    # Tutorial Mine event
    event('tutorial_mine', triggers=('map_res_6', 'map_res_7', 'map_res_8',), run_count=1, only=True, priority=pr_story)


label first_village_captured:
#when Rowan discovers the first village
$ renpy.block_rollback()

#village outskirk CG

scene black with fade
show rowan necklace neutral at midleft with moveinleft

"Когда Роуэн приблизилась к деревне Бриарбридж, он глубоко вздохнул. Будучи ближайшим селом к Артдейлу, это место, где он был много раз."
"Он знал людей, он знал семьи, и теперь ...."
"Он коснулся следящего медальона так, как ему было приказано связаться с Андрасом."

ro "Я в деревне, что ты хочешь, чтобы я сделал?"

an "Разведай их оборону, определи, какое сопротивление они могут оказать и найди самое слабое место."
an "Сегодня это миссия завоевания, но в будущем будут и миссии ... разрушения."

"Демон смаковал это последнее слово, наслаждаясь интонацией каждого слога. Роуэн почувствовал себя плохо."

an "Оккупация деревень дадут нам регулярный доход для поддержки армий."
an "Уничтожение же принесет большое количество добычи, а также заключенных, при условии, что у нас есть место для них в наших подземельях."
an "Конечно, мы не сможем этого сделать, если не сможем победить защитников.  В таком случае нам придется уйти и вернуться позже."
an "О, и еще одна вещь. Я уверен, что ты хорошо знаешь, что в деревнях могут быть солдаты и \"герои\" вернувшиеся на родину."
an "Каждого из них, который мы примем или убьем, ослабит способность царства, в котором они находятся, защищаться от нашего возможного завоевания."
an "Не очень быстро, но это случится."
an "А теперь иди и собирай информацию. Я подготовлю орков, они уже рвутся в бой."

scene bg1 with fade

"Это был сюрреалистический момент для Роуэна, когда он шел по деревне и получал от жителей деревни приветливые волны и спрашивал их о здоровье и благополучии."
"Он много раз думал о том, чтобы сбежать и забыть все это, но в конце концов, он сделал свой доклад Андрасу."

#Show soldier selection interface.  Only option is orcs, and the village's military strength is ~30 (6 orc losses).

an "По мере расширения наших армий, мы должны будем решить, какими силами мы рискуем в этих экспедициях. Потери - это факт завоевания."
an "Орки готовы, жди моего прибытия."

"Роуэн отправился на окраину села, отчаянно пытаясь не думать о том, что случится вечером. Он ждал несколько часов, чувствуя как вина, постоянно грызет его."
"Это случилось незадолго до наступления вечера...."

show rowan necklace neutral at midleft with moveinleft

qm "Роуэн?  Ты вернулся!"

ro "Да, я, я...."

show village elder happy at midright with dissolve
show rowan necklace shock at midleft with dissolve

ro "Я...."
ro "(О, нет.)"

show rowan necklace neutral at midleft with dissolve

el "Что случилось, дитя мое? Я еще не встретился с Богиней, если ты так думаешь."
el "Пожалуйста, скажи мне, как Алексия? Что случилось в замке Бладмин?"

ro "Старый друг, зачем ты здесь? Ты же собирался в Растедель?"

el "Эти старые кости не предназначены для большого города. Я никогда не чувствовал себя там комфортно и мне нужно было вернутся в Артдейл на случай, если ты вернешься."
el "Бриарбридж был естественным местом для проживания поближе к дому."
el "Но не беспокойся об этом. Пожалуйста скажи, что с Алексией? Я думал, что..."

play sound "music/SFX/VillageBells.ogg"

"Громкий звон тревожных колоколов прервал их разговор, и Роуэн почувствовал, что мир выпал из-под него во второй раз. Не слыша слова старейшины, он побежал из Бриарбриджа."

hide rowan with moveoutleft

scene black with fade

"Герой осады Карста бежал, бежал, пока не услышал звуки битвы, и тогда он схоронился в гроте вдали от дорог."
"..."
"Чуть более часа спустя."

show bg4 with fade
play music "music/burning village loop.ogg" fadein 1.0
show orc soldier neutral at edgeright
show andras displeased at midright


show rowan hood neutral at midleft with moveinleft

an "Ах, слуга, так здорово, что ты присоединился к нам. Твой доклад был весьма полезен, мне удалось устранить защитников с минимальными потерями."
an "Оставшиеся жители деревни были вынуждены принять их новое положение."

show andras happy at midright with dissolve

an "Очень хорошо сделано."
an "О, я даже нашел твоего старого друга."

ro "?????"

show village elder wounded at edgeleft with moveinleft

el "*Кашляет* Роуэн? В чем дело?"

#elder eyes closed

"Андрас грубо толкнул старика на колени и обратился к толпе испуганных зевак."

an "Не чего не обычного, просто будет казнь. Я хочу показать, что будет с непослушными."

"Красный демон повернулся к Роуэну и заговорил достаточно тихо, чтобы толпа не могла их услышать."

show andras angry at midright with dissolve

an "Возьми свой меч, мальчик, и оторви голову этой жалкой вещи от ее шеи. Если этого не сделаешь, я казню десять сельских жителей наугад."

menu:
    "Убей старшину.":
        $ renpy.fix_rollback()
        stop music
        "Не говоря ни слова, Роуэн шагнул вперед и вытащил лезвие из ножен."
        "Он посмотрел на человека, которого знал всю свою жизнь, который так сильно помог ему. Герой зажмурился на мгновение, и слезы потекли по его лицу."
        "Затем он поднял свой клинок и опустил его."
        # sword sfx
        show bg4 with sshake
        show bg4 with redflash
        play sound "music/SFX/BodyfallDirt.ogg"
        hide village elder with dissolve
        show andras happy at midright with dissolve
        an "Ах. Это было прекрасно."
        ro "..."
        scene black with fade
        #Rowan gains guilt, castle income increase from village is 1 higher.
        $ avatar.base_guilt += 3
        $ castle.villages += 1
        $ castle.villages_income += 6
        #End of event. Give player summary of event: Village was occupied, how many orcs were lost, and how much income increased by.
        #return to castle for week end
        $ codex_add('village_elder_killed_by_rowan')

    "Отказаться.":
        $ renpy.fix_rollback()
        "Роуэн просто стоял мгновение, затем медленно покачал головой."
        show andras happy at midright with dissolve
        an "Тогда ладно. Капитан, пусть ваши люди выберут с десяток жителей."
        "Когда вокруг них возобновились крики о помощи, деревенский старец попытался встать и заговорил."
        el "Почему это происходит? Что ты пытаешься сказать?"
        stop music
        show andras angry at midright with dissolve
        an "Заткнись старик."
        show bg4 with sshake
        show bg4 with redflash
        play sound "music/SFX/BodyfallDirt.ogg"
        hide village elder with dissolve
        an "Слабые бесполезны для меня."
        ro "Зачем?"
        an "Я говорил тебе, чтобы продемонстрировать, что происходит, за неповиновение."
        ro "..."
        #Rowan gains less guilt.
        $ avatar.base_guilt += 2
        $ castle.villages += 1
        $ castle.villages_income += 5
        #End of event. Give player summary of event: Village was occupied, how many orcs were lost, and how much income increased by.
        #return to castle for week end
        $ codex_add('village_elder_killed_by_andras')
#~ $ renpy.set_return_stack(renpy.get_return_stack()[:1])
# return to map currently
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label tutorial_mine:
# Tutorial Mine event

#countryside BG

scene black with fade

show rowan necklace neutral at midleft with dissolve

ro "Я нашел то, что выглядит как заброшенная шахта. Нет никаких признаков того, что кто-то работал здесь в последнее время, но, это железная шахта."

je "Полезная находка, мы можем продавать железо, чтобы собрать средства."

an "Или построить кузницу и создавать собственный запас оружия и доспехов."

je "Где именно она?"

ro "Рядом с порталом, на юго-запад от него."

je "Отлично. Я приму меры, чтобы привести туда рабочих. Если только у тебя нет орков, готовых делать эту работу, брат."

an "Ха, воины не хотели бы, чтобы их отправляли заниматься подневольным трудом после того, как я их покормил."
an "Позже я не буду возражать против того, чтобы их отослать туда, но у меня нет свободных сейчас."

je "Значит, люди."
je "У меня уже есть несколько человек в этом районе, которыми мы можем воспользоваться, но в следующий раз придется использовать средства из казны, чтобы начать добычу с помощью местных жителей."
je "Подожди меня там, Роуэн."

scene black with fade

#xp +10
$ add_exp(10)
# mines + 1
$ castle.mines += 1
#iron production +3 per week (to be balanced later)
$ castle.iron_per_week += 3
#end turn
#return to castle for week end
#~ $ renpy.set_return_stack(renpy.get_return_stack()[:1])
# return to map currently
return

###################################################################################################
###################################################################################################
###################################################################################################

