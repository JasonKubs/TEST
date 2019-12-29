#Level 3 party:
#Requirement: None. Triggers on entering mine, usual mine menu appears at the end of the event
init python:

    event('mine_level_3_party', triggers=('map_res_6', 'map_res_7', 'map_res_8',), group='mine', run_count=1, priority=pr_map_res)

label mine_level_3_party:
scene black with fade
show rowan necklace neutral behind black

"Taking a bit of a detour, Rowan approached what he knew was an abandoned iron mine. A couple of years back, he heard from a passing merchant about it being overrun by monsters, though by then he had already retired from being a hero and general, and was enjoying a peaceful family life with Alexia."
"Never really one for adventuring – he was a soldier in the past, not a glorified mercenary for hire – he chose to leave the matter to the local authorities."
"Though knowing the level of enthusiasm with which lords react to peasants asking them to do their damn job of protecting the countryside, he honestly expected the mine to be still filled with monsters."

if avatar.corruption > 59:
    "Not like that would be an issue, now that he had literal disposable orcs at the snap of his fingers. "
else:
    "Not like that would be an issue, with the orcs he had under his command."

"Maybe if said monsters turned out to be driders, he might get a chance to grab a couple of eggs. Two birds with one stones, if lady luck smiles on him."
"Filled with such optimistic thoughts, he approached the slope leading to the mine entrance-"
"- and instantly noticed the faint trail of campfire smoke on the horizon."
"Sensing trouble, Rowan stepped off the dirt path he was on, and entered the nearby forest. With his usual expertise, he started sneaking up to the source of the unexpected smoke."
"As he drew nearer, he started overhearing snippets of a conversation between two particularly agitated people. A minute later, he was close enough to grasp the words being said."

qais" … then you shouldn’t have tossed in so much wood into the fire!"

"The first voice complained, annoyed. It sounded male, young."

shee "Yes, yes, blame everyone but yourself."

"Another answered. This one was high pitched. Girly."

qais "I did everything right! I got the recipe from the innkeeper in Rastedel and followed it to the letter!"

shee "Horseshit! Show me that- "

qais "Hey knock it of you bi-"

isaa "Please, there’s no reason to be upset! We still have rations!"

"A third voice, sounding very young. Either a young boy or another girl."
"Rowan crept in closer. A minute later, he was close enough to see who the voices belonged to."
"Near the entrance to the mine, a group of… Adventurers, apparently, set up camp, and was in the middle of bickering with one another in a rather lively fashion."
"A young sorceresses, dressed in red robes, tried to lay her hands on a piece of paper desperately protected by a young man in leather armor. These must have been the first voices he heard."
"To the side, he noticed the likely owner of the third voice – a short haired… Boy, Rowan guessed? No older than 16. Hiding his face in his hands, he looked like was about to cry."
"There was another person, who kept his silence so far. A burly, serious man, with a long beard, tanned skin and a gentle, if disapproving gaze, sat next to the young boy. He wore a simple shirt, but Rowan quickly noticed a breastplate and a shield lying nearby."
"Again, Rowan crept a bit closer, kneeling behind one of the trees, trying to get a better look at the odd party, and to wait and see how the situation develops -"
"- but he wouldn’t get the opportunity to do so."
"He must have passed some sort of invisible line, because the the sorceresses head suddenly snapped upwards, and she turned her gaze in his direction."

$ sheenaName = "Sorceress"

shee "We have company."

"Like a well oiled dwarf mechanism, the group instantly sprung into action. The big man in the back jumped forward, grabbing his shield and sword, placing himself in the front."
"The other man and the woman positioned themselves behind him, by his sides, with the man taking out a crossbow, while the sorceress’s hand burst ablaze with magical fire."
"The boy lingered in the back, protected by the three clearly more experienced fighters."

$ qaisName = "Burly man"

qais "Show yourself, interloper!"

"With a soft sigh, Rowan stood up, and waved his arm from behind the tree."

ro "I mean you no harm! But I would prefer if the other guy lowered his crossbow before I leave cover."

"The three exchanged glances, then with some hesitation lowered their weapons."

show rowan necklace neutral at midleft with dissolve

"Rowan showed his face-"
"-and the woman gawked at him instantly."

shee "Holy shit."
shee "It’s Rowan Blackwell."

show rowan necklace shock at midleft with dissolve

"All of them, Rowan included, looked at her in surprise. It wasn’t often he would be recognized so quickly. There wasn’t anything particularly characteristic about his face or clothes – bar the magical amulet, but this was a recent addition."

qais "… Are you certain?"

shee "Yes! How could I not be!"

shee "Didn’t I tell you like, a thousand times how I saw Deanara and her party in Rastedel!  Of course I would recognize him!"

show rowan necklace neutral at midleft with dissolve

"The sorceress quite literally jumped up with giddiness, and waved at him, urging him to come closer."

shee "Mister Blackwell, please, join us!"

show rowan necklace happy at midleft with dissolve

shee "… We’d offer drider omelettes, but SOMEONE fucked up the recipe!"

show rowan necklace neutral at midleft with dissolve

"… Drider omelettes?"

$ bernName = "Young man"

bern "I told you I did not!"

qais "I don’t think it’s even possible to cook a drider egg…."

