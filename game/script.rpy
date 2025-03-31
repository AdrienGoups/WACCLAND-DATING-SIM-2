label splashscreen:
    scene black

    "The Time has Cometh, for the peakest of the peak."
    "Now Sit back and get your ass blown away by peak fiction."
    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Kamiya", who_color="#f06767")
define u = Character("Usui", who_color="#ade7f7")
define b = Character("Bob", who_color="#eb9c71")
define c = Character("Big Chungus", who_color="#ccfffa")
define a = Character("Asami", who_color="#de6ac9")
define t = Character("Teacher", who_color="#7489d4")
define i = Character("Mr. Izumi", who_color="#7489d4")
define y = Character("Yomki", who_color="#e0bf72")
define mi = Character("Miyuki", who_color="#8f72e0")
define g = Character("Gorou", who_color="#79db9a")
define go = Character("Gotou", who_color="#4079bb")
define mo = Character("Momoka", who_color="#ffaf96")
define cl = Character("Classmates")
define unk = Character("???")

# The game starts here.

label start:
    
    $ Asami_Event_1 = False
    $ Yomki_Event_1 = False
    $ Yomki_Event_2 = False
    $ Miyuki_Event_2 = False
    $ Izumi_Event_3 = False
    $ Asami_Event_3 = False
    $ Gorou_Event_4 = False

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

    "APRIL 1, 20XX."
    "The final day has arrived."
    "No one could have guessed what was coming."
    "But even then, we had to fight it..."

    # MET UNE IMAGE DE LA PLANETE QUI SE FAIT ATTACKER OR SOME SHIT
    scene destroyed_world with Dissolve (3):
        ypos -0.3 xpos -0.3
        ease 10.0 ypos 0

    pause 0.5

    "The land was scorched to the ground..."
    "They had come, the ones he warned us about..."

    #MC, the only way you can save this world is gone
    unk "MC, the only way you can save this world is ############."
    #I will send you back to the past, exactly 1 year ago.
    unk "I will ######### to ##########."
    #Masashi, you have one mission. One of the greatest importance...
    unk "###########, you have one mission. One of the greatest importance..."
    unk "You must find love. At any cost, no matter if it's one or a thousand... You must get a Girlfriend!"
    #I'm sorry, I couldn't do anything about her... but that's why you need to succeed... no matter the cost.
    unk "########## I couldn't do anything about ######## why you need to succeed... ########## the cost."
    m "I understand..."
    m "I'll do it!"
    m "I will get a Girlfriend... and-"

    play music ("bgm/man....mp3") fadeout (3.5)

    scene black with Dissolve (3)
    scene white with Dissolve (.5)

    show chungus with Dissolve (3)

    c "It is nice to meet you, MC."
    c "I am the being known as Big Chungus,"
    c "The overseer of this world."
    c "Masashi Kamiya... Thoust grand quest begins here."
    c "Acquire a partner. That is thy task."
    c "Altough, you are unfortunately but an average high school student."
    c "You shall better yourself in due time to have any chance of winning the heart of a maiden."
    c "You shall face many trials and challenges, but I believe in thy potential."
    c "Now, go forth with Wacc and Land, my child!"
    c "For this is YOUR Waccland Dating SIM 2: Electric Boogaloo."

    play sound "sfx/bonk.mp3"

    pause 0.2

    scene black with Dissolve(.1)

    stop music fadeout 0.5

    pause 2

    scene bedroom with Dissolve (3)

    m "Huh..."
    m "(A blinding light passes through the curtains straight into my face...)"
    m "(I realize that I have overslept and that my alarm has been ringing for a good 15 minutes.)"
    m "Have I really been ignoring it for 15 minutes?!"
    m "(I quickly turn off the alarm.)"
    m "..."
    m "The hell was this dream??"
    m "I feel like I should be remembering something important just now..."
    m "Dammit, I can't remember..."
    m "(This oddly feels like the plot of an anime I watched not long ago...)"
    m "(Couldn't tell which one, this trope's too common.)"
    m "..."
    m "I shouldn't stay in bed for much longer or I'll be late."
    m "Yet another captivating school year awaits me..."

    scene black with dissolve

    m "(I quickly prepare myself for school.)"
    m "(I also vaguely question why I suddenly started to think out loud, but I dismiss the idea pretty quickly.)"
    m "(Whatever, I'm leaving now!)"

    scene residential with dissolve

    play music ("bgm/2.ogg") fadeout (1)
    
    m "(Today's my first day of high school.)"
    m "(Most people would be either excited or discouraged, but what I'm feeling is different.)"
    m "(I've got this weird feeling of anxiety slowly invading my body, like something is wrong.)"
    m "(...I'm probably worrying for nothing.)"
    m "(I should probably hurry up though.)"
    m "(I bolt towards the school quickly dodging the cars as I pass through crosswalks on my way there.)"
    m "(A set of stairs separate me from the entrance to the school.)"

    scene school with Dissolve (1)

    m "(The school is now right in view. And still 5 minutes until the bell rings.)"
    m "(And now I'm standing at the doors of Waccland's Peak Academy.)"
    m "(First founded in 1869, this school was the gathering place for all the most brilliant minds.)"
    m "(It's name derives from Kevin Waccland, the saviour of the world, inventor of WA KU OH!)"
    m "(It is said that he lived about 2000 years ago.)"
    m "(A place for such amazing people, named after the most amazing person.)"
    m "(Well it would be but... now it's just a normal high school that even normal people can go. That's how I got here.)"
    m "(You can thank the war 40 years ago for this.)"
    m "(Well I better go to my class before the bell rings.)"

    play sound ("sfx/vine boom.mp3")
    show saul with Dissolve (0.5)
    "Saul Goodman Jumpscare."
    hide saul with Dissolve (0.5)

    m "(I follow the indications to my new class, class 1-C.)"
    scene classroom with Dissolve (1)
    m "(As I enter the door, I quickly maneuver through the desks to arrive at my assigned desk, right beside the window in the second to last row.)"
    m "(I sit at my desk while trying my hardest to stay awake.)"
    m "(I'm still sleepy... shouldn't have gamed all night...)"
    m "(I slowly close my eyes...)"
    scene black with Dissolve (2)
    unk "Hey!!"
    scene classroom with Dissolve (2)

    m "?!"
    m "What?!"
    show asami_neutral with Dissolve (1)

    unk "You've just woken up for school and you're gonna go back to sleep now?"
    m "...?"
    m "Who even are you?"
    unk "Me? That's not really important right now!"
    unk "You can't just start sleeping in the middle of class!"
    unk "I'm telling this for your own good, you know?"
    m "(What's with this annoying girl, I was just minding my own business and she starts critizing my lifestyle of sleeping through the entire class.)"
    m "(I have also never even seen her face before...)"
    m "(With that kind of personality, I'm pretty sure I would have at least taken notice of her in middle school.)"
    unk "What's with that reaction! Very well, I shall introduce myself."

    show asami_smug
    hide asami_neutral

    a "The name's Nakamura Asami! You better remember it!"
    a "I'll have you know I was the most popular girl at my middle school!"
    m "(With this attitude? This girl's delusional... I better ignore her, maybe she'll leave soon if she sees I'm not interested in small talk.)"
    a "Well, I just arrived here, can't afford to be picky with friends!"
    a "And you were conveniently in the desk right in front of me!"
    a "My parents came here for work, so I don't know anyone here."
    a "Back home, I had tons of friends. Now, I have to start back at square one. But I won't let that stop me!"
    a "After all, I'm not some kind of loser that talks to no one!"
    m "(What is she even talking about, I stopped listening ages ago...)"
    m "Sigh..."

    hide asami_smug
    show asami_mad

    play music ("bgm/7.ogg") fadeout(1)

    a "Hey are you ignoring me!"
    m "I sure am. Now, leave me alone."
    m "I'm too tired to be dealing with someone who doesn't know what personal space is."
    a "That's not very polite! You're talking to such a cute girl and you don't even bother listening to a word she says!"
    m "I don't see the correlation between your points. I'm trying to sleep here."
    m "Besides, just because you're pretty doesn't mean you can get away with doing whatever you want."
    a "The audacity! Are you stupid or what?"
    a "Don't answer. I already know you are!"
    a "Who even greets a stranger like that?"
    
    "Suddenly, the doors slams open."

    play music ("bgm/2.ogg") fadeout(1)

    show asami_mad:
        ease 1 xpos 1600

    show izumi_neutral with Dissolve (0.5)

    t "Quiet everyone, class is going to start soon!"
    a "We'll continue this later! I won't stop until you understand the errors of your ways!"
    t "I said quiet, Asami!"
    a "Okay..."
    a "(...How does he already know my name?)"

    hide asami_mad with Dissolve (1)

    m "She then goes to sit right behind me, unfortunately..."
    i "Well, Good Morning everyone. My name is Izumi Naoki, just a plain' ol' teacher."
    "Female Student 1" "Wow, he's so cool and hot!"
    "Female Student 2" "He looks so mature!"

    hide izumi_neutral with Dissolve (0.5)

    m "(Man, all the female students are talking about the new teacher...)"
    m "(This is so cliché, can't they just, I don't know... concentrate on the class instead????)"
    m "(It's almost always the same as soon as we have a male teacher that looks slightly better than average.)"
    m "(Well, no use complaining about that on the first day of school, they'll stop once they realize he's just a plain old teacher.)"
    m "(I sat through the entire class between dream and reality, contemplating the meaning of life and why I decided to play games all night.)"
    m "(I briefly wonder if this whole scenario was schemed by someone...)"
    m "(...Although I quickly dismiss the idea.)"
    m "(That's what I get for playing games during the whole spring break.)"

    "Ding dong bing bong!"

    show izumi_neutral with Dissolve (0.5)

    i "Well, looks like time is up, we'll continue next class where we left off."

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
    m "(We've known each other since elementary school.)"
    m "(Like me, he's also a huge gamer and he's also my best friend.)"
    m "(Unfortunately, he isn't in my class this year.)"
    y "Sup, it's me Yomki. What you tryin' to do with my bro?"
    y "Huh, don't tell me MC has a girlfriend now???????"

    hide asami_neutral
    show asami_mad:
        xpos 900
        ypos 140

    play music ("bgm/7.ogg") fadeout(1)

    a "How dare you insinuate that I am this loser's girlfriend!"
    a "This guy's been ignoring me for the entire time while I talked about my life story."
    y "Isn't there supposed to be a skip button somewhere?"
    m "Sorry bro, we're not in a video game, you'll have to listen to her profoud speech.."
    y "I have no idea what's going on."
    a "Returning to the original subject, Kamiya-kun, I require an apology."
    m "Yeah, and why should I? From what I recall, you're the one who's been bothering me."
    a "'Bothering me', You ignored me and then you call me annoying!"
    y "Guys, does it even matter?"
    y "You are not enemies... Nobody here has any enemies."
    y "Thus, you two are not enemies."

    hide asami_mad
    show asami_unsure:
        xpos 900
        ypos 140

    stop music

    m "..."
    a "..."

    play music ("bgm/8.ogg") fadeout(1)

    m "I'm sorry Asami, I shouldn't have ignored you. I was rude even though I barely knew you..."

    stop music
    
    hide asami_unsure
    show asami_mad:
        xpos 900
        ypos 140
    
    a "Well I don't care! You should've apologized sooner!"
    a "You really piss me off."

    play music ("bgm/2.ogg") fadeout(1)
    
    hide asami_mad with Dissolve (1)

    m "(She leaves the class running. She probably forgot that classes still aren't done for the day. Maybe she'll realize this and return soon.)"

    show yomki:
        ease 1.5 xpos 400 ypos 25

    y "Bruh. I guess better luck next time MC."
    y "Maybe one day you'll have as much charisma as me."
    m "Yeah... I guess."
    m "I'll have to use your secret technique."
    y "Yeah told you bro, girl loves guys who play souls games."
    y "If I were in your place she would have 100 percent accepted my apology."
    m "Can't deny that."
    y "But don't worry bro, you just gotta climb harder."
    y "I gotta go now, bye."
    y "Don't forget to hop on VC tonight."
    m "Yeah I will, homie."

    hide yomki with Dissolve (0.5)

    m "(What a chad, this dude.)"
    m "(She later came back after realizing it's still 10 in the morning.)"
    m "(Well, not that I really care.)"
    "The rest of the day goes by without any other incident."
    "Ding dong bing bong."
    m "(Maybe I should try to patch things up with Asami, if I let things like this, it's probably only gonna bring me trouble knowing her personality.)"

    show yomki with Dissolve (0.5)

    y "Hey bro, wanna head to WaccDonald's with me!"
    y "I know I said to hop on VC, but I'm hungry and could really use some WaccDonald's."
    m "(His offer is tempting, but he'll have to wait a bit.)"
    m "(The future of my school life rests upon this operation, I can't ignore it.)"
    m "Sorry, not right now. I have something to do."
    m "I'll join you later though, I'm in dire need of some chicken nuggets."
    y "Huh, something to do?"
    y "You don't mean..."
    y "Oh wait never mind, gotta no-life dark souls XX while you take care of your business."

    hide yomki with Dissolve (0.5)

    m "(I couldn't even say anything before he left.)"
    m "Well whatever."
    m "(She left already, so I'll have to run after her.)"
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

    show asami_judge
    hide asami_happy

    a "What? Why are you looking at me like that?"
    a "You aren't happy to be friends with me?"
    m "Take a guess."
    a "..."

    show asami_unsure
    hide asami_judge

    pause 0.5
    
    m "(Asami then grabbed her bag that she put on the floor when I interrupted her.)"

    hide asami_unsure with Dissolve (0.5)

    m "(She left without saying anything else.)"

    play music ("bgm/5.ogg") fadeout (1)

    m "(Welp, time to call Yomki to tell him I'm done.)"

    scene waccdonald with Dissolve (1)
    show yomki with Dissolve (0.5)

    y "Yo those new Big Waccs are bussin' frfr."
    m "Sure is bro."
    m "That special rizz sauce sure is something."
    y "Yeah I know what you mean, it tastes like when you finally find a bonfire after a long and arduous climb in Dark Souls."
    m "Couldn't find a better analogy than this bro."
    m "Still, no matter what year it is, Wacc Nuggets are still so poggers."
    y "Yeah bro, the quality of the chicken is really nuts."
    y "And the crispy exterior is also really fire."
    m "No matter what products they do, any Waccland products are straight up peak."
    y "Yeah, no wonder they're such a big company."
    y "BTW, bro. You started Dark Souls XX?"
    m "Yeah, I spent the entire night playing. I was so sleepy at school that I just wanted to sleep all day."
    m "But like you saw, things didn't go as planned."
    y "Damn, I hate when that happens bro."
    y "Oh, you won't believe who they brought back for the final boss."
    m "No way! Let me guess... Michael Zaki's Foreskin duo?"
    y "Nah bro! MANX THE SOUDER!"
    m "NO WAY FRFR ONG???!?!?!?"
    y "No cap, bro ong."
    m "(Me and Yomki finish our meal. Time passes quickly as we discuss the strategies we used for each bosses.)"
    m "(From the godly Rick, soldier of god to the amazing Patches consort of Miyazaki, truly Michael Zaki never missed.)"
    m "(After a while we decided to go back home.)"
    hide yomki with Dissolve (0.5)

    scene bedroom with Dissolve (1)
    play music ("bgm/bedroom.mp3") fadeout (1)

    m "Man, today was exhausting... what was that girl's problem!"
    m "And then she wants to be friends with me?"
    m "She seriously pisses me off."
    m "Aside from that, school looks as boring as ever."
    m "I hope something interesting would happen soon..."
    m "At least it wouldn't be this boring."
    m "Well, I'm pretty tired from today, might as well go to sleep early."
    m "Especially since I barely slept last night."
    m "(Or did something make me exhausted this morning.)"
    m "(My memories seems a bit hazy.)"
    m "(Maybe it's the chicken nuggets that's hitting.)"
    m "(...that doesn't make any sense though.)"
    m "(*Sigh*, it's probably nothing.)"

    scene black with Dissolve (1)
    scene residential with Dissolve (1)

    play music ("bgm/2.ogg") fadeout (1)

    "The next day."
    m "(My alarm clock was as loud as ever.)"
    m "(At least this time I woke up on time.)"

    pause 0.5

    m "Yet another captivating day at school..."
    m "(On my way to the school I see a pale haired girl running with a toast in her mouth.)"
    m "(There's still 5 minutes left before the bell rings...)"
    m "(Why is she even running...?)"
    m "Huh... anyway."
    m "(I make my way to school once more)"

    scene classroom with Dissolve (1)

    "Waccland's Peak Academy, Place Japan, Hour: 7:58"

    m "(I arrive in class and sit at my desk.)"
    m "(The class is as loud as ever, gossiping about all the latest news like usual.)"
    cl "Hey, did you hear about what happened to Leo!"
    cl "Word is that he got beaten by the one and only Ninja!"
    cl "Damn, that's crazy bro!"
    cl "Didn't think Mkleo could lose a match."
    cl "This just proves how good ninja has gotten!"
    m "(As always talking about celebrities no one cares about.)"
    m "(I do love myself some WA-KU-OH! but those pro players don't get it at all.)"
    m "(Card games were never about being competitive, it was always just about having fun.)"
    m "(But I have more pressing matters to attend to right now...)"
    m "(An annoying face is staring at me from behind, eager to disturb the peace that I found myself in.)"

    show asami_happy with Dissolve (0.5)

    a "Hey Kamiya, good morning!"
    a "Don't you feel blessed being graced by such a cute girl in the morning?"
    m "No, I don't, thank you very much."
    
    show asami_judge
    hide asami_happy
        
    a "*Sigh* You just can't appreciate the good things in life can you?"
    m "Well maybe I would be happier if I had some peace for once."
    a "It's school, what did you expect?"
    a "Altough, I guess..."

    pause 0.5

    a "Forget about that last part."
    a "I was just thinking out loud"
    m "...Okay?"

    hide asami_judge
    show asami_neutral

    a "Anyway, I'll never get all that celebrity talk."
    a "Everyone's just been spouting the same things ever since the day started."
    a "I honestly don't get it."
    m "Yeah, true."
    m "I was thinking the same thing earlier... before you interupted my train of thought."
    a "Oh, I thought you were just sleeping like yesterday!"
    m "There's a huge difference between sleeping and thinking, you know?"
    a "Don't feel like arguing anymore."
    m "Well, at least you admited defeat."
    a "I didn't!"
    a "Anyway, We'll talk again later."
    m "(As if I would want to talk to you.)"

    hide asami_neutral with Dissolve (0.5)

    show izumi_neutral with Dissolve (0.5)

    "Mr. Izumi enters the classroom."
    i "Class is about to begin."
    i "Today we're going to be studying ancient history."
    i "As you probably already know, not much is known from the times before Kevin Waccland saved the world."
    i "According to archeologists, the land was previously known as the land of the Seventh, although some sources also claim that it was known as WACCLAND."
    i "In those times, people were able to use magic to cast powerful spells able to pierce the heavens themselves."
    i "Which then leads us to the tale of Kevin Waccland."
    i "Kevin Waccland was born about 2000 years ago as the prince of the great empire of Waccland."
    i "Yet, turmoil lurked in the darkest reaches of the empire."
    i "Dark cultists summoned forth forbidden magic to try and take control of the world."
    i "Yet, Kevin rose up to those cultists and battled them."
    i "In their final battle, the cutlists had managed to summon an old and powerful god."
    i "The odds were stacked against him, but Kevin had a plan."
    i "The dark god fueled itself of the magic of the people."
    i "Kevin decided to seal away the magic of the people inside cards and challenged the god to a duel."
    i "Inside those cards lied beasts conjured of pure magic."
    i "With this power, Kevin Waccland was able to succesfully seal the dark god inside a card."
    i "This very card is sealed in a location unknown to the masses, as it's power could most certainly provoke the end of the world."
    i "And that's why you rarely ever see anyone able to use magic these days."
    i "It's all sealed in the original WA-KU-OH! cards which is also kept in an undisclosed location."
    i "The only cards with magic in them are the original deck of Kevin and the Old one card."
    i "Although according to Kevin's words, it doesn't matter if the cards are genuine or not, the real magic were the friends he made along the way."
    i "And thus concludes today's class."
    i "Altough a bit of trivia before the bell rings."
    i "Back in the days, issues amongst the populace were traditionally settled with a game of WA-KU-OH!"
    i "With Waccland entertainments acquiring the liscence to the game, it's popularity has skyrocketed in the past 10 years."
    i "Before that, the church was responsible for producing and updating the ruleset of the game."
    i "Must have been hard to get the liscence to such a huge game."
    i "But seeing it's popularity and the ammount of cash it's printing, I don't think they're regretting one bit."
    
    hide izumi_neutral with Dissolve (0.5)

    "Ding dong bing bong."
    i "Well, class is over, see you guys tommorow."

    play music ("bgm/break.mp3") fadeout (1)

    m "(Any real WA-KU-OH! fan would already know all of this.)"
    m "(The card game is it's own thing, but any real fan would also bundle it up with the manga.)"
    m "(The hit manga WA-KU-OH! was produced by veteran manga artist Kazuki Tenoizoro and liscenced by Waccland entertainments. He worked closely with archeologists to preserve the myth in all of it's glory.)"
    m "(The blend of real and fiction and it's absurd humour is what makes the series an absolute masterpiece.)"
    m "(It was later adapted in an animated series produced by the one and only Waccland animations.)"
    m "(It brought many professional voice actors such as Nenjiro Tsukasa. The sheer quality of the animations and voice acting makes it one of the best animated shows ever created.)"
    m "(With how good the WA-KU-OH! manga is, you'd think it was written by Kevin Waccland himself.)"
    m "(But enough talking about my favorite Manga.)"
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
    m "(I mentionned the class we just had about Kevin Waccland.)"
    m "(Yomki continued to listen to my yapping for a while.)"

    pause 0.5

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

    m "(That has to have been the most cliché confession I've ever seen.)"
    m "(The dumbass quickly left while tears dropped from his eyes. What a dumbass? He really asked out a girl that he never talked to???)"
    m "(This dumbass has truly mastered the art of mob-fu.)"
    m "(Truly the background character of background characters.)"

    show yomki with Dissolve (0.5)

    y "Damn bro, this dude got destroyed. Not cool."
    y "For serious."
    m "(I quickly turned around again towards the girl.)"

    hide yomki with Dissolve (0.5)
    show miyuki_neutral with Dissolve (0.5)

    unk "What a waste of time..."
    m "(While quickly glancing at her bag, I noticed a pin on it.)"
    m "(It's a pin of WA-KU-OH!, my favourite manga!)"
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

    show miyuki_mad
    show miyuki_mad:
        xpos 1400 ypos 1200
    hide miyuki_neutral

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
    m "(It's not everyday you meet a diehard WA-KU-OH! fan here.)"
    m "(Everyone just simps for the top players because they're hot while not caring about the game at all.)"

    pause 2

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

    show bob_neutral with Dissolve (0.5)

    unk "Sup, bébé chat. You here to get gains as well?"
    m "Who the hell are you?"
    m "(Who even starts a conversation with someone by calling them bébé chat?)"
    m "Huhhh... yeah."
    unk "Damn, I go here every day. I'm gonna get as buff as a JuJu character."
    unk "You do know what JuJu's bizzare adventure is bro?"
    m "Yeah, I know about that one, it's the one with Julian Juestar beating up muscular vampires."
    unk "Yeah man! That one!"
    unk "The dudes in that show literally have muscles on top of their muscles."
    unk "By the way, do you take the Sauce?"
    m "The fuck you mean sauce?"
    unk "The Sauce. Don't you know what Sauce is?"
    b "Anyway, the name's Yasuhiro Bob, you can call me Bob, or bébé chat, I don't really care."
    m "(Sauce, does he mean like, steroids? Of course I don't take that.)"

    hide bob_neutral with Dissolve (0.5)
    show masashi_neutral
    with Dissolve (0.5)

    m "My name is Masashi Kamiya, but you can call me MC!"
    m "Gaming is my life and Wacc-Fuel is my blood."
    m "As darkness covers this land, I will become the light that banishes evil."

    hide masashi_neutral 
    show bob_neutral with Dissolve (0.5)

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
    b "Sup my dudebro."
    b "Name's Bob, me and MC have been friends for a while"
    b "And by a while I mean I met this dude 5 minutes ago."
    y "Damn, that's crazy bro."
    y "Name's Yomki, I'm what you can call a climber."
    b "Nice to meet you bébé chat."
    b "Anyway, *With deep ass voice* later bébés chats."
    b "I got some chemistry to study."

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

    show bedroom with Dissolve(1)
    play music ("bgm/bedroom.mp3") fadeout (1)

    m "(I arrived home at last after another tiring day.)"
    m "(That Bob guy was weird as hell...)"
    m "(Why does he insist on calling ice cream sandwiches ''Sauce''...)"
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

    m "(And soon the bell chimes to announce launch break.)"
    m "(There was that WA-KU-OH! girl from yesterday, maybe she'll be there today too.)"
    m "(I gotta ask her about the pin. WA KU OH! is my life after all.)"

    scene rooftop with Dissolve (0.5)

    play music ("bgm/6.ogg") fadeout (1)
    
    show miyuki_neutral with Dissolve (0.5)

    m "(Yes, she's here. Now I can ask her.)"
    unk "Hmmm... Who are you again?"
    
    hide miyuki_neutral with Dissolve (0.5)
    show masashi_neutral with Dissolve (0.5)

    m "My name is Masashi Kamiya, but you can call me MC!"
    m "Gaming is my life and Wacc-Fuel is my blood."
    m "For over ten thousand years, I have protected this world from iminent destruction!"

    hide masashi_neutral with Dissolve (0.5)
    show miyuki_unimpressed with Dissolve (0.5)

    unk "Huh? The hell is wrong with this guy?"

    # serious face
    hide miyuki_unimpressed
    show miyuki_mad

    unk "Well, what business did you have with me?"
    m "Well, uhm..."
    m "It's about the pin on your backpack, could you possibly be a fan?"

    #change expression
    hide miyuki_mad
    show miyuki_neutral

    unk "Huh, this? I just picked it up 'cause it was popular at the time."
    unk "Don't know anything about it. Except it's popular in Waccland city."
    m "(Damn, my luck ran out. She's a fake.)"
    m "(A damn normie. What a waste of my time.)"
    m "(Well, after all the trouble I went through, might as well ask for her name.)"
    m "Well, sorry for bothering you. But before I go, could I at least know your name?"

    #change expression
    show miyuki_unimpressed

    unk "My name?"

    #change to miyuki neutral
    show miyuki_neutral
    hide miyuki_unimpressed

    mi "My name is Mochizuki Miyuki. Do you have anything else to say? I'm quite busy after all."
    mi "I got club practice to do."
    m "(If she has practice to do, then why is she alone on the rooftop?)"
    m "(Whatever, I got what I asked for, time to leave.)"
    m "Then goodbye, Miyuki."
    m "(I quickly leave before the embarassment of revealing myself to a fake fan kills me.)"

    scene black with Dissolve(1)

    mi "Guess I should remove the pin before I get annoyed by any more fans."

    scene corridor with Dissolve (1)

    m "(As I head back towards my class to eat lunch, I hear a faint trumpet melody.)"
    m "Guess she wasn't kidding about that club practice?"

    scene black with Dissolve (1)

    m "(The rest of the day goes by without much notable event.)"

    scene classroom with Dissolve (1)

    play music "bgm/5.ogg" fadeout (1)

    "Ding dong bing bong"

    m "Guess the day's over."
    m "What should I do next."
    m "Don't feel like hanging out with Yomki today."
    m "Maybe I should just go home and game all evening."

    show asami_neutral with Dissolve(0.5)

    m "Huh... why is she looking at me?"
    a "Hey MC!"
    a "See you tommorow!"
    m "..."
    m "(I guess I could try my chance talking with Asami too.)"

    play music "bgm/3.ogg" fadeout (1)

    "Alright, I'll talk to Asami"
    m "Asami, wait."
    m "Don't leave yet."
    m "I wanted to talk with you."
    a "What is it?"

    hide asami_neutral
    show asami_smug

    a "You want to ask me out?"
    m "Huh-"
    a "Well, of course you would!"
    a "You are talking to the cutest girl in school after all."
    m "..."

    hide asami_smug
    show asami_judge

    a "Well, just so you know, I refuse!"
    m "...I never said anything about asking you out..."

    hide asami_judge
    show asami_confused

    a "What?"

    pause 1

    hide asami_confused
    show asami_neutral

    a "Nevermind then."
    m "The fuck you mean by that?!?"

    hide asami_neutral
    show asami_judge

    a "I was joking. Like you know... A JOKE."
    a "Ugh... I can't expect someone like you to understand how deep that joke was."
    a "Anyway-"

    hide asami_judge
    show asami_neutral

    a "Kamiya, I had something I wanted to ask you."

    hide asami_neutral
    show asami_smug

    a "Do you perchance, have a InstaWACC account?"
    a "I shall grace you with my friendship!"
    m "Yeah, I got one, altough I barely use it."

    show asami_neutral
    hide asami_smug

    a "Alright, what's your username"
    m "Why should I tell you?"

    show asami_mad
    hide asami_neutral

    a "You're getting a friend request from a girl as cute as me, and you refuse her offer?"
    a "What a weirdo."
    a "But, unfortunately for you, you have no choice!"
    m "*Sigh*"
    m "(At this rate it's going to be more annoying if I don't give her my username.)"
    m "My username is MC_Kun_420."

    hide asami_neutral
    show asami_judge

    a "What a lame username..."
    m "You asked for it didn't you?"

    show asami_neutral
    hide asami_judge

    a "By the way, while we're at it."
    a "Did you want to hang out today?"
    a "This isn't a question by the way, you're coming with me no matter your answer."
    m "Okay, sure, it's going to be more annoying if I say no anyway."

    hide asami_neutral
    show asami_smug

    a "I'd like you to show me around town!"
    m "uhhh...."
    m "Do I look like the kind of guy who knows about the outside world...?"
    m "And shouldn't you find a place to go since you were the one who forced me to hang out with you?"
    a "What do you mean?"
    a "If you're going to ask for a date with a girl as cute as me, of course I get to choose what to do!"
    m "...You were the one who proposed to hang out, also since when is this a date?"
    a "Either way, you're from here? Shouldn't you know your way around town?"
    m "..."

    scene black with Dissolve(0.5)

    m "(Despite these unfortunate circumstances, I show Asami around town.)"
    m "(Even with me repeating over and over that this is NOT a date, Asami keeps on rambling on and on about how I should be grateful that a girl as cute as herself is accepting a date with me.)"
    m "(I somewhat ponder about if choosing to hang out with her was a bad decision...)"
    m "(But back to the original topic, I showed her all the popular places where people hang out... not that I'd know myself, I just looked it up online.)"

    scene waccdonald with Dissolve (0.5)

    show asami_unsure with Dissolve (0.5)

    m "Anyway, this is the Waccdonald's."
    m "Me and my bro Yomki often eat lunch here."
    m "For fast food, the quality and the price is really good."
    a "You're on a date with a girl and you bring her to a Waccdonald's?"
    a "Have you no shame?"
    m "You asked me to show you around town, that's what I'm doing."

    hide asami_unsure
    show asami_annoyed

    a "Can't you come up with a better reaction?"
    m "How the hell do you want me to react?"

    hide asami_annoyed
    show asami_kill

    a "How about aknowledging my cuteness for once, Kamiya-kun!"
    m "No, thank you very much."
    m "Anyway we're leaving since ms. perfect wants to complain about every little detail."

    show asami_confused
    hide asami_unsure

    a "What is this about ms. perfect?!?"

    scene gym with Dissolve (0.5)

    show asami_neutral with Dissolve (0.5)

    m "This is the local gym, me and my homie Yomki often come here to train."
    m "Although I don't think someone like you would be interested in gyms."
    a "Yeah, can't deny that."
    a "Didn't think you trained."
    m "I mostly just go with Yomki."
    a "Personally, I usually just go jogging."
    m "That's surprising, I thought you wouldn't care about staying fit."

    hide asami_neutral
    show asami_mad

    a "Hey!"
    a "I have a reputation to uphold as the cutest girl in the school!"
    a "Just because I'm cute doesn't mean I can skip on excercise."
    m "Fair."

    scene house with Dissolve (0.5)

    show asami_neutral with Dissolve (0.5)

    m "(After showing her around town, we make a brief stop.)"
    m "(Asami then turned towards me.)"
    a "Hey MC."
    m "What?"

    show asami_happy
    hide asami_neutral

    a "Where do you live?"
    m "Where I live?"
    m "Well, if you want to know..."
    m "43, Mind Your Own Business Street."
    a "..."

    hide asami_happy
    show asami_judge

    a "Where even is that?"
    m "Is your head so empty that it can't even comprehend a simple joke?"

    hide asami_judge
    show asami_mad

    a "Well, that's just mean MC."
    a "You shouldn't say that to such a cute girl!"
    m "Well, what if I don't care then?"
    a "Enough! You're going to tell me where you live now!"
    a "That's an order!"
    m "Why the hell do you even want to know!?"

    hide asami_mad
    show asami_judge
    
    a "Why?"

    hide asami_judge
    show asami_smug

    a "I just felt like asking."
    m "Can't you tell me the real reason?"

    hide asami_smug
    show asami_serious

    a "...Fine."

    hide asami_serious
    show asami_annoyed

    a "It's because..."

    hide asami_annoyed
    show asami_smug

    a "Actually, why should I tell you?"
    a "You haven't told me where you lived!"
    m "(Once again, this girl has pebbles instead of a brain.)"
    a "So tell me-"

    show bob_neutral
    
    show bob_neutral:
        ypos 1100 xpos 1400
    with Dissolve(0.5)

    b "Woah bébé chat, didn't know you had a girlfriend!"
    b "Must be 'cause of your GAINS!"

    hide asami_smug
    show asami_mad
    
    a "What?"
    a "This guy my boyfriend?"
    a "You must have hit your head really hard!"
    a "Who the hell do you think you are to assume that me, such a cute girl, would have this guy as a boyfriend!"
    b "I don't know man, you two seemed pretty close."
    a "Like I said, he is just my friend!"
    b "Woah, no need to be so defensive, you should take some Sauce!"
    a "Hphm!"
    a "Okay."
    a "But, I better not see you calling me this guy's boyfriend again!"
    b "Yeah, no problem bébé chat."
    b "By the way, my name is Yasuhiro Bob, nice to meet you."
    a "Nice to meet you too... I guess."
    a "My name is Nakamura Asami, THE cutest girl at our school!"
    b "Quite a bold claim, I like that."
    b "Anyway, MC, don't give up."
    b "Continue stacking those GAINS!"
    m "Will do, Bob."

    hide asami_mad with Dissolve (0.5)

    b "Anyway, I gotta go take the sauce!"
    b "See you later!"

    hide bob_neutral with Dissolve (0.5)

    show asami_neutral with Dissolve (0.5)

    a "That guy sure was something."
    a "Anyway, forget about where you live."
    a "I'll just ask your friend Yomki!"
    m "Please don't do that..."
    a "Okay, I shall totally ignore what you just said!"

    pause 0.5

    a "Anyway, farewell!"
    a "See you tommorow!"
    m "Goodbye."

    hide asami_neutral with Dissolve(0.5)

    m "(Asami left.)"
    m "Man, these days don't get any weirder."
    m "Anyway, time to head home."

    scene bedroom with Dissolve (0.5)

    play music ("bgm/bedroom.mp3") fadeout (1)

    m "Today went about like I expected it to."
    m "But that doesn't really matter right now because I have some homework to do."

    scene residential with Dissolve (0.5)

    play music ("bgm/2.ogg") fadeout (1)

    m "(Yet another boring day.)"
    m "(Well, I just have to endure 3 more years of this and I'll be done with high school.)"

    scene classroom with Dissolve (0.5)

    "Ding dong bing bong"

    m "(Man, today was really boring...)"
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

    unk "..."
    unk "I..."

    play music ("bgm/edge.mp3") fadeout(1)

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
    m "Throughout Heaven and Earth, I alone am the Honored One which will guide the world to salvation!"

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

    scene school 
    with Dissolve(1)

    show yomki with dissolve

    m "(As usual, the road to exit the school is completely filled with students.)"
    m "(Not surprising, who in their right mind would want to stay in this purgatory?)"
    m "(I start to walk towards the exit alongside Yomki.)"
    m "(Altough while turning to get on the sidewalk, we notice someone we know.)"

    show yomki:
        ease 1 xpos 1400 ypos 1100
    show izumi_smoke with Dissolve(0.5)

    m "Mr. Izumi?"
    i "Ah, Kamiya and Yomki, didn't know you guys were friends."
    i "Heading home?"
    m "Yeah."
    i "Also you can drop the mister while outside school."
    i "Puts some kind of distance between people when you use honorifics."
    m "Well yeah... that's true."
    y "Can't disagree, that's why I always call everyone bro."
    m "Didn't know you smoked."
    i "Huh, yeah, been smokin' for quite a long time."
    i "All 'cause of this one guy."
    i "Always rambled on and on about how he much he despised lazy people."
    i "He was always like: ''Those damn fools don't even bother doing anything with their lives.''"
    i "Sure enough, the guy went on to become CEO of the largest company in the entire world."
    i "I saw him a couple of years ago and he invited me for a drink."
    i "He kept talking about business and stuff."
    y "What was the guy's name?"
    i "Michel."
    m "I'm pretty sure I heard that name before..."
    m "Wait-"
    m "THE Michel Popstonia studied here at Waccland's Peak Academy?!?"
    y "That's kinda crazy actually."
    i "Yep, That's right."
    m "Doesn't seem like his attitude changed much."
    i "Yeah."
    i "It was shortly after the big war."
    i "Waccland's Peak Academy hadn't fallen from grace yet."
    i "You kids probably don't know the full story yet."
    m "Yeah, that's weird they never really tell why it fell from grace."
    i "Well, long story short, the director was a corrupt piece of shit."
    i "Michel himself was the one who accused him of his crimes."
    i "The reputation of the school got ruined in a couple of years because of that."
    y "Damn..."
    m "..."
    i "Those days weren't all that bad though."
    i "I remember back in my days, we didn't even have phones."
    i "Hell, we didn't even have electricity."
    i "It was all just swords, and magic, and all."
    m "Wait, wasn't electricity discovered in like 1800?"
    i "1752."
    i "Just an exaggeration by the way."
    i "Me and my friends went on a long long journey."
    i "Reminds me, one of my friends looked just like you Yomki."
    y "Damn, did he climb as much as me though?"
    i "I'm sure one day you'll meet him, you'll get your answer then."
    y "Lookin' forward to it then."
    i "Going back on track, we were on a quest to find and restore the balance of the seven crystals of the elements."
    i "The one we called the Lord of the Seventh had created a dark crystal which destroyed the balance of the world."
    i "So we defeated him and were hailed as the heroes of the land."
    i "That's about it, I guess."
    m "Huh...???"
    m "(After this long monologue how could we not ask myself a thousand questions?)"
    m "...Uhhh... Mr. Izumi...?"
    i "You don't have to call me mister."
    m "...Naoki, how often do you smoke?"
    i "Not that much."
    i "One day you'll understand how it feels like to be a living legend."
    m "...Alright then, have you been playing WACC Quest XIII too much?"
    i "Probably."
    m "(Interesting, I didn't think he'd be the type to play games like that.)"
    y "Damn, you one of us bro?"
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
    y "You ever play any souls games bro?"
    i "Yeah, beat all of them when they came out."
    i "Fantastic games, all of them."
    y "What a chad."
    y "We need to talk more later bro."
    i "Yeah, I usually hang arround here when school ends."
    i "Either way, I gotta go."
    i "Got to take care of my boy."
    m "You have a son?"
    i "Nah, not a son."
    i "I got a salamander."
    y "That's quite a weird pet."
    i "Yeah, I know."

    hide izumi_smoke with Dissolve (0.5)
    show yomki:
        ease 1 xpos 900

    i "See you tommorow, MC and Yomki."
    m "...See you tommorow Mr. Izumi."
    m "..."
    m "Well, that wasn't what I was expecting."
    y "Yeah me too bro, his vibe was completely different than during class."
    m "I'm not sure yet if he's cool, ...or just kinda crazy."
    y "Definitely a chad in my book."
    y "Anyway, let's go climb brother."

    scene black with Dissolve (0.5)

    m "(While walking home, me and Yomki continue talking about our countless playtroughs of Dark Souls XX.)"
    m "(We talked about all the secrets and hidden items we found.)"
    m "(Truly, Michael Zaki never misses.)"
    m "(Altough the time for us to part ways soon came.)"

    scene bedroom with Dissolve(0.5)

    play music ("bgm/bedroom.mp3") fadeout (1)

    m "..."
    m "(The faint glimmer of sunlight left pierces the curtains of my rooms.)"
    m "(As I lay down on my bed, I begin to ponder about all these strange events that have followed me for 4 days now.)"
    m "(It somehow feels all intentional, like a mastermind is actively pulling the strings.)"
    m "(Yet, a part of me doesn't want me to accept this idea.)"
    m "(With these questions in my mind, I slowly go through the rest of the day without thinking about it much more.)"

    scene residential with Dissolve (0.5)

    play music ("bgm/2.ogg") fadeout (1)

    m "(With the coming of the 5th day, it feels like I should be getting used to this new daily routine, yet...)"
    m "(With all these bizzare events, I haven't had the time to get accustomed to my new surroundings.)"
    m "(Altough today feels different... somehow...)"
    m "(Even more than during the past 4 days.)"
    m "(Well, it's no use worrying about it, these past few days have only been a series of a bunch of weird stuff.)"
    m "(It's normal I'd be worried about it.)"

    scene school with Dissolve (0.5)

    stop music fadeout 2

    m "(As I make my way to the school, the feelings of unease I felt earlier begin to intensify.)"
    m "(Without leaving a second for me to wonder what could be the cause...)"
    m "(It aproaches ME.)"

    play music ("bgm/chungus_confrontation.mp3") fadeout (1)

    show chungus:
        ypos -1000 xpos 515
        ease 0.2 ypos 190
    play sound ("sfx/explosion4.ogg") volume 0.2

    m "(Like a meteor falling from the sky, HE fell right in front of me.)"

    pause 0.5

    c "Missed me bitches?"

    pause 1

    m "Who... are you again...?"
    c "Thy greatest Chungus is gracing thyself with his presence and thou doth not even remember him?"
    c "I, am Big Chungus, the greatest and the one and only true Chungus!"
    c "The overseer of this world, of this wacc, of this land."
    c "Brave warrior of the maidens... I challenge thou to the Dunktastic Duel of WACC AND LAND!"
    c "Thou hast no other choices!"
    c "Face me OR thou shall never feel the touch of a woman ever again!"

    pause 1

    m "..."
    m "(What the hell is this rabbit even saying?)"
    m "(Dunktastic duel of WACC AND LAND?)"
    m "(And, could I really defeat a god?)"
    m "(Altough, my hesitation is quickly dispelled by the thoughts of my friends.)"
    m "(They're here for me.)"

    pause 0.5

    m "Alright."
    m "Almighty Chungus!"
    m "I accept your D-D-D-D-D-DUEL!!!"
    m "(The space arround us started to shift as if reality itself was but a hazy dream.)"

    scene school_gym
    show chungus
    with Dissolve (1)

    play music "bgm/chungus_battle1.mp3" fadeout (1)

    m "(We were transported into the school gym.)"
    c "The rules are simple-"
    c "The one who balls the hardest wins."
    c "Ready?"
    m "Yeah!"

    # zoom sfx

    m "(As he said this, the chungus zoomed arround the court at lightning speed.)"

    scene ballcg1 with Dissolve (1)

    m "(Without even being able to process what was happening, the chungus had already jumped.)"
    m "(I watched in horror as the chungus dunked the ball straight into the basket.)"

    play sound ("sfx/ball i guess.mp3")
    queue sound ("sfx/explosion4.ogg") volume (0.5)
    pause 1
    play sound2 ("sfx/metal pipe.mp3") volume (0.1) fadeout (3)

    scene school_gym
    show chungus
    with Dissolve (1)

    c "One point, motherducker."
    c "A bit slow this one, don't you think?"
    c "Thou can do better, Masashi Kamiya."
    m "(I began to wonder if I even had a chance...)"
    m "(Did he purposefully challenge me knowing that I never had a chance?)"
    m "I..."
    m "I refuse to go down this easily!"
    m "(I begin to run straight to the ball, catching it in mid-air as it bounced on the floor.)"
    m "(Although, when I turned I saw an imposing figure.)"
    m "(Big chungus seemed even larger than usual.)"
    m "(As I tried to outmaneuver him, Big Chungus managed to snatch the ball from me.)"
    c "Looks like I get another point."

    hide chungus with Dissolve (1)

    m "(Big Chungus then bolted straight to the basket.)"
    m "..."

    scene ballcg1 with Dissolve (1)

    m "(He jumps again...)"
    m "(His paw hits the ball...)"

    stop music fadeout 1

    pause 1

    m "(I expected to hear the sound of the ball bouncing on the floor...)"
    m "(All hope was lost, yet...)"
    m "(Instead of the sound of the ball, I heard footsteps.)"

    pause 1

    scene school_gym with Dissolve(1)

    play music "bgm/you_say_run.mp3" fadeout (1)

    play sound ("sfx/catchball.mp3")

    m "(You see a figure catching the Chungus' dunk, milimiters before it passed the basket.)"
    m "!!!"
    m "Y-Yomki!!!"
    m "My bro, my man, my dude!!!"

    show yomki with Dissolve (1)

    y "Yo MC, you should've told me you were ballin' bro."
    y "You know I love balls."
    m "Sorry, homie."

    hide yomki
    show yomki_smug

    y "Alright, let's show this Chungus what real bros can do!"
    m "Yeah bro!"

    hide yomki_smug with Dissolve (0.5)

    "As the two of you ball with Big Chungus, even more of your friends arrive."

    show gorou_yell with Dissolve (0.5)

    g "MC, Yomki! The phoenix's divine darkness shall forever be at your command!"
    g "May your balls light up the way to the heavens!"

    hide gorou_yell
    show bob_neutral
    with Dissolve(0.5)

    b "Yo bébé chats! I believe in you guys!"
    b "You're sure to win with all those GAINS!"

    hide bob_neutral
    show miyuki_unimpressed
    with Dissolve(0.5)

    mi "The hell those three doing???"
    mi "And why is there a big rabbit?"

    hide miyuki_unimpressed
    show izumi_neutral
    with Dissolve(0.5)

    i "Now! This is it!"
    i "Now is the time to choose!"
    i "Be maidenless and die without bitches, or live and fight for your maidens!"
    i "Now is the time to shape your stories!"
    i "Your fate is in your hands!"

    hide izumi_neutral with Dissolve(0.5)

    "Everyone's voices echo within you and your homie Yomki."
    "Everyone's hopes and dreams rest within you!"
    m "(With this newfound power, I jump forward, straight for the basket.)"
    y "MC, catch!"
    m "(Yomki tosses me the ball.)"

    play sound ("sfx/catchball.mp3")
    scene ballcg with Dissolve (1)

    pause 0.5

    m "With all our powers combined, our wills as one..."
    m "We have the power to pierce even the heavens!"

    m "(The palm of my hands hit the ball.)"

    play sound ("sfx/ball i guess.mp3")
    queue sound ("sfx/explosion4.ogg") volume (0.5)
    pause 1
    play sound2 ("sfx/metal pipe.mp3") volume (0.1) fadeout (3)

    m "(The piercing sound echoes through the gym.)"
    m "(Everyone is speechless.)"
    m "(No one has ever balled this hard.)"
    m "(No one...)"
    m "(Not even big Chungus.)"

    scene school_gym with Dissolve (1)

    pause 1

    show chungus with Dissolve (1)

    c "!!!"
    c "This power."
    c "I was right all along."
    c "Masashi Kamiya, you are the one."
    c "You are destined for greatness."
    c "The Chungus congratulates you, for you have outballed him."
    c "Thou hast passed the trial."
    c "May your L's be few, and your bitches many!"

    scene white with Dissolve (0.5)

    scene school_gym with Dissolve (0.5)

    play music "bgm/8.ogg"

    m "(The chungus then vanished in a flash of light.)"
    m "(I have finished his trial.)"
    m "(As the dust settles, everyone who gathered in the gym begin to leave.)"

    show yomki_smug with Dissolve(0.5)

    m "Yomki, I couldn't have done it without you bro!"
    y "Together, we can pierce even the heavens bro!"
    m "(Me and Yomki proceed to have the manliest handshake ever.)"
    y "*Kisses you on the cheek* homie."
    m "Huh? What was that for?"
    y "Don't worry about it, No homo bro."
    m "Sure bro."

    hide yomki_smug with Dissolve(0.5)

    m "(And with that, the only ones left were me, Yomki...)"
    m "(And her...)"

    show asami_serious with Dissolve(0.5)

    a "Kamiya..."
    a "I-I..."
    a "I was wrong about you..."
    a "I didn't know you were able to ball that hard."
    a "I thought you were a just a loser who never left his room..."
    a "Now..."

    pause 2

    hide asami_serious
    show asami_neutral

    a "...Alright, I'll be honest for once."
    a "I won't pretend to be all impressed by that and suddenly change my opinion of you."
    a "But that was some nice balling."
    a "Good job to you two."
    a "Also I guess I should also tell you this."
    a "The whole time I've been annoying you on purpose."
    a "We do a minuscule ammount of tomfoolery."

    hide asami_neutral
    show asami_smug

    a "You know, you're lucky to have a friend as cute as me."
    m "No, I am not."
    m "Also you decide to tell me this now?!?"

    hide asami_smug
    show asami_neutral

    a "Anyway, I better leave before I'm late to class."

    hide asami_neutral with Dissolve(0.5)

    m "(Asami left the room before I could say anything else.)"
    m "(Not exactly the reaction I was expecting.)"
    m "(I thought she'd say something like: Nah, you're still just some loser! That bunny guy didn't even break a sweat!)"
    m "(And then she's apparently been annoying me on purpose.)"
    m "(What is that girl's deal?!?)"
    m "(At least that means she wasn't this stupid.)"
    m "(But still...)"
    m "(This girl pisses me off.)"
    m "(But the problem is that even if she pisses you off you can't help but be pulled into her antics.)"

    show yomki with Dissolve(0.5)

    y "You guys dating or what?"
    y "You were talking to her on the first day of school."
    m "Nah, quite the contrary, she actively pisses me off."
    y "What did she do?"
    m "Nothing really... she just pisses me off."
    y "Isn't she like the (self-proclaimed) cutest girl in the school though?"
    m "Urgh, not you too..."
    m "A real man's gotta have standards!"
    y "Anyway, wanna hit the Waccdonald's MC?"
    m "Hell yeah brother!"

    hide yomki with Dissolve(0.5)

    m "(As the both of us left the gym, I see the figure of a man.)"
    m "(Altough he leaves as soon as I looked at him...)"
    m "..."
    y "Something bro?"
    m "Nah, just my imagination."

    scene black with Dissolve(2)

    m "(And with that wrapped up, me and Yomki skipped school to go to the Waccdonald's.)"
    m "(And thus concludes the first chapter of my new life.)"
    m "(At this time, I was blissfully unaware of what horrors would befall me...)"
    m "(But that's a story for another day!)"

    pause 2

    m "(AND THAT DAY IS NOW!)"

    "CHAPTER 1: Murder at the school trip?!?"

    scene bedroom

    play sound "sfx/explosion4.ogg"

    play music "bgm/bedroom.mp3"

    pause 2

    m "(Yesterday came and went like a whirlwind, and soon I woke up in my bed like usual...)"
    m "(Although I feel like my memories are a bit hazy)"
    m "That dream sure was weird..."
    m "That huge bunny was crazy fast."
    m "..."
    m "(In my dream... I was balling with this huge bunny, yet... it was a bit too clear)"
    m "(was it really a dream...?)"
    m "..."
    m "Wait, we did play basketball but against who?"
    m "I must have hit my head pretty hard yesterday."
    m "I really don't know."
    m "...I do remember someone being in a bunny suit."
    m "Woke up earlier than usual though..."
    m "Guess I'll just go to school earlier."

    scene club with Dissolve(0.5)

    play music "bgm/2.ogg" fadeout 1

    m "(I made my way to school, and arrived 30 minutes early.)"
    m "(Classes haven't started yet, and I don't know what else to do, so might as well wait for Yomki.)"
    m "(I waited a couple minutes before a familiar figured popped up.)"

    show gorou_smug with Dissolve(0.5)

    g "Could it be...? MC! My bro, my man, my dude!"
    m "Yo Gorou, what's up?"

    hide gorou_smug
    show gorou_neutral

    g "I had a strange dream."
    g "A storm was brewing, thunder roaring..."
    g "A man took a leap of fate-"
    m "Was there a big fat bunny?"
    g "..."
    g "Well..."
    g "Yeah."
    m "I have an hypothesis..."
    m "What if... this wasn't actually a dream...?"
    g "What are you insinuating MC?"
    m "I think-"

    show gorou_neutral:
            ease 1 xpos 1400 ypos 1100
    
    show yomki with Dissolve(0.5)

    y "Top of the mornin'"
    y "No way?!?"
    y "Gorou and MC talking together?!?"
    y "Didn't know you two were dating?!?"

    pause 2

    m "..."
    g "..."
    y "I ain't judging you bro."
    m "Huh... Yomki."
    m "You know I'm not gay bro."
    m "It's not that I don't like men, I just like girls too much"
    y "Fair."

    pause 1

    y "Anyway, you guys were talking about friday?"
    y "That Big Chungus guy was strong."
    m "So, it wasn't a dream after all."
    g "...That's weird."
    y "Huh? That actually happened???"
    y "I was just talking about the dream I had-"
    m "Wait- we all had the same dream?"
    g "..."
    y "..."
    m "..."
    m "I think we're overthinking this."
    y "I saw you head to the gym with a guy in a bunny suit and you guys started to play basketball and that's about it."
    m "Man, I really must have hit my head really hard to have imagined that scenario."
    m "Any idea who was in that bunny suit?"
    y "I seem to have seen a teacher removing a bunny suit behind the gym while leaving."
    y "But as to why... I don't know."
    y "Anyway, we climbed so hard yesterday."
    y "We both managed to beat Dark souls XXI in a single day."
    m "Yeah bro, that was crazy."
    g "Ah yeah, the famous Dark souls series. I've heard legends of it's challenge and it's infamous 2nd entry- Dark Souls II."
    g "Some say it's the best video game that has ever existed..."
    g "Or so the legend goes..."
    y "Huh... are you high?"
    y "Dark Souls II kinda mid bro, easily the worst Dark Souls"
    y "Dark Souls XXI is where it's at bro."
    m "Yeah, it takes everything that made Dark Souls II good, and multiplies it by 10."
    y "Can you even call it Dark Souls if you don't have to no-hit every boss while every attack has a 1 frame dodge and parry window?"
    m "That game is for casuals bro."
    g "Damn bro, Michael Zaki really never misses."

    "Ding dong bing bong."

    m "(The bell rang interupting our conversation.)"
    m "We'll talk more about it later."
    m "See you guys later."
    g "Farewell."
    y "See you bro."

    scene classroom with Dissolve(0.5)

    m "(It wasn't long after I sat down that I realized something.)"
    m "(The whole class seemed... excited.)"
    m "(I guess I'll just ask Asami.)"

    show asami_neutral with dissolve

    m "Hey, do you have any idea why everyone's so excited?"

    hide asami_neutral
    show asami_smug
    with dissolve

    a "I'm glad you asked!"
    a "You see, it's simple-"

    hide asami_smug
    show asami_cat
    with dissolve

    a "Apparently there's a new teacher they hired."
    a "And... well... he's apparently quite good looking so... yeah..."
    m "Classic high school students..."
    a "They really should feel ashamed of themselves!"
    a "He can't be that hot, right?"


    show asami_cat:
        ease 1 xpos 1400 ypos 1200
    show gotou_neutral
    show gotou_neutral:
        xpos 800 ypos 1100
    with dissolve

    pause .5

    hide asami_cat
    show asami_judge
    show asami_judge:
        xpos 1400 ypos 1200
    with dissolve

    a "..."
    a "With their reactions I was expecting a bit more..."
    a "Don't get me wrong, he's not bad looking but..."
    m "Your standards may be a bit high Asami."
    a "Says the guy who would date a fictional character."
    m "I wouldn't do that though."
    m "I'm not that desperate-"
    go "Okay everyone! Class is going to start soon."
    a "I'm not convinced, but that will have to wait for after class, unlike you I actually pay attention during class!"

    hide asami_judge with dissolve
    show gotou_neutral:
        ease 1 xpos 900 ypos 1100

    pause 1.0

    go "My name is Hidetaka Gotou, I will be your science teacher this year."
    go "As you probably already know this is my first day teaching here."
    go "If you have any questions you are free to ask them to me at my office after classes end."

    pause 1.0

    "Gotou started his lecture"
    "Words melded together as your conciousness started to fade, yet by a miracle a glimpse of interest sparked."
    go "-This brings us to WACC energy, or as some called in the past 'Magic'."
    go "Altough the name magic is a bit misleading-"
    go "Altough our understanding of WACC energy is limited, it is far from what you could call 'magic'."
    go "WACC energy as long since been used to produce miracular feats."
    go "Miraculous is a bit misleading though, as the ancient journals reveal that to control WACC energy required great power and intense training."
    go "Yet why haven't we seen these kinds of feats for more than 2 thousand years?"
    go "Well first we must know the origin of WACC energy."
    go "WACC energy as you might already know is able to produce a seemingly infinite ammount of electrons."
    go "Altough it's potential infinite, even the most talented could never harness even a fraction of it's power."
    go "The only recorded person to have been able to unleash the true power of WACC energy is none other than Kevin Waccland."
    go "You must already be familiar with that name?"
    go "When he sealed the god inside the cards, so came the power of WACC along with it."
    go "These days, only very specific people are able to awaken the power of WACC, and even then, they can't even wield a fraction of the power ancient mages had."
    go "Not only are people with powers exeedingly rare, what they can do with these powers is extremely limited."
    go "Altough if we look at matters outside humans, WACC energy explains many phenomenons in nature."

    hide gotou_neutral with dissolve

    pause 1

    "The lecture continued for a while longer before the bell rang once again."

    pause 1.0

    m "Well, better go see my homie Yomki since I got nothing better to do."

    scene corridor with dissolve

    m "(I make my way to Yomki's classroom when I suddenly bump into the man himself.)"

    show yomki with dissolve

    y "Yo, sup MC."
    m "Good, I was looking for you bro."
    y "Did you need anything bro?"
    m "Nah, just wanted to chill with my homie."
    y "Alright, I'm down to netflix and chil- uh I mean BRO I GOT HACKED?!?!? NO WAY?!?!?"
    m "Damn, I hate when that happens bro..."
    y "Yeah, it's crazy bro."
    m "Alto-"

    show yomki:
        ease 1 xpos 1400 ypos 1100
    show gotou_neutral with dissolve

    go "Oh, Masashi-san... and... Yomki was it?"
    y "Yep, that's me."
    y "Altough I haven't seen you before?"
    y "You MC's teach?"
    go "Yes, we actually just saw each other."
    m "I gotta say though, you were pretty interesting, usually I just fall asleep during classes."
    m "But this time I actually felt like listening."
    go "That's good, sometimes all it takes to make something interesting is having someone that's good at explaining."
    go "Altough I had something else I wanted to talk to you two about."
    m "Okay? What did you want to talk about?"
    go "You know last friday before class? I happened to see you two in the gym."
    go "That was some nice balling."
    y "Thanks bro, not every day you see people who can truly appreciate the art of balling."
    go "Well, I just so happen to have a bit of experience playing basketball when I was younger, and I gotta say, I've never seen a game quite like this."
    go "That bunny guy was no slouch either."
    go "Felt like either of you could win this."
    m "Well, I don't really have that much experience playing basketball, but I did use to play with Yomki a bit when we were kids."
    go "Hmm... that's pretty interesting."
    y "Didn't really take you for the sports type though."
    go "People often tell me that. I stopped playing after high school though."
    go "These days I just hit the gym a once or twice a week."
    go "Anyway, I gotta go, I got a meeting in 5 minutes."
    m "See you later teach'."

    hide gotou_neutral with dissolve

    y "Didn't think he'd be chill like that."
    m "..."
    y "Something wrong bro?"
    m "Nah, must be my imagination."
    y "You sure bro?"
    m "Yeah, just a strange feeling I got when I talked to him."
    m "Anyway, forget I said anything."
    y "...Sure, I guess."
    m "Anything you wanna do before going home bro?"
    y "Idk, could take a bit of a walk though."
    m "Searching for a ''cute girl'' again, if you know what I mean?"
    y "Yep, gotta look for ones with special assets."
    y "With my years of practice I can more or less guess if their feets look good."
    m "I mean I don't judge or anything, but care to tell me why feet of all things?"
    y "Bro, don't you see how good it would feel to-"
    m "I'm gonna stop you right there Yomki."
    m "Don't feel like hearing all about your fetishes."
    y "Like you're any better bro."
    y "I know what you have on your hard drive."
    m "Look here Yomki, we don't talk about my secret collection."
    y "Yeah bro, I wouldn't tell a soul about it."
    m "I am COOKED if anyone finds out about it."
    y "Yeah I know, but what's so wrong about having he-"
    m "Bro, watch your mouth!"
    m "Someone's coming."

    pause 1.0

    show gorou_neutral with dissolve

    g "Hey, MC and Yomki!"
    g "What were you two talking about?"
    y "Nothing all that interesting bro."
    m "Y-yeah bro."
    g "That's weird, I heard you talk about a secret collection of some sorts..."
    m "Ahhh uhhhh... you know how it is uhhh...."
    y "He's talking about games he downloaded very legally on Supreme games UK bro!"
    g "Oh yeah, that. Guess you wouldn't want some teacher hearing about that."
    m "(Thanks Yomki for saving my ass.)"
    y "(No prob bro.)"
    g "So yeah, I was actually looking for you two."
    g "I am forcing you to go with me."
    m "And what if I say no?"

    stop music fadeout 1.0

    pause 1.0

    g "..."

    pause 1.0

    play music "bgm/2.ogg" fadeout 1

    m "Uhh... nevermind then, I'll go with you."
    y "Don't have anything else to do, so I'll follow."
    g "Ok, we'll be heading to the courtyard."

    scene rooftop with dissolve

    show yomki
    show yomki:
        xpos 1400 ypos 1100
    show gorou_neutral
    with dissolve

    g "Alright, we're here."
    m "Mind explaining why there's a summoning circle on the floor?"
    y "And also who's that girl akwardly standing over there?"

    show momoka_intrigued
    show momoka_intrigued:
        xpos 400 ypos 1200
    with dissolve

    g "Oh... her?"
    g "That's Momoka, one of my friends."
    g "We've known each other since elementary school!"
    g "She follows me in my path to the darkest abyss imaginable..."
    mo "..."
    g "...?"
    g "Momo-tan, didn't you agree to contribute to my dark and edgy catchphrase?!"

    hide momoka_intrigued
    show momoka_panick
    show momoka_panick:
        xpos 400 ypos 1200

    mo "...but isn't it really embarassing to say it out loud in front of people you've never seen before?!"
    g "Like I said before, they will be too busy being intimidated by our edginess that they'll cower in fear!"

    hide momoka_panick
    show momoka_serious
    show momoka_serious:
        xpos 400 ypos 1200

    mo "Look, I don't want to get teased because of that-"
    mo "People already tease me for being friends with you."
    mo "I don't want it to get worse..."
    g "Don't worry about that then, those two are my friends."
    g "Anyway, like I was saying..."
    g "Momo-tan follows me in my path to the darkest abyss imaginable..."
    mo "...W-where even the light can't e-escape!"
    g "Anyway, here's Momoka, my good friend."
    m "(What the hell are those two yapping on about.)"
    y "(Dunno bro, didn't listen to a word they said.)"
    g "Anyway, guy with the red hair's Kamiya and the other's Yomki"
    m "Name's Masashi Kamiya but you can call me MC, through despair and hope, only myself, the ultimate hope, can pierce the way towards the heavens!"
    m "For I am the one who games."
    mo "Uhm... are you one of those Chuunibyo like Gorou...?"
    m "Nah, I just do it for my introduction."
    mo "Okay."
    y "Sup guys, it's me Yomki, name's Tenma Yomki."
    mo "Nice to meet you two, my name is Arima Momoka."
    mo "Like he said I've been friends with him for quite a while."
    m "(Hey Gorou, how'd you find a friend like that?)"
    g "(It's a long story.)"
    m "(Are you two dating or something?)"
    g "(...?!?)"
    mo "...?"
    mo "What are you two being all sneaky for?"
    g "Uhhhh... nothing!"
    m "(Okay, think I got my answer.)"
    m "(I'm rooting for you bro.)"
    g "(I didn't say anything about having a crush on her!)"
    y "(Well, you just did.)"
    g "(Dammit.)"

    pause 1.0

    g "Anyway, the reason I called all of you here is for one very important reason."
    g "You know the game Waccland Impact?"
    y "What's that?"
    m "Oh, lord..."
    g "It's a game that's popular right now, there's millions of people playing the game."
    g "And they just released a brand new character!"
    y "Yeah and?"
    g "It's time to gamble!"
    g "The brand new character is called Hai Hoshino, the idol who hates everyone!"
    mo "..."
    mo "That girl again...?"
    mo "Didn't you get her last time?"
    g "Those are two completely different characters Momo-tan."
    mo "???"
    mo "But- don't they just look the same?"
    g "Rookie mistake, can't you see that this is an alternate version of the main antagonist of the game Nightmare-chan?"
    g "But this time she was reborn as an idol in another world where she will get her revenge against the world!"
    g "I've been saving up for 5 months to get her!"
    g "It's time to start..."

    pause 1.0

    m "What have you been yapping on about for the last 5 minutes bro."
    y "Didn't get a single word he was saying."
    g "Silence you two! The ritual must not be disturbed..."
    "You, Yomki and Momoka all look at yourself, dumbfounded by the utter cringe that you have just witnessed."
    
    pause 1.0

    g "...Nah... not this... decent... already have her maxxed out..."

    pause 1.0

    g "Oh!"
    g "She's coming home!!!"
    g "I can feel it."
    g "It's turned golden!"
    g "Come on, come on...."

    pause 1.0

    g "..."
    g "WHAT IN THE ACTUAL FUCK?!?!?"
    g "ARE YOU GODDAMN FUCKING KIDDING ME?!?!?"
    m "Woah, calm down bro."
    g "...hahahaha...."
    g "HAHAHAHAHAHA...."
    g "Once again..."
    g "YOU'VE COME TO HAUNT ME ONCE AGAIN?!?"
    g "I'LL NEVER FORGIVE YOU!!!!!!!"
    g "CURSE YOU SHITTY CATGIRL BITCH!!!!!"
    g "YOU'VE RUINED MY 50/50 ONCE AGAIN..."
    g "Know that I shall haunt your nightmares for the rest of your entire miserable fucking life..."
    mo "Calm down Gorou!"
    mo "She isn't even real!"
    g "..."
    g "Why must it always be like this..."
    g "Oh mighty lord of the gacha... why have you forsaken me yet again...?"
    y "Damn bro, must be tough being addicted to gacha."
    m "Yeah sure, he can quit whenever he wants, isn't that right?"
    g "Why...?"
    g "Why are you looking at me with those smug eyes..."
    m "Man, he's still locked up in his world."
    mo "...He's always been like this..."
    m "I can't even laugh about this, he just looks so pathetic..."
    y "Damn..."
    mo "Sorry for how Gorou's acting."
    mo "He tends to overdo things a bit too much..."
    m "Don't worry about that, I've had my fair share of run-ins with weirdos."
    m "And besides, he's a fan of Waccland chronicles, I already respect him."

    hide momoka_serious
    show momoka_neutral
    show momoka_neutral:
        xpos 400 ypos 1200

    mo "Oh yeah, he did talk to me about meeting another fan."
    mo "So that was you?"
    m "Yeah."
    mo "Well, I think you'd be happy to know I'm also a fan."
    m "R-really?"
    m "Damn, didn't think I would ever find two fans at school."
    m "That game is really an underated gem."
    mo "Yeah, the story, the music, the characters, they're all fantastic."
    mo "There's so many good things about this game..."
    
    pause 1.0

    g "Momo-tan!"
    g "Why is it that I always get shitty luck in this game?!?"
    mo "Well... I guess I'll have to entertain Gorou for a bit."
    mo "We'll talk again later."

    pause 1.0

    mo "Don't worry Gorou, you'll get her next time."
    g "Like hell I will!!!"
    g "The gacha gods have forsaken me!"
    mo "Well... can't you get her guaranteed though since you lost the 50/50...?"
    g "Do I look like I have enough currency for that?"
    mo "...I... Uhh... I give up..."
    
    pause 1.0

    g "I swear upon the darkness, this wretched catgirl shall know my wrath!!!"
    y "Here he goes again."
    mo "Yeah..."
    mo "I really wish I could defend him... but like you see... it's just a tiny bit hard to do that..."
    g "There is nothing to defend!!!"
    g "For I am the heir of darkness!"
    g "Anything that stands in my path shall know despair!"
    g "Anyway, see you guys later."

    hide gorou_neutral with dissolve

    pause 1.0

    "Gorou left the courtyard."
    mo "Well, I'll go with him."
    mo "See you guys later."
    y "Later bro."
    m "Yeah, see you later."

    # this will not be in the game

    scene classroom with dissolve

    show asami_judge
    show asami_judge:
        xpos 1400 ypos 1200
    with dissolve

    m "Yo Asami you should sit on my face frfr."
    a "Well if you subscibed to my onlyfans, maybe I will consider."
    m "YO YOU GOT AN ONLY FANS GIRL, i hope there's feet!"
    y "Did someone call?"
    "Shitting Noise."

    hide asami_judge

    "mariowinner" "yo this is just like my favourite game dangit granpa 2 where john granpa suses the impostor from amongus then sucks of tanigo komaea"
    m "ain't no fucking way"
    

    # end of shitpost

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
    m "(My skibidi sigma rizz failed me...??????)"
    m "THIS GAME SUCKS!"
    m "Fuck this shit I'm OUT!"
    "You then jump off from the window and die."
    play sound "sfx/vine boom.mp3"
    "The end."

    # m "Roll credits!!!"

    # play music "bgm/credits.mp3" fadeout 2

    # "WACCLAND DaTING SIM 2: elecrtric boogaloo - Prologue: To ball, is to live."
    # "Created by" " Aqua 'Rhadish' 'Goups' Hoshino"
    # "Created by" "Joker 'Lean' 'Lédouzy' Persona5 AKA 'The real Goups'"
    # "Character art by" "Rhadish"
    # "Background art by" "stolen assets from Doki Doki Literature Club and other various non-copyright free sources online."
    # "Music by" "stolen from Doki Doki Literature Club and other various video games or animes."
    # "Script written by" "Lédouzy and Rhadish."
    # "Concept by" "Rhadish"
    # "Special thanks" "Gabriel 'Bob' Théroux"
    # "Special thanks" "Yomki 'Yomki' Yomki"
    # "Special thanks" "Manx 'Oof Slayer' 'OddWerty05' The Soudeux"
    # "Special thanks" "And... NOT YOU! FUCK YOU! KEEP YOURSELF SAFE."

    # "The end."

    # This ends the game.

    return
