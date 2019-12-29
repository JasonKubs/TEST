init python:
    
    event('powerless', triggers='week_end', conditions=('all_actors["alexia"].flags["andras_influence"] > 5','all_actors["alexia"].relation < 50', 'alexiaJezObedient == False',), depends=('alexia_med_corruption',), run_count=1, priority=pr_story)
    

label powerless:
    
if rowan_shares_room_with_helayna == False:
    scene bg9 with fade
    "The morning sun was streaming through the window when Alexia awoke from her slumber, roused from her sleep by the noise in the room. It was her husband, Rowan, who was already up from their bed, and fully dressed."
    show alexia necklace neutral at midleft with dissolve
    show rowan necklace neutral at midright with dissolve
    al "You are up early this morning, my love."
    "Rowan had been facing the desk. He stopped what he was doing, and turned to smile at her."
    ro "Another busy day out in the field, no rest for the wicked I’m afraid."
    if all_actors["alexia"].relation < 25:
        "So her husband was leaving her. All alone. Again. Was it just her impression, or has been avoiding her lately? What excuse did he have for her this time?"
    else:
        "She smiled back, but felt a small twinge in her heart. She couldn’t help but feel he was working himself too hard, and all on her account as well. He may be the most capable man she ever knew, at some point though it would be all too much for even him."
        al "Alright my love, you just be careful though, okay?"
    
else:
    scene bg13 with fade
    "She sat up and wiped the sleep of her eyes.  There was only one person who would enter her room without knocking. "
    show alexia necklace neutral at midleft with dissolve
    if all_actors["alexia"].relation > 25:
        al "Is that you, my love? "
    else:
        al "Is that you, Rowan?"
    show rowan necklace neutral at midright with dissolve
    "He graced with a soft smile. He stopped by her desk, and she could see a folded up note on it, no doubt just left by him"
    if all_actors["alexia"].relation < 25:
        if raeve_keep_rowan_claimed_helayna:
            "She felt her temper rise on the spot. So this was their marriage now? Not only did he want to replace her with that noble slut, but now they were to communicate through notes?!"
        else:
            "She felt her temper rise on the spot. So this was their marriage now? Separate bedrooms, and communicating through notes? "
    ro "Good morning my love. Sorry for waking you up."
    if all_actors["alexia"].relation < 25:
        if raeve_keep_rowan_claimed_helayna == False:
            show alexia necklace happy at midleft with dissolve
            al "Wasn’t the entire point of separate bedrooms avoiding precisely this very scenario? With you coming in and out at odd hours?"
            ro "Hey, it was working out splendidly... Up to this very moment. "
            al "I suppose so. So what’s the matter? Did something happen?"
        else:
            "He answered his smile with her own, warm one. Always looking out after her comfort..."
            al "Don’t worry about it. But why the sudden intrusion? Did something happen? "
            ro "Everything is fine. Another busy day out in the field, no rest for the wicked I’m afraid."
            
ro "I was just leaving you a note. The twins want me to survey troop movements out in the field, but Andras has asked me to deliver orders to his orcs."
            
"He indicated towards the desk where she could see he had placed some sort of document, presumably Andras’ orders."

ro "Unfortunately, the orcs are about as well organized as their master. I went by the barracks earlier, but there was no one around to give the orders too."
ro "Probably all still in their bunks from yet another late night of heavy drinking. "

"Alexia nodded, she’d often seen orcs stumbling down the corridors late at night, and even sometimes in the morning. Her husband had always told her discipline was the most important attribute of a soldier, and they seemed to have zero."

al "Have you tried whipping them? "

if avatar.corruption > 60:
    ro "Yes, and digging latrines, AND actual decimation. But every time I make some progress Andras just finds new, creative ways of undoing it."
else:
    ro "Doesn’t really help. I’ve been testing more creative solutions, but… No successes thus far. "
    
ro "But I won’t bore you with the details. Would you mind dropping this off by the barracks later in the day, when you have a moment?"

al "Of course darling, it is no problem."

if all_actors["alexia"].relation < 25:
    "She quietly wondered if he actually admired all the things she did to make his life in the castle easier and more comfortable… "
    "Probably not. Men always were like this. Just took everything you did for them for granted…  "
    
ro "Thank you. It should take you but a minute. Andras said to give them to an orc called Drokk, big fellow. If you can’t see him, just ask one of the other orcs to point you in the right direction. "

al "Okay, I’ll drop it off later in the morning."

ro "That’s fine. If anybody gives you any trouble, you let me know okay?"
ro "Now you get some more rest, I didn’t mean to wake you up."

scene black with fade

"After the pleasantries of parting for yet another day, Alexia lay her head back down on the cool pillow, and was starting to drift away just as she heard the door quietly click shut…"

scene bg14 with fade

"Alexia didn’t have much to do today, so when she woke up, she got ready and made her way through the castle hallways to visit the barracks and drop off the orders."

scene bg11 with fade

"By the time she got to the barracks, it was mid-morning. The place, however, was still mostly empty. It seemed even by this time, the orcs were still either too tired, too hungover, or too lazy to report for duty."
"In fact, there was only one group of orcs currently in the room, all hunched around a table at the far end. Three male orcs, and one female. One of the males was exceptionally large, even for an orc."
"If she was in luck, this would be Drokk, and she could hand the orders over and get out before any more orcs turned up."
"The orcs were making a lot of noise, and as she approached the table, it died down to an almost eerie silence. The big orc glared at her."

show alexia 2 necklace concerned at midleft with dissolve
show wild orc neutral at midright with dissolve

drok "What da fuk you want humi?"

"Alexia was taken aback by his aggressive tone. Even after all this time in castle Bloodmeen, the casual vulgarity of the orcs and their lack of basic decency still caught her off guard, even if only from time to time nowadays."

show orc soldier neutral at edgeright with dissolve

os "Ha, looks like dis one scared of yous, Drokk."

show alexia 2 necklace neutral at midleft with dissolve

if all_actors["alexia"].relation < 25:
    "For the second time this day, she felt her temper spike. She started the day in a foul mood, and like hell was she going to let a bunch of orcs ruin it further."
else:
    "Alexia steeled herself, trying to control her rising temper. She wasn’t going to let a bunch of stinking orcs disrespect her! Prisoner or not, she was the wife of their direct commanding officer, and they should know better than this!"
    
al "My husband, Rowan, asked me to deliver these new orders to you. They are to be followed to the letter."

"Drokk snatched the orders from her hands and glanced at them."

$ drokkname = "Drokk"

drok "You waits der, pink slut."

"The other orcs fell about laughing at their boss’ insult, as if it had any shred of originality in it. At this point, she didn’t know what angered her more, the disrespect, or the lack of creativity."

menu:
    "Leave.":
        $ released_fix_rollback()
        "She knew better than to say anything nasty back as a response, that would only escalate the situation, and orcs lacked common sense. Starting an argument with one could soon turn dangerous, she’d seen them fighting when drunk around the castle enough times to know that."
        al "No. I have delivered your orders like I was asked, and now my job is done. I have other duties in the castle that are more important than standing here being insulted by you and your orc friends for the rest of the day."
        drok "Look. Pathetic humi so eager to scurry back to her master like good little pet."
        "Laughter roared from the table once again, but Alexia had heard enough. She turned on her heels and headed toward the barracks door." 
        "More insults, lewder than the ones she had already been subjected to, rang out from behind her, but she ignored them. It was clear they were trying to get a rise from her, and she would not give them the satisfaction of causing one."  
        "Reaching the door, she exited into the hallway, leaving the barracks, and any thoughts of the orcs that currently resides in it, behind her as she went about the rest of her day."
        return
        
    "Insult him back.":
        $ released_fix_rollback()
        jump drokkscene
        