"Rowan shook his head as the group almost instantly forgot about his presence and descended into what he assumed was their usual bickering. It had been some time since he had seen a honest, proper adventuring group."
"Not that they weren’t present in Rosaria. With the nobles more or less completely ignoring the countryside, it wasn’t uncommon for people to hire mercenaries to deal with their problems."
"Though Rowan couldn’t help but feel the group in front of him was considerably more… Lighthearted than he had expected them to be."
"A sign of times, perhaps. With Karnas defeated, hope returned to Rosaria."

show rowan necklace concerned at midleft with dissolve

"… For a time, at least."

hide rowan with dissolve

"Normally Rowan might have paid no attention to random adventurers like that, but judging by their location, it was safe to assume they were here for the same purpose as he was. If they already scouted they mine, it would make his job that much easier."
"Adopting a pleasant smile, he joined the group for supper. With the “innovative” dish ruined, the party offered him some of their usual dried rations, and with them – customary introductions."
"The sorceress’s name proved to be Sheera. She was a fire mage who used to study in Rastedel and dreamed of becoming a heroine, just like Deanara was."
"The burly man called himself Qais. He was a mercenary from the Empire of Sand, but after seeing the destruction caused by Karnas he chose to quit the life of a sellsword and devote himself to hunting down the monsters that now plagued the countrysides of all the nations Karnas invaded."
"The man in leather told Rowan his name was Bernard, and that was that. He didn’t seem like the talkative kind, which contrasted with his earlier, loud behavior. Guess he only ever opened to people he was close with?"
"The last adventurer was a scrawny boy who, contrary to Bernard, just didn’t seem like the kind to open up at all. Sheera said his name is Isaac, and that the group rescued him from orc slavers two years ago. Ever since, the four of them travel together."
"Frowning, Rowan asked why exactly did they think that dragging an adolescent boy around for monster hunting was a good idea. This was no life for a kid!"

$ bernName = "Bernard"
$ sheenaName = "Sheena"
$ qaisName = "Qais"
$ isaaName = "Isaac"

shee "It’s fine, it’s fine."
shee "Isaac is stronger than he looks. He’s blessed by Solansia, you know?"

bern "Sheera!!"

"Bernard hissed at his companion, but the sorceress waved him off."

shee "Oh come on, you want me to keep things away from the Hero of Karst? He’s the most trustworthy person we could ever possibly meet, bar Deanara herself!"

bern "This is NOT your secret to tell!"

"The sorceress pouted."

shee "Sheesh, whatever… "

"Rowan looked at the boy, who turned his eyes away. He chose not to pry on the subject… At least not yet. "
"After they all exchanged backstories, before Sheera could shower with various question regarding his  time spent with Deanara, Rowan asked them what were they doing in the area."
"As he expected, they also heard the rumors about the mine being occupied by monsters, so they came to clear it out. But they didn’t find anything except a lone drider – whatever used to haunt the tunnels must have left a long time ago."
"As for the mine itself, they still saw traces of ore here and there, but it was hard to say if it was abandoned because of monsters, or because it was no longer profitable. Regardless, it could be reopened, and Rowan did a mental note to inform the castle of that as soon as possible."
"With his main objective achieved and the day nearing its end, Rowan asked if the group would mind if he joined them for the evening. It was always safer in a group, and he wouldn’t mind having some company for a change."
"Isaac didn’t mind at all, and if Bernard had anything against it, he decided to keep it to himself. Now, Sheera and Qais…"
"Both of them were all too happy about Rowan’s company. The sorceress kept finding more and more excuses to rub her body against him, or to lean forward so he could look down her cleavage."
"Her robes were loose enough that Rowan could easily see her modest breasts whenever she did so, and it would be a lie to say he didn’t look at least once. The sorceress noticed, the corners of her cute mouth turning upwards into a devious smirk."

if avatar.corruption > 49:
    "Rowan found himself responding to their flirtations, wholeheartedly enjoying the feeling of being courted. After all the time spent in Castle Bloodween, it was nice to spend some time with someone who didn’t have an ulterior motive when attempting to fuck him."
    "There would be nothing wrong with fooling around a bit, would there?"

elif avatar.corruption <= 50 and all_actors['alexia'].relation < 30:
    "Rowan found himself responding to their flirtations. With Alexia giving him the cold shoulder, he couldn’t help but enjoy being courted."
    "Surely nobody would blame him if he let himself have a little bit of fun for a change, would they?"
else:
    "Despite himself, Rowan found himself responding to their flirtations. He felt a bit guilty about doing so – with Alexia waiting for him back in Castle Bloodmeen, it didn’t feel right to mess around with other people."
    "Though It would be a nice way to release some tension… "

menu:
    "Encourage Sheena.":
        $ released_fix_rollback()
        jump encourageSheena
        
    "Encourage Qais.":
        $ released_fix_rollback()
        jump encourageQais

    "Keep things platonic.":
        $ released_fix_rollback()
        jump adventurersPlatonic


label encourageSheena:

scene black with fade
show rowan necklace happy behind black

