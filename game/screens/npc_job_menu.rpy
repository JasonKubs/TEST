# small menu for choosing a job for NPC and show some info
screen npc_job_menu(align=None):
    if castle.npc_with_jobs and systems.npc_jobs:
        frame:
            background Frame('gui/stats_border.png', 12, 12)
            xsize 150
            ysize 110
            if align:
                align align
            hbox:
                style_prefix 'small'
                for npc_name in castle.npc_with_jobs:
                    hbox:
                        xpos 100
                        ypos 10
                        xsize 200
                        text '{}\'s Stress: {}'.format(all_actors[npc_name].name, all_actors[npc_name].job_state.stress) align (0.5, 0.5)
                    hbox:
                        xpos -100
                        ypos 40
                        xsize 200
                        button action [Show('npc_job_selector', ac_uid=npc_name), SensitiveIf(alexia_cant_work_weeks <= 0)]:
                            #xpos 15
                            xsize 200
                            if get_actor_job(npc_name):
                                text '{}  ({:.1%})'.format(all_actor_jobs[get_actor_job(npc_name)]['name'], all_actors[npc_name].job_state.efficiency())
                            else:
                                text 'Choose job' align(0.5, 0.5)

screen npc_job_selector(ac_uid):
    modal True
    default selected_job = None
    default selected_job_uid = None

    add 'gui/UI_Screens/UISCreen_{}Job.png'.format(ac_uid.title())
    text "ASSIGN {}".format(ac_uid.upper()) color "#ffffff" bold True xalign 0.5 ypos 20
    frame:
        background 'listbox_border'
        xpadding 3
        ypadding 3
        pos (55, 130)
        vpgrid:
            cols 1
            xysize (400, 550)
            mousewheel True
            scrollbars 'vertical'
            spacing 1

            for job_uid in all_actor_jobs:
                button:
                    right_margin 1
                    xfill True
                    ysize 72
                    background 'button_border'
                    hover_foreground 'rect_highlight'   
                    
                    text all_actor_jobs[job_uid]['name'] color "#2c6427" bold True xoffset 25 yalign 0.6
                    action SetScreenVariable("selected_job", all_actor_jobs[job_uid]), SetScreenVariable("selected_job_uid", job_uid)

    frame:
        background 'gui/workshop/UI_DescriptionBox.png'
        xpos 495
        ypos 130
        xysize (403, 484)

        if selected_job:
            text selected_job['name'].upper() bold True color "#ffffff" xalign 0.5 ypos 25
            add 'gui/job/' + ac_uid.title() + "_" + selected_job['image_suffix'] + ".png" xalign 0.5 ypos 75
            text selected_job['description'].upper() size 12 bold True color "#ffffff" xmaximum 350 xalign 0.5 ypos 285
        else:
            text 'No selection' size 25 xalign 0.5 ypos 25

    if selected_job:
        textbutton _("Start"):
            style 'room_button'
            xysize (410, 55)
            action [SetJob(ac_uid, selected_job_uid), Hide('npc_job_selector'), renpy.restart_interaction]

            xpos 495
            yalign 0.95

    textbutton 'Back' action Hide("npc_job_selector") style 'back_button'

init python:
    class SetJob(Action):
        def __init__(self, ac_uid, job_uid):
            self.ac_uid = ac_uid
            self.job_uid = job_uid

        def get_sensitive(self):
            if self.job_uid == 'breeding' and castle.buildings['pit'].lvl == 0:
                return False
            elif self.job_uid == 'forge' and castle.buildings['forge'].lvl == 0:
                return False
            if alexia_cant_work_weeks > 0:
                return False
            return True

        def __call__(self):
            all_actors[self.ac_uid].job_state.job = self.job_uid
