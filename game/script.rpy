﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Kamiya")
define u = Character("Usui")
define b = Character("Bob")
define c = Character("Big Chungus")
define a = Character("Asami")
define t = Character("Teacher")
define i = Character("Mr. Izumi")
define y = Character("Yomki")
define mi = Character("Miyuki")
define g = Character("Gorou")
define unk = Character("???")

# The game starts here.

label start:
    
    $ Asami_Event_1 = False
    $ Yomki_Event_1 = False
    $ Yomki_Event_2 = False
    $ Miyuki_Event_2 = False
    $ Izumi_Event_3 = False
    $ Gorou_Event_3 = False
    $ Asami_Event_3 = False

    play music "bgm/chungus.mp3" fadeout (1.5)

    #scene black

    #pause 1.5
    
    #show asami_neutral
    
    #with Dissolve (1.5)
    
    #a "So, you're here! Welcome to WACCLAND DaTING SIM 2, where the game isn't even started yet and I'm just here to test the character sprites"
    
    #show asami_dumbass
    #hide asami_neutral
    #show miyuki_neutral with Dissolve(0.5):
        #xpos -300
        #ypos 100
    #show bob_neutral with Dissolve(0.5):
        #xpos 1000
        #ypos -50
    
    #b "Hello, it is me Bob"
    #hide bob_neutral with Dissolve(0.5)
    
    #show masashi_neutral with Dissolve(0.5):
        #xpos 1000
        #ypos -50
    #a "Did you know that!"
    # This joke isn't funny!
    # It's so not funny I hid it in the code!
    #m "My real name is Mathias Cockland!"

    #pause 10

    #"The time has cometh for the Wacclandeth of Dating SIM.... 2!!!!!!!!!!"
    #"the revengeance of the electric boogaloo of CHUNGUS"
    #"No adrien I ain't fixin' the goddamn script"

    # FR THIS TIME THIS IS THE start

    "NOVEMBER 21, 20XX"
    "The final day has arrived."
    "No one could have guessed what was coming."
    "But even then, we had to fight it..."

    # MET UNE IMAGE DE LA PLANETE QUI SE FAIT ATTACKER OR SOME SHIT
    scene destroyed_world with Dissolve (3):
        ypos -0.3 xpos -0.3
        ease 10.0 ypos 0

    pause 0.5

    "The land was scorched to the ground..."
    "They had come, the ones who are only known as the *REDACTED FOR SPOILERS*..."

    unk "MC, the only way you can save this world is to ############"
    unk "I will ######### from ##########"
    unk "########### you have one mission. One of the greatest importance..."
    unk "Go get bitches. At any cost, no matter if it's one or a thousand... You must get a Girlfriend!"
    m "I understand..."
    m "I'll do it!"
    m "I will get a Girlfriend... and-"

    scene black with Dissolve (1.5)
    scene white with Dissolve (3)

    play music ("bgm/man....mp3") fadeout (1.5)

    show chungus with Dissolve (3)

    c "It is nice to meet you, sussy boi."
    c "I am the being known as Big Chungus,"
    c "the god of this world."
    c "Masashi Kamiya... Thoust grand quest begins here."
    c "It all begins here..."
    c "Acquire a Maiden. That is thy task."
    c "Now, go forth with Wacc and Land, my child!"
    c "For this is YOUR Waccland Dating SIM 2: Electric Boogaloo."

    play sound "sfx/bonk.mp3"

    scene bedroom with dissolve
    
    stop music

    m "Huh..."
    m "A blinding light passes through the curtains straight into my face..."
    m "(I realize that I have overslept and that my alarm has been ringing for a good 15 minutes.)"
    m "Isn't 15 minutes a bit much?!"
    # nah i'd win
    m "(I quickly turn off the alarm.)"
    m "..."
    m "The hell was this dream??"
    m "I feel like I should be remembering something important just now..."
    m "Dammit, the curse of shitty games has befallen me."
    m "..."
    m "...Wait... yeah probably should get up..."
    m "Yet another captivating school year awaits me..."

    scene black with dissolve

    m "(I quickly prepare myself for school.)"
    m "(I also vaguely question why I suddenly started to think out loud, but I dismiss the idea pretty quickly.)"
    m "Whatever, I'm leaving now!.... Why am I yelling this, I literally live alone..."

    scene residential with dissolve

    play music ("bgm/2.ogg") fadeout (1)
    
    m "Huh...? Something feels different today..."
    m "Probably nothing..."
    m "I should probably hurry up."
    m "(I bolt towards the school quickly dodging the cars as I pass through crosswalks on my way there.)"
    m "(A set of stairs separate me from the entrance to the school.)"
    m "(The school is now right in view. And still 15 minutes until the bell rings.)"
    m "(And now I'm standing at the doors of Waccland's Peak Academy.)"
    m "(First founded in 1869, this school was the gathering place for all the most brilliant minds.)"
    m "(It's name derives from Kevin Waccland, the saviour of the world, inventor of Wa Ku Ho!)"
    m "(A place for such amazing people, named after the most amazing person.)"
    m "(Well, now it's just a normal high school that even normal people can go. That's how I got here.)"
    m "Well I better go to my class before the bell rings"
    m "(I follow the indications to my new class, class 1-C)"
    scene classroom with Dissolve (1)
    m "As I enter the door, I quickly maneuver through the desks to arrive at my assigned desk, right beside the window in the second to last row."
    m "(I'm still sleepy... shouldn't have gamed all night...)"
    m "I slowly close my eyes..."
    scene black with Dissolve (2)
    unk "HEYYYYYY!!!!!"
    scene classroom with Dissolve (2)

    m "What?!"
    show asami_neutral with Dissolve (1)

    unk "You've just woken up for school and you're gonna go back to sleep now?"
    m "Who the hell are you?"
    unk "Me? That's not important right now!"
    m "(What's with this annoying girl, I was just minding my own business and she starts critizing my gamer lifestyle of sleeping through the entire class.)"
    m "(I have also never even seen her face before...)"
    unk "What's with that reaction! Very well, I shall introduce myself."

    show asami_smug
    # change to smug when it will be available
    hide asami_neutral

    a "The name's Nakamura Asami! You better remember it, for I am the one who shall soon rule this world!!!"
    m "(This girl's delusional... I better ignore her, maybe she'll leave soon if she sees I'm not interested in small talk.)"
    a "Well, I just arrived here, can't afford to be picky with friends!"
    a "And you were conveniently in the desk right in front of me!"
    a "My parents came here for work, and with that I arrive here with no one I know!"
    a "Back home, I had like a hundred friends. Now I have to start back at 0. But I won't let that stop me!"
    a "After all, I'm not a loser that talks to no one!"
    m "(What is she even talking about, I stopped listening 5 minutes ago...)"
    m "Sigh..."

    hide asami_smug
    show asami_mad

    a "Hey are you ignoring me!"
    m "I sure am, now leave me alone."
    a "That's not very polite! You're talking to such a cute girl and you don't even bother listening to a word she says!"
    m "I don't see the correlation between your points. I'm trying to sleep here."
    a "The audacity! Are you stupid or what?"
    a "Don't answer. I already know you are!"
    a "Who even greets a stranger like that?"
    
    "Suddenly, the doors slams open."

    show asami_mad:
        ease 1 xpos 1600

    show izumi_neutral with Dissolve (0.5)

    t "Quiet everyone, class is going to start soon!"
    a "We'll continue this later! I won't stop until you understand the errors of your ways!"
    t "I said quiet, Asami!"
    a "Okay..."

    hide asami_mad with Dissolve (1)

    m "She then goes to sit right behind me, unfortunately..."
    i "Well, Good Morning everyone. My name is Nanami Izumi, just a plain' ol' teacher."
    "Female Student 1" "Wow, he's so cool and hot!"
    "Female Student 2" "He looks so mature!"

    hide izumi_neutral with Dissolve (0.5)

    m "(Man, all the female students are talking about the new teacher...)"
    m "(This is so cliché, can't they just, I don't know... concentrate on the class instead????)"
    m "(It's almost always the same as soon as we have a young male teacher.)"
    m "(Well, no use complaining about that on the first day of school, they'll stop once they realize he's just a plain old teacher.)"
    m "(I sat through the entire class between dream and reality, contemplating the meaning of life and why I decided to game all night.)"
    m "(I briefly wonder if this whole scenario was schemed by someone...)"
    m "(...Altough I quickly dismiss the idea.)"

    "Ding dong bing bong!"

    show izumi_neutral with Dissolve (0.5)

    i "Well, looks like time is up, we'll continue next class were we left off."

    hide izumi_neutral with Dissolve (0.5)

    show asami_kill with Dissolve (0.5)
    
    a "But for us it's now, I-STILL-HAVEN'T-ASKED-FOR-YOUR-NAME-kun!"
    m "Class just finished and you're already rambling..."
    m "Well, no use not introducing myself."

    hide asami_kill with Dissolve (0.5)
    show masashi_neutral with Dissolve (0.5)

    m "I'm Masashi Kamiya, but you can call me MC!"
    m "Gaming is my life! And Wacc-Fuel is my blood!"
    m "Over these last 10 years, I have played many games!"
    m "But I have never lost... For I am the ultimate gamer!"

    hide masashi_neutral with Dissolve (0.5)

    show asami_neutral with Dissolve(0.5):
        xpos 900
        ypos 140

    unk "Yeah, for real, this guy has never lost before. Trust."

    show yomki with Dissolve (0.5):
        xpos 0
        ypos 25

    m "(This guy is my good friend Yomki, I have no idea why he's backing up my obvious bullshit.)"
    m "(Unfortunately, he isn't in my class this year.)"
    y "Sup, it's me Yomki. What you tryin' to do with my bro?"
    y "Huh, don't tell me MC has a girlfriend now???????"

    hide asami_neutral
    show asami_mad:
        xpos 900
        ypos 140

    a "How dare you insinuate that I am this amoeba's girlfriend!"
    a "This guy's been ignoring me for the entire time while I talked about my life story."
    y "Can we skip dialogue here?"
    m "Nah, bro. This is a visual novel, if you skipped everything you wouldn't even have a game."
    y "I have no idea whats going on."
    a "Returning to the original subject, Kamiya-kun, I require an apology."
    m "Why should I need to apology, I didn't do anything. You're the one who's annoying me!"
    a "'Didn't do anything', You ignored me and then you call me annoying!"
    y "Guys, does it even matter?"
    y "You are not enemies... Nobody here has any enemies."
    y "Thus, you two are not enemies."

    hide asami_mad
    show asami_unsure:
        xpos 900
        ypos 140

    m "..."
    a "..."
    m "I'm sorry Asami, I shouldn't have ignored you. I was rude even though I barely knew you..."
    
    hide asami_unsure
    show asami_mad:
        xpos 900
        ypos 140
    
    a "It's too late now! We'll never be friends! I'm done talking to you!"
    
    hide asami_mad with Dissolve (1)

    m "(She leaves the class running. I think she forgot that classes still aren't done for the day. Maybe she'll realize this and return soon.)"

    show yomki:
        ease 1.5 xpos 400 ypos 25

    y "Bruh. I guess better luck next time MC."
    y "I gotta go now, bye."

    hide yomki with Dissolve (0.5)

    m "(What a chad, this dude.)"
    m "(She later came back after realizing it's still 10 in the morning.)"
    m "(Well, not that I really care.)"
    "The rest of the day goes by without any other incident."
    "Ding dong bing bong."
    m "(Maybe I should try to patch things up with Asami, if I let things like this, it's probably only gonna bring me trouble.)"

    show yomki with Dissolve (0.5)

    y "Hey bro, wanna head to WaccDonald's with me!"
    m "(If I go with him, I won't be able to patch things out right away.)"
    m "(But Yomki's my friend since elementary school.)"

    menu: 
        "What will you do?"

        "Talk to Asami":
            jump AsamiEvent1
        "Hang out with Yomki":
            jump YomkiEvent1

