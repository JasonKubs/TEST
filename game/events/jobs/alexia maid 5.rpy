init python:

    event('mary_and_the_cabinet', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), depends=('alexia_and_mary',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('trapped_in_the_closet', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", 'alexiaJezObedient == True', 'all_actors["alexia"].corruption > 30',), group='alexia_maid', run_count=1, priority=pr_npc)


label mary_and_the_cabinet:

scene bg14 with fade
show alexia maid shock at midleft with dissolve

"Alexia heard a high pitched scream coming from a nearby room and rushed to find the source. Much of the servant staff was in one of the unused wings clearing it out for future use."
"The scream had sounded like Mary."
"She rushed into one of the empty rooms. A dark dusty place that hadn’t seen life in a long long time."

#show alexia maid concerned

"Only, no one was there. No Mary. Everything in the room was exactly what one would expect from any of the castle’s hundreds of old rooms."
"The only notable distinction was that one of the cabinets, a large oak creation nearly ten feet tall, had fallen over to the ground. Alexia slowly approached it."

#show alexia maid shock at midleft with dissolve

show mary neutral behind bg14

mary "Help me! Help me!"

"Alexia nearly jumped. Mary’s voice was coming from underneath the cabinet, so muffled as to be hard to make out."

al "Mary!? Are you alright? What happened?"

mary "I don’t know! I don’t know! I was just cleaning the cabinet and it attacked me. Started coming right at me and fell over on top of me!"

al "W-what?"

"She glanced at the cabinet. She’d seen nearly 100 in this exact make today alone. None had attacked her yet."

show alexia maid neutral at midleft with dissolve

al "Doesn’t matter right now. We need to focus on getting you out. Lift together on the count of three."

al "One."
al "Two."
al "Three."

hide mary
#mary tired or similar
show mary neutral at midright with dissolve

"At first, the going was difficult. The cabinet was so heavy, they barely made it budge. But, through screaming and shaking, they eventually made the cabinet lift just enough that Mary was able to wriggle her tiny body through a gap."
"Mary rolled on to her back. Eyes closed and panting."

show alexia maid happy at midleft with dissolve
show mary happy at midright with dissolve

"When her eyes opened again, she saw Alexia just standing there, dumbfounded. Mary squealed and hugged Alexia’s leg."

mary "My lady... I thought I was going to die under there! You’re amazing."

#if they've had sex - TODO
#mary aroused
#"Mary giggled to herself and smirked."
#mary "Well, I already knew you were amazing, but…"
#alexia maid angry
#"Alexia rolled her eyes."

show alexia maid neutral at midleft with dissolve

al "How did you even end up under there? You said it tried to attack you?"

"Mary rose to a ball, her eyes wearily trained on the heavy piece of furniture."

#mary angry

mary "Mhm. Right after I entered the room, it just came lunging at me out of nowhere. This place hasn’t been cleaned out since the days of Mistresses’ father. Who knows who used to live here?"

"Alexia leaned down, brushing her hands on the cabinet. She traced it with her fingers looking for unusual markings. Perhaps just waiting for it to move. It did not."

al "This is a totally normal cabinet."

"She gave it a hard kick. No response."

al "Not moving or anything. Are you sure about that?"

mary "It’s a monster! Really! I don’t know why it’s not moving now. But, it was before. It was. I promise."

#alexia maid angry

"Alexia sighed to herself. She liked Mary. But, she didn’t really understand Mary."

al "Let’s get you back to the house keeping room. You’ve got a bunch of scrapes and bruises. There are bandages there."

#mary neutral

"Mary rubbed her wrists and nodded slowly."

mary "Okay."

"As they turned to leave though, she turned back into the room and yelled out loudly towards the inert hunk of wood."

#mary angry

mary "But, right after we’re going to bring a bunch of tough orcs with axes down here."
mary "You hear me, asshole!? They’re going to turn you into firewood."

"Mary slammed the door behind them."

hide alexia with moveoutleft
hide mary with moveoutleft

cabinet "They’re going to have to find me first..."

return

############################################################################################################
############################################################################################################
############################################################################################################

label trapped_in_the_closet:
    
scene bg14 with fade
show alexia maid neutral at midleft with dissolve
show mary happy at midright with dissolve

"Early in the morning, Alexia joined a line of servants. Jezera had wanted them for something important before tasks began for the day. The entire castle staff was standing in ranks like a military unit."

show jezera displeased at edgeleft with dissolve

"They had to wait five minutes before Jezera, hair still a mess, wandered in."

je "Good morning, boys and girls."

"She advanced slowly down the line, looking up and down at whomever she passed. The maid or servant in question straightened their posture and prayed to whatever deity they respected that Jezera would not notice an imperfection in their posture."
"Alexia went into the same posture as the others."

je "We have a guest coming from the east. I will need four staff working, specifically, under me today, for the sake of ensuring his room is kept constantly clean and whatever he desires is given to him. That means that representing Bloodmeen is your job."
je "Alright alright alright. As lovely as my voice is, I’m sure you’re all just wondering who has the job."

"She walked up and down the line. Then, she suddenly pointed at one of the maids."

je "You."

"She moved her finger to the maid’s neighbour."

je "You."

"She paused in place, putting her finger to her lips. Then, she suddenly picked one in the back."

je "You."

"Jezera kept on walking down the line, absentmindedly looking over potential prospects. Alexia’s heart thumped along with the clacking of Jezera’s heels. Was she about to be picked?"
"Jezera reached Alexia...and kept on walking along."

show alexia maid aroused at midleft with dissolve

"But, as she did, Alexia exchanged glances with her for a brief moment. Jezera’s eyes reached into hers, and for the briefest of seconds, her Mistress gave her a secret smile. Just for her. It made Alexia think of satin and chokers."
"Alexia was still giving a goofy grin towards empty air even seconds after Jezera passed."

je "Hrmm. Perhaps, Mary. How do you feel about the idea of being the face of our hospitality?"

show mary neutral at midright with dissolve

"Mary stood at attention a few paces over from Alexia. When her name was called out, she gave a proper curtsy. Or at least as much of one as she could manage with that minuscule skirt of hers."

mary "Such a position would be an honour. I’d love to work under you. Mistress."

"Jezera brushed one her long fingernails down her cheek slowly."

je "No. Not the right kind of guest."

"She turned away. Mary didn’t seem to consider it much of a slight. With a lowered head, she returned to proper attention."

je "I think Sazaria. You will join them as well."

hide jezera with moveoutleft

"Alexia barely noticed as the meeting broke up. Jezera had other work to be done, of course. The entire castle relied on her. Alexia and the other maids remained to receive their assignments."
"Yet, Alexia was half in a trance as she went about her morning. What did Jezera have planned for the next time she was summoned down to her quarters? The thought consumed her."

show alexia maid shock at midleft with dissolve

"So much so, in fact, that it took a sudden and shocking pinch in the rear to break her from her stupor."
"She was standing a hallway alone now. That is, except for Mary."

show mary happy at midright with dissolve

mary "You were walking in the wrong direction, silly. We’re on kitchen duty today."

show alexia maid neutral at midleft with dissolve

"She blinked twice. The petite maid was standing in front of her with a beaming facial expression. Her usual unquenchable cheerfulness was on full display."

al "Oh? You’re right."

"Mary giggled in a high girlish tone."

mary "You don’t gotta say a word about it. I understand. You were all giddy thinking about Mistress Jezera, right? Totally normal."

al "I was-"

show alexia maid shock at midleft with dissolve

"Alexia blinked again."

al "What?"

"Mary raised her shoulders and struck up a mischievous smile."

mary "I’m not blind, silly goose. Those “Fuck me” eyes you were making at her. Those “I will” eyes she was giving you back. And all of those late night visits to-"

#alexia maid angry
show alexia maid neutral at midleft with dissolve

"Alexia moved without thinking. No one else was in the hallway. So she shoved the smaller girl to the wall and loomed over her with narrowed eyebrows. Her arms slammed the wall, holding Mary in place."
"She couldn’t know. If people knew they could tell Rowan."

al "I don’t know what you think you saw, Mary. But, you don’t know what the slightest thing about what you’re talking about."

"Mary, for her part, just kept on smiling. She hadn’t even reacted to being shoved against the wall, except with a mouse-like squeak."

mary "Ooh, rough."
mary "Don’t worry. I’m not about to run around screaming about it. No worries. I know how to be to keep my lips gagged."

#alexia maid concerned

"Alexia slowly eased backwards, moving her arms to the side. As the surprise faded, so too did the rage. Mary would not be telling her this if she planned to skip off to Rowan. Besides, that wasn’t Mary’s style."
"Besides, she knew Mary. Would Mary actually try to harm her?"

al "Is there something you want from me?"

mary "Oh, nothing at all. We’re friends, silly.  I’m just glad to have you as a serving sister is all."

#alexia maid neutral

"Alexia tilted an eyebrow."

al "Serving sister?"

show alexia maid shock at midleft with dissolve
#show mary naked happy

"Instead of answering in words, Mary answered by lifting up her skirt. Alexia froze, dumbfounded. For starters, Mary was not wearing any panties."

if maryNakedSeen == True:
    "Alexia already knew what she would find, but could not help looking down. She’d seen it all before."
    scene cg399 with fade
    pause 3
    "The intricate tattoos, the piercings to most intimate places. Even the word slave written dramatically above her sex."
    "It had been shocking at the time. In truth, even all this time later, it was still stunning."
    scene bg14 with fade
    show alexia maid shock at midleft with dissolve
    #show mary naked happy
    show mary happy at midright with dissolve
    "Now Mary was showing it all to her voluntarily. Did this mean that-"
    
else:
    "But, had the pussy it revealed been an average one, Alexia would not have been left so shocked."
    "No, Mary’s pussy was something unique entirely. It was laced with a string of piercings. Alexia struggled to count them." 
    "More than that, it was marked with the word “Slave” written in beautiful cursive above it."
    "Alexia took a step back and muttered under her breath. How? Why? Who would do something like this to their body?"

mary "A slave must have an Owner, after all. Perhaps one beautiful and a bit sadistic. Now we have the same Owner!"

show alexia maid aroused at midleft with dissolve

"Alexia’s knees shook. Without even meaning to she took a step backwards, ceding ground to Mary. She didn’t mean...she couldn’t mean...But, yet.."

al "D-Did she make you get all that?"

"Mary giggled softly and played with the hem of her skirt."

mary "Worried it might be your turn next? Hehe. Don’t worry. I was the one who asked her to get them. My idea. It was too sexy not too."

#show mary happy

"Finally, she brought the skirt back down, removing the depraved sight from Alexia’s gaze."

mary "So, tell me the story, sister. Oh, you have got to tell me everything. I want to hear every last juicy detail!"

show alexia maid happy at midleft with dissolve

"Alexia rolled her eyes. This was much more like the Mary that she knew." 
"Still, here was someone who not only would keep a secret, but probably had a similar experience. Alexia had to admit it would be interesting to open up to someone about it."
"Oh, she didn’t say everything. If a detail concerned Rowan, Alexia kept it from her tongue. She also didn’t mention the trip to Rosaria." 
"Still, Mary hung on every last word, asking the occasional clarification question. When the story finished, Mary clapped her hands together."

mary "Wow! You must really be a prize to her. She never did anything remotely that impressive for me!"

show alexia maid neutral at midleft with dissolve

al "You serve her, but she doesn’t value you?"

mary "Nope. I’m just a toy! You’re clearly much more important to her."

"Mary sighed happily. Alexia couldn’t help raising an eyebrow. Mary had said it so matter-of-factly. No, she almost relished it. Shouldn’t that make her sad?"

mary "But, that’s okay. Everyone has their place. Mine just happens to be on my knees. "

#alexia maid concerned

"Alexia’s heart was torn by this. Mary was her friend. How had she had internalized the idea of her own inferiority to the point where it no longer even bothered her?"
"Yet, Alexia couldn’t help turning over what Mary was saying in her mind. She’d known for awhile that Jezera had other pets. If Jezera really was treating her as something special, did that mean that she really did..."
"She lost her footing slightly. She suddenly felt woozy."

al "This all feels...I don’t know how to say it...wrong? What kind of woman enjoys something like that?"

"Alexia blurted it out before she realized that she’d just insulted her friend."

show alexia maid shock at midleft with dissolve

al "Oh. I’m sorry. I didn’t mean to-"

"Mary interjected."

mary "A fuckslave!"

"Alexia blinked twice."

mary "I’m a pussy addicted fuckslave. That’s the kind of woman who enjoys something like that."

"For the first time since they’d met, Mary wasn’t smiling. She wasn’t angry. Just...serious."

mary "I’m a slave with a Mistress. I have a purpose. And it’s to serve with everything I have. Especially my body."
mary "Back in my home village, they had all these dumb rules about who I could fuck. Who I couldn’t fuck. It had to be a man. It had to be someone I was married too. My parents had to approve."
mary "But, that just wasn’t me. I wanted to be kissing, rubbing, and fucking every pretty girl that crossed my path. That’s why Mistress made me her slave. Now I can fuck and fuck all I want, and no one cares. I’m just a slave. What’s wrong with enjoying myself?"

"Alexia found herself silent yet again. Mary had a way of disarming her with her bluntness. Especially about such lewd topics."

"Mary stepped closer and placed a hand on Alexia’s waist."

mary "You don’t need to struggle so much with it, cutie. Do you like having sex with Mistress?"

show alexia maid aroused at midleft with dissolve

"Alexia sighed."

al "...Yes."

mary "So you do like fucking girls, then?"

"She was suddenly much more aware of Mary’s hand."

al "Well, I don’t know if it’s all girls…"

mary "But, when you see her perfect purple skin, it makes you all hot and steamy, doesn’t it?"

"Alexia closed her eyes."

scene black with fade
show jezera happy at center with dissolve

"…"

scene bg14 with fade
show alexia maid aroused at midleft with dissolve
show mary happy at midright with dissolve

al "I suppose so."

mary "And when Mistress fucks you, is it tame and chaste?"

"Mary was brushing her hand now along Alexia’s stomach in a slow rhythmic fashion. Light, fleeting touches constantly moving."

al "Well no…"

mary "And she wants you to develop your skills at sex and using your body, right?"

al "..."

"Alexia sealed her eyes shut. Was Mary...insinuating they were the same? That couldn’t be right."
"Mary’s hand trailed up slightly. Alexia let out a slight gasp. She’d felt the back of Mary’s hand brush over her nipple through her outfit."

mary "And do you like it when she teaches you those things? When you get to act like a bad girl?"

"Alexia tried to formulate a way to say that Mary didn’t understand. That it was more complicated than that. Nothing of the sort ever came out."

al "...Yes."

"Mary drew her hand back suddenly. Alexia suppressed a groan. Her eyes fluttered open to see Mary grinning in a way she’d never seen before. Less cutesy and more...hungry."

mary "See! You’re a fuckslave too! You just haven’t accepted it yet!"

"Alexia stumbled back a step. The back of her foot hit the wall."

al "I’m not..I’m not that…"

mary "Mm. Silly silly. Your slave sister Mary is here to help drive all those silly lies away."

"Mary advanced slowly."

mary "In fact, you probably got all wet and steamy just from talking about it, didn’t you? I’m willing to bet a pretty penny on it."

"Alexia huffed. She was letting Mary get the better of her. Letting her read her mind. Letting her read her body. This had gone far enough already."

#alexia maid angry
show alexia maid neutral at midleft with dissolve

al "I’m not a fuckslave like you. There isn’t a tattoo on my crotch. Jezera is just showing me a few things. I still have control of myself. I still have choices."

"Mary did a twirl and giggled to herself. Alexia let herself exhale."

mary "Well, fuckslave or no. Jezera does always allow her toys to spend quality time together."
mary "So, miss self-control. We could always take a teeny little break in that closet over there. I could help you with that wet pussy of yours. What do you say, sister? Think you’re going to, hehe, choose to do that?"

show alexia maid aroused at midleft with dissolve

al "..."

"Alexia’s attention distinctly went between her own legs and the sensations emanating from them. Her eyes couldn’t help drifting to the opening of the closet."
"Mary leaned up to her ear and gave her final pitch in a husky whisper."

mary "No one would have to know. It would just be between us girls."

menu:
    "Nod.":
        $ released_fix_rollback()
        "Alexia almost shook her head. She’d spent the better part of the conversation denying all of Mary’s totally baseless assertions."
        "And yet.."
        "Alexia nodded." 
        al "I don’t think...I don’t think that would be so bad..."
        "The words flowed from her mouth, as though she hadn’t been the one to say them." 
        "Why had she said it?"
        "Alexia wondered that even as a grinning Mary pulled her by the hand towards the waiting closet. She had all the eagerness of a puppy."
        "Still, the reason why she was doing this could not be denied for long. Mary had been right about one thing, at least. She was wet."
        "The closet itself was small. An old stone enclave into the castle for the purpose of storing supplies. Alexia nearly hit a broom on the way in." 
        "The space was cramped and dark. The only light came from a crack in the door that Mary left open behind them. The size of the closet forced their bodies together. Already Alexia’s bosom pressed to Mary’s. That wasn’t an unpleasant feeling."
        "To her surprise, Mary didn’t start throwing herself at Alexia the moment they were safe in the darkness. She actually dutifully removed her glasses and stashed them away in a spot out of reach. It was a smooth, practiced gesture, like a habit she’d built up over time."
        al "I've never quite had a tryst this way before. What now?"
        mary "Now this."
        #mary aroused
        "Mary went to the tips of her toes, and slowly brought her lips to Alexia’s. Her lips tasted good. Like cherries. After only a few seconds, Alexia was starting to get into it."
        #CG1
        scene black with fade
        #mary naked
        show mary happy behind black
        show alexia necklace naked aroused behind black
        "In the darkness, there were a flurry of hands. Grasping. Undressing. Garments fell to the floor of the closet. The largest of which was the longer maid dress Alexia wore. Mary’s entire dress slipped off like it was hardly there, though. Had it been made to be removed easily?"
        "Alexia and Mary both started to sink, landing gently on their knees. It put them on an even plane. By now, Mary was down to little more than her lace undergarments and her heels. Mary didn’t even have undergarments."
        "Their hands explored each other’s bodies and their tongues explored each other’s mouths. Mary was so soft. It felt good to rub against her body. Their breasts and stomachs met." 
        "Her companion quickly had her pussy pressed against Alexia’s leg. Alexia followed suit." 
        "Mary’s body had a strange texture to it. Alexia was only still getting used to the soft sweet feeling of another woman’s body. Mary’s petite form certainly fit that bill." 
        "But, as Mary ground her nipples and crotch into her, the feeling was interspaced with hard metal. Each sensation heightened her awareness of the other. The piercings made her softer, and her body made the piercings more overpowering."
        "It was driving Alexia crazy."
        mary "Mph. Mph. I'm getting all wet…"
        "Alexia rode Mary’s thigh. It reminded her of the way she’d use a pillow back during her youthful experimentations. The harder she ground herself, the more and more she drowned in the pleasure. Her juices coated everywhere she rubbed. Hot and wet."
        "The same was happening to Mary. Her head rolled back and her posture grew more restless by the moment. Alexia’s thighs were getting wet with juices besides her own."
        "It went on and on without advancing or progressing. There was none of the urgency of sex with a man. When her body was locked with another woman’s she could rub and tease and play for so long that it was hard to pay attention to time."
        "Who would even want to think about time when her breath was at your neck and your entire body felt so good?"
        "Alexia's breath caught at her throat. A long throating moan was building up...only to be silenced by Mary’s hand."
        mary "We have to be quiet, sis. We can't have someone open up and see a p...pair of sluts in here."
        "Mary’s voice came out in a breathy whisper."
        "Alexia nodded slowly. A pair of sluts..."
        al "Dizzy…"
        "Without thinking, Alexia kicked out her leg. She’d been so lost in the fog that her space constraints were not on her mind. When she kicked out, it hit the wall with a loud bang."
        "Alexia and Mary both froze in place. Alexia’s eyes shot open. What had she just done?"
        "Then, from outside the closet, the sound of heavy male footsteps grew louder and louder. Mary silently drew the door totally closed, leaving them in darkness."
        scene bg14 with fade
        show andras displeased at midleft with dissolve
        "Andras walked slowly down the hallway. His muscles were tense. He looked as though he were preparing for battle." 
        "Suddenly, Andras froze in place." 
        "He thought he heard something. Breathing perhaps. Only it was very heavy. He sniffed the air. His large frame towered over the hallway."
        "No one was there. Seemingly." 
        "He brushed his hair back and kept on walking. Though, if he looked tense before, it was only more so now."
        #CG1
        scene black with fade
        #mary naked
        show mary happy behind black
        show alexia necklace naked aroused behind black
        al "Mary…"
        "Alexia panted softly. It was hard to even form words."
        al "Why were you teasing me? We could have been found out…"
        "The entire time that someone had been walking past, Mary’s hand had been between Alexia’s legs. It would have been a struggle to keep totally quiet even without the mischievous touches."
        "Mary gave a breathy giggle."
        mary "Why did you like it so much, then?"
        "Alexia sealed her eyes shut. Then she opened them once more. Some of the lust that clouded her gaze receded."
        al "No more teasing."
        al "You’re the lesbian fuckslave, right? The one who spends all of her time with other girls? You like to pretend that you’re so skilled."
        "Alexia brushed a hand over Mary’s cheek."
        al "Prove it."
        "Alexia leaned back, as much so as space would allow, and pulled away her panties. By now, they were so soaked that they were practically unwearable."
        mary "..."
        mary "As you command."
        #CG2
        scene black with fade
        show alexia necklace naked aroused behind black
        "If Alexia had actually believed Mary to be bluffing, she had made a real mistake. Without another word, Mary was on all fours, practically throwing her face between Alexia’s legs."
        "Alexia’s eyes flew open. Mary’s tongue had plunged deep inside of her and was now frantically exploring her inner walls." 
        "Mary didn’t have a technique built on slow and steady buildup. She attacked Alexia’s sex like a woman possessed. Her tongue twisted and flicked at expert speeds."
        "She was completely unprepared."
        al "Oh...fuck…"
        "In mere moments, her head was rolled back and her chest was rising and falling fast. Alexia sucked in air but couldn’t stop feeling breathless. Mary’s tongue always seemed to find the exact right spot to do the maximum damage."
        "Already dripping, she was soon bucking and spasming. She was going to cum. She was going to cum."
        al "M...Mary…"
        #CG2 - var 1
        scene black with fade
        "Alexia spasmed. Waves of toe curling delight filled her body. Every nerve ending was alight."
        "But, Mary wasn’t done. Games between girls don’t have to stop after one."
        "For the next half hour, the closet was filled with the sounds of desperate moaning. At times even aroused screaming. Alexia was pushed past the edge over and over again."
        "Mary’s tongue never seemed to tire or grow sore. She just kept on attacking and attacking. A flick of the clit. A move deeper into her folds. All of it made Alexia squirm."
        "By the time she was done, she’d left the redhead crumpled on the closet floor like a puppet whose strings had been cut."
        scene bg14 with fade
        show alexia maid aroused at midleft with dissolve
        show mary happy at midright with dissolve
        "Both women, fully clothed once more, left the closet holding hands. They were both flushed red, although Mary was not half as flushed as Alexia." 
        "Mary’s glasses were crooked. She’d put them back on in the dark." 
        "Alexia, meanwhile, found it hard to even hold Mary’s hand. Her hand would still spasm every few seconds. Aftershocks."
        al "You’re such a slut, Mary."
        mary "I thry. Sisth."
        "Her words came out so slurred that Alexia could barely understand it. So, she just kissed Alexia’s cheek instead to get the point across."
        "Alexia groaned. Something told her that Mary wouldn’t be content with a single tryst."
        al "Sisters, huh…"
        "She brushed a shaky hand along her neck."
        $ change_actor_num_flag('alexia', 'jezera_influence', 3)
        $ change_corruption_actor('alexia', +5)
        return

    "Shake head.":
        $ released_fix_rollback()
        "Alexia paused. She was wet. She could feel it. The proximity of Mary’s body did nothing to alleviate that. Neither did the feeling of her breath at Alexia’s ear."
        "But, was she so wet that she couldn’t maintain control of herself?"
        show alexia maid neutral at midleft with dissolve
        "Alexia shook her head firmly, and playfully pushed Mary out of her personal space."
        al "Nice try, Mary. Did you really think I would be that easy? The answer is no."
        mary "But, what if-"
        show mary neutral at midright with dissolve
        "The smaller maid pouted. Alexia’s head was already starting to defog."
        al "Nope."
        "Alexia glared into Mary’s eyes and Mary glared back. They held their stare for a few seconds that felt like minutes. Like two sams circling each other with horns out." 
        "Mary broke her glance first."
        mary "Mph. Darn it."
        "She stomped her foot."
        mary "I was doing my best purring seductress voice too!"
        show alexia maid happy at midleft with dissolve
        show mary happy at midright with dissolve
        "They both laughed a little bit."
        "Alexia rolled her eyes. Was this what Mary was like with other girls who she’d seduced? A little disappointment and she turned to a petulant child. Her parents really must not have done a good job with her."
        al "You were. It almost worked even. Almost."
        "Mary sighed. They started walking towards the Kitchen, where they were both expected for work."
        mary "You may have won this battle, sis. But, I’ll get you next time. Don’t think I’ve given up yet!"
        "She giggled playfully. Alexia couldn’t help but smile a bit too."
        al "Sister, huh?"
        mary "Mhm. Sister slaves to the same Mistress."
        al "I see."
        #alexia maid concerned
        show alexia maid neutral at midleft with dissolve
        "It was almost like there was an entire kingdom beneath Jezera. A series of feudal dues and power structures invisible to anyone who wasn’t clued into the network."
        "The question for Alexia was...where exactly was she in this kingdom? Was she a duke? Or a peasant?"
        return









