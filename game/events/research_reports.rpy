init python:

    event ('research_report', triggers="week_start", conditions=('len(castle.completed_researches) > 0',), priority=pr_new_rs)


# an event to present reports of completed researches at the beginning of a week
label research_report:

# Show library background, Rowan and Cliohna appear.
scene library
show rowan necklace neutral at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

# Randomly decide one of the following scenes to be displayed.
$ temp = renpy.random.choice(('.v1', '.v2', '.v3', '.v4'))
jump expression ''.join(('research_report', temp))

label .v1:
    cl "Вот отчет о последнем проекте.  Уверена, результаты будут полезны."

    # Show completion report.  It fills the screen, rather than using the regular text box.
    # delete uid of completed research from castle.completed_researches
    $ temp2 = castle.completed_researches.pop()
    call screen research_completion_report(temp2)

    ro "Профессионально сработано.  Пожалуйста, передай мне список доступных проектов, чтобы я мог назначить следующий."

    "Без слов и выражения, Клиона передала свой обновленный лист Роуэну."

    # Select a new research project.
    call screen researches_screen(True)

    cl "Понятненько.  Если больше ничего нет, я начну немедленно."

    #end scene.
    return

label .v2:
    ro "Итак, Клиона, что у тебя есть для меня?"

    cl "Несмотря на пару неудач, я закончила проект."

    # Show completion report.
    $ temp2 = castle.completed_researches.pop()
    call screen research_completion_report(temp2)

    "Не успел Роуэн закончить ознакомление с результатами, как Клиона поднесла ему другую бумагу."

    cl "Вот мой новый список возможных направлений исследований."

    # Select a new research project.
    call screen researches_screen(True)

    ro "Удачи."

    cl "Вряд ли мне это нужно."

    # end scene
    return

label .v3:
    cl "Я закончила это немного раньше, чем ожидалось, поэтому я провела предварительную работу над некоторыми из других проектов в ожидании твоих задач."

    # Show completion report.
    $ temp2 = castle.completed_researches.pop()
    call screen research_completion_report(temp2)

    cl "Иногда я поражаюсь тому, насколько близнецы доверяют тебе.  Никто из них не хочет назначать исследовательский проект вместо тебя."

    "Затем ведьма передала ему список потенциальных проектов, который несколько изменился по сравнению с прошлым разом."

    # Select a new research project.
    call screen researches_screen(True)

    ro "Извини, если ты не этого ожидала."

    cl "Ты должен принимать трудные решения, основываясь как на текущей ситуации, так и на наших потенциальных будущих ситуациях.  Это непростая задача."

    # End scene
    return

label .v4:
    "Клиона сегодня, похоже, не была в настроении, так что Роуэн не утруждался вести светскую беседу, когда пришел забрать отчет о  последнем  проекте."

    "Он нашел его на столе рядом с ее списком новых исследовательских тем, рядом с ведьмой, которая в настоящее время была погружена в  эксперимент."

    # Show completion report.
    $ temp2 = castle.completed_researches.pop()
    call screen research_completion_report(temp2)

    "Закончив чтение, он взглянул на список тем."

    # Select a new research project.
    call screen researches_screen(True)

    "Записав свой выбор на неиспользованном клочке бумаги, агент близнецов свалил из библиотеки."

    # End scene.
    return
return