"Smiling, Rowan turned his attention to Sheera, happily indulging her many questions about his past adventures."
"Sheera’s enthusiasm and general sunny disposition proved to be infectious, and Rowan quickly forgot about the many struggles he was forced to endure in present days."
"He gladly spent the evening reminiscing about old times, when thing weren’t nearly as complicated, and he didn’t need to balance his soul and Alexia’s safety with every decision."
"At one point, when they thought he wasn’t looking, he saw the sorceress smile triumphantly at Qais, who raised his hands in defeat."
"When night came, he laid to bed with the others, agreeing to take the last watch. But he didn’t sleep. He waited patiently, and as expected, half an hour later, he heard someone approach him."
"He opened his eyes and smiled at Sheera, who stared in surprise, before returning the gesture, again offering him that cute, devious smile of hers."
"She helped him get up, and with a skip in her step started to drag him into the woods."

ro "Should we just leave them like that?"

"Rowan asked, casting a glance at the reminder of the party. The sorceress smirked in response."

shee "We literally just killed the only thing that could ambush us, and I have magical alarms all around the camp. How did you think I noticed you earlier?"

ro "Fair."

"Choosing their steps carefully – at least Rowan was, the concept of sneaking was foreign to the woman – they left the camp, and started walking deep into the forest."
"Deep enough for that the two of them could talk comfortably, without the fear that they might be overheard. Or that they would wake up the others."

shee "Mhm! Yes, this will be perfect!"

"The sorceresses declared suddenly, once they were a fair distance from the camp. Without allowing Rowan a chance to respond, she jumped him, using the momentum to press him against the nearby tree."
"Her lips sought his, while her hands started to undress them both. She wasn’t wasting any time, and Rowan felt she’d rather just tear the clothes off him, if given the option."

ro "No foreplay?"

shee "Fuck foreplay. I want to feel the Hero of Karst inside of me already!"

ro "(Oh, so that’s what this is…)"

"Rowan didn’t mind a casual encounter, but he had no intention of letting the lively sorceress treat him like a trophy fuck. Annoyed, he grabbed her by the wrists, and with one swift motion turned their positions around, pinning her to the tree, arms over her head."

ro "Young lady, I think you got the wrong idea about who’s claiming who here."

"Sheera giggled in response, not at all dissatisfied with the sudden turnaround. She tried to lean in to kiss him again, but Rowan kept her firmly in place. Her enthusiasm was quite flattering – but he had no intention of letting her dictate the tempo."
"Exploiting the physical advantage he had over her, he locked the sorceress wrists with one hand, and used the other to undo the front of her robe."
"Sheera’s accursed mounds, previously taunting him with occasional appearances through the entire evening, were finally revealed to him in full glory."
"They were petite, but perky, with small, erect nipples. Rowan pinched one of them teasingly, then grabbed the teat forcefully, making his partner gasp."

shee "If you like them, why not give them a kiss?"

"The sorceress smirked at him mischievously, again, not at all discouraged by her current position. She kept trying to free herself, but it was a token effort."
"Rowan’s arm trailed lower, and with deliberate slowness started undoing her belt, revealing her nether regions."
"As he expected, her lower lips were not unlike her upper ones. Just like the sorceress couldn’t shut up her mouth for 5 minutes, so was her slit partially open, already wet and ready."

shee "You won’t be needing to force these gates open, general Zerias!"

ro "..."

"Rowan stared at her through half-lidded eyes. Sheera giggled again."
"Rowan thrust two fingers inside of her, evoking a delightful gasp from the sorceress."

ro "You talk too much."
ro "I’d much rather hear you keep squealing like this."

"Sheera smiled impishly, but this time spared him the commentary. Satisfied the girl was starting to listen, Rowan began to lazily explore her insides, setting up a steady, slow tempo, as he kept driving his fingers further into her."
"Sheera tried to get him to speed up, gyrating her hips to his movements, but whenever she did so, Rowan simply stopped. She grumbled with frustration, but rather than keep struggling, surrendered herself to his caresses."
"Satisfied with the result of his ministrations, Rowan started to thrust his fingers with greater enthusiasm."
"He released Sheera’s arms, staring her in the eyes as he did so. She dropped them to her sides obediently, while he used his newly freed hand to reach out and grab her perky breasts again."

shee "Aa-aah!"

"She left herself at Rowan’s mercy, moaning sweetly. Her eyes, her green eyes, betrayed her excitement as she awaited his next move."
"Not being in any hurry, Rowan kept exploring her pussy for a longer moment, paying careful attention to her growing excitement."
"When he breathing grew even deeper, he decided she’s finally ready. He leaned in for a passionate kiss, which the sorceress eagerly returned, then whispered in her ear:"

ro "Turn around. Hands on the tree."

"Sheera obeyed without a moment of hesitation, giddy at the prospect of finally being fucked by the hero of her childhood. She eagerly presented her cute ass to him, swaying it to the sides enticingly."
"Rowan undid his pants and, again, without any haste whatsoever, started to rub his phallus against her overflowing opening. Sheera whined in response, much to Rowan’s delight."

shee "Please… Haven’t you toyed with me enough, Rowan?"

ro "Maybe."

"It was tempting to just keep on toying with the sorceress, but doing it anymore would be simply cruel. For all her faults, Sheera did choose to play along, and it was high time she was rewarded for her obedience."
"Though perhaps not in a way the sorceress expected."
"He pushed the tip in, into the welcoming, warm folds of Sheera pussy. The woman tensed in anticipation. Was this finally it? Was her sweet torture at an end?"
"But Rowan’s tool would retreat as unexpectedly as it thrust in. Sheera turned her head to the hero, letting Rowan get a good look at her confused, fearful expression."

scene cg200 with fade
show rowan necklace happy behind cg200
pause 3