label drokkscene:

show alexia 2 necklace happy at midleft with dissolve

al "I’m surprised you have enough of a brain to discern more than the basic three colors. "
al "But worry not, I understand. I’ll politely wait for you to finish flexing your muscles to your friends, so that you can crawl to me later and beg me to read the orders for you, you illiterate shriveled cucumber. "

"The orcs around the table whooped with more laughter, one Drokk did not participate in this time. He simply glared at Alexia, face twisted in anger."

femorc "I like dis one, she got spunk."

drok "She gon’ get spunk, if she don’t shut her stoopid whore mouth."

al "If anyone should watch their mouth, it is you, orc. I’m the wife of your commander, and if he heard the way you are speaking to me-"

drok "Hahaha, and pink slut puni human would do wat? She think tiny pinkskin can hurt mighty Drokk?"

femorc "Puni humi too busy running twinses errands to do anyfin’ anyway. Don’t even have time to deliver orders, bwahaha! "

os "Guess that makes you the twinses bitch’s bitch!"

drok "Not even pink slut! Slut’s slut!"

show alexia 2 necklace angry at midleft with dissolve

"More laughter. How dare they- How dare they-! "

al "Oh, I’m sure my husband wouldn’t be too busy to order the whole lot of your executed. I’m thinking…"

menu:
    "Decapitation.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +1)
        pass
        
    "Burning on a stake.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +2)
        pass
    
    "Sawing in half.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +3)
        pass

    "Skinning, then boiling alive.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +4)
        pass

al "… Would be nothing more but another errand for him. "

"She wasn’t sure why she said that. This wasn’t like her. But seeing their shocked, horrified faces made it worth it." 
"Drokk brought his massive first down on the table, the slam shaking his comrades out of their shock. If looks could kill…"

drok "Pinkslut {b}dares{/b} to threaten Drokk?!"

"All her life, she was taught to deescalate rather than escalate.Turn the other cheek." 
"… And she was starting to have enough of it. After everything that had been said, Alexia wasn’t about to back down, no matter how scary the orc might look in the moment." 

al "It wasn’t a threat."

"The other orcs sat watching the twist that the scene had taken, uncharacteristically silent, waiting to see what their boss would do. Meanwhile Drokk was also silent, clearly contemplating whether the woman could actually have him executed."

"Moments passed, and Alexia started to feel a unfamiliar glow raise in her chest. Giddy with happiness, she felt a triumphant smile creep onto her face.That will teach them! Stupid orcs, always acting rude and thinking they’re better than everyone-"

drok "No."

"The word cut through the air like an executioner's axe. Drokk gave her a small, almost pitying smile."

drok "No. Is nice bluff, slut, but Drokk mighty champion of Andras. Master Andras never let puni humi execute great warrior like Drokk."

"He chuckled and leaned back, spreading his arms, as if asking her “What now?”. The orcs around them felt the tide turn, mocking smiles and crude remarks quickly resurfacing. "

femorc "Everyone know pink humi Andras bitch. Won’t touch Drokk without master letting him."

os "Pink slut talk big, that’s all. Should use 'er mouth for suckin' cock instead." 
    
"Her laughter burned her ears. They were right, if Drokk really was Andras favourite, the red demon would never let Rowan touch it." 
"…" 
"But Andras had other favourites as well." 

show alexia 2 necklace happy at midleft with dissolve

al "I suppose you are right. Andras does respect strength and he does need warriors…"

"The smug look didn’t budge from his face, but the orc began to wonder why the human was smiling when he was the one who was right."

al "But “our” Master Andras also has other, more important needs… "

"His smile started to melt, while hers grew. Her mouth moved faster than her mind would register, and yet she kept talking. Nothing mattered anymore, except seeing that bastard brought down a notch."

al "I’m sure you’ve all noticed the way he looks at me. The way his eyes roam over me, over my tits… Over my ass."

"She leaned forward over the table, and hiked her skirt, giving the orcs a good view of both. One was smart enough to look away. "

al "Oooh, you did, didn’t you? You’ve seen how he hungers for me, how he desires his servant’s wife."
al "That’s all you all just sit here, like a bunch of eunuchs. None of you will touch me. All you can do is fantasizes about the things you would like to do to me…"

if all_actors["alexia"].corruption > 60:
    al "Force me to my knees to make me worship your cock. Stretch out my holes with your fat, green dicks. Fill me with all your hot, thick seed until it oozes from my red, well used cunt and loose asshole."
    al "Humans are just cocksleeves for your pleasure, and to bear your children after all, aren’t they? I’m sure you’ve all had your impotent revenge fantasies of turning the wife of the “pathetic humi” who orders you around into your personal cumdumpster."
    "She laughed out loud, not noticing how her voice carried across the silent room."
    
al "And perhaps you even heard some rumours about me. That maybe, just maybe... I’m not all that… Unapproachable. "

"The other orcs watched, still silenced by the events that had unfolded before their eyes. She watched, with growing satisfaction, the lust in some, and impotent rage in others."

al "What do you think would happen then, if I were to tell him about the things you have said to me?"
al "Do you think he would appreciate a lowy, pathetic orcs like YOU thinking he was entitled to the very thing HE himself coveted so much?"

drok "..."
drok "You try too hard humi. Maybe Andras be mad about what Drokk say, but Drokk only insult you. Andras no kill good warrior over dis. Plus you just humi, would be bad for morale."

al "Do you listen to yourself, Drokk? Andras kills an orc if the bath he drew is too lukewarm for his tastes."
al "… But you are right, I suppose. If you are as valuable as you claim… Then he might not *kill you* for simply insulting me… Beat you up a little, but not kill you. "
al "Now, if I were to do this…  "

show alexia 2 necklace concerned at midleft with dissolve

"Alexia made an anguished expression, and started to wipe imaginary tears off her face."

al "“Master Andras, Master Andras! … I- I went to the barracks… There was this o-orc… I think his name wa-as Dro-kk…. And he… He…”"
al "“He said I-I was to get n-naked and spread my l-legs… I told him I’d never touch a filthy orc like him. So he-”"
al "“He threw against the table, and- Oh Master Andras! He took his dick out and-!”"

show alexia 2 necklace happy at midleft with dissolve

al "I’m sure you can imagine the rest."
al "Do you think he would punish you  then? Do you think there’s a chance he’d be my protector and saviour?"

if all_actors["alexia"].corruption > 60:
    al "Imagine the things I could do to entice him. I’d ask him to cleanse my violated pussy with his massive cock, keep pumping me full of cum till he washes out the pathetic load left by you."
    
"Seeing Drokk tremble with rage was the sweetest thing she had experienced in all her captivity in Bloodmeen. Ah, if she could just save this moment for all eternity! "

al "So, orc, do you still feel like playing stubborn, or would you rather change your tone? Apologize maybe? "

if all_actors["alexia"].corruption > 60:
    al "If you want my advice, I’d start with getting on your knees, and licking the soles of my boots. "
    
drok "GAAAAAAAAAAAH!"

show bg11 with sshake

show alexia 2 necklace shocked at midleft with dissolve

"Alexia screamed, surprised as the massive orc reached across the table, grabbed her by the throat and lifted her into the air." 

drok "You thinks yous can threaten Drokk, dumb slut. You puni humis have your words, but Drokk has strength, strength win every time."
drok "How you tell lies about Drokk if yous can’t talk eh? Not so clever now."

