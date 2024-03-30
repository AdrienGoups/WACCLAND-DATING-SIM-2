# The script of the game goes in this file.

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
define unk = Character("???")



# The game starts here.

label start:

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

    c "Masashi Kamiya... Thoust grand quest begins here."
    c "It all begins here..."
    c "Acquire a Maiden. That is thy task."
    c "Now, go forth with Wacc and Land, my child!"

    play sound "sfx/bonk.mp3"

    scene bedroom with dissolve
    
    stop music

    m "Huh..."
    "A blinding light passes through the curtains straight into your face..."
    "You realize that you have overslept and that your alarm has been ringing for a good 15 minutes"
    m "Isn't 15 minutes a bit much?!"
    # nah i'd win
    "You quickly turn off the alarm"
    m "..."
    m "The hell was this dream??"
    m "I feel like I should be remembering something important just now..."
    m "Dammit, the curse of shitty games has befallen me."
    m "..."
    m "...Wait... yeah probably should get up..."
    m "Yet another captivating school year awaits me..."

    scene black with dissolve

    "You quickly prepare yourself for school."
    "You also vaguely question why you suddenly started to think out loud, but you dismiss the idea pretty quickly"
    m "Whatever, I'm leaving now!.... Why am I yelling this, I literally live alone..."

    scene residential with dissolve

    play music "bgm/2.ogg"
    
    m "Huh...? Something feels different today..."
    m "Probably nothing..."
    m "I should probably hurry up"
    "You bolt towards the school quickly dodging the cars as you pass through crosswalks on your way there."
    "A set of stairs separate you from the entrance to the school."
    "The school is now right in view. And still 15 minutes until the bell rings."
    m "(And now I'm standing at the doors of Waccland Peak Academy.)"
    m "(First founded in 1869, this school was the gathering place for all the most brilliant minds.)"
    m "(It's name derives from Kevin Waccland, the saviour of the world, inventor of Wa Ku Ho!)"
    m "(A place for such amazing people, named after the most amazing person.)"
    m "(Well, now it's just a normal high school that even normal people can go. That's how I got here.)"
    m "Well I better go to my class before the bell rings"
    "You follow the indications to your new class, class 1-C"
    scene classroom with Dissolve (1)
    "As you enter the door, you quickly maneuver through the desks to arrive at your assigned desk, right beside the window in the second to last row."
    m "(I'm still sleepy... shouldn't have gamed all night...)"
    "You slowly close your eyes..."
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

    "She then goes to sit right behind you, unfortunately..."
    i "Well, Good Morning everyone. My name is Nanami Izumi, just a plain' ol' teacher."
    "Female Student 1" "Wow, he's so cool and hot!"
    "Female Student 2" "He looks so mature!"

    hide izumi_neutral with Dissolve (0.5)

    m "(Man, all the female students are talking about the new teacher...)"
    m "(This is so cliché, can't they just, I don't know... concentrate on the class instead????)"
    m "(It's almost always the same as soon as we have a young male teacher.)"
    m "(Well, no use complaining about that on the first day of school, they'll stop once they realize he's just a plain old teacher.)"
    "You sat through the entire class between dream and reality, contemplating the meaning of life and why you decided to game all night."
    "You briefly wonder if this whole scenario was schemed by someone..."
    "...Altough you quickly dismiss the idea."

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
    m "Why should I need to apology, I didn't do anything. You're the one who's annoying me"
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

    y "Hey bro, wanna head to WaccDonald with me!"
    m "(If I go with him, I won't be able to patch things out right away.)"
    m "(But Yomki's my friend since elemantary school.)"

    menu: 
        "What will you do?"

        "Talk to Asami":
            jump AsamiEvent1
        "Hang out with Yomki":
            jump YomkiEvent1

label YomkiEvent1:

    # TrueEnding Flag 1 here btw (Yes it's mandatory)
    m "(Finally, I decide to hang out with my bro Yomki.)"
    m "I'm coming! We're taking nuggets for sure!"

    jump Day1EventEnd

label AsamiEvent1:

    # +1 Asami Rizz Point

    m "(After thinking about it, I gotta fix things up.)"
    m "Sorry, not right now. I have something to do."
    y "Huh, something to do?"
    y "Oh yeah Dark Souls XX just dropped."
    y "I gotta go get it from Epic Games UK."
    y "Well good luck with Manx the Souder Requiem Over Heaven!"

    hide yomki with Dissolve (0.5)

    m "(I couldn't even say anything before he left.)"
    m "Well whatever."

    jump Day1EventEnd

label Day1EventEnd:

    "but suddenly"

    play sound "sfx/vine boom.mp3"

    show saul with dissolve

    "Saul Goodman Jumpscare"
    hide saul

    stop music

    "HE appears."
    "HE approaches YOU."

    show billy
    play music ("bgm/alphen.mp3") fadeout (3)

    "Billy" "YO ITS ME BILLY WACCLAND SMP IV HERE TO TELL YOU TO GET BITCHES LOSER!!!!!!!!"
    "Billy" "COCK AMIRITE FELLAS"
    "Billy" "Anyway, this is YOUR Waccland DaTING SIM 2: Electric Boogaloo, now go now."
    "With Wacc and land."
    "YOu suddenly remember Big CHungus'S words."
    m "NO WAY I NEED TO COOK"
    m "BE MY GIRLFRIEND ASAMI"
    a "Fuck no! WTF!"
    y "Damn, such a rizzler."
    m "(I...I-I.... failed....?)"
    m "(My sigma rizz failed me...??????)"
    m "THIS GAME SUCKS"
    m "Fuck this shit I'm OUT!"
    "You then jump off the window and die"
    play sound "sfx/vine boom.mp3"
    "The end."

    # This ends the game.

    return