"With a smile, Rowan spread her ass-cheeks and started to push the tip of his penis forward, but not into the same hole as before."

shee "Oooo-ooooo?"

"The sorceress gasped in surprise, and unexpectedly burst into giggles. She threw him a wild smile, then braced herself better, ready to accommodate him with her tight asshole."
"His cock, wet with her juices, worked its way steadily into her depths. Her insides squeezed around him, too tight for his size. But rather than force his way in with one brutal stroke, Rowan kept pushing in gently, allowing Sheera’s anus to stretch with minimal pain."

ro "Brave girl. "

"Finally, his balls touched her ass. Against all odds, she managed to take him all the way in. His hand trailed against her back possessively, as Sheera waited for him to start moving."
"And he did just that."
"Slowly, but mercilessly, he started to fuck her tight asshole, pushing against her twitching inner muscles. She wasn’t used to it, but what she lacked in experience, she   made up with enthusiasm and endurance."

ro "Ready for me to go faster?"

shee "Yes!"

"Smirking, Rowan pick up the tempo methodically pounding her tight ass. Sheera moaned something incoherently – she no longer had the strength to keep throwing cheeky responses as she loved to do."
"Her head hung low, as she focused her attention on keeping her sphincter nicely relaxed for him."
"Ever the gentleman, Rowan resisted the temptation to pick up the pace any further – the poor sorceress was already barely holding herself together."
"He grabbed her sides firmly, helping her keep her posture as he kept thrusting in – her tight insides constantly trying to keep his cock in place, and constantly giving way as kept pushing in and out of her."

shee "A-aah! Aaah!"

"Rowan’s grunts and Sheera’s half-pained, half-ecstatic moans were the only sounds filling the forest now – and it would stay that way for a while, as Rowan was in no hurry to finish the girl off."

"But despite that, there was an end to even his endurance. Her narrow ass was simply too good to resist for long, and Rowan felt himself approach his limit."
"He buried himself deep inside of her, and reached between her legs once more, his hand seeking her overflowing pussy. He pushed his fingers into her, their movement mirroring the pistoning of his cock -"

shee "Aah!!"

"- and finally pushing her over the edge."
"A moment later, he came as well, his hot cum pouring into her freely. Sheera trembled in joy, and Rowan had to grab her by the stomach so she wouldn’t fall."
"He remained like that for a moment, lazily exploring her breasts as the sorceresses rested  with her body against the tree trunk."
"Breathing heavily, she turned her head around, and familiar devious smile forming on her lips."

shee "So that’s why general Zerias lost."
shee "He kept trying to force the front gate, rather then push into the backdoor!"

"Sheera's delighted giggle filled the forest, only to be stopped when Rowan thrust into her ass once more, shutting her up again."

#Set flag = “Fucked Sheera”, “Isaac mage”
$ fucked_sheera = True
$ isaac_mage = True
jump adventurersConclusion

############################################################

label encourageQais:

"Rowan turned to face the big man, flashing him a wide smile. The man was handsome, bronze skin stretched over a taut, muscled body. He was comely, to be certain." 
"Rowan decided to innocently prod him on his backstory. Out of the corner of his eye, he saw Sheera pout angrily. Her sulking did no escape Qais either, as the large man let out a low chuckle in his deep voice before answering him."

qais "There isn’t much to tell. My father owned a small farm in the southern regions. I worked there for most of my youth. "

"He cracked his neck and flexed his impressive shoulder muscles. Rowan noted the girth of them."
 
qais "It’s thanks to him that I’m as strong as an ox. "

shee "And almost as dumb as one, too."

"Qais snickered, making a rude gesture in the direction of the sorceress, who smirked and turned to talk to her other companions. She seemed resigned to Rowan’s choice of partner."

qais "The old man sired four of us, brothers all. He used to call us his little soldiers... till we all ended up a full head or so taller than him.  "

"His voice took a melancholic tone. Rowan saw Sheera roll her eyes in the background."

qais "Back then... I thought my might made me special. I was the youngest you see, and by the time I reached adolescence, my father was old and decrepit. I didn’t want to listen to his wisdom-"

shee "Oh Goddess, I can’t listen to this again! Ladies and gentlemen: the master of the mood-slayer! It’s like  the knight from Uverth all over again!"

"The gentle giant spread his hands defensively to try to calm the sorceress down."

qais "Sheera, that knight needed a night of comfort, not passion. A man like that… let’s just say tears dont make for good pillow talk."

bern "Is that why you make this story so fucking depressing every time you tell it?"

qais "Maybe I’m just hoping one day it will give life to your ironclad heart? Maybe even let me sneak my way into it?"

bern "Oh, fuck off."

qais "Hmm, I guess there’s still room for improvement."

"He winked at Rowan, and the hero shook his head with a smile. It was refreshing to see a man who wasn’t just looking for an easy lay." 
"…Though that did make Rowan somewhat self-conscious. An easy lay was exactly what he was looking for."

scene black with fade
show rowan necklace happy behind black

"The lighthearted, cozy atmosphere continued on through the evening, with the bratty sorceress doing her best to get under Qais’s skin, and the unflappable giant taking it all in stride." 
"It was almost a shame to see the sun go down. Stifling yawns, the rest of the group headed to their bedrolls." 
"Leaving Rowan and Qais alone to take the first watch."

