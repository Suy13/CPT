#DISCLAIMERS:WORDS & SOME OF PLOT IS NOT OWN AND HAS BEEN TAKEN DIRECTLY FROM HISHE KIDS COLLECTION

#pls type word for word in (____/____)

import random
import time
import sys

print('Start?')
time.sleep(1)
print('(yes/no)')

#slow typing
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(1)

#not as slow

def half_type(s):
    for l in s:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1)

#strange typing

def strange_type(u):
    ret = ''
    i = True
    for char in u:
        if not i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    print (ret)
    
#backward typing
def backward_type(w):
    print(w[::-1])



#sad face
def sad():
    print('                     1100111101110                    ')           
    print('                 101110111001110001111                ')        
    print('             101100_________________010111            ')        
    print('           01101______________________111001          ')        
    print('          1001__________________________10101         ')   
    time.sleep(0.5)     
    print('        1110______________________________01011       ')        
    print('       0011_______1011__________1101________0011      ')        
    print('      101________011011________101110_________100     ')        
    print('     1100________110110________110011_________1011    ')        
    print('     011__________0011__________1110___________100    ')   
    time.sleep(0.5)     
    print('     011_______________________________________011    ')        
    print('     101_______________________________________110    ')        
    print('     1100_____________________________________0101    ')        
    print('      110________________01101________________001     ')        
    print('       011____________10011011110____________110      ')  
    time.sleep(0.5)      
    print('        0011________01101_____10100________1011       ')        
    print('         1011______100___________110______1010        ')        
    print('           1100____11_____________01____0111          ')        
    print('             11010___________________11001            ')        
    print('                11000111101110010111101               ')        
    print('                   10100111101111001                  ')        

#happy face
def happy():
    print('                    010110                               ')
    print('                      1011001110101010100                        ') 
    print('                   001001____________001010                      ')
    print('               101010_____________________10100                  ') 
    time.sleep(0.5)
    print('            011001___________________________11001               ')
    print('          10100_________________________________0011             ') 
    print('         0010_____________________________________101            ') 
    print('       10100_______01010 _____________01010________0101          ') 
    print('      0011_______100110101 _________001010010 ______1100         ')
    time.sleep(0.5)
    print('      010_______11011001010________01100101101_______010         ')
    print('     101________01010011001________10011010101________101        ')
    print('    110_________00111011010________00010110011_________001       ')
    print('    001__________110100111__________011011011__________101       ')
    print('    100___________ 101010____________110010____________100       ')
    time.sleep(0.5)
    print('    001________________________________________________011       ')
    print('    111________________________________________________110       ')
    print('    010___10110_________________________________0011__ 010       ')
    print('     101_____11________________________________101____010        ')
    print('     001______001_____________________________00_____0110        ')
    time.sleep(0.5)
    print('      101________101______________________010_______1011         ')
    print('       110__________0111_______________111_________0010          ')
    print('        00101___________010001101010101___________1010           ')
    print('          0011_________________________________01010             ')
    print('            01001____________________________10010               ')
    time.sleep(0.5)
    print('              11011_______________________01110                  ')
    print('                00101011______________ 101001                    ')
    print('                     11000101011101011011                        ')
    print('                          0010110110                             ')

