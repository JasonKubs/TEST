init python:
    
    event('more_appropriate_profession', triggers="week_end", conditions=('alexiaJezObedient == True', "get_actor_job('alexia')!='maid'", "get_actor_job('alexia')!='none'",), group='ruler_event', run_count=1, priority=pr_ruler)


label more_appropriate_profession:

scene bg14 with fade

if get_actor_job('alexia')=='breeding':
    show alexia breeding concerned at midleft with dissolve
    "A disgusting shambling mess marched down the hallway. That mess was Alexia. Her work uniform was absolutely covered in drider shit. It had even gotten into her hair." 
    "The expression on her face matched the outfit. Disgust. Her nose twitched with the stench. This was going to take hours to clean up. Hours."
    "Draith had told her that someone needed to clean up the mess. But, how could he stutter so heavily when talking about the broken segment of the railing? It was too important to misspeak about."

elif get_actor_job('alexia')=='forge':
    show alexia forge concerned at midleft with dissolve
    "A figure, covered completely black from head to toe in coal soot, marched down the hallway, leaving a black trail in her wake. The figure was Alexia. Her entire body, work uniform, hair, face was covered in it."
    "The expression on her face matched the outfit. Supreme discomfort. Every so often, she’d sneeze out dust. This was going to take hours to clean up. Hours."
    "Oh, Greyhide had been apologetic about it. Falling into the waste pit had been an accident. It almost made it hard for Alexia to maintain her rage. Almost."
    
elif get_actor_job('alexia')=='research_assistant':
    show alexia librarian concerned at midleft with dissolve
    "A figure in a burning uniform shambled down the hallway. The figure was Alexia. The fire was mostly out, but little embers remained on the uniform and even in her hair." 
    "No real damage or scarring, but her outfit was mostly destroyed and she’d need to do something about any singed hairs. Her expression matched her outfit. Annoyance." 
    "This was the last time she’d act as a spell test dummy for one of Cliohna’s apprentices. Had the sorceress not acted fast, the damage might have been less trivial."

else:
    show alexia barmaid concerned at midleft with dissolve
    "A figure shambled down the hallway, covered in what had to be several layers of spilled liquid. Some of which certainly included vomit. The figure was Alexia. Every part of her outfit was a mess."
    "She has a facial expression to match her disheveled state. Exhaustion. The stink of alcohol radiated from her clothes and even her hair."
    "She hadn’t had any herself. But, Indarah had suggested she serve the main group from a rowdy horde of dragons tail pirates who’d stopped in. Indarah didn’t want to be the one to serve them. She didn’t say why."
    "The process had not been fun. As they got progressively more drunk, they got progressively more disgusting. It had been a nightmare shift, from which she’d only just now returned."

"But, before Alexia could make her way to a much needed bath, someone stopped her in the hallway."

show jezera happy at midright with dissolve

je "I see you dressed to impress, Dove."

#alexia embarrassed

al "Oh no."

"Alexia tried to duck away as fast as she could. Her Mistress was the last person who she wanted to be seen by in this state."

al "Apologies, but I-"

"Jezera just giggled."

je "Don’t be shy. I’m a demoness and you’re worried I’ll recoil because you’re icky. I’m made of sterner stuff, darling."

"She put a hand on Alexia’s shoulder, not even caring one wit about what might get on her skin."

je "You’re having a bad time at work, aren’t you?"

al "I wouldn’t know if I’d say that…"

je "Well, that’s perfectly alright. How about we go somewhere and talk about it?"

scene bg9 with fade
show alexia 2 necklace angry at midleft with dissolve
show rowan necklace neutral at midright with dissolve

al "I want to work as a maid, Rowan."

ro "Hrmmm?"

"Rowan looked up towards Alexia from the bed. He’d only returned from doing paperwork moments earlier." 
"Alexia’s appearance showed little sign of her earlier mishaps. There’d been plenty of time to clean off. But, her anger had not cooled."

al "I’m sick and tired of my current post. It’s too stressful working there."
al "So, I was thinking about it earlier. The castle staff have a much easier time. Much less difficult. And Jezera largely makes sure no one harasses them."
al "So I want you to schedule me to work with the castle staff."