shee "… If you two wake me up before daybreak, I’m flinging fireballs."

"Rowan shared a smile with Qais, but said nothing.  The burly man’s dark eyes gleamed with mirth in the firelight. There was no hurry, and the quiet conversation was pleasant."
"Almost an hour passed, the night deepening to a comforting stillness. After a while, Qais stood up from the campfire and stretched. Rowan liked the sight of his tanned muscles flexing, the casual strength of his thick biceps." 
"Without a word, Qais headed for the woods. He shot Rowan a glance and a smile over his shoulder, indicating with his eyes for him to follow."
"Rowan tramped a short ways behind Qais through the woods, fascinated by the calm, assertive way he moved. He was a bulky fellow, but he carried himself with the ease of a far more limber man." 
"Qais stopped only a short distance away from the camp. Rowan looked back - the tents were still within eyeshot. Qais chuckled at his unspoken concern."

qais "We’re on guard duty, it would be irresponsible to leave them {i}completely{/i} unprotected."

ro "And on the off-chance someone hears us…?"

qais "Isaac sleeps like a log, and Bernard - despite his attitude - understands all too well how necessary stress release can be."

"The big man shrugged, flashing Rowan a sultry smile."

qais "Besides, Sheera is going to be insufferable whether we wake her or not. So we might as well give her ample reason to be."

ro "And here I thought you were the ‘matron’ of the team."

"Rowan felt a thrill run down his spine at the smirk Qais gave in response to the little jab."

qais "I am. But even a matron needs to let her kids run free and focus on herself, for once."

"Qais quirked an eyebrow, looking Rowan up and down before unbuckling his sword belt. Rowan noticed for the first time how large his hands were."

qais "-And just so we’re clear:  you’re gonna pay for that last comment."

"Rowan’s heart pumped a little faster as he hurriedly undid his own sword belt."

ro "Don’t threaten me with a good time unless you intend to follow through on that threat."

"Qais chuckled, his deep voice rolling off into a masculine purr. Rowan watched, mesmerized as he removed his shirt, exposing his rippling chest. He was hairy, with fine black curls coating his tawny skin in a patch of thick fuzz."
"Here, was a man."
"As Qais removed his trousers, he let out a low grunt, nodding at Rowan’s still-clothed body. Rowan peeled off his shirt, exposing his pale chest. Qais’ eyes drifted across his body with the appraisal of a man who knew the value of things."

qais "There’s something I wanted to ask you. Everybody knows of your skill in commanding men."
qais "But was there ever a man you wished to serve {i}under{/i}?"

"Rowan  narrowed his eyes at the large man, doing his best to hold back a smile as he unbuttoned his pants. Qais expression was that of pure innocence, as if his words were not dripping with innuendo."

ro "Perhaps there was. "

qais "They must have been quite remarkable, to attract your attention. "

ro "Would you rather be {i}with{/i} them?"

qais "No. I’d rather {i}be{/i} them."

"And just like that he was in the man’s arms. Rowan let out a heavy breath, settling into Qais’ embrace as the two locked lips. His thick beard tickled his chin, his cock stiffening as he drew close to the imposing warrior."
"Qais’ large hands settled on Rowan’s shoulders, rubbing his back in soft circles. Despite his formidable frame, the man was quite the gentle giant. Rowan let out a groan of pleasure, kneading Qais’ biceps in wonder at their thickness."
"His scent was heavy, masculine and potent. A lingering sheen of sweat made his swarthy skin glisten in the night air. Rowan breathed it in with a pleasured sigh."
"There was little time for foreplay. Despite their mutual attraction, both men were still professionals. An absent night watchman spelled doom for a sleeping camp. They would have to be quick about this."
"Fortunately for Rowan, Qais knew what he wanted. His thick hands drifted down to cup Rowan’s butt, kneading the cheeks as he pulled him close. Rowan could feel Qais’ large erection poking him in the stomach."

qais "Supple."

"Qais said the word as if that was all there was to say on the matter. Rowan almost let out a bawdy joke, but instead groaned as he felt Qais’ large finger sink into his ass."

qais "Turn around, Hero."

"His voice was deep, but his tone was soft. Rowan, blushing, turned around. Qais sat back against a nearby tree trunk, spreading Rowan’s cheeks as he examined his nethers."
"Rowan stood half bent over with his hands to his thighs, bearing the embarrassing position as best as he could."
"Thick fingers trailed across Rowan’s growing erection before moving once more to his ass."
"He stuck his index finger in his rump again, letting out a huff of appreciation when he managed to push to the second joint before encountering stiffer resistance."

"Qais pulled his index finger free, only to replace it with the one on his other hand. Rowan groaned as he felt the finger press deep inside, wigging back and forth to test the proverbial waters."

qais "Relax, Rowan. Breathe..."

"Qais’ warm breath at his neck made Rowan shudder with anticipation. He did as he asked, taking in slower, deeper breaths as he relaxed his contracting muscles. Qais pulled free from Rowans ass, planting his hands on the hero’s hips."

qais "Easy now, slow and steady. Lean back into me."