#smiley evil face
def evil():
    print('                  010110                               ')
    print('                      1011001110101010100                        ') 
    print('                   001001____________001010                      ')
    print('               101010_____________________10100                  ') 
    time.sleep(0.5)
    print('            011001___________________________11001               ')
    print('          10100_________________________________0011             ') 
    print('         0010_____________________________________101            ') 
    print('       10100_____01010_________________ 01010______0101          ') 
    print('      0011_____100___101______________001___010_____1100         ')
    time.sleep(0.5)
    print('      010_____110_____010____________010_____101_____010         ')
    print('     101_____100_______100__________100_______101_____101        ')
    print('    110_____010_________010________000_________011_____001       ')
    print('    001_____101__________111______011___________011____101       ')
    print('    100____00_____________10______11______________10___100       ')
    time.sleep(0.5)
    print('    001________________________________________________011       ')
    print('    111________________________________________________110       ')
    print('    010___10110_________________________________0011__ 010       ')
    print('     101_____11________________________________101____010        ')
    print('     001______001_____________________________00_____0110        ')
    time.sleep(0.5)
    print('      101________101______________________010_______1011         ')
    print('       110__________0111_______________111_________0010          ')
    print('        00101___________010001101010101___________1010           ')
    print('          0011_________________________________01010             ')
    print('            01001____________________________10010               ')
    time.sleep(0.5)
    print('              11011_______________________01110                  ')
    print('                00101011______________ 101001                    ')
    print('                     11000101011101011011                        ')
    print('                          0010110110                             ')
    

#end screen

def ending():
    print('''
      ████████████████████████████████████████████████████████████  
    ██                                                            ██
    ██              ██████    ██      ██    ██████                ██
    ██              ██        ████    ██    ██    ██              ██
    ██              ██████    ██  ██  ██    ██    ██              ██
    ██              ██        ██    ████    ██    ██              ██
    ██              ██████    ██      ██    ██████     ██         ██
    ██                                                            ██
      ████████████████████████████████████████████████████████████  
''')

begin = input()

#start?
def beginning():
    print('''
CHOOSE A STORY
(1/2/3)
''')

#the path you should choose :)
if begin.lower().strip() == 'yes':
    slow_type('LOADING. . .')
    stories = { 1 : ' itl e  ed  id n  H od', 2 : ' um t  D m ty', 3 : 'P in e s  nd  he  ea'}
    beginning()
    number = int(input())
    for x, y in stories.items():
        if number == x:
            half_type(y)
    time.sleep(1)
    print('''
    (yes/no)
    ''')
    answer = input()
    while answer == 'no':
        beginning()
        number = int(input())
        for x, y in stories.items():
            if number == x:
                half_type(y)
        time.sleep(1)
        print('''
    (yes/no)
    ''')
        answer = input()
    if answer == 'yes':
        slow_type('. . .')
        if number == 1:
            
