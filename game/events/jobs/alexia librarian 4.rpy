init python:
    
    event('alexia_nileth', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'", "alexia_knows_magic", "arzylDialogueStage > 2",), group='alexia_library', run_count=1, priority=pr_npc)
 
label alexia_nileth:

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

"Alexia always felt a sort of watchful discomfort when walking through these particular bookshelves. It was late in the day, and she had been assigned to the magical section of the library." 
"It was a place where a book was as likely to come to life and devour your research as it was to teach you a useful spell." 
"Cliohna might feel comfortable strolling through these halls as one would through an aromatic garden, but Alexia - despite her own growing magical knowledge - was wary in the extreme."
"So it came as some surprise to her when a creature out of a children’s fable appeared amongst the bookshelves."

show nileth neutral at edgeright with dissolve

"He was a small thing, going almost unnoticed when she strode between the rows. Only the multicolored glow of his gossamer wings had tipped her off that he was there."
"He walked up the aisle facing away from her, his hands folded behind his back as he took gentle steps, reading the spine of each book he came across. A soft smile graced his lips, as if he were reminiscing about an old friend while he read."

al "Um… hello?"

"The strange fairy creature tensed, his wings flapping wildly as he spun around to face her. His eyes went wide, and he held his hands up as if to protect himself."

#nil concerned

nil "{i}Ah{/i}! By Kassandra’s eternal mercy!"
nil "I-I’m sorry, I didn’t see you there."

"Alexia kept her distance. If her time studying the occult had taught her one thing, it was that appearances could be deceiving." 
"She had no idea who this being was, if he was a real creature, or if he was some spectral projection cast by one of the (very much alive) books on the shelf."

al "Who are you?"

#nil happy

nil "Oh! A polite mortal! How refreshing."
nil "My name is Nileth. Pleased to meet you!"

"His smile was innocent. His body posture almost childlike in stance. But, Alexia nevertheless kept her distance." 
"He had a strange, otherworldly nature about him. Simultaneously ancient and youthful. There was more to this creature than meets the eye."

#nil neutral

nil "I’m sorry for reacting like I did. I didn’t hear you sneak up on me."

al "I didn’t sneak up on you."

#nil sad

"Her words deflated him for some reason. He hunched his shoulders, muttering to himself in some strange, foreign tongue."

nil "Of course… I guess I’m just not used to being caught off guard by mortals. Usually only my mistress does that."
nil "But ever since Arzyl cursed me, I haven’t been able to-"

al "Arzyl? Arzyl the witch?"

"Nileth nodded at her, his delicate wings fluttering behind him as he hovered. "

al "You’re one of the Fae?"

#nil happy

nil "I am! I hadn’t expected our presence here to be common knowledge around the castle yet."
nil "Pleased to meet you, Miss…?"

show alexia librarian happy at midleft with dissolve

al "Alexia."

#nil shocked

nil "Oh! You’re Rowan’s wife?"

"Now it was Alexia’s turn to be surprised. She felt her stomach turn at the ease with which he had identified her."

show alexia librarian concerned at midleft with dissolve

al "...Yes. How do you know that?"

#nil neutral

nil "My Lady Arzyl told me you were here in the castle."

"Alexia wasn’t sure how happy she was to learn how well known she was in Castle Bloodmeen. The Fae were relative newcomers, and yet she was already the subject of court gossip."
"..Goodness knows what else they knew."

show alexia librarian angry at midleft with dissolve

al "What are you doing in our library, Nileth?"

#nil shocked

nil "O-oh! Am I not allowed to be in here? Lady Arzyl didn’t mention any restrictions about this part of the Castle."

"The Fae glanced up at the row of spell books sitting on the shelf above his head, a tremulous smile building upon his youthful features."

#nil happy

nil "I’m sorry, I was just marveling at all the magical tomes you have stored here! You’ve got quite the collection."

show alexia librarian neutral at midleft with dissolve

al "If you intend to borrow a book, you should check in with Cliohna first."

nil "Oh, I wouldn’t want to trouble her, I’ve read most of these already. It was just a rare treat to see so many gathered together again in one place."
nil "You see that one?"

"Nileth pointed to a particular book, with a blue, wavy cover the texture of seaweed."

nil "That is a replication of the spellbook of Ursaali the Sea Witch. They say she was so powerful in the art of water magic that she could actually change the tides of the sea itself. She brought hurricanes and shifted the coastlines at her whim."
nil "She supposedly sank an entire continent that once existed off the coast of the Dragon’s Tail, because the men of the region dared to spearfish near her coral palace! Legend says she married a Marlin-man, and rode a tamed sea-dragon as her steed."

show alexia librarian shocked at midleft with dissolve

al "...Is any of that true?"

#nil happy

nil "Probably not. But it makes for a fun story, don't you think?"

"Despite herself Alexia found herself smiling. There was a charming sort of earnestness in the little Fae’s personality. She began to relax: if he was indeed a threat, he was doing a great job of concealing his motives."

#nil neutral

nil "The spells in the book, however, are very real."

show alexia librarian neutral at midleft with dissolve

al "I learned a bit of water magic myself, recently. I am no Sea Witch, but-"

#nil happy

nil "Oooh! Could you show me?"

"Alexia considered the idea. She {i}had{/i} been looking for opportunities to display her newfound powers. And the Fae seemed to be a harmless enough sort."

show alexia librarian happy at midleft with dissolve

al "Okay. Stand back."

"Using the methods that Cliohna had shown her, Alexia drew upon her power. She brought her hand up, her palm glowing with raw energy."

show bg12 with flash

show alexia librarian shocked at midleft with dissolve

"It was only after the bolt of ice was free from her hand that Alexia realized she had put too much into the shot. A thick spear of ice far larger than she had been expecting leapt from her hand."
"It threw off her aim, causing the bolt of magic to fly directly past the astonished Nileth’s head."

#nil concerned

nil "{i}Aaah!{/i} Seven Agonies!"

al "{i}Ah!{/i} Are you okay?"

"Nileth’s wings fluttered at a hummingbird’s pace. He had only just managed to dodge out of the way of Alexia’s magical might. He now hovered several feet above her, staring down at her with a mixture of surprise and awe."

#nil happy

nil "Gosh Alexia, was quite the bolt! You darn near clipped my wing off!"

show alexia librarian concerned at midleft with dissolve

al "I am so sorry, Nileth!"

nil "You don’t have to apologize. That was a very impressive spell."

#nil neutral

nil "{i}Maybe{/i} you could work on your aim, though?"

"His wide smile made Alexia cover her mouth to hide her laughter. He reminded her almost of a cavorting jester who had passed through Arthdale in her youth."
"He had been a silly fellow: all ridiculous expressions and tumbling buffoonery, but he had made the children smile, and he had always been kind to her. Nileth wore his same, eager grin."

nil "Tell you what, why don’t I give you some pointers! You have quite a skill there. Maybe just a bit... rough around the edges."

show alexia librarian neutral at midleft with dissolve

al "Pointers?"

nil "Well, did you see how you kept your stance so wide? You drew  too much energy into you at once, and didn’t know where to put it. It’s why that ice nearly took my head off."
nil "Notice too that you’re now out of breath. You expended too much energy for too little gain. You can get the same deadly effect from a Ice Shard with less effort."

al "...Really? How?"

nil "It’s all in the stance. Look: If you just narrow your hips, like so…"

"It took several minutes of effort for Alexia to get what Nileth was getting at with her stance. But he was patient with her, gently nudging her torso in one direction while positioning her arm." 
"His touch was gentle, his body moving in graceful circles around her as he sized up her spellcasting talent."

nil "So you see, when you let the energy flow {i}through{/i}-"

"A far slimmer, far sharper Ice Shard leapt forth from Alexia’s hand like it had been hit with a sudden gale. It flew down the corridor of books at a speed that astounded the would-be mage. Alexia’s jaw dropped."

show alexia librarian happy at midleft with dissolve

al "I did it!"

#nil happy

nil "Amazing!"

al "I really did it!"

"Nileth did a little swoop with his wings, pirouetting in the air, displaying his honest excitement through flight. He landed on his toes, fluttering in the air as he smiled that wide, innocent smile at her."

nil "Ha ha ha!"

al "You’re a really good teacher, Nileth. Are you a mage yourself?"

#nil neutral

nil "Oh, no. I don’t do magic anymore. Arzyl would {i}never{/i} allow that."

show alexia librarian neutral at midleft with dissolve

al "She won’t... ‘allow’ it?"

"Nileth nodded, flashing Alexia a nervous grin that told her there was more to the story than mere ‘allowance.’"

nil "I am Arzyl’s servant. It wouldn’t do for me to practice spells behind her back."

al "...Is she your Lady, or your owner?"

"Nileth shrugged, his wings fluttering as he hovered in the air."

nil "Both, I suppose."
nil "Besides: I no longer have any magical talent to speak of. But I haven’t forgotten the basics. It’s a skill, just like any other. Once you know the tricks, it's easy to teach others."

al "Wait, you don’t have any magical ability yourself?"

"Nileth shook his head. Alexia couldn’t wrap her head around the idea. How would one go about ‘losing’ their magical abilities? She had never heard of such a thing."
"She was about to ask him something more, but a small, glowing creature buzzed up between them both."

dag "Hey! Get your grubby little mitts off the walking sperm bank, would ya?"

show alexia librarian angry at midleft with dissolve

al "What the hell?"

#nil happy

nil "Oh, that’s Daggertongue. My Imp friend."

dag "Friend, nothin’. I’m just here to make sure you don't end up on the wrong end of an Orc gangbang again."

nil "Hello, Daggertongue!"

dag "Yeah, hey. Hello. What are you doin’ in here, Twinky?"

"If Nileth was bothered by the Imp’s insulting tone, he didn’t show it. He smiled at the Imp as if he was an old drinking buddy, gesturing in the direction of Alexia as he fluttered in the air."

#nil neutral

nil "Daggertongue, let me introduce you to my new friend Alexia. She’s-"

dag "Yeah, hello toots."

"The Imp spared less than half a glance in Alexia’s direction before he rounded on the Fae."

dag "D’you know how long its been since Lady Arzyl has heard from you? Sol’s Bones, if I hadn’t found you sooner, you was gonna be {i}late{/i} for your daily ‘session,’ if you catch my drift."

#nil concerned

nil "I-I wasn’t gone for long! I was just showing Alexia-"

dag "-Your fat ass as you fly outta here. I know. "
dag "You need to get back to Arzyl, and pronto. Cause I am {i}not{/i} takin’ the punishment she’s gonna dish out to you if you’re not around when she comes calling."

"Nileth wilted into himself. The strength went out of his wings, his shoulders sagging as he let out a tired sigh. Alexia frowned, seeing the wind go out of her newfound friend’s sails right before her eyes."

#nil sad

nil "Of… of course. Thanks for looking out for me, Daggertongue."

dag "Don’t mention it. Now make like a shepard and get the {i}flock{/i} outta here."

"Nileth’s wings lifted him off the ground and he flew for one of the high windows in the library. He glanced back at her one last time and gave a wave and a small smile."

#nil happy

nil "It was nice to meet you, Alexia."

show alexia librarian happy at midleft with dissolve

al "It was nice to meet you too, Nileth."

"The Fae lifted off the ground, floated away into the rafters. He spared a last, nervous glance back in the direction of Alexia, who waved as he left. She saw him smile."

hide nileth with dissolve

"Then, like a flash of fairy dust, he was gone. She was alone with the angry, glowing Imp. Daggertongue fluttered in the air for a long moment, his eyes trained to the distance as if waiting to make sure Nileth was gone."

dag "Listen, toots. For your own sake: keep well away from that little rainbow twinkle. That guy? He’s trouble."

show alexia librarian neutral at midleft with dissolve

al "He seemed nice enough to me."

dag "‘Nice’ ain’t got nothing to do with it."

show alexia librarian angry at midleft with dissolve

al "And who are you to tell him what to do? He didn’t do anything wrong. We just met, and he {i}helped{/i} me."

dag "Oh I’m sure he did, toots. He’s got a bad habit of helpin’ people he shouldn’t be helpin’. Tends to end poorly, for all parties involved. Just look at me."

show alexia librarian neutral at midleft with dissolve

al "What’s that supposed to mean?"

dag "Nothin’ you need to worry your big red head about. You see Nileth again? You keep on walking. S’better for everybody that way. Including him."

"And just like that, the Imp shot off into the air after his erstwhile companion, leaving Alexia confused and alone in the row of bookshelves, wondering what exactly had just happened."

return