"Rowan leaned back, falling into Qais’ lap as the heat of his skin suffused him. Rowan felt the weight of the man beneath him, his back rubbing up against Qais’ hairy chest." 
"He positioned himself as best he could, spreading his legs to either side of Qais’ as the burly man angled his thick erection towards his ass. Rowan’s knees trembled, his face scrunching in both embarrassment and excitement."
"He shuddered as he felt the head of Qais’ dick press against his anus. His large hands pulled Rowan downwards, drawing him inexorably deeper onto a proper mounting of the adventurer’s cock."
"It came as a shock when their genitals made physical contact. An electric thrill ran up Rowan’s spine, pain and pleasure mixed together as he sank down onto Qais’ dick."

qais "Relax…"

"His big hands were at Rowan’s shoulders now, kneading them softly to accentuate his point. Rowan took in a deep breath and relaxed, feeling his whole body follow suit." 
"Qais’ cock slowly entered him, inch by inch, sinking deep into his ass. Rowan felt his own erection harden still further as the girthy length entered him, blood flowing like a river to his extremities."
"He got nearly halfway down the shaft before Rowan had to pause. He was panting, his stomach clenching tight from the sensation of the intruder in his insides."
"It was a deep, filling sensation. Qais’ cock throbbed inside of him, like a second heartbeat radiating erotic heat into his body."
"Qais’ hands lifted him, guiding Rowan upwards. They paused at the apex of the thrust, with just the tip of his cock still inside of him."

qais "Ready?"

ro "Yeah..."

"The big man’s hands pulled down on him again, sliding deep into his rectum. Rowan grunted, feeling every inch entering him as Qais’ member throbbed with each stroke."
"The thrusts were slow at first, building in momentum as they continued onward."
"Soon the hot, wet {i}slaps{/i} of human copulation filled the night air. Rowan moaned, reaching down to jerk himself off as Qais took control, bucking his hips upwards in tune with Rowan’s downstrokes."

ro "{i}Aaah!{/i}"

"Rowan’s hand leapt from his precum-slick dick to cover his mouth in embarrassment."
"Qais had poked his prostate so hard and so suddenly that he had nearly cum then and there. The large man chuckled, his hot breath tickling the back of Rowans neck."

qais "Careful, hero. Wouldn’t want our fun to end so soon, would you?"

"Qais leaned his head forward and kissed the back of Rowan’s shoulder, the tanned adonis’ thick beard tickling his skin with its raspy texture. Rowan moaned, reveling in Qais’ masculine body, the way he held him tight and wouldn’t let go."
"He was beautiful, this untamed stallion that Rowan was riding."
"Having found Rowan’s g-spot, Qais made a point to time his thrusts to caress it each time he reached the downswing. It was maddening, like he was trying to test the limits of Rowan’s resistance."
"Rowan moaned, leaning back to plant his hand on Qais’ tanned shoulder for support as the thrusts went ever deeper. He continued to jerk himself furiously with the other hand, an orgasm rising like a crashing wave."
"Qais let out a deep growl at the base of his throat. While he’d been a gentle lover at first, now he had revved up to full speed. His breathing deepened, manly exhales of exertion that Rowan replied in desperate kind."
"The thrusts came shorter and deeper now. More than once Rowan felt his hips connect with Qais’ own, their balls touching together as Rowan settled onto his man-made love seat. The pain was gone, replaced only by a growing need to cum."
"Qais’ cock twitched once, twice, three times, then unloaded. Rowan heard his breathing quicken into shallow breaths, then a final, loud exhale."

qais "{i}Aaahn{/i}, R-rowan!"

"Rowan jerked himself like a horny , his body clenching in pleasure as he created a vice-like grip on Qais’ fat cock. He gasped, feeling it thicken and bulge inside of him as Qais’ testicles clenched beneath him."

ro "Come on! Let it out!"

"Qais did as he was told. His large hands dragged Rowan down into his lap and held him there, his breath expelling in great gouts as he came. Rowan felt a sudden warmth blossom inside him, spurts of cum firing off into his deepest places as he felt himself."
"Rowan took his own advice, letting out a cry of pleasure as his cock spurted a jet of ivory liquid high into the air, he clenched and held in place, feeling the warmth blooming from inside his ass."
"The two stayed there for a long moment, reveling in the joy of post-orgasmic bliss. Qais tilted Rowans head around to look at him fondly for a moment, then planted a slow kiss on his lips."

qais "Just as good as I imagined."

"His quiet voice was comforting, but also filled with a certain… pride? As if Rowan had been the easy lay, rather than the other way around."

ro "Does that mean you’re ready for round two?"

"Qais let out a low laugh."

qais "I’ll be lucky to feel my legs in the morning, at this point."

$ rowanGaySex += 1
$ isaac_mage = True
jump adventurersConclusion

###########################################################
label adventurersPlatonic:

#If Alexia influence is 50 or higher.
if all_actors['alexia'].relation > 50:
     "Rowan turned down both of them, kindly noting that he was, in fact, a married man."
else:
    "Rowan turned down both of them, preferring not to sleep with every random stranger he met on his travels."

#rejoin.
"Instead, he paid more attention to the other half of the party, hoping to get them to open up."
"With no success. Bernard said he had no intention of sharing his life story with every stranger on the road, hero or not-"

shee "He’s a reformed criminal who killed his bandit chief when he learned he was engaged in child slavery!"

bern "Dammit woman!"