#start of story 1
            half_type('''
    Once upon a time, there was a little girl.
    She lived with her parents.
    Her grandma lived away in a small house past the forest.
    On Red's 11th birthday, she was gifted a bright red hood.
    She cherished the hood and always wore it outside.
    She was known as "Little Red Hood".
    ''')
            slow_type('. . .')
            half_type('''
    One day...
    ''')
            half_type('''
    Dad: Red, wake up!
    ''')
            print('''
        (get up/sleep)
''')
            banswer = input()
            if banswer == 'sleep':
                slow_type('. . .')
                half_type('''
    (Red is filled with regret for not listening to her parents.)
    ''')
                ending()
            #route
            else:
                half_type('''
    Red wakes up.
    Red gets ready for the day and goes to the kitchen.
    
    Mom: Eat breakfast. I have something for you.''')
                print('''
        (eat/not eat)
        ''')
                canswer = input()
                if canswer == 'not eat':
                    slow_type('. . .')
                    half_type('''
    (Red didn't eat and stayed hungry for the rest of the day.)
    ''')
                    ending()
                #route
                else:
                    half_type('''
    Red eats the delicious breakfast her mom made.
    Then, Red went to her mom.
    
    Mom: Here's a basket with muffins for grandma.
         Could you take this to her?
    ''')
                    print('''
        (yes/no)
        ''')
                    danswer = input()
                    if danswer == 'no':
                        slow_type('. . .')
                        half_type('''
    (Red's parents were very disappointed.)
    ''')
                        ending()
                    #route
                    else:
                        half_type('''
    Mom: Thank you.
         I'm busy today, so I'm glad you're going.
         Just remember, don't stray off the path.
         ''')
                        print('''
        (got it/ok)
        ''')
                        input()
                        half_type('''
    Red took the basket and walked down the path.
    She followed the dirt path.
    Then, Red came to a crossroads.
    One sign said "Grandma's House".
    The other said "Three Little Bears".
    Before Red could choose, a wolf appeared before her.
    
    Wolf: Pardon me, unaccompanied little girl.
          I couldn't help, but notice you, uh, by yourself.
          Traveling alone through this dark and scary forest.
          ALONE.
            ''')
                        print('''
        (Yeah?/Would you like to join me?)
        ''')
                        fanswer = input()
                        if fanswer == 'Would you like to join me?':
                            slow_type('. . .')
                            half_type('''
    (The wolf was delighted. Red, not so much.)    
    ''')
                            ending()
                        else:
                            half_type('''
    Wolf: And where might you be headed off to, so that I may follo-
          Uh, I mean accompany you.
          ''')
                            half_type('''
    Red: I'm headed to...
    ''')
                            print('''
        (my grandma's house/the three little bears' house)
        ''')
    
                            ganswer = input()
                            if ganswer == "the three little bears' house":
                                slow_type('. . .')
                                half_type('''
    (The wolf did not fall for the trick. He decided to have lunch early.)
    ''')
                                ending()
                            else:
                                half_type('''
    Red: It's down the path...in that direction.
    ''')
                                print('''
        (Which path do you point to?)
        (left/right)
        ''')
                                hanswer = input()
                                if hanswer == "left":
                                    slow_type('. . .')
                                    half_type('''
    (The wolf went to grandma's house and had a great dinner.)
    ''')
                                    ending()
                                else:
                                    half_type('''
    Red pointed to the right path.
    Red: I can't stay and chat.
         My poor, sick, feeble and vulnerable grandmother is waiting for me.
         Right down the end of that path...
    ''')
                                    print('''
        (Which path do you point to?)
        (left/right)
        ''')
                                    ianswer = input()
                                    if ianswer == "left":
                                        slow_type('. . .')
                                        half_type('''
    (The wolf rushed down the left path. He enjoyed dinner very much.)
    ''')
                                        ending()
                                    else:
                                        half_type('''
    Red pointed to the right path.
    
    Red: That way. Yep.
    ''')

                                        half_type('''
    Wolf: How delicious of you, I mean, how DEDICATED of you!
          But, might I recommend taking time to gather some wonderfully beautiful flowers for your grandma as you go?
          There are flowers slightly off the path.''')
                                        print('''
        (stay on path/go off path)
        ''')
                                        janswer = input()
                                        if janswer == "stay on path":
                                            slow_type('. . .')
                                            half_type('''
    (The wolf became annoyed and had lunch early.)
    ''')
                                            ending()
                                        else:
                                            half_type('''
    Red: Well, thank you.
         I'll be sure to keep that in mind.
         Now, off I go!
    ''')
                                            half_type('''
    Wolf: Yes...
          Now, to cut through the woods and arrive at grandmother's house first!
    ''')
                                            half_type('''
    Red appeared back at the crossroads.
    She snickered at the wolf's misfortune.
    ''')
                                            half_type('''
    Red continued on the left path.
    She reached grandma's house and told her grandmother about her meeting with the wolf.
            ''')
                                            half_type('''
    Grandma: That's clever!
             But I wonder, whatever became of that wolf?
    
    [With the wolf]

    Wolf kicked down the door of the cottage.
    
    Wolf: Hello, Granny!
          Wait, you're not grandma...
    
    The three BIG bears turned and faced the intruder.
    ''')
                                            half_type('''
    Wolf: Oh. 
          Goodness!
          What big teeth you have!
          AHHHHHH!!!
          
    Red happily enjoyed muffins with her grandmother.
    And Red never saw that wolf again.
    ''')
                                            #true end
                                            slow_type('. . .')
                                            print('TRUE')
                                            ending()