"The orc lifted her off the ground with seemingly no effort at all. And even though his grasp was not that tight, his hand was so large that she was already struggling to breathe."
"… All it would take for him to crush her windpipe was to tighten his grip a little. He could snap her spine in half, neither Rowan, nor Andras would arrive in time to save her life. "

femorc "Drokk, don’t yous think this is going too-"

drok "Shut it, Laz!"

"She clawed at his hand, hoping to break his grip, but it was no use. She saw the crazed looked in his eyes, and knew none of his comrades would risk their lives trying to save her."

drok "You think you important, pink slut? You not only slut in castle. You think you important than Drokk?"

#cg1
scene cg453 with fade
show wild orc neutral behind cg453

"He threw her against the table, hard. She let out a voiceless scream, his hand not letting go off her throat for even a moment."

drok "You tell Andras Drokk fucked you? Then Drokk may as well fuck you. "

"She continued to squirm, continued to resist but it was no use. Stupid. Stupid, stupid! She brought this on herself. She could’ve walked away at any moment. But no - she had to prove she was better. She had to see him humbled. She had to see him crushed beneath her heel." 
"And now she would pay the price for her own ego trip."  

drok "Bet yous ain’t never seen no cock like dis on a human."

#cg1 - var 1
scene cg454 with fade
show wild orc neutral behind cg454
pause 3

"He used his free hand to pull his cock loose from under his kilt, and Alexia’s eyes widen in shock when she saw it spring free. It was proportionate to his size, and even half-erect, it was much larger than she would have expected an orc’s dick to be."
"When the orc saw her reaction, he let out a laugh."

drok "Puni humi husband can’t compare to dis, eh? Drokk show you why orcs are most powerful race. "

if all_actors["alexia"].corruption < 60:
    "She thrashed around even harder now, but it was still no use. She didn’t want that thing anywhere near her, it looked like it was going to split her in half."
    
else:
    "She thrashed around even harder now, but it was still no use. The orc’s cock continued to taunt her, a glorious slab of meat, ready to penetrate her. Against herself, she felt a hint of curious. How would it feel? To be brutally fucked by a cock like this? "
    "Brutally fucked against her will, stretched to the limits…"  

"With a grunt he ripped away her panties, tearing them from her body, and leaving her pussy exposed for everyone to see."

drok "Hope yous nice and wet slut, dis gon’ be a tight fit."

#cg1 - var 2
scene cg455 with fade
show wild orc neutral behind cg455
pause 3

if alexia_knows_magic:
    "Alexia struggled desperately. If only he didn’t hold her by the throat, she could smash a water bolt straight into his face. But no matter how hard she tried, no sound would leave her mouth."
else:
    "Alexia struggled desperately, still trying to get away from the orc. But what could she do? She was no fighter, no mage. She was a stupid, peasant girl from small village that no longers existed…"


"It was hopeless. She closed her eyes, so she would not see everyone’s face as they watch him take her."

scene cg456 with fade
show wild orc neutral behind cg456
pause 2

"First there was warmth. Then the press of flesh upon flesh."

show cg457 with dissolve
pause 2

"She could feel the fat head of his gargantuan cock press against the entrance of her womanhood but go no further. He was taunting her now, taunting her now, rubbing against the outside without forcing his way in. Just as she took her sweet time mocking him earlier, he would take him time torturing her now." 

show cg458 with dissolve
pause 2

"Suddenly, the feeling was gone. She clenched her teeth, waiting for it to hammer into her."

femorc "That’s enuff Drokk, ‘less yous want to lose it."

drok "What the fuck you thinks you’s doing Laz?"

scene bg11 with fade
show alexia 2 necklace shocked at midleft with dissolve
show wild orc neutral at midright
#show female orc at edgeright

"When she opened her eyes, Alexia was in for another surprise. While Drokk had been distracted in his attempt to assault her, the female orc had snuck up behind him. She was now holding a large knife to his rapidly deflating dick."

drok "What the fuck you thinks you’s doing Laz?"

femorc "Stopping you from getting us all killed. You do this, Andras’ll execute yous, and then us for not stopping you. "
femorc "Yous may be a big fooker, but I’ll take your anger over the demon’s any day, you daft cunt."

"Drokk glared at her with the same sort of anger he had looked at Alexia before. For a moment, she felt like he was about to tear her head off."

femorc "Just fookin’ try it. If yous are that keen to end up a cockless wonder, I don’t mind giving you a hand, that’s if you don’t bleed out first anyway."

"He bared his teeth at female orc, growling. She answered by pressing her knife harder. This stalemate lasted for what felt like eternity, before Drokk finally removed his hand from Alexia’s throat, and let her go with an angry grunt."

drok "Fine. Dumb humi slut learned her lesson anyway. "

"Alexia scrambled from the table to her feet, gasping for air, trying to stop the tears from rolling down her face. Leaning on the wall, she somehow managed to raise to her feet."

femorc "I suggest yous better be leavin’ now, miss. And when yous tell whoever yous gonna tell about this, don’t forget it was Laz that put a stop to it, alright?"

"She didn’t have to be told twice. Unable to get a sound out of her abused throat, she gave the orcess a stunted nod, and hurried out of the barracks." 
"And as she was running away, she heard Drokk’s distant words, spoken to his female companion. "

drok "Tis’ not going to end like tis, Laz. I guarantees it."

"Oh, in that, he was right. It wouldn’t. Alexia would personally see that it doesn’t."
"No matter the price."  

if rowan_shares_room_with_helayna == False:
    scene bg9 with fade

else:
    scene bg7 with fade
    
show alexia 2 necklace concerned at midleft with dissolve

"Alexia ran back to her room, and slammed the door shut behind her. She locked the door, but that wasn’t enough, so she took a chair from the nearby desk and wedged it under the handle. Not that it would stop a giant orc from smashing the door open if he wanted."
"The small illusion of safety that it afforded her was better than nothing, though."
"She was still trembling, half out of fear, and half out of anger. The nerve of that bastard Drokk. Placing her hand on her throat, she gently felt where the monster had grabbed her and hoisted her into the air."
"The memory flooded back into her mind; the ease at which he suspended her by her throat, her difficulty breathing, her need to cry out, to scream, but having no voice to do so."
"And then… what followed. He pinned her down, and no matter how hard she struggled, tried to get out from under his grasp, it was no use. And the orc wasn’t even trying, he was just that much stronger than her."
"She didn’t even want to think about what happened after that. If it wasn’t for that female orc…"
"Drokk nearly raped her. Hell, he could have killed her... "
"His hand was around her throat, all it took was one squeeze, and with the size of the thing, he wouldn’t even have had to squeeze hard."
"She wanted to cry, but no, she would not give the beast that. It was one thing that she could keep from him, a small triumph in the face of his superior strength. She would not be broken, not by someone like him."
"Alexia realized then that she had become too accustomed to this place. She had been here so long that she had grown comfortable, had forgotten that she was not home, but instead living in a nest of vipers."
"The servants of the twins looked down on her, they saw her as an enemy. They talked about her behind her back, saying terrible things, and wanted to do even more terrible things to her. What had just happened was irrefutable proof of that." 
"Now she had to worry about what Drokk might do. He knew that she would report his actions to somebody, and that it would be very bad for him if she did." 
"He’d shown his true colours, it wasn’t much of a push to imagine he’d go further. Or if not him, some other orc sent in his place. She’d have to watch her back now, not that she trusted orcs in the first place."
"If being kept as a captive at Castle Bloodmeen wasn’t already bad enough, now she’d have to live in very real fear for her life."

al "No."