"Rowan put a hand to his head. Did he really have to think about this now? The day had been long and difficult for him. Alexia’s anger didn’t quite have the visual punch that it had before her shower."

ro "I’ll review your working arrangements in a week or two. We can see how your current job is-"

al "No. I want you to change my job, first thing in the morning."

menu:
    "Agree to Alexia’s demand":
        $ released_fix_rollback()
        show rowan necklace concerned at midright with dissolve
        "Rowan’s head was killing him. He was the one who was supposed to place her for work. But, she clearly wanted to work somewhere else. Hadn’t he been picking for her sake? It’s not like it would seriously damage the function of the castle."
        "She was just one woman, after all."
        "Mainly though, he just wanted to escape this conversation. Alexia was in his face. She was angry. Rowan didn’t know what to do."
        ro "Okay. I’ll do it."
        ro "First thing in the morning, I’ll go in and change your workplace assignment to the castle staff."
        show alexia 2 necklace happy at midleft with dissolve
        "His wife visibly brightened."
        al "You will?"
        ro "Having a big outing about it isn’t worth it. If you want to work as a maid, that your choice. I won’t get in the way."
        al "I-"
        al "Thank you, Rowan. You listened to me. I’m sorry I lost my temper too."
        al "I’m going to be much happier with work now. You’ll see."
        "She leaned forward and planted a kiss on his cheek. Rowan groaned and put a hand to his temple."
        $ do_job_maid('alexia')
        #stress cost of alexia working as a maid reduced - TODO
        return
        
    "Refuse.":
        $ released_fix_rollback()
        show rowan necklace angry at midright with dissolve
        ro "Alexia, you can’t just come in here and demand that I change the castle schedules without sitting down to review. I’ve spent the better part of months trying to beat this castle into shape."
        "Alexia held her ground with arms crossed."
        al "You do not know how terrible a day I had. I am your wife. I am telling you that I want to work as a maid with the castle staff."
        al "It upsets me when you don’t listen to me."
        "The two held their ground, locking eyes with one another. This had not been their first fight of late. They were getting more adept at it."
        "Alexia really seemed, to Rowan, to mean it. If he held up on his refusal, Alexia would not be quick to forget this."
        menu:
            "Just agree.":
                $ released_fix_rollback() 
                show rowan necklace concerned at midright with dissolve
                "Rowan’s head was killing him. He was the one who was supposed to place her for work. But, she clearly wanted to work somewhere else. Hadn’t he been picking for her sake? It’s not like it would seriously damage the function of the castle."
                "She was just one woman, after all."
                "Mainly though, he just wanted to escape this conversation. Alexia was in his face. She was angry. Rowan didn’t know what to do."
                ro "Okay. I’ll do it."
                ro "First thing in the morning, I’ll go in and change your workplace assignment to the castle staff."
                show alexia 2 necklace happy at midleft with dissolve
                "His wife visibly brightened."
                al "You will?"
                ro "Having a big outing about it isn’t worth it. If you want to work as a maid, that your choice. I won’t get in the way."
                al "I-"
                al "Thank you, Rowan. You listened to me. I’m sorry I lost my temper too."
                al "I’m going to be much happier with work now. You’ll see."
                "She leaned forward and planted a kiss on his cheek. Rowan groaned and put a hand to his temple."
                $ do_job_maid('alexia')
                #stress cost of alexia working as a maid reduced - TODO
                return
                
            "Continue to refuse.":
                $ released_fix_rollback()
                ro "You’re never going to convince me this way. I’m the one who makes the castle assignments. You agreed to it."
                ro "This entire outburst is making me want to change your job even less."
                al "..."
                "There were words on Alexia’s tongue. Rowan didn’t hear them, but he knew they were there. But, those words never came out. Instead, came a different, more terse, answer."
                al "Fine. I understand."
                al "Don’t forget what I asked for."
                hide alexia with moveoutleft
                "Without giving him another look, she turned on her heels and stormed out of the room. Rowan watched her go with a frown. He could still go after her. But, nothing short of telling her that he’d give in would appease her now."
                "Rowan ran a hand through his hair."
                "Why couldn’t she be obedient? That’s how she’d always been back in Arthdale."
                $ change_relation('alexia', -10)
                #stress cost of alexia working as a maid reduced - TODO
                return

                