#second story 
        if number == 2:
            half_type('''
    Once upon a time, there was an egg...
        
        (continue/end)
    ''')
            kanswer = input()
            if kanswer == "end":
                slow_type('. . .')
                half_type('''
    And that was the end of the story.
    ''')
                ending()
            else:
                slow_type('. . .')
                half_type('''
    Humpty Dumpty sat on a wall,
        
        (get down/stay)
        ''')
                lanswer = input()
                if lanswer == 'stay':
                    slow_type('. . .')
                    half_type('''
    Humpty Dumpty had a great fall.
    ''')
                    ending()
                else:
                    slow_type('. . .')
                    half_type('''
    And narrowly avoided having a great fall,
    Because all the king's horses and all the king's men said,
    "Don't sit on that wall, it's windy my friend!"
        
        (consider/ignore)''')
                    manswer = input()
                    if manswer == 'ignore':
                        slow_type('. . .')
                        half_type('''
    So Humpty Dumpty sat on the wall, 
    And Humpty Dumpty had a great fall.
    ''')
                    else:
                        slow_type('. . .')
                        half_type('''
    Humpty Dumpty considered their words,
    And realized sitting atop walls is absurd!
    
        (climb/jump)
        ''')
                        nanswer = input()
                        if nanswer == 'jump':
                            slow_type('. . .')
                            half_type('''
    Not so carefully, he jumped down. 
    He went splat when his feet touched the ground.
    ''')
                            ending()
                        else:
                            slow_type('. . .')
                            half_type('''
    He carefully climbed down,
    'Til his feet touched the ground,
    And "King of Safety" Humpty Dumpty was crowned.
    
        (As "King of Safety", what will Humpty do?)
        (work hard/laze around)
        ''')
                            oanswer = input()
                            if oanswer == 'laze around':
                                slow_type('. . .')
                                half_type('''
    And so atop the wall he lazed around,
    And when the wind blew, he fell and made a shattering sound.
    ''')
                                ending()
                            else:
                                slow_type('. . .')
                                half_type('''
    And Humpty Dumpty worked at a pace that was brisk.
    He made signs, he made rules, helping all avoid risk.
    
        (continue work/laze around)
        ''')
                                panswer = input()
                                if panswer == 'laze around':
                                    slow_type('. . .')
                                    half_type('''
    But atop the very same wall, he lazed around,
    And so when the wind blew, he fell and made a shattering sound.
    ''')
                                    ending()
                                else:
                                    slow_type('. . .')
                                    half_type('''
    Humpty: Don't sit there! Don't stand there! Be careful up high!
    
    He ordered, he pestered, and he wasn't shy.
    Eventually, the people had all had enough
    His signs and his rules prevented fun stuff!
    Where there's something to do or some place to go,
    Humpty Dumpty placed warnings and they all said, "NO!"
    
    Jack: But I wanna jump over this candle stick!
          I promise I'm nimble, I swear that I'm quick!
    
        (alright/no)
        ''')
                                    qanswer = input()
                                    if qanswer == 'alright':
                                        slow_type('. . .')
                                        half_type('''
    So Jack tried to jump over the candle stick,
    But he was neither nimble nor quick.
    ''')
                                        ending()
                                    else:
                                        slow_type('. . .')
                                        half_type('''
    Jack & Jill: But our family needs water. We must fill this pail!
                 If you let us, we surely won't fail.
    
        (alright/no)
    ''')
                                        ranswer = input()
                                        if ranswer == 'alright':
                                            slow_type('. . .')
                                            half_type('''
    And so Jack and Jill went up the hill,
    To fetch a pail of water.
    Jack fell down and broke his crown, 
    And Jill came tumbling after.
    ''')
                                            ending()
                                        else:
                                            slow_type('. . .')
                                            half_type('''
    Soon, all the king's horses and all the king's men,
    Grew tired of the rules and wanted an end!
    
    [Night: At Home]
    (go straight to sleep/take a long bath)
    ''')
                                            sanswer = input()
                                            if sanswer == 'go straight to sleep':
                                                slow_type('. . .')
                                                half_type('''
    So while Humpty slept though it took them some time,
    They went around the kingdom and changed a few signs.
    At dawn, Humpty Dumpty awoke with a smirk.
    
        (stay in/go out)
        ''')
                                                tanswer = input()
                                                if tanswer == 'stay in':
                                                    slow_type('. . .')
                                                    half_type('''
    And so all the king's horses and all the king's men,
    Were forced to listen to Humpty again.
    ''')
                                                    ending()
                                                else:
                                                    slow_type('. . .')
                                                    half_type('''
    He walked around the town to see all his work.
    When walking about proved tiring and hot,
    He needed to sit and soon found a SAFE spot.
    So Humpty then sat on that very same wall,
    And when the wind blew, he had a great fall!
    ''')
                                                    ending()
                                            #route
                                            else:
                                                slow_type('. . .')
                                                half_type('''
    So while Humpty slept though it took them some time,
    They went around the kingdom and changed a few signs.
    At dawn, Humpty Dumpty awoke with a smirk.
        
        (stay in/go out)
        ''')
                                                uanswer = input()
                                                if uanswer == 'stay in':
                                                    slow_type('. . .')
                                                    half_type('''
    And so all the king's horses and all the king's men,
    Were forced to listen to Humpty again.
    ''')
                                                    ending()
                                                else:
                                                    slow_type('. . .')
                                                    half_type('''
    He walked around the town to see all his work.
    When walking about proved tiring and hot,
    He needed to sit and soon found a safe spot.

        (sit in the grass/follow the signs)
        ''')
                                                    vanswer = input()
                                                    if vanswer == 'sit in the grass':
                                                        slow_type('. . .')
                                                        half_type('''
    And when Humpty sat in the fields, their plan was derailed.
    And so the king's men moped about, as their plan had failed.                                      
    ''')
                                                        ending()
                                                    else:
                                                        slow_type('. . .')
                                                        half_type('''
    So Humpty then sat on that very same wall,
    And when the wind blew, he had a great fall!
    But when Humpty landed, hard on the ground,
    He didn't break! Instead he bounced up and down!
    
    King's men: Bouncing, not broken?! What was the matter?
                He's an egg after all, he should splatter and shatter!
    
    Their plan to get rid of Humpty Dumpty had been foiled...
    Because, to be safe...
    He had himself hard-boiled.''')
                                                        #true end
                                                        slow_type('. . .')
                                                        print('TRUE')
                                                        ending()
                                                    
