# various "warning" events
init python:
    #### Warning about not conquering Raeve keep (end of eighteenth week) ####
    # Always triggers week 18 immediately after exploration finishes if you haven't yet conquered Raeve keep.
    # TODO check if real goal 2 is completed
    event('warning_raeve_keep', triggers="week_end", conditions=('week == 18', 'not goal2_completed'), group='warning', run_count=1, priority=pr_warning)


label warning_raeve_keep:
#### Warning about not conquering Raeve keep (end of eighteenth week) ####
# Always triggers week 18 immediately after exploration finishes if you haven't yet conquered Raeve keep.

scene black with flash
show bg10 with fade
show rowan necklace neutral at midleft with dissolve
show andras smirk at midright with dissolve

ro "(Ой-ой.  Андрас никогда не встречает меня у портала.)"

an "Ну слуга, как дела? Тебе понравилось на родине?"

show andras angry at midright with dissolve

an "Просто хотел напомнить, что ты еще не захватил определенную крепость и часы тикают."

show andras happy at midright with dissolve

an "Продолжай."

hide andras with moveoutright

ro "(Всегда приятно иметь с тобой дело, Андрас.)"

#end event
return