"… While Isaac still didn’t want to open up. The kid kept staring at him though, like there was something he wanted to say after all, but couldn’t bring himself to do it."
"Every attempt and finding some common ground with the boy proved unsuccessful. As night came, Rowan headed to bed defeated, informing the others he would take the last watch.
Isaac took the one before him."
"…"
"The boy woke him up at the agreed hour. With a polite “Thanks kid”, the hero headed to the front of the camp."
"Isaac stood motionless for a moment, then followed suit."

show rowan necklace happy at midleft with dissolve

ro "Something bothering you, Isaac?"

isaa "…"

show rowan necklace concerned at midleft with dissolve

isaa "There is darkness in you. I feel it."

"Isaac kicked the ground, eyes down."

if avatar.corruption > 69:
    isaa "It’s… Suffocating. It envelops you. Surrounds you. Taints everything you touch."

elif avatar.corruption < 69 and avatar.corruption > 30:
    isaa "It’s like a… Stain. Living… Expanding. Tainting you."

else:
    isaa "It’s… Subtle. But it’s there."

isaa "But you don’t seem bad… So I didn’t want to say anything with the others listening."
isaa "Are you…"
isaa "Are you okay, Mister Blackwell?"

show rowan necklace shock at midleft with dissolve

ro "What?"

isaa "Well… Everyone kept saying what a great hero you were, so… Something bad must have happened to you… Against your will… I think?"

show rowan necklace neutral at midleft with dissolve

"Goodness gracious…  It was heartwarming to see the kid show such concern for someone who in his eyes had to be tainted."
"Naive as well. Heartwarming, but naive."

ro "You could say so."

"Still..."

if avatar.corruption > 69:
    "“Tainting everything he touched”?  That sounded pretty ominous."
    "He knew, the moment he agreed to serve the twins, that he wouldn’t be able to keep himself pure. But was the situation this bad already?"

else:
    "He wasn’t surprised his aura wasn’t entirely pure. He knew this would happen the moment he agreed to serve the twins."

ro "I was forced to make some… Difficult choices."
ro "It’s a long story."

isaa "… I see."

"The kid wasn’t one to push an uncomfortable subject, and for that, Rowan was grateful."
"Though the fact he was capable of seeing the twin’s influence on him was… Worrying. It shouldn’t be possible for most faithful – the kid obviously had strong affinity for divine magic."

show rowan necklace concerned at midleft with dissolve

ro "Do you… See such things often?"

"Isaac kicked the ground again. He still refused to meet his eyes."

isaa "Sometimes."
isaa "An abbey we passed a while ago felt… Wrong."
isaa "The others wanted to investigate it, but I begged them not to."

"His voice dropped to a whisper."

isaa "I don’t think we’d survive if we did."
isaa "Then there was this big woman in Rastedel… "
isaa "I… Think she felt I felt something, because when we crossed gazes, she smiled this sweet, friendly smile, and started walking in my direction. "
isaa "But then I think she saw Qais and Bernard, and I quickly lost her in the crowd."

#if past week 49
if week > 49:
    isaa "And recently, the entire region just feels… Wrong."
    isaa "I don’t think we’ll stay here."
else:
    pass

"Rowan studied the boy closely. He was no expert on the matter of magic, but he could see a hero in the making when he saw one."

ro "You have a rare gift. Why haven’t you joined the church?"
ro "They would welcome you with open arms in Prothea."

isaa "… It wasn’t Prothea that saved me. And It wasn’t Solansia that protected me."
isaa "Or my family."

"His voice was now that of an angry whisper. He turned his head to the sleeping adventurers."

isaa "I owe everything to them. I won’t abandon them."
isaa "Not even for a Goddess."

menu:
    "Tell him he could serve Solansia and still help his friends.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "You don’t have to. You can embrace your gift without turning your back on them."
        ro "Didn’t Deanara herself lead a ragtag bunch of heroes despite being Solansia’s chosen?"
        "Isaac smiled gently, but didn’t seem fully convinced."
        isaa "I guess she did."
        ro "We all have our part to play in all of this, Isaac. We might not always like the roles that have been given to us… But Solansia picks her chosen for a reason."
        ro "Sometimes to save people she herself couldn’t reach."
        ro "You can do much good in the world, but you’ll have to put your faith in the Goddess."
        "Isaac finally met his eyes, hesitating with his response. Coming from someone else, Rowan’s word would ring hollow."
        "But hearing them from the Hero who helped slay Karnas… It gave them weight."
        isaa "… I’ll think about it."
        "Rowan nodded solemnly-"
        "- then, he ruffled his hair affectionately."
        isaa "H-hey! Stop it!"
        "He couldn’t help himself. Precious kid. Goddess knew he needed it."
        #set flag = “Isaac Cleric”. Gain small favour with Solansia.
        $ isaac_cleric = True
        #$ change_favor('solansia', 2)

    "Tell him he should follow his own path.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "I understand."
        ro "… When we slayed Karnas, many years ago, not everyone had their fill of blood yet."
        ro "Some people had enough of the noble rule. They thought it was time for a change."
        show rowan necklace concerned at midleft with dissolve
        ro "They came to me, and asked me to lead them into battle. To tear down the society they thought unjust."
        show rowan necklace neutral at midleft with dissolve
        ro "I refused. All of them. I didn’t… I didn’t want to spend all my life fighting. I had someone waiting for me back home. I wanted a different life for us both."
        isaa "… I take it that didn’t work out, then?"
        "Rowan laughed bitterly."
        ro "Oh, it did… For a while."
        ro "But I guess destiny doesn’t look kindly on people who refuse its call."
        ro "And I never regretted my choice, present complications notwithstanding."
        ro "The point is, kid – never let anyone rope you into a war that isn’t yours. Always fight for what you believe in."
        if serveChoice == 2:
            "His own words sounded hollow to him. Never fight a war you don’t believe in? He joined the twin’s out fear, not conviction."
            "And now he paid the price fort that. Every day. Some role model he was."
            "… But that wasn’t what the boy needed to hear right now."
        else:
            pass
        ro "You can be who you want to be.  Don’t let anyone convince you otherwise, Solansia blessing or not."
        "Isaac nodded solemnly, a determined expression on his face."
        isaa "I will. I promise."
        "He would grow up to be someone noteworthy, of that, Rowan was certain."
        #Set flag = “Isaac mage”, slightly increase favor with Kharos.
        $ isaac_mage = True
        $ change_favor('kharos', 2)

        show rowan necklace happy at midleft with dissolve