label YomkiEvent1:

    # TrueEnding Flag 1 here btw (Yes it's mandatory)
    # +1 Yomki Rizz Point
    $ Yomki_Event_1 = True

    m "(Finally, I decide to hang out with my bro Yomki.)"
    m "I'm coming! We're taking nuggets for sure!"

    play music ("bgm/5.ogg") fadeout (1)

    hide yomki with Dissolve (0.5)
    scene waccdonald with Dissolve (1)
    show yomki with Dissolve (0.5)

    y "Yo those new Big Waccs are bussin' frfr."
    m "Sure is bro."
    m "Still, no matter what year it is, Wacc Nuggets are still so poggers."
    y "BTW, bro. You started Dark Souls XX?"
    m "Yeah, I spent the entire night playing. I was so sleepy at school that I just wanted to sleep all day."
    m "But like you saw, things didn't go as planned."
    y "Damn, I hate when that happens bro."
    y "Oh, you won't believe who they brought back for the final boss."
    m "No way! Let me guess... Michael Zaki's Foreskin duo?"
    y "Nah bro! MANX THE SOUDER!"
    m "NO WAY FRFR???!?!?!?"
    y "No cap, bro."
    m "(Me and Yomki finish our meal. Time passes quickly as we discuss the strategies we used for each bosses.)"
    m "(After a while we decided to go back home.)"
    hide yomki with Dissolve (0.5)

    jump Day1EventEnd