"That was too far. Hadn’t she already endured enough? Being held against her will as an insurance policy against her husband was an indignity she could barely stand, but to suffer Drokk’s treatment as well?"
"No, she refused to allow a lowly orc like him to render her powerless."

scene bg6 with fade

"Full of rage and unwilling to let the indignity she had endured stand, Alexia marched straight to the throne room. It was only when she passed through the chamber’s large doors that she remembered that Rowan wasn’t in the castle."

show alexia 2 necklace neutral at midleft with dissolve

al "Hello? Is there anyone here?"

"She waited for a moment in silence. Nothing." 
"The demonic throne loomed large before her, its tentacular appendages spread outward, as if poised to grasp. It was monstrous in appearance, gaudy, surely the design of a ruler with very little subtlety. As a metaphor for power, it was too much."
"Power it did award though, that she could not deny. Karnas had sat here as his forces razed half the six realms. Whoever sat here could make laws, command armies, and enforce their will. "
"The throne may be symbolic, but a symbol could have as much power as any concrete thing, sometimes more. "
"She wondered when all was said and done, and they got everything they wanted, if the twins would be able to share it. How long would it be before they disagreed on something important? Until the rift grew into open hostility?"
"Would the castle’s forces war against each other? Would Jezera poison her brother or use some other underhand tactic to kill him off, or would her brother simply rip her to pieces with his bare hands?"
"Hopefully it wouldn’t come to that, she still had faith that Rowan would find some way to stop their conquest of the Six Realms, just as he had stopped the last demon who had sat on this throne. But..."
"She took one tentative step toward the throne, and then another, almost unconsciously. It wouldn’t hurt right? Just to see what it would feel like. It would only be for a moment, and no one would ever know. "
"Plus she had seen Rowan up there before when acting on the twin’s behalf, so it wasn’t like another human hadn’t already sat on it."
"She placed a hand on the throne’s stone arm, it was cool beneath her touch. She ran it down, tracing the length as she felt the lines expertly etched into it by a master stone shaper’s tools. "
"Yes, to sit there for a minute or so wouldn’t hurt anyone."
"Just as she was about to sit, a familiar figure emerged from the small room that Rowan had turned into an office on the other side of the cavernous chamber."
    
show liurial neutral at midright with moveinright

liur "Hello, Mistress Alexia."

show alexia 2 necklace shocked at midleft with dissolve

al "AHH!"

"Alexia almost jumped out of her skin when she heard the voice of the intruder. She hurried down the stairs, almost tripping as she went. When she got to the bottom, she turned to the elvish woman, her face flushed with the scarlet tone of embarrassment."

al "Oh, Liurial, I didn’t see you there. I was just, errrr…"

show liurial happy at midright with dissolve

if alexiaLiurialFriendly:
    "Liurial gave her a knowing smile, it was hardly the most compromising situation she had seen the redhead in."
    
else:
    "Liurial gave her a knowing smile, before giving her the small courtesy of pretending that she had not seen anything."
    
liur "Is there something that I can aid you with, my Lady?"

show alexia 2 necklace neutral at midleft with dissolve

al "Ummm… I know Rowan is out in the field doing something for the twins at the moment, but do you have any idea when he might be back?"

show liurial neutral at midright with moveinright

"The elf seemed to contemplate what the other woman had said for a moment, before responding."

liur "Well, that is a bit of a tricky question."
liur "He was only supposed to be gone for the rest of the day, but it seems the situation is worse than the twins had initially thought."
liur "He could be gone for days, perhaps even for the rest of the week."

show alexia 2 necklace concerned at midleft with dissolve

"She felt her heart fall. To be alone in the castle for a week, who knows what Drokk or his orcs might do to her before he returns."

al "Oh, I see…"

show liurial happy at midright with dissolve

"Liurial had spent enough time around humans to know when something was wrong. She offered the redhead a warm smile."

liur "Is there anything I can do for you? I would be happy to help."

"Alexia shifted nervously in place, unsure what to do with the fact there was very little chance of seeing her husband soon."

al "No, there’s not much you can do. But thanks…"

"Sensing this was something of a larger problem, Liurial tried a different tact."

liur "I see. I do know that Mistress Jezera is in her room, perhaps she might be able to do something for you?"

show alexia 2 necklace happy at midleft with dissolve

"Alexia gave her a soft smile, in appreciation for the fact she was obviously trying hard to be of some service."

al "She might be able to help, thanks."

liur "Anytime. Now I have to get back to this paperwork, it would organize itself. If you think of anything I can do, don’t hesitate to let me know."
liur "And if I see your husband, I will let him know you are looking for him."

hide alexia with moveoutleft

"The two exchanged pleasantries before Alexia headed off to the second floor in search of Jezera."

scene bg18 with fade
show jezera neutral at midright with dissolve

je "Come in."

show alexia 2 necklace neutral at midleft with moveinleft

al "Mistress Jezera."

show jezera happy at midright with dissolve

je "Ah, Alexia. To what do I owe the pleasure?"

"Alexia shuffled uncomfortably in place, how best to broach the subject of what had happened? Jezera was a woman, which meant she should be outraged at Drokk’s actions, but she was also a demon, which made her reaction unpredictable."

je "Out with it child, I haven’t got all day. I have a delightful encounter with one of the maids planned for later."

al "Well..."

"The redhead decided to just come out with it. At the very least, the twins needed her alive to blackmail Rowan, so no matter how Jezera felt about the situation, she had a large incentive to ensure that Alexia was not harmed. "

al "Because Rowan was busy he asked me to deliver a letter to the orcs in the barracks from Andras, containing new orders. "

show jezera neutral at midright with dissolve

"At the mention of orcs and orders, the demoness’ eyes glazed over, she wasn’t off to the best start."

al "I was to give them to a large orc champion called Drokk."

je "I know that one. Stupid by even orc standards, which is saying something."

"Alexia had come this far, all that was left now was to finish the story."

al "Well, I found him in the barracks, and he was very rude to me. Some of the things he said-"

"Jezera interjected, nonchalantly."

je "Par for the course with orcs I’m afraid. Hardly worth informing me though, you have been here a while Alexia, you should know good manners are beyond them. "

"The other woman nodded, trying not to let her emotions get the better of her."

al "And if that was all that happened, Mistress, I would not be here. "
al "I decided I wouldn’t let him talk to me, and I said a few things back…"

show jezera happy at midright with dissolve

"Jezera smirked."

je "That’s my girl."

"The hard part now."

al " But that only made him madder, until… until…"

show jezera displeased at midright with dissolve

"Jezera frowned as the human tried her hardest to get it out."

al "He grabbed me by the- the throat-"

"The demonesses’ eyes flashed wide at what she had just heard."

je "He did WHAT?!"

al "And then he pinned me on the table. I tried to get away but he was too strong, and he- he-"

"Rage pulses through Jezera now, the air around her crackled as if filled with electricity."

je "Did he rape you, my sweet child?"

"Alexia looked down at the floor, as if her mistresses’ intensity was too much to bear."

al "No, he tried, but there was a female orc- I think he said her name was Laz? She stopped him before he…"

"The tension in the air around Jezera seemed to dissipate, as her rage morphed to displeasure."

je "Are you hurt?"

al "Not really, I suppose my neck is a little sore…"
al "It’s just… He knows I will tell Rowan, and perhaps suspects I’d even tell you… I’m worried about what he might do…"

show jezera happy at midright with dissolve

"Jezera smiled at her warmly. It was odd to see a smile on her face that wasn’t caused by childish amusement, or some other dark delight. It was strangely human."