ro " Alright, that’s enough philosophical discussions for today."

isaa "… The sun has yet to come up. "

ro "Yes."

show rowan necklace neutral at midleft with dissolve

ro "Yes, the sun has yet to come up."

show rowan necklace happy at midleft with dissolve

ro "Get some rest. Even if only for an hour."
"The boy nodded, and left Rowan alone for the reminder of the night."

label adventurersConclusion:

scene black with fade

"Morning came, and the adventuring party gathered for breakfast, with Rowan joining them."
"They inquired if he would also join them in their travels, at least for a while. The group was heading west, planning to walk the southern bank of river Yael till they reach the coast, and then turn north, into forest Ealoaen."
"The prospect of some honest company wasn’t an unpleasant one, but Ealoaen wasn’t his target at the moment, and even if it was, he couldn’t allow himself to be limited by people who didn’t know the nature of his present quest."
"So instead, they exchanged some information on the surrounding area."
"Among the general advice, they also told him there were rumors of a massive orc camp between the river and the mountains to the north, west of Rastadel. That’s why the wanted to stick to the southern bank, to avoid any possible orc raiding parties."

show rowan necklace neutral at midleft with dissolve

#if rowan has visited the orciad camp
if orciad_state > 0:
    ro "(That would be Ulcro’s/Batri’s/Tarish’s camp. Wise choice on their part.)"
else:
    ro "(Hmm. Might be worth checking out.)"

#rejoin
"With that, their business was concluded, and it was time say their goodbyes."

qais " It was an honour meeting you, Rowan."

show rowan necklace happy at midleft with dissolve

ro "The honor is all mine. I still can’t believe I ran into an actual adventuring party!"

shee "Ha, how is that surprising? Do you know how many orc camps they have in Rosaria? Dozens!"

#if Rowan has claimed at visited 3 orc camps
#bern "But they haven’t been very active recently… "
#bern "Something must be going on."
#qais "Perhaps. But I fear that this time we’ll have to leave that to the nobles."
#"Bernard spit to the side, obviously not convinced they would be of any use."
#"And being very right in that regard."
#else
#pass

ro "Regardless, let’s just say it was a nice change of pace."
ro "I wish you all good luck."

shee "Aye aye! Tell Deanara to ask about Sheera of Arkeny, if she’ll be visiting the elf lands next year by any chance!"

bern "Yeah, take care."

isaa " … Stay safe, Mister Blackwell."

"They lingered for a moment, delaying the goodbye, until Qais nudged Isaac gently, and the four finally started moving. Rowan stayed behind, having told them he needed to take one last look at the mine – and already contacting Castle Bloodmeen to have them send people in."
"If he ever finds himself in Ealoaen, he should keep an eye out for these guys."

#Show usual mine menu.
# Gain normal mine rewards. Reduce corruption a little. Reveal all hexes within a radius on 3, but keep them unexplored/ grayed out.
# roll 1d10.
# on 10, add “Drider omelette recipe” to the inventory.
#Drider omelette recipe
#Icon: A piece of paper.
#Value: 0
#Description: “The fabled omelette recipe. Someone must have put it in your backpack by mistake. Due to wet stains on the paper, likely from being left in the open during a passing rain, the writing has been rendered completely Illegible.”
$ change_base_stat('c', -2)
$ temp2 = mines_defs[eventHex[6]][1]
$ temp3 = mines_defs[eventHex[6]][2]
$ temp4 = temp2 * miner_cost
menu:
    # Choice 1: Hire workers
    # costs some gold.
    "Hire workers ([temp4] gold)" if castle.treasury >= temp4:
        $ released_fix_rollback()
        $ change_treasury(-temp4)
        $ castle.mines += 1
        $ castle.iron_per_week += temp3
    # Choice 2: Deploy Soldiers
    # costs some soldiers, but also some morale.
    # TODO count soldiers able working at mine (different barracks)
    "Deploy Soldiers ([temp2] soldiers)" if castle.buildings['barracks'].troops >= temp2:
        $ released_fix_rollback()
        $ castle.buildings['barracks'].troops -= temp2
        $ castle.morale -= temp2
        $ castle.mines += 1
        $ castle.iron_per_week += temp3
    #Choice 3: Leave
    #does nothing, but leaves the mine unexplored so that the player can come back later.
    "Leave":
        $ released_fix_rollback()
        $ prevent_tile_exploration()
return