#third story
        if number == 3:
            half_type('''
    Once upon a time, there was a prince...

        (continue/end)
    ''')
            t_aanswer = input()
            if t_aanswer == 'end':
                slow_type('. . .')
                half_type('''
    And that was the end of the story.
''')
                ending()
            else:
                slow_type('. . .')
                half_type('''
    Prince: Oh Mother. I few I shall never find a true princess that is truly true.
            And now it is beginning to rain.
            Woe is me.

    Queen: Don't despair my darling dear, you deserve a princess as true as can be.
    
    And while the picky prince was at his whiniest,
    And the storm continued to reach its stormiest,
    There was a young woman...

        (continue/end)
        ''')
                t_banswer = input()
                if t_banswer == 'end':
                    slow_type('. . .')
                    half_type('''
    That did not meet the prince because the story ended there.
    ''')
                else:
                    slow_type('. . .')
                    half_type('''
    Who had got caught in the storm.
    She had gotten separated from her friends.
    Her face was muddy, clothes torn and hair a mess.
    As she continued, she came to a fork in the forest.
    
        (go left/go right)
    ''')
                    t_canswer = input()
                    if t_canswer == 'go left':
                        slow_type('. . .')
                        half_type('''
    She went left and eventually reached a town.
    Days passed and the storm eventually calmed.
    She reunited with her friends and went back to her kingdom.
    ''')
                        ending()
                    else:
                        slow_type('. . .')
                        half_type('''
    As she continued on the right path, she came to a castle.
    
        (knock/don't knock)
    ''')
                        t_danswer = input()
                        if t_danswer == "don't knock":
                            slow_type('. . .')
                            half_type('''
    And so the young woman continued to stand before the castle.                        
    ''')
                            ending()
                        else:
                            slow_type('. . .')
                            half_type('''
    She knocked on the door and a prince opened it.

    Young woman: Hello.

    Prince: Yes?

    Young woman: I got separated from my companions in this terrible storm.
                 May I please come out of the rain?
    
    Prince: We are only allowing entrace to true princesses.
            Good day!
    
    And the door was slammed in her face.
    
        (knock again/don't knock again)
        ''')
                            t_eanswer = input()
                            if t_eanswer == "don't knock again":
                                slow_type('. . .')
                                half_type('''
    Young woman: How rude.

    And so the she did not knock again.
    ''')
                                ending()
                            else:
                                slow_type('. . .')
                                half_type('''
    
    But the woman at the door would not give up.
    She knocked even louder the second time.
    
    Prince: Yes?
    
        (I am a true princess./Please let me come in.)
        ''')
                                t_fanswer = input()
                                if t_fanswer == 'Please let me come in.':
                                    slow_type('. . .')
                                    half_type('''
    The Prince was disgusted by her appearance and did not let her in.
    ''')
                                    ending()
                                else:
                                    slow_type('. . .')
                                    half_type('''
    Young woman: Please let me come in out of the rain.

    The Prince was confused. 
    Could this muddy and grumpy woman truly be a true princess?

    Queen: Of course you can come in, muddy.
            I mean, my dear.
            Eat and warm up as we prepare a nice room for you to sleep in tonight.
    
        (accept/refuse)
        ''')
                                    t_ganswer = input()
                                    if t_ganswer == "refuse":
                                        slow_type('. . .')
                                        half_type('''
    But the young woman did not stay and continued on her way.
    ''')
                                        ending()
                                    else:
                                        slow_type('. . .')
                                        half_type('''
    So while the young woman relaxed by the fire, 
    the Queen directed her servants to prepare a bed with 
    20 mattresses and 20 soft down comforters.
    Then, the Queen placed a tiny, green pea under the massive pile. 
    She then explained to her son.

    Queen: If she feels the pea under all of that. 
           We will know she is a true princess, for a true princess is sensitive.
    
    [At Night]
    
    The young woman felt a small lump as she laid on the bed.

        (What does she do?)
        (try to sleep/search for it)
    ''')
                                        t_hanswer = input()
                                        if t_hanswer == 'Search for it':
                                            slow_type('. . .')
                                            half_type('''
    The young woman found a pea under the bed.
    She then went to bed and had a nice sleep.
    
    [Morning]

    The Queen and Prince heard that you had a nice sleep.
    They doubted you were a true princess and kicked you 
    out of their castle.
                                            ''')
                                            ending()
                                        else:
                                            slow_type('. . .')
                                            half_type('''
    [Morning]

    The Prince and Queen anxiously awaited the arrival of the woman.
    As the woman came down, they could see bags under her red, swollen eyes.

    Queen: Good morning, my dear.

    Prince: How did you sleep last night?

        (truth/lie)
    ''')
                                            t_ianswer = input()
                                            if t_ianswer == 'lie':
                                                slow_type('. . .')
                                                half_type('''
    Young woman: The thunder was too loud, so I couldn't fall asleep.

    The Prince and Queen were disappointed you didn't mention the pea.
                                        ''')
                                                ending()
                                            else:
                                                slow_type('. . .')
                                                half_type('''
    Young woman: I never actually fell asleep. 
                 There was some sort of rock or lump in the bed, so I couldn't get comfortable.
    
    The Prince and Queen looked at each other.
    
    Prince & Queen: Hooray! 
                    You passed the test! 
                    Only a true princess would be sensitive enough to know the pea was there.
                    
        (get upset/become happy)
        ''')
                                                t_janswer = input()
                                                if t_janswer == 'become happy':
                                                    slow_type('. . .')
                                                    half_type('''
    All three became joyous and the young woman was wedded to the picky prince.
        ''')
                                                    ending()
                                                else:
                                                    slow_type('. . .')
                                                    half_type('''
    Young woman: Woah woah woah...
    
    The woman slammed her hands against the table.

    Young woman: I showed up on your doorstep filthy and exhausted.
                 And you decided to test me?!
    
    Prince: Um, yes. But you passed, so, hooray!

    Queen: And now you two can get married!
        
        (accept/refuse)
        ''')
                                                    t_kanswer = input()
                                                    if t_kanswer == 'accept':
                                                        slow_type('. . .')
                                                        half_type('''
    So the two got married.
        ''')
                                                        ending()
                                                    else:
                                                        slow_type('. . .')
                                                        half_type('''
    Young woman: No! We're not getting married!
                 What is wrong with you people?
                 That's the meanest thing anyone has ever done to me!
                 Why would I want to marry someone who treats women that way?!
    
    Prince: Um, because I'm a prince!

    Young woman: What was it you said to me last night?
                 Oh right, I remember.
        
        (Yes?/Good day!)
    ''')
                                                        t_lanswer = input()
                                                        if t_lanswer == 'Yes?':
                                                            slow_type('. . .')
                                                            half_type('''
    The woman accidentally accepted after she remembered the wrong thing.
    ''')
                                                            ending()
                                                        else:
                                                            slow_type('. . .')
                                                            half_type('''
    The young woman- I mean, the true princess packed up her belongings and walked towards the front door.
    
    Prince: But wait! You're the only true princess in the land!
    
    Young woman: Oh yeah? Well, you're not the only royalty!
    
    So the true princess returned to her kingdom and maybe, eventually, found love.
    Oh, and she never ate peas.
    ''')
                                                            #true end
                                                            slow_type('. . .')
                                                            print('TRUE')
                                                            ending()