je "Do not worry your pretty head about that, Alexia. I will ensure that Drokk never so much as looks at you again, never mind talks to you."
je "You are our guest, and as long as you remain so, you will have my protection. Insubordination on that point shall not be tolerated."

"Alexia stood in silence for a moment, lost in thought. To be told she would be safe was a relief, but was that all?"

al "Umm… Will he not… be punished?"

show jezera displeased at midright with dissolve

"Jezera sighed loudly, Alexia wasn’t sure why, but her question had clearly frustrated the demon."

je "Would that I could, darling Alexia. If it were up to me, I’d cut the bastard’s balls off, and feed them to him. "

show jezera neutral at midright with dissolve

je "The orcs, however, are my brother’s purview. He's the one who they trust and fear."
je "I fear I'd be a poor agent of your desire for vengeance. Perhaps you should consider getting his help? I will assist you in showing how serious the matter is if needed of course."

al "Oh."

"Alexia’s hopes were crushed. Jezera couldn’t punish Drokk for the terrible things that he had to her, and if it meant risking her brother’s wrath, she couldn’t ask Rowan to either. It was either ask Andras, or let him get away with it."

je "I will ensure that you come to no further harm. I would suggest you find someway to become stronger though, the world can be a very dangerous place."

"She nodded."

al "Thank you, Mistress."

je "Now, will that be all? I have business to prepare for."

al "Oh. Yes, sorry."

hide alexia with moveoutleft

"Alexia gave her a courteous bow, and exited the room, leaving Jezera standing alone."

show jezera displeased at midright with dissolve

je "Silly girl, as if I have the time to deal with every horny orc in this damned place. But I am going to have a very stern talk with them about laying their hands on {b}my{/b} property... "

scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve

"Alexia stood in the hallway outside Jezera’s room, overwhelmed by disappointment. She had come here thinking that Jezera would understand and help, but instead she had told her there was nothing she could do and sent Alexia on her way."
"She only had two options now, neither of which she found particularly palpable."
"She could try to forget about what had happened; she was at the least safe now, so she would not have to deal with any sort of reprisal, but that meant letting Drokk get away with what he had done to her." 
"She would have to put up with the looks, and the whispers behind her back whenever she came across an orc, a frequent occurrence these days."
"The other option was to do what Jezera had suggested and ask her brother for help. She could probably convince Andras to help her, but when he was involved there was always a price, she had learned that much from her time in Castle Bloodmeen."
"Also, the punishment that he would inflict on Drokk would no doubt be at least brutal, if not fatal, and, as angry and humiliated as she was, she still was not sure if she could stomach that."

menu:
    "Let it go.":
        $ released_fix_rollback()
        "No. As horrible as the experience had been, and no matter how terrifying and humiliated she felt, she could not go to Andras and ask this of him. The price would be too steep, and the outcome too violent."
        "She hated the fact that Drokk would get away with it, but this was life at Castle Bloomeen. It would be naive of her to expect justice in a place like this, with masters like these, and she couldn’t risk making Rowan’s life harder."
        "She’d have to endure all the leering looks, and snide comments, but that was nothing compared to what Rowan had to endure on a daily basis. She would just have to accept for now, at least, she was too powerless to do anything about it."
        "With a heavy heart, she headed down the hallway toward the stairs to go about the rest of her day. Hopefully, she’d be able to push the memory of what had happened to her from her mind and not think about it too much."
        "But now, who was being naive? "
        return
    
    "Ask Andras for help.":
        $ released_fix_rollback()
        "No. This couldn’t be how it ended. That green bastard couldn’t get away with what he had done to her, she would not allow it." 
        "Earlier, she had said that she would do whatever it took, and if this is what it took, so be it. She refused to be powerless."
        "Whatever price Andras wanted her to pay, she would pay, and whatever the punishment Drokk received would be on the demon’s head, and not hers." 
        jump askAndrasHelp

label askAndrasHelp:

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve

"When Alexia finally found the room, she stood at the door with some trepidation. After all, she had never been here before, and for all she knew, Andras might not even be here."
"But she had come this far. She knocked three times loudly, before announcing herself."

al "Andras, are you there? It’s Alexia..."

"A response came from the other side of the door."

show andras happy behind bg14

an "Oh Alexia, please, come in."

scene bg41 with fade
show alexia 2 necklace shocked at midleft with moveinleft

al "Sorry to bother you bu-"

"Alexia was stopped dead in her tracks by what she saw when she entered the room."

scene thotintro with fade
pause 3

"The most beautiful woman she had ever seen."

"Plump lips, and luxurious long black hair that fell down onto a very ample bosom accentuated by an hourglass figure with curves to die for." 
"The woman was wearing an outfit that could barely be described as clothing, and had been adorned in gold, most shockingly with golden hoops that hung from her nipples."
"The redhead had never seen this woman in the castle before, of this she was sure. She would never have forgotten such a striking beauty. Just who was this woman?"
"Alexia’s fascination had made her oblivious to everything around her. She’d been so taken by the woman, she hadn’t even noticed what was going on in the room. The sight turned her pale skin crimson as she burned with embarrassment."

#cg1
scene thotsexanimation1 with fade
show alexia 2 necklace aroused behind thotsexanimation1
show andras smirk behind thotsexanimation1

"Andras was sat on the edge of the bed, propping himself up with one of his large hands as he leaned back slightly. The woman who had captured her imagination so thoroughly was sat on his lap, legs spread slightly, with the demon’s cock inside her." 
"Bracing herself with both her hands on the edge of the bed, she was slowly moving her body up and down with a steady rhythm with a smile on her face as she did so. "
"Alexia looked away from the scene and stammered:"

al "Oh. I.. I.. Uh… Will come back-"

an "That won’t be necessary, we are almost done here."

"The redhead didn’t reply. She wanted to leave, but she could hardly disobey Andras, especially when her sole reason for coming here was to ask for his head. She simply nodded."
"Responding to the demon’s words, the other woman began to speed up, moaning and she rode him on the bed. Again and again she lifted herself and allowed herself to fall, accompanied by the squeaking of the bed."
"Alexia tried to look away, but unless she turned around, the woman was always somewhere at the edge of her vision, and she couldn’t ignore the  moaning, growing louder and louder as the woman rose Andras to climax." 
"Again and again the demon’s huge red cock appearing and disappeared inside of the gorgeous woman’s tanned cunt, as she did all of the work. Andras was sat there, doing none of the work, just allowing himself to be serviced who seemed far more than willing." 
"Alexia felt incredibly awkward, she couldn’t leave - not just because Andras had told her not to - but because she needed his help, and so she didn’t want to do anything to jeopardize that." 
"Worst though, she could feel herself growing aroused. The creaking, moaning, and the slapping of flesh against flesh was one thing, but despite her best attempts to avoid looking, she was being forced to watch."
"The woman’s large breasts, adorned with gold rings swayed as she rode him, her face contorted from the bliss of pleasing her lord. Her pierced cunt engulfing the large red cock of Andras over and over as she raced towards orgasm."

an "That’s it… Almost…."

scene thotsexanimation2 with fade
show andras smirk behind thotsexanimation2

"The woman sped up now, determined to milk the demon of his seed. Beneath her loud moans, Alexia could hear the heavy breaths of Andras as he tried to control himself. He was failing."
"With one last thrust and a very loud, low moan, she pushed herself down onto him, taking him to the hilt. It pushed Andras over the edge, and he shuddered and his spunked his load deep inside the slave."

show cg492 with sshake
show cg492 with sshake
show cg493 with flash
pause 3 

"It was too much for poor Alexia as well, mumbling an apology she fled from the room with great haste." 
"The demon just laughed."

