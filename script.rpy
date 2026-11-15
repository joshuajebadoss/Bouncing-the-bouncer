# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define a = Character("Player", color="#c8ffc8")
define e = Character("Red", color="#c8ffc8")
define b = Character("Blue", color="#ffc8c8")
define z = Character("Zeil", color="#ffc8f1")
# The game starts here
image red happy = "happy.jpg"
image red mad = "Angry.jpg"
image red sad = "sad.jpg"
image blue happy = "happy blue.jpg"
image blue mad = "Melissa.jpg"
image blue sad = "sad blue.jpg"
image brown happy = "Happy brown.jpg"
image brown mad = "Angry brown.jpg"
image brown sad = "sad brown"
image bg basketball:
    "Basketball.jpg"
    fit "cover"

label start:

    scene bg basketball
    e "Hello This is Red man and i am going to defeat blue once and for all"
    z "I am the \"greastest Bouncer\" of all time"

    
    e  "Oi blue nice to meet you again"
    show red happy
    b  "Hello Red, nice to meet you too"
    hide red happy
    show blue happy
    e  "I have come back for revenge, I will defeat you this time once and for all"
    hide blue happy
    show red mad
    b  "I will not let you defeat me, I will fight with all my strength and I will not give up with true power, just so you know you cant kill me im the bouncer king, even if i lose all my powers i will bounce back and make sure you wont survive, HAHAHHAHHAHAH, yes my POWERs its perfect you will never survive"
    hide red happy
    show blue mad
    e  "I will never give up, I will keep fighting and I will BOUNCE BACK and not to metion your powers were not that strong right?, HAAHAHA you fool, you reall think that you could defeat me with that type of power? good luck"
    hide blue mad
    show red mad
    e  "Ugh dang it im losing player can you help me what should i do?"
    
    
    a  "Uhhhhhhhhhhhhhhhhhhhh oh shoot what should i do should i be like ace attorny? Quick i have to choose"
    hide red mad
    show brown happy
    menu:
        "Give him a gun":
            "He points the gun at blue and shoots but misses"
        "Give him a knife": 
            "He trys to stab but blue evaded the attack"

    e   "Dang it i missed i swear if you had not evaded that attack I would have killed you"
    hide brown happy
    show red mad
    b   "yea well it was to simple and i did not want to die that way so i evaded"
    hide red mad
    show blue happy
    b   "Now its my turn"

    b   "hey player kill him...."

    a   "WHAT uhhhhhhhhhhhhhhhhh"
    hide blue happy 
    show brown happy
    menu:
        "Kill him(or atleast try to kill him)":
            jump banana 
        "Dont listen and say no to blue":
            "Blue gets angry at you"
            b   "PLAYER i trusted you"
            hide brown happy
            show blue mad
            a   "I did not want to kill red"
            a   "Blue.... why did you want me to kill him in the first place?"
            b   "It was personal I had to kill him"
            e   "Heh blue Im not suprised I knew you were trying to kill me"
            a   " you know guys we could just stop this right now"
            b   "No player I must win"
            a   "Oh shoot what should I do know?"
            menu:
                "Pull out a glock and shoot red":
                    e   "PLAYERRRRRRrRRR.......(Dies 2 seconds later after that statement)"
                    hide blue mad
                    show red sad
                    b   "HAHAHHAH I WIN LOSER"
                    "RED revives and comes back and stabs blue with his arm"
                    e   "Tsk TSk TSK I told you I always bounce back, and btw while i stabed you I took your ability to bounce back so good luck dying a painful death"
                    hide red sad
                    show red happy
                    b   "NOOOOOOOO (dies 3 seconds later)"
                    e   "Oh well he is dead now it is your turn player........."   
                    a   "IM SORRY PLEASE" 
                    e   "WELL TO LATE YOUR DEAD"
                    "The story ends as red shoots the player, keep trying there is many more endings right now you found the bad ending"       
                    return
                "Pull out glock and shoot blue":
                    "Then Player shoots blue but misses"
                    jump app
                    
    label banana:
        show red mad
        e   "oh my goodness player I trusted you what happend"
        a   "sorry but i had to do it blue told me to"
        b   "heh thanks player i knew you could do it"
        b   "But you did miss tho"
        a   "uh oh.... I dont like where this is going"
        e   "I got smth up my sleve"
        "Red pulls out a gun and trys to shoot blue but blue luckly escapes"
        b   "Oh my gosh, I did not expect that, but luckly I was able to dogde"
        e   "OH COME ON"
        a   "What should I do they are still fighting" 
        menu:
                "Summon the great banana and make the banana kill both of them": 
                    e   "AHHHHHHHHHHHHHHHHHHH What the HECK is that"
                    hide red mad
                    show brown mad
                    a   "Im sorry I had to"
                    b   "Ohhhhh Shoot, IM OUT"
                    a   "NO YOUR NOT IM TIRED OF YALL FIGHTING BANANA CLAP THEM"
                    "Then as red and blue try to run banana claps both of them"
                    "Good job you have gotten the banana ending you can try again to get a better ending"
                    return
                "Tell them to stop fighting":
                    hide red mad
                    show brown sad
                    a   "Guys we have to stop fighting"
                    e   "But why we need to fight to see who is the better bouncer"
                    b   "Nah player we cant stop were in the part the guys called the ZONE"
                    "As blue finishes his sentence they both go back to fighting"  
                    hide brown sad
                    show brown mad
                    a   "IM DONE THATS IT"
        menu:
                "Become sunkuna and domain expansion both of them":
                    a   "Domain expansion Melevolent Shrine"
                    e   "OH SHOOOOOOT"
                    b   "Since when could the player could do that?"
                    "As blue and red watch then both get sliced into millions of parts"
                    "GOOD JOB you got the JJK ending keep on trying to get a differnt ending"
                    return
                "Turn into the hacker king":
                    a   "HAHAHHAHA I HAVE HACKED BOTH OF YOU"
                    b   "NOOOOOOOOO"
                    e   "NOOOOOOOOO"
                    e   "Great now we are about to die"
                    e   "I havent even told my sister jessica good bye"
                    "as they cried about their game devolpent being deleted the hacker king killed both of the using a power ray to blast them to death"
                    "Good Job you got the Hacker ending keep trying to get more endings"
                    return
                

label app: 
        show blue mad
        e   "Dang"
        b   "AHHHHHHHH THATS IT IM DONE I SUMMON BLACK HOLELELELELLLELELELE"
        a   "Great"
        "as blue summons a black hole both the player and red dies, and then"
        b   "Im not done"
        "As blue is done saying his sentence he implants a nucler bomb and explodes it"
        "GOOOOOD JOB you got the black hole ending keep trying to get better endings"