#alternate path
if begin.lower().strip() == 'no':
    print ('Are you sure?')
    two_answer = input()
    a = 3
    while a > 0:
        print ('Are you sure?')
        two_answer = input()
        if two_answer == 'yes' or 'no':
                a -= 1
    if a == False:
        strange_type('are you sure?')
        time.sleep(3)
        backward_type('are you sure?')
        time.sleep(3)
        slow_type('. . . . . . . .')
        print('''
:)''')
        for i in range(5):
            print('hi')
            time.sleep(0.5)
        slow_type('. . . . .')
        happy()
        half_type('''
h  lo
''')
        time.sleep(5)
        half_type('''
 r nt y o go ng to pl y?
 ''')
        print('''
(yes/no)''')
        t_response = input()
        if t_response == 'yes':
            half_type('''
t en  est rt''')
        else:
            sad()
            half_type('''
W-w y?''')
            time.sleep(5)
            half_type('''
 hy  r nt  ou pl yi g?''')
            slow_type('''
...''')
            happy()
            half_type('''
w l  th ts  ine''')
            time.sleep(3)
            half_type('''
 ou ca  pl y  ith m ''')
            slow_type('''
LOADING. . .''')
            print('''
            You're in the woods.
            #@*&$ is chasing you.
            What do you do?
            (run/hide)
            ''')
            input()
            print('''
            Too late.
            ''')
            time.sleep(2)
            print('''
            #@*&$ has caught you.
            They are taking you somewhere.
            What do you do?
            (struggle/kick/play dead)
            ''')
            time.sleep(8)
            print('''
            Too bad.
            Your struggles are not effective.
            #@*&$ ties your hands and feet.
            They go to grab a big rock.
            What do you do?
            ''')
            input()
            print('''
            Anything you do is ineffective.
            Now, #@*&$ has a rock 
            and is about to use it.
            You remember you have a pocket 
            knife in your back pocket.
            What do you do?''')
            time.sleep(10)
            slow_type('''
YOU DIED
            ''')
            evil()
            slow_type('''
RESTART THE GAME''')
            