an "Some people are no fun."

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve
show andras happy at midright with moveinright

al "I’m sorry, I didn’t know… I didn’t mean to disturb you… I…."

an " It is fine. I take it you need something? It must be important, since this is the first time you have ever come to my room."

al "Oh, uh.. Yes…"

"Alexia thought about what to say next. Andras wasn’t exactly the nicest person in the world to put it lightly, and he might be as unsympathetic as Jezera had been, or worse, take Drokk’s side." 
"She had no other options though."

al "Well, you gave Rowan a task…"

an "Delivering my orders, yes, I remember."

al "But he had to leave early, so he asked me to do it…"

an "Forcing his wife to do his work for him, is this the sort of person my sister wants for her castellan? I don’t know."

show alexia 2 necklace happy at midleft with dissolve

"His attempt at a joke, she smiled back at him, weakly."

al "It was no trouble, I don’t mind. I try to help around the castle as much as I can..."

an "So I have seen."

al "Yes, well, when I got to the barracks, there was this orc… Drokk."

"Something lit up in his eyes when she said the name."

an "Ah, Drokk."

al "He was there with some other orcs, and I tried to give him the orders, but- but-"

show alexia 2 necklace concerned at midleft with dissolve

"She felt like she was about to cry, again. Andras put a hand on her shoulder gently."

an "It’s okay, just tell me what happened. "

al "He started saying horrible things to me, and when I tried to talk back, he grabbed me by the throat and..."

"Having to describe it again brought it all back and she broke down crying. It was the last thing she wanted to do in front of Andras, but it was all too much for her."

an "It’s okay Alexia, you don’t have to say anymore. "
an "You just take a minute for yourself, and when you are ready, we’ll go."

"Alexia wiped her eyes, trying to control herself."

al "Go... Go where?"

"He just smiled at her."

an "To make sure that Drokk, nor any other orc, ever lays a hand on you again. "

scene bg11 with fade
show wild orc neutral behind bg11

show andras displeased at midleft with dissolve

"By the time that Andras arrived, the barracks was a lot more lively than it had been earlier. More of the castle’s soldiers had dragged themselves from their pits, and were not sitting around drinking, laughing and gambling."

show alexia 2 necklace concerned at edgeright with dissolve
 
"None of them even batted an eyelid when the demon walked in, Alexia timidly in tow. Drokk was still sat at the same table with his lackeys, but the female orc who had intervened earlier had departed in the meantime." 
"All eyes turned toward him when they noticed that human woman when he approached Drokk’s table though, and the volume of ambiance in the room became a lot quieter. Drokk hadn’t noticed the demon arrive, and was laughing as he slammed his tankard down on the table."

drok "And den Drokk said, since yous had such a big mouth, Drokk didn’t think yous have trouble taking alla his cock!"

"Another hearty laugh, accept no one else was laughing. It was then he noticed the figure that was standing aside him."

drok "Masta Andras, nice to see yous in da barracks."

"Then he saw the other figure who had hung back, keeping her distance from his table, which noticeably soured his mood."

drok "What da fuck is she doing back here?"

an "*She* is with me, do you have a problem with that?"

"Drokk scoffed and took another swig of his ale."

drok "No problem, Drokk just surprised she’d come back here afta shit she pulled, that’s all."

show andras smirk at midleft with dissolve

"The demon smiled; it was a dark smile, unsettling and betraying nothing of what was really going on in his head."

an "Yes, she told me all about everything that happened earlier. "

"The orc smiled back in a similar fashion, two could play at this game it seemed."

drok "Did she now?"

an "She did, and she was in quite a state. What happened was very upsetting for her. "

"The demon’s face remained a mask, unchanging, while a frown formed on the huge orc’s face."

drok "She should be upset, cunt’s lucky to still be alive afta da way she talked to Drokk."

an "Did you hurt her?"

drok "Only put my hands on her a bit, not Drokk’s fault humis are all so weak."

an "She says you did a lot more than just “put your hands on her a bit”."

"He glanced at Alexia, who looked very uncomfortable at being put on the spot. The best she could do was nod meekly."

drok "Yeh, well. So what if I did? Stupid humi slut insult Drokk."

"All the orcs in the room were watching in nearly complete silence, Andras tilted his head slightly, as if studying something."

an "Watch your tongue Drokk, you forget yourself."

"If Andras intended to cool the orc down, orc cow him into submission with his tone, it clearly had the opposite effect. Having to defend himself was only making the massive orc visibly more agitated."

drok "Why should Drokk watch tongue? What humi slut gots to do with yous anyways?"

an "Were you not told that she and her husband were both under the protection of both my sister and myself?"

"The demon gestured to the rest of the room, in almost a showmanship-like fashion."

an "Were you not all told that?"

"Grumbles of approval from the crowd, but Drokk remained unconvinced."

drok "So what?"
drok "Drokk not going to kill humi, Drokk was just gonna have sum fun." 

"The orc looked at Alexia with the same hate in his eyes as he had shown earlier."

drok "Plus humi bitch was askin’ for it."
drok "Dumb slut insult Drokk in front of da other orcs, Drokk can’t stand for dat."

"Andras seemed completely unfazed by Drokk’s rising temper, if anything he looked bored."

an "So, you ignored my order because Alexia hurt your feelings?"

"A snigger rose up from the other tables scattered around the barracks. If orcs could turn red, Drokk probably would have in this moment. Alexia clutched her dress tightly."

drok "Feelings no hurt, puny humis words can’t hurt Drokk. Is about respect. "

"The demon smirked, catching on to that last word."

an "Respect, yes, that is the word exactly."

"He looked around the room and all the other orcs, making sure that they knew what he was about to say was as much for their benefit as Drokk’s."

an "I’d like you think you all respect me, I’ve surely earned it."
an "Nevermind the fact I put a roof over all of your heads, and give you all the opportunity to share in the spoils of our conquest."

show andras displeased at midleft with dissolve

"He looked at Drokk now, the smile dissolving from his face."

an "But do you think it shows respect, Drokk, when you blatantly ignore my commands?"

"Drokk was beginning to look uncomfortable now."

drok "Drokk respect masta, but Drokk a great leada, need other orcs  to respect him."
drok "Drokk strongest ‘der is. Orcs won’t respect him if he let any humi talk to him the way dat one did before. "

an "So, it is more important that the other orcs respect you than it is for you to show respect to me, is that way you are saying?"

"Confusion crossed the face of the massive orc. The demon was deliberately twisting his words, but he wasn’t intelligent enough to realize it."

drok "No, dat not what Drokk mean."

an "Then, what exactly does Drokk mean?"

"Silence. Drokk was clearly thinking long and hard about what he was going to say next."

drok "Drokk didn’t mean no disrespect to masta, he just got mad. If he disrespected masta it was not on purpose, and he is sorry. "

show andras happy at midleft with dissolve

an "There, that wasn’t so hard now, was it?"
an "Except I am not the person you should be apologizing to."

"Realizing what the demon wanted him to do, Drokk grimaced. He’d probably prefer swallowing glass over apologizing to a human, and a woman, no less."

drok "Drokk sorry, humi-"

an "Alexia."

drok "..."
drok "Alexia."

"The demon turned to face the woman."

an "So what do you think Alexia, has Drokk learned his lesson?"

