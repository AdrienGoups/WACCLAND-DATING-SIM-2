# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Kamiya")
define u = Character("Usui")
define b = Character("Bob")
define c = Character("Big Chungus")
define a = Character("Asami")
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
    m "I will get a Girlfriend... and ##########"

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
    m "Yet another captivating day of school awaits me."

    scene black with dissolve

    "You quickly prepare yourself for school."
    "You also vaguely question why you suddenly started to think out loud, but you dismiss the idea pretty quickly"
    m "Whatever, I'm leaving now!.... Why am I yelling this, I literally live alone..."

    scene residential with dissolve

    play music "bgm/2.ogg"
    
    m "Huh...? Something feels different today..."
    m "I should probably hurry up"
    "You bolt towards the school quickly dodging the cars as you pass through crosswalks on your way there."
    "A set of stairs separate you from the entrance to the school."
    "As your foot approaches the floor, your body begins to plummet towards the ground."
    m "Oh shit, I'm gonna die!"
    "Mustering up your determination to not end your life prematurally, you execute a quadruple backflip before griping the rail with your hands and pulling yourself up on the rail."
    "Now with your feets on the rail, you grind down the remainder of the stairs before landing safely at the bottom."
    m "Damn, it's like I'm the protagonist or something!"
    "Suddenly, a scream echoes out behind before you're pushed to the ground by a great force."
    m "What in the-???"
    unk "AHHHHH!!!! GOMENASAI!?!?!? WHATASHI WA GENERIC ANIME GIRL MOMENT #3??!!?!??!"
    "uh what the fuck is he cooking??????"
    # I ain't cookin' more until you figure out what to do
    m "(What the hell is happening right now? It's like my life has been turned into a generic anime!)"

    play sound "sfx/vine boom.mp3"

    show saul with dissolve

    "Saul Goodman Jumpscare"

    # This ends the game.

    return