label AsamiEvent1:

    # +1 Asami Rizz Point
    $ Asami_Event_1 = True

    m "(After thinking about it, I gotta fix things up.)"
    m "Sorry, not right now. I have something to do."
    y "Huh, something to do?"
    y "Oh wait never mind, I gotta no-life dark souls XX."
    y "Well good luck with Manx the Souder Requiem Over Heaven!"

    hide yomki with Dissolve (0.5)

    m "(I couldn't even say anything before he left.)"
    m "Well whatever."
    m "(She left already, so I have to run after her.)"
    m "(I quickly packed up my things and left.)"

    scene corridor with Dissolve (1)

    m "(I see her walking towards the stairs to leave.)"
    m "(I quickly chase after her and yell out:)"
    m "Asami wait!"
    
    show asami_judge with Dissolve (0.5)

    a "Eh?"
    a "..."
    m "I wanted to apologize again for earlier."
    a "..."

    hide asami_judge with Dissolve (0.5)

    m "(She continued walking down the stairs, ignoring me.)"

    show asami_mad with Dissolve (0.5)

    a "..."

    hide asami_mad with Dissolve (0.5)

    m "(She glances at me once before continuing.)"
    m "(I didn't go there just for nothing!)"
    m "(I go down the stairs, although she seems annoyed by my persistence.)"

    show asami_judge with Dissolve (0.5)

    a "..."
    a "Kamiya-kun... if you really want to apoligize to me..."
    a "I'll accept your apology only on one condition."

    hide asami_judge
    show asami_smug

    a "If you become my friend, then I'll gladly accept it!"
    m "..."
    m "(Is she stupid or what...?)"
    m "(I began wondering if I should accept.)"
    m "(On one hand, the entire case will be solved. But...)"
    pause 0.1
    m "(Man, she really is annoying.)"
    m "(Well, I went to the trouble and all of going to apologize.)"
    m "(I take a deep breath before sealing my fate.)"
    m "..."
    m "Okay, I accept. I'll become your friend."

    hide asami_smug
    show asami_intrigued

    a "You really mean it...?"

    hide asami_intrigued
    show asami_smug

    play music ("bgm/7.ogg") fadeout (1)

    a "Well, of course you'd accept!"
    a "You couldn't possibly decline being friends with such a cute girl!"

    hide asami_smug
    show asami_happy

    a "Just be glad you're now friends with someone as great as me!"
    m "(Man, I already regret my choice.)"
    m "(I may have accidently ruined my entire year.)"
    m "(Too late to go back.)"
    m "(Asami then grabbed her bag that she put on the floor when I interrupted her.)"

    hide asami_happy with Dissolve (0.5)

    m "(She left without saying anything else.)"
    m "(So, here I am... left alone wondering what to do now.)"
    m "Sigh.... guess I'll go home."

    jump Day1EventEnd