menu:
    "Yes.":
        $ released_fix_rollback()
        $ drokkPunish = "Yes"
        "The human spoke for the first time since she had entered the room."
        al "Yes, he apologized and he won’t do it again, that is enough."
        al "It doesn’t need to go any further."
        an "That is certainly very forgiving of you Alexia. "
        show andras smirk at midleft with dissolve
        "There it was, that smirk."
        an "But I’m afraid I don’t share your opinion."
        
    "No.":
        $ released_fix_rollback()
        $ drokkPunish = "No"
        $ change_corruption_actor('alexia', +2)
        "The human spoke for the first time since she had entered the room."
        al "No, the bastard nearly raped me. If the other orc- hadn’t- hadn’t..."
        show alexia 2 necklace angry at edgeright with dissolve
        "She looked like she was on the verge of tears, but it quickly morphed to fury."
        al "He needs to be punished properly, he needs to suffer like he made me suffer!"
        an "Well, you know what they say about an eye for an eye…"
        show andras smirk at midleft with dissolve
        "There it was, that smirk."
        an "But I’ve always been partial to capital punishment myself."
        
        

scene cg494 with fade
show andras smirk behind cg494
show wild orc neutral behind cg494
pause 3



"Fast as lightning, Andras spun around, grabbing Drokk by his throat and lifting him into the air as if he were light as a feather. The huge orc let out a choked hiss of surprise."

an "Drokk. Drokk. Drokk."
an "As much as I’d love to let it slide, you are an excellent warrior after all, I’m afraid I’m going to have to make an example of you."

"Drokk’s eyes bulged with surprise, as he tried to say something. Anything."

an "I don’t give you soldiers orders as suggestions, and if I start letting people off when they disobey them, people might start to get the wrong idea, and then there’ll be no discipline at all, will there?"

if drokkPunish == "Yes":
    show cg495 with dissolve
    pause 3

else:
    scene cg496 with dissolve
    pause 3  

if drokkPunish == "Yes":
    "Alexia wanted to say something, to stop him, but she knew there was no point."
    
else:
    "Alexia smiled as she watched the orc squirm, excited to see him get what he deserved."

"The air was punctuated with the sickening crack of bone as Andras used his free arm to wrench the huge arm’s arm in an unnatural way.  Alexia could see white bone tear though green skin, she almost fainted."

if drokkPunish == "Yes":
    scene cg497 with redflash
    pause 3

else:
    scene cg498 with redflash
    pause 3  

drok "UKK!!!"

an "Maybe-"

scene black with redflash

"The crack again, as the demon broke his other arm in the same fashion, followed by an orcish roar of pain."

if drokkPunish == "Yes":
    scene cg499 with fade
    show andras smirk behind cg499
    show wild orc neutral behind cg499
    pause 3

else:
    scene cg500 with fade
    show andras smirk behind cg500
    show wild orc neutral behind cg500
    pause 3  

an " -after seeing this, all of you will understand what it means to disobey me."

"Satisfied, he dropped the orc to the floor with the same level of regard one has when disposing of trash."

scene bg11 with fade
show andras displeased at midleft with dissolve
show alexia 2 necklace concerned at edgeright with dissolve

an "I should kill you Drokk, I should tear your heart from your chest and be done with it."

show andras happy at midleft with dissolve

"Andras smiled, it was almost magnanimous."


an "But you are good warrior after all, and I can’t exactly spare any of those at the moment. I’m sure you’ll think better before disobeying me again, won’t you?"

"A grunt of acknowledge and a nod were all that the orc could muster. Andras turned his attention to the rest of the crowd."

an "I trust the rest of you have learned the same lesson?"

"More grunts and nods. Alexia felt pretty certain that no other orc would mess with her after seeing this, and despite the brutal scene she had just witnessed, she felt much better."

an "Good. Now someone get Drokk to the mender before he pisses himself. Come Alexia, we are done here."

al "Oh, uh.. Yes."

hide andras with moveoutright
hide alexia with moveoutright

"The demon left, promptly followed by the human woman. If the orcs had anything to say to or about her, this time they would wait until she was far out of earshot."

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve
show andras happy at midright with dissolve

an "I doubt any orc will harass you after that little scene, but if any of them try anything, come straight to me. You know where my room is."

"Alexia was lost in thought, still trying to process what had just happened. What Andras did to Drokk was brutal, and she abhorred violence, but she’d be lying to herself if she didn’t admit that it had been exciting."
"What he did to Drokk- what he did for her, sent a thrill down her spine. She needed someone to stand up for her, and Rowan wasn’t here yet again. If it wasn’t for the demon, she didn’t know what would have happened…"

an "Alexia? Are you alright?"

"Brought out of her thoughts by Andras’s voice, a wave of embarrassment hit her as she realized she had been stood there daydreaming."

al "Oh! Uh.."

show alexia 2 happy at midleft with dissolve

al "I’m okay. I don’t think they’ll bother me again after that display, they’ll be too scared to."
al "I have to thank you. Rowan wasn’t here, and Jezera refused to do anything. I don’t know what Drokk would have done if you hadn’t intervened…"

an "There’s no need to thank me."

al "But-"

"He cut her off with a friendly wave of his hand."

an "Really. The orcs have been acting very unruly as of late, even worse than they normally behaviour. Castle fever I suppose. We can’t have that."
an "By taking Drokk down a peg it will remind them who is the boss around here. I was hoping your husband would take care of it, but he’s been too busy I suppose."

"Yes, even too busy to protect her."

al "Still."

an "Drokk disobeyed an order, now the others won’t. It is as simple as that."
an "Plus I seem to recall telling you that no one in this castle would lay a hand on you unless you wanted them to, including me."

"He was right. He may have been a manipulative bastard on a number of occasions, but he had never laid a hand on her without her permission, not like Drokk."

an "So think nothing of it, I was just doing my duty as the ruler of Bloodmeen."

"His refusal to take any credit for saving her was beginning to frustrate Alexia, she decided to try something a bit more forward."

if all_actors["alexia"].corruption > 60:
    "Placing one hand on his crotch, she said:"

else:
    "Placing one hand on his chest, she said:"

al "Surely there must be some way that I can thank you."

an "Well, when you put it that way…"

"He leaned in for the kiss, and she accepted it. Tongues snaked, brushing against each other, until, eventually, it was the demon who pulled away."

al "Mmm…."

an "Meet me tonight in the throne room, after everyone else has gone to bed."

hide andras with moveoutright

"He didn’t wait for a reply, disappearing down the corridor. Alexia felt a mix of emotions all at once; excitement, shame, arousal, betrayal."
"Could she really do this?"

label andrasNTRDecisionMenu:

menu:
    "Meet Andras later.":
        $ released_fix_rollback()
        "Yes, she could. After all, Andras had saved her from the orcs, not her husband, and he deserved a proper thank you for that. Rowan wouldn’t be back for days yet, and he needn’t ever have to know."
        "She hated to admit it, but the thought of sneaking around excited her, and the power that the demon had displayed when he punished Drokk had been like nothing she had ever seen before."
        "She would meet him later to show her appreciation, it was the least she could do after what Andras had done for her. Plus it wouldn’t hurt her or Rowan if Andras was to think protecting them was to his benefit. He’d kept his word about her after all."
        jump AnThroneNTR
        
    "Don’t meet Andras later.":
        "This option may lock off certain segments of content. Alexia will have made her choice. Only select this if you really mean it."
        menu:
            "Don’t meet him.":
                $ released_fix_rollback()
                "No, Andras may have saved her, but she was still a married woman. It wasn’t Rowan’s fault that he wasn’t here after all, it was because of Andras and Jezera, and the task they had him doing."
                "If he were here, he would have stopped them himself, of this, she was sure. She wouldn’t even be in a position to be assaulted by assaulted by Drokk if it wasn’t for the twins in the first place."
                "She might be grateful for Andras putting a stop to it, but she wasn’t about to betray her husband to thank him for it."
                "The demon would find himself waiting to be stood up in the throne room tonight."
                return
            "Reconsider.":
                $ released_fix_rollback()
                jump andrasNTRDecisionMenu
                
label AnThroneNTR:

scene bg6 with fade

"It had gone midnight by the time that Alexia snuck down to the throne room. She had lived here long enough to know her way around the place, and made her way there taking the long, winding corridors that she knew were likely to not be used at this time of night."
"When she pushed open the large doors at the front of the cavernous chamber, she found it dimly lit, only the braziers on the walls giving out a soft glow."

show alexia white neutral at midleft with moveinleft

al "Hello? Andras?"

"His voice echoed softly from the far side of the room."

show andras happy behind bg6

an "I’m here, I was beginning to think that you weren’t going to come."

hide andras
show andras happy at midright with dissolve

"She could see him now as her eyes began to adjust to the darkness of the room, he sat on the throne, waiting for her. She began to walk towards him."

al "Sorry, I had to wait until the castle quietened down. Jezera’s maids work until late, and there’s always a few drunken orcs milling around close to the barracks."

an "True, true. We wouldn’t want anyone to see you now, would we?"

show alexia white happy at midleft with dissolve

"She blushed with shame. She would have been hard pressed and anyone stumbled upon her to explain where she was headed late at night, wearing nothing but her nightie." 
"He saw her grow flushed and crimson and laughed, the eyes of a demon were much better suited for the darkness than those of a human. "

an "I’m just teasing you, I’m sure you would have thought of something. "

al "I don’t think I would have been able to if I had been put on the spot, I could hardly have told them the truth."

show andras smirk at midright with dissolve

an "And what would the truth be?"

"He said, with a smirk."

al "You know what it is."

an "Do I?"

al "Yes."

an "I’m not sure I do, you’ll have to remind me."

"He was playing with her, so she decided to play a little game of her own." 
"She stopped at the foot of the dias, looking up at him, and bowed her head."

al "I came to thank you Lord Andras."

an "Oh, for what?"

al "For protecting me from Drokk and all the other orcs, I don’t know what I would have done if you hadn’t intervened."
al "You are so strong, and powerful…"

an " I am, aren’t I?"

al "Yes, when you held up Drokk like he was nothing, and you- you-"

"He grinned, clearly enjoying the redhead’s performance. "

an "Go on."

al "When you punished him… When you broke his arms, it was like you were saying it was because he touched me with them, and if anyone else touched me…"

an "Perhaps, I was."

al "Ohhh…."

"Alexia theatrically feigned a shudder, she was enjoying this almost as much as she was. "

an "I was rather heroic, wasn’t I?"

al "Very heroic, my Lord. Like some hero out of legend, Ser Alarec, or Ser Ferrano, defending the honour of a lady."

an "Yes, yes, rescuer of maidens, defender of damsels in distress, that definitely sounds like me."

"She let out a giggle. "

an "What, don’t you think so?"

"She tried to stifle her laughter as best as she could."

al "Of course not. You are very virtuous, my Lord."

an "Good, good."
an "I think I should be rewarded for it."

al "You should, my Lord."
al "How do you think you should be rewarded?"

an "Come here."

"She sashayed up the stairs slowly as he stood from the throne, exuding power."

al "And what, pray tell, would you like me to do?"

an "Kneel."

#cg1
scene cg501 with fade
show andras happy behind cg501
show alexia white happy behind cg501

"She did as she was told, and it felt good to do so. Whatever anyone might say about him, Andras certainly had the authority needed to be a demon lord. An aura of command almost, a surety in what he said that made you feel compelled to follow orders."

show cg502 with dissolve
pause 1
show cg503 with dissolve
pause 2

"Using his free hand, he freed his cock from beneath its cover. She gazed at it, hungrily."

show cg504 with dissolve
pause 3

"His fat cock was in her face now, she breathed it in, the musky smell of masculinity. Looking up, his frame was so muscular and powerful, he towered above her like a giant. "

if greyhideMet == True:
    "Only Greyhide was larger, but even then, Alexia knew that the minotaur was no match for Andras in pure strength."

"He’d crushed Drokk like a gnat, and while the woman liked to think of herself as more enlightened, she couldn’t help but find it hot."

show cg505 with dissolve
pause 3

"She didn’t need to be told what to do anymore. Taking the dick in one hand, she began to stroke it, while kissing the head."
"Thank. You. Lord. Andras - she said, punctuating each word with a kiss on the shiny crimson head of his cock. The demon said nothing, simply enjoying the sight of the woman below him, working his dick."

"She began to tongue and suck it, slavering it with her saliva as her hand worked away, tugging and twisting. She wanted to tease him first, just like he had teased her earlier."  
"She kissed, licked, and sucked the head, but everytime it seemed she was about to begin the blowjob proper, she slowed down, or moved away, denying him the pleasure. "

an "Want to play it like that, do you?"

al "I have no idea what you mean."

"She said sarcastically, as she lazily licked his shaft."
"The demon had had enough of being frustrated, and he was going to show her exactly what he meant." 

scene powerlessthronesexanimation1 with fade
show alexia white happy behind powerlessthronesexanimation1

"She shuddered as he grabbed her by the back of the head and started to direct her movements. She moved back and forth, taking his cock as deep as she could, before receding, only to impale her mouth on it again. "
"Andras was forceful, enough to make her feel controlled in an arousing way, but not enough to make her feel like she had no control. Each time he made her gag on his cock, he held her just the right amount of time, so she never felt like she would choke. "
"Before long her head was bobbing back and forth at a steady rhythm, the sound of flesh and wetness echoing through the chamber."
"She slid her right hand down to her sodden pussy and began to stroke her clit, as she continued to pleasure him. Why shouldn’t she get off as well? Her cunt throbbed with need, wishing it was as full as her mouth."
"She slid one finger in, then a second and a third, up to the knuckle. Andras saw what she was doing and laughed, as he continued to pump away, fucking her face, as she frigged herself chasing her own climax."
"A few minutes later, they were both approaching the edge. Alexia came first, cumming hard as she frantically fingered her cunt with Andras’s cock buried in her throat."

al " Fuuuuuuuck……"

scene cg512 with sshake
show black with sshake
show cg513 with flash
show cg513 with sshake
show cg514 with dissolve
pause 2

"Andras grunted and released her head. As he pulled back, he sprayed her face with her load, glazing her in warm jizz."

scene bg6 with fade
show alexia white happy at midleft with dissolve
show andras smirk at midright with dissolve

al "Fuck, I’m a mess."

an "I guess I wasn’t so virtuous after all."

"She grinned at him, her face thick with his cum."

al "I’m not complaining."
al "I suppose if you are going to keep protecting me, then I will have to keep thanking you?"

an "Hmmm, I suppose you will."

al "I think I can live with that."

"The shame and the guilt would come later, but for now, she was still basking in the post-orgasm glow. "

al "I’d better go and clean myself up, it wouldn’t do for anyone to discover me with a face full of your cum."

"He laughed:"

an "No, I suppose it wouldn’t. "
an "Go, I’ll send for you when it is time for you to “thank me” again."

al "Yes, my Lord."

hide alexia with moveoutleft

"She emphasised the word “Lord” with a wink, made an overexaggerated curtsy and left, leaving the demon alone. He sank back into the throne."
"That idiot Drokk had almost ruined it by taking it too far, but it had still gone as planned. Sending Rowan away, having the orc accost her, that little scene with his favourite slave - it had all worked out like he thought it would."
"And now it was time to plan his second gambit."

return