label Day1EventEnd:

    scene bedroom with Dissolve (1)
    play music ("bgm/bedroom.mp3") fadeout (1)

    m "Man, today was exhausting... what was that girl's problem!"
    m "Aside from that, school looks as boring as ever."
    m "I hope something interesting would happen soon..."
    m "At least it wouldn't be this boring."
    m "Well, I'm pretty tired from today, might as well go to sleep early."
    m "Especially since I barely slept last night."
    m "(Or did something make me exhausted this morning.)"
    m "(My memories seems a bit hazy.)"
    if Yomki_Event_1:
        m "(Maybe it's the chicken nuggets thats hitting.)"
        m "(...that doesn't make any sense, why the fuck would chicken do that?)"
        
    #YOMKI EVENT END
    
    else:
        m "(That's weird...)"
        m "(I don't remember eating something weird...)"
        
    #END OF ROUTE SPLIT
    
    m "(Meh, it's probably nothing!)"

    scene black with Dissolve (1)
    scene residential with Dissolve (1)

    play music ("bgm/2.ogg") fadeout (1)

    "The next day."
    m "Another captivating day at school..."
    m "(On my way to the school I see a pale haired girl running with a toast in her mouth.)"
    m "(There's still 5 minutes left before the bell rings...)"
    m "(Why is she even running...?)"

    show usui_neutral:
        xpos -800 ypos 140
        ease 1 xpos 1920 ypos 140
    pause 1

    m "Huh... anyway."
    m "Onward to hell!"

    scene classroom with Dissolve (1)

    "Waccland's peak academy, Place Japan, Hour: 7:58"

    m "(I arrive in class and sit at my desk.)"
    m "(An annoying face is staring at me right behind me.)"

    # if asami rizz point 1 = idk how to set variables

    if Asami_Event_1:

        show asami_happy with Dissolve (0.5)

        a "Hey Kamiya, good morning!"
        a "Don't you feel blessed being graced by such a cute girl in the morning?"
        m "No, I don't, thank you very much."
        
        show asami_judge
        hide asami_happy
        
        a "*Sigh* You just can't appreciate the good things in life can you?"

        hide asami_judge with Dissolve (0.5)

    # else the good route

    else:

        show asami_judge with Dissolve (0.5)

        a "..."
        m "(Of course she's ignoring me. Well not that it matters.)"
        m "(At least she's not bothering me.)"

        hide asami_judge with Dissolve (0.5)

    # END OF CHANGE IN ROUTE

    show izumi_neutral with Dissolve (0.5)

    "Mr. Izumi enters the classroom."
    i "Class is about to begin."

    hide izumi_neutral with Dissolve (0.5)

    "Ding dong bing bong."

    play music ("bgm/break.mp3") fadeout (1)

    m "(It's finally time for lunch break.)"
    m "(I'm gonna go see my bro Yomki.)"

    scene club with Dissolve (0.5)

    m "Yo Yomki."

    show yomki with Dissolve (0.5)

    y "Yo MC, I gamed so much last night."
    y "I'm already at my 7th playthrough of Dark Souls XX."
    m "What? No way, bro?"
    m "You're such a god gamer."
    y "True."
    m "(We continue to chat for a while.)"
    m "Hey, Yomki. Wanna go on the roof"
    y "Yeah bro. I love breaking school regulations."
    m "(And with that, we headed to the school rooftop.)"

    scene rooftop with Dissolve (1)

    show yomki with Dissolve (0.5)

    play music ("bgm/sus.flac") fadeout (1)

    m "(We arrived at the school rooftop, but we were not alone.)"
    y "No way, bro."
    m "(We witnessed a girl being confessed by what I can only describe as a dumbass.)"

    hide yomki with Dissolve (0.5)
    show miyuki_neutral with Dissolve (0.5)

    "Dumbass" "Miyuki-chan, ... please go out with me!!!"
    unk "Huh...?"
    unk "Are you stupid? I don't even know who you are?"
    unk "Eww, getting asked out by a random loser..."

    hide miyuki_neutral with Dissolve (0.5)

    m "(The dumbass quickly left while tears dropped from his eyes. What a dumbass? He really asked out a girl that he never talked to???)"

    show yomki with Dissolve (0.5)

    y "Damn bro, this dude got destroyed. Not cool."
    y "For serious."
    m "(I quickly turned around again towards the girl.)"

    hide yomki with Dissolve (0.5)
    show miyuki_neutral with Dissolve (0.5)

    unk "What a waste of time..."
    m "(While quickly glancing at her bag, I noticed a pin on it.)"
    m "(It's a pin of WA-KU-Oh!, my favourite anime!)"
    m "(Could perhaps this girl be one our kind???)"
    m "(Yomki noticed me staring at her, which he quickly whispered to me.)"

    show miyuki_neutral:
        ease 1 xpos 1400 ypos 1200
    show yomki with Dissolve (0.5):
        xpos 100 ypos 25

    y "She may look good bro, but that girl ain't one of us."
    y "She could never be a true gamer."
    m "Nah, bro, I saw that she had a WA-KU-OH! pin. Only real ones watch that shit."
    y "Hmmm... IDK then bro..."

    # Change to mad sprite or some shit
    unk "What are you two exactly staring at...?"
    m "Uh, nothing."
    m "(We quickly left before we were questioned by the girl.)"
    m "(Wouldn't want to ruin another day after what happened yesterday.)"

    scene corridor with Dissolve (1)

    show yomki with Dissolve (0.5)

    y "Anyway bro, we spent all these days grinding in Dark Souls XX."
    y "It's about time we go grind in real life."
    y "Let's go hit the gym and get GAINS after school!"
    m "(I could do what Yomki said, but I'm also intrigued by that girl...)"

    menu:

        "Hit the gym with your bro Yomki.":
            jump YomkiEvent2
        "Talk to the girl on the rooftop.":
            jump MiyukiEvent1

    label YomkiEvent2:
        #The True Route
        $ Yomki_Event_2 = True

        m "(I can't abandon my bro. We gotta get gains!)"
        m "Hell yeah, bro!"
        m "(We then left school to go the gym after class ended.)"

        scene gym with Dissolve (1)
        play music ("bgm/bro time.mp3") fadeout (1)
        show yomki with Dissolve (0.5)

        y "One more bro."
        m "Ngyaaaaahhhhh!!!!!"
        y "Heck yeah, bro! You da man!"
        m "(We passed time training in the gym.)"
        m "I'm about done for today now."
        y "Yeah, more than that and we're gonna literally die."
        m "Wait a sec, gonna buy you a drink."
        y "No way."
        
        hide yomki with Dissolve(0.5)

        m "(I then went to the vending machine to get a drink for me and Yomki.)"

        show bob_neutral with Dissolve (1)

        unk "Sup, bébé chat. You here to get gains as well?"
        m "Who the hell are you?"
        m "(Who even starts a conversation with someone by calling them bébé chat?)"
        m "Huhhh... yeah."
        unk "Damn, I go here every day. I'm gonna get as buff as a JoJo character."
        unk "Do you take the Sauce?"
        m "The fuck you mean sauce?"
        unk "The Sauce. Don't you know what Sauce is?"
        b "Anyway, the name's Yasuhiro Bob, you can call me Bob, or bébé chat, I don't really care."
        m "(Sauce, does he mean like, steroids? Of course I don't take that.)"
        m "Well, my name is Masashi Kamiya, you can call me MC."
        b "Okay, bébé chat."
        m "I didn't say you could call me that."
        m "But to answer your question, no. Why would I take steroids."
        b "Huh, what do you mean? The Sauce man!"
        b "I mean Ice Cream sandwiches."
        m "Huh?! But that's not even sauce."
        b "It is if your as bébé chat as me."
        
        show bob_neutral:
            ease 1 xpos 1400 ypos 1100

        show yomki with Dissolve(1):
            xpos 0 ypos 25

        y "What's taking you so long, MC. It's not long to get water."
        y "Who the fuck this???"
        y "Didn't know you were gay, MC!!?!?!"
        m "The fuck you mean, I just met this dude."
        b "Anyway, *With deep ass voice* later bébés chats."

        hide bob_neutral with Dissolve(0.5)
        show yomki:
            ease 1 xpos 400 ypos 25

        y "Whaaaaaatt theee heeeeeeelllllllll..."
        m "(Very intersting person...)"
        m "(I better act like nothing ever happenned.)"
        m "(It would be better for my mental health.)"
        y "By the way, where's my water?"
        m "Comin' right up!"
        m "(After this, me and Yomki went our separate ways and I headed back home.)"

        jump Day2EventEnd

    label MiyukiEvent1:
        #You really are a beta cuck
        $ Miyuki_Event_2 = True

        m "(I gotta ask her about the pin. WA KU OH! is my life after all.)"
        m "Sorry bro, not today. I have no energy."
        y "You better not be thinking of talking to that girl again. That would be cringe."
        m "Nah, nah, this ain't it."
        m "A gamer such as I would never fall to some lowly temptation like this!"
        y "That's true bro. G'day."

        hide yomki with Dissolve (0.5)

        m "(Yomki then left to go to his class.)"
        m "(I feel bad for lying, but a chance like this will never present itself ever again.)"
        m "(I go back to the rooftop after class, with some chance she'll be there again.)"

        scene rooftop with Dissolve (0.5)

        play music ("bgm/6.ogg") fadeout (1)

        m "(Class ended, and I went straight to the rooftop.)"
        
        show miyuki_neutral with Dissolve (0.5)

        m "(Yes, she's here. Now I can ask her.)"
        unk "Hmmm... Who are you again?"
        
        hide miyuki_neutral with Dissolve (0.5)
        show masashi_neutral with Dissolve (0.5)

        m "My name is Masashi Kamiya, but you can call me MC!"
        m "Gaming is my life and Wacc-Fuel is my blood."
        m "For over ten thousand years, I have protected this world from iminent destruction!"

        hide masashi_neutral with Dissolve (0.5)
        show miyuki_neutral with Dissolve (0.5)
        # changer l'expression pour une meilleure

        unk "Huh? The hell is wrong with this guy?"

        # serious face

        unk "Well, what business did you have with me?"
        m "Well, uhm..."
        m "It's about the pin on your backpack, could you possibly be a fan?"

        #change expression

        unk "Huh, this? I just picked it up 'cause it was popular at the time."
        unk "Don't know anything about it. Never bothered to watch it."
        m "(Damn, my luck ran out. She's a fake.)"
        m "(A damn normie. What a waste of my time.)"
        m "(Well, after all the trouble I went through, might as well ask for her name.)"
        m "Well, sorry for bothering you. But before I go, could I at least know your name?"

        #change expression

        unk "My name?"

        #change to miyuki neutral

        mi "My name is Mochizuki Miyuki. Do you have anything else to say? I'm quite busy after all."
        m "(If she's so busy, then why is she alone on the rooftop?)"
        m "(Whatever, I got what I asked for, time to leave.)"
        m "Then goodbye, Mochizuki-san."
        m "(I quickly leave before the embarassment of revealing myself to a fake fan kills me.)"

        scene corridor with Dissolve (1)

        m "(At this point, I have nothing else to do, so might as well go home.)"

        jump Day2EventEnd

    label Day2EventEnd:

    show bedroom with Dissolve(1)
    play music ("bgm/bedroom.mp3") fadeout (1)

    m "(I arrived home at last after another tiring day.)"

    if Yomki_Event_2:

        m "(That Bob guy was weird as hell...)"
        m "(Why does he insist on calling ice cream sandwiches ''Sauce''...)"

    elif Miyuki_Event_2:

        m "(She was not a real fan after all. I hate people who just ride the wave of popularity of things.)"
        m "(And she talked like she wanted me out of her sight. Well, I guess since I kinda showed up out of nowhere it makes sense.)"

    else:
        "You shouldn't be here..."
        "YOUR COCK..., YOUR VERY BALLSACK..."
        "I WILL CUT IT DOWN."
        "TF IS THIS SHIT."

    m "(No use thinking about this more than necessary.)"
    m "(I should just go to sleep...)"

    scene black with Dissolve(0.5)

    "The next day..."

    scene residential with Dissolve(0.5)

    play music ("bgm/2.ogg") fadeout (1)

    m "(Day 3 of my new school life, and it's not going very well...)"
    m "(Everyone I've met thus far has been either completely insane or kind of assholes.)"
    m "(I do wonder what other quirky people I will meet next...)"
    m "(But I sure wish this streak of weirdness would end soon...)"
    m "(I don't mind weird stuff happening once in a while... but this is a bit much.)"

    scene classroom with Dissolve(0.5)

    m "(I sit down and attend my classes like usual.)"
    m "(The classes go by without much interesting happening.)"

    "Ding dong bing bong"

    m "Guess the day's over."
    m "What should I do next."
    m "I could hang out with Yomki like usual."
    m "Or just go home and game all evening..."

    if Asami_Event_1:

        show asami_neutral with Dissolve(0.5)

    else:
        show asami_judge with Dissolve(0.5)
    #Route split finished

    m "Huh... why is she looking at me?"

    if Asami_Event_1 == False:
        a "..."
        m "She's been quiet for the last few days."
        m "Should I try to apologize to her again?"
        m "I really don't know if it's a good idea."
    else:
        a "Hey MC!"
        a "See you tommorow!"
    #Route split finished

    m "..."
    m "(I guess I could try my chance talking with Asami too.)"

    menu:

        "Go straight home.":
            jump IzumiEvent3
        "Hang out with Yomki again.":
            jump GorouEvent3
        "Talk with Asami.":
            jump AsamiEvent3

    label IzumiEvent3:

        $ Izumi_Event_3 = True

        m "(I decide to go straight home.)"
        m "(With these past few days being so weird, I merit a break of sorts.)"
        m "(I take my bag and head straight towards the exit.)"

        scene school with Dissolve(0.5)

        play music ("bgm/8.ogg") fadeout(1)

        m "(As usual, the road to exit the school is completely filled with students.)"
        m "(Not surprising, who in their right mind would want to stay in hell?)"
        m "(I start to walk towards the exit.)"
        m "(Altough while turning to get on the sidewalk, I notice someone I know.)"

        show izumi_neutral with Dissolve(0.5)

        m "Mr. Izumi?"
        i "Ah, Kamiya, heading home?"
        m "Yeah."
        i "Also you can drop the mister while outside school."
        i "Puts some kind of distance between people when you use honorifics"
        m "Well yeah... that's true."
        m "Didn't know you smoked."
        i "Huh, yeah, been smokin' for a quite a long time."
        i "All 'cause of this one guy."
        i "Always rambled on and on about how he much he despised lazy people."
        i "He was always like: ''Those damn fools don't even bother doing anything with their lives.''"
        i "Sure enough, the guy went on to become CEO of the largest company in the entire world."
        i "I saw him a couple of years ago and he invited me for a drink."
        i "He kept talking about business and stuff."
        m "What was his name?"
        i "Michel."
        m "I'm pretty sure I heard that name before..."
        m "Wait-"
        m "THE Michel Popstonia studied here at Waccland's peak academy?!?"
        i "Yep, That's right"
        m "Doesn't seem like his attitude changed much."
        i "Yeah."
        i "I remember back in my days, we didn't even have phones."
        i "Hell, we didn't even have electricity."
        i "It was all just swords, and magic, and all."
        m "Wait, wasn't electricity discovered in like 1800?"
        i "1752."
        i "Just an exaggeration by the way."
        i "Me and my friends went on a long long journey."
        i "We were on a quest to find and restore the balance of the seven crystals of the elements."
        i "The one we called the lord of the seventh had created a dark crystal which destroyed the balance of the world."
        i "So we defeated him and were hailed as the heroes of the land."
        i "That's about it, I guess."
        m "Huh...???"
        m "(After this long monologue how could I not ask myself a thousand questions?)"
        m "...uhhh... mr.Izumi...?"
        i "You don't have to call me mister."
        m "...Izumi, how often do you smoke?"
        i "Not that much."
        i "One day you'll understand how it feels like to be a living legend."
        m "...Alright then, have you been playing WACC Quest XIII too much?"
        i "Probably."
        m "(Interesting, I didn't think he'd be the type to play games like that.)"
        m "Then, are you one of us?"
        i "''One of us...?''"
        m "A gamer."
        i "I guess you could call me that."
        i "I've played pretty much all the classics from the 90's."
        i "From WACC Fantasy, to the legend of WACC, to WACCLAND 64."
        m "Damn-"
        m "You're old."
        i "You do know I'm 36?"
        i "Wait, I think I've forgotten a couple of digits."
        i "When you start getting as old as me, you start forgettin' things like that."
        m "...?"
        m "How old are you again?"
        i "That's not relevant-"
        i "Either way, I gotta go."

        hide izumi_neutral with Dissolve (0.5)

        i "See you tommorow, Masashi-kun."
        m "...See you tommorow mr.Izumi."
        m "..."
        m "(Well, that wasn't what I was expecting.)"
        m "(I'm not sure yet if he's cool, ...or just kinda crazy.)"

        jump Day3EventEnd
    
    label GorouEvent3:

        $ Gorou_Event_3 = True

        m "(I guess I'll hang out with Yomki again.)"
        m "(He IS my best friend after all.)"

        scene club with Dissolve (0.5)

        play music ("bgm/5.ogg") fadeout(1)

        m "Hey, Yomki! You here?"

        show yomki with Dissolve (0.5)

        y "Yeah bro, I'm here."
        y "Was just talking with one of my homies."

        show yomki:
            ease 1 xpos 1400 ypos 1100

        show gorou_neutral with Dissolve (0.5)

        y "He's pretty cool, no cap."

        hide yomki with Dissolve (0.5)

        stop music fadeout (1)

        #Edgy music here

        unk "..."
        unk "I..."
        unk "I am-"
        unk "The prince of darkness himself."
        unk "The owner of the black throne, the one they call the ultimate despair!"
        unk "I am..."

        show gorou_neutral:
            ease 1 xpos 1400 ypos 1100

        show yomki with Dissolve (0.5)
        
        y "His name is Furukawa Gorou."

        play music ("bgm/7.ogg") fadeout(1)

        g "..."
        g "C'mon, you ruined my introduction!"
        m "..."
        m "(Are you kidding me?)"
        m "(Yet another mentally ill student?)"
        g "Like I said, I am the one they call the prince of darkness."
        g "Common mortals such as you should not come too close to me."
        m "Uhhh..."
        m "I have a question."
        m "Are you stupid?"
        g "W-what?!?"
        g "You dare insult me?"
        g "My power of darkness shall rend you apart."
        g "There shall be nothing left of your corpse."
        g "As the wind howls, the shadows within still unsatisfied."
        m "Can't you just cut the bullshit?"
        m "Stop acting like a fucking kid, you're a high schooler."
        g "What did you just say-"
        g "...hahaha..."
        g "HAHAHAHAHAHA!!!"
        g "No one..."
        g "No one has ever been so foolish as to challenge me!"
        m "Well sure makes sense, why would anyone want to talk with you."
        m "You're the kind of guy who never even spoke to a woman before."
        m "The world doesn't revolve arround you dumbass."
        y "Yo MC! Not cool bro. That's going too far."
        g "Indeed, your insolence knows no limit."
        g "but of course-"
        g "You have not been chosen by the throne of darkness to stand above heaven and earth."
        m "Yeah, 'cause my father didn't leave for milk when I was a kid."
        y "Guys!"
        y "That's enough!"
        g "No!"
        g "This man has insulted me and my whole lineage!"
        y "Wait, I know what to do."

        stop music fadeout (1)

        "Yomki whispers something into Gorou's ears."

        g "!!!"
        g "Yomki!"
        g "Why didn't you tell me earlier that this guy played Waccland chronicles!!!"
        m "...?"
        m "Huh?"

        show gorou_neutral:
            ease 1 xpos 900 ypos 1100

        hide yomki with Dissolve(0.5)

        play music ("bgm/8.ogg") fadeout(1)

        g "I sincerely apologize, MY BEST FRIEND!"
        g "It seems I was mistaken about you!"
        g "You are not my enemy."
        g "I have seen the errors of my way."
        g "How could I forget the words of wisdom my master left me-"
        g "''Nobody has any enemies, not you, not me.''"
        g "I don't have any enemies."
        g "I thank you MY BEST FRIEND, for teaching me this valuable lesson!"
        m "No need to thank me, MY FRIEND."
        g "..."
        g "Wait-"
        g "I never asked for your name..."

        hide gorou_neutral
        show masashi_neutral
        with Dissolve (0.5)

        m "My name is Masashi Kamiya, but you can call me MC!"
        m "Gaming is my life and Wacc-Fuel is my blood."
        m "For over ten thousand years, I have protected this world from iminent destruction!"

        hide masashi_neutral 
        show gorou_neutral
        with Dissolve (0.5)

        m "I'm sorry for doubting you Gorou."
        m "You were one of my people after all."

        hide gorou_neutral
        show gorou_smug

        g "As they say in the lands between, those who play Waccland Chronicles are your friends."
        m "Facts Brother!!!"
        m "Spit Your shit indeed!"
        m "(Me and Gorou then proceed to have the nerdiest handshake ever.)"
        g "It was nice to meet you MC, MY FRIEND."
        g "Unfortunately, I must go now, for my untouched game needs some playing!"
        g "Farewell!"
        m "Bye!"

        hide gorou_smug with Dissolve (0.5)

        m "I got this guy completely wrong..."
        m "Man."

        show yomki with Dissolve (0.5)

        y "Told you he was epic, bro!"
        m "You never dissapoint, bro."
        m "Alright, wanna walk home?"
        y "Sure thing, bro."

        scene black with Dissolve (0.5)

        m "(While walking home, me and Yomki continue talking about our countless playtroughs of Dark Souls XX.)"
        m "(We talked about all the secrets and hidden items we found.)"
        m "(Truly, Michael Zaki never misses.)"
        m "(Altough the time for us to part ways soon came.)"

        jump Day3EventEnd

    label AsamiEvent3:

        $ Asami_Event_3 = True

        "This is the Asami day 3 event."

        if Asami_Event_1 == False:

            $ Asami_Event_1 = True

            "You had not completed the day 1 event with Asami."
        else:
            "You have completed the day 1 event with Asami."

        "This is the continuation of the event."

        jump Day3EventEnd

    label Day3EventEnd:

    scene bedroom with Dissolve(0.5)

    play music ("bgm/bedroom.mp3") fadeout (1)

    m "Uhhhhh tf do i cook??????"
    "but suddenly"

    play sound "sfx/vine boom.mp3"

    show saul with dissolve

    "Saul Goodman Jumpscare"
    hide saul

    stop music fadeout (3)

    "You feel a strong aura approaching."
    "Someone enters the classroom."
    "HE approaches YOU."

    show billy with Dissolve (2):
        xalign 0.7
        ypos 25
    play music ("bgm/alphen.mp3") fadeout (1)

    "Billy" "YO ITS ME BILLY WACCLAND SMP IV HERE TO TELL YOU TO GET BITCHES LOSER!!!!!!!!"
    "Billy" "COCK AMIRITE FELLAS!!!"
    "Billy" "So basically, this is YOUR Waccland DaTING SIM 2: Electric Boogaloo, now go now."
    "With Wacc and land."
    hide billy with Dissolve (1)
    "YOu suddenly remember Big CHungus'S words."
    m "NO WAY I NEED TO COOK!!!"
    m "BE MY GIRLFRIEND ASAMI!!!"
    a "Fuck no! WTF!"
    y "Damn, such a rizzler."
    m "(I...I-I.... failed....?)"
    m "(My sigma rizz failed me...??????)"
    m "THIS GAME SUCKS!"
    m "Fuck this shit I'm OUT!"
    "You then jump off from the window and die."
    play sound "sfx/vine boom.mp3"
    "The end."

    # This ends the game.

    return
