import requests
import random
import string
import json
import os
import http.cookiejar
import time
import http.cookies
import urllib

caesar = ['SCENE I. Rome. A street.  Enter FLAVIUS, MARULLUS, and certain Commoners',
          'FLAVIUS    Hence! home, you idle creatures get you home:    Is this a holiday? what! know you not,    Being mechanical, you ought not walk    Upon a labouring day without the sign    Of your profession? Speak, what trade art thou?',
          'First Commoner    Why, sir, a carpenter.',
          'MARULLUS    Where is thy leather apron and thy rule?    What dost thou with thy best apparel on?    You, sir, what trade are you?',
          'Second Commoner    Truly, sir, in respect of a fine workman, I am but,    as you would say, a cobbler.',
          'MARULLUS    But what trade art thou? answer me directly.',
          'Second Commoner    A trade, sir, that, I hope, I may use with a safe    conscience; which is, indeed, sir, a mender of bad soles.',
          'MARULLUS    What trade, thou knave? thou naughty knave, what trade?',
          'Second Commoner    Nay, I beseech you, sir, be not out with me: yet,    if you be out, sir, I can mend you.',
          'MARULLUS    What meanest thou by that? mend me, thou saucy fellow!',
          'Second Commoner    Why, sir, cobble you.',
          'FLAVIUS    Thou art a cobbler, art thou?',
          'Second Commoner   Truly, sir, all that I live by is with the awl: I    meddle with no tradesmans matters, nor womens    matters, but with awl. I am, indeed, sir, a surgeon    to old shoes; when they are in great danger, I    recover them. As proper men as ever trod upon    neats leather have gone upon my handiwork.',
          'FLAVIUS    But wherefore art not in thy shop today?    Why dost thou lead these men about the streets?',
          'Second Commoner    Truly, sir, to wear out their shoes, to get myself    into more work. But, indeed, sir, we make holiday,    to see Caesar and to rejoice in his triumph.',
          'MARULLUS    Wherefore rejoice? What conquest brings he home?    What tributaries follow him to Rome,    To grace in captive bonds his chariot-wheels?    You blocks, you stones, you worse than senseless things!    O you hard hearts, you cruel men of Rome,    Knew you not Pompey? Many a time and oft    Have you climbd up to walls and battlements,    To towers and windows, yea, to chimney-tops,    Your infants in your arms, and there have sat    The livelong day, with patient expectation,    To see great Pompey pass the streets of Rome:    And when you saw his chariot but appear,    Have you not made an universal shout,    That Tiber trembled underneath her banks,    To hear the replication of your sounds    Made in her concave shores?    And do you now put on your best attire?    And do you now cull out a holiday?    And do you now strew flowers in his way    That comes in triumph over Pompeys blood? Be gone!    Run to your houses, fall upon your knees,    Pray to the gods to intermit the plague    That needs must light on this ingratitude.',
          'FLAVIUS    Go, go, good countrymen, and, for this fault,    Assemble all the poor men of your sort;    Draw them to Tiber banks, and weep your tears    Into the channel, till the lowest stream    Do kiss the most exalted shores of all.    Exeunt all the Commoners    See whether their basest metal be not moved;    They vanish tongue-tied in their guiltiness.    Go you down that way towards the Capitol;This way will I    disrobe the images,    If you do find them deckd with ceremonies.',
          'MARULLUS    May we do so?    You know it is the feast of Lupercal.',
          'FLAVIUS    It is no matter; let no images    Be hung with Caesars trophies. Ill about,    And drive away the vulgar from the streets:    So do you too, where you perceive them thick.    These growing feathers pluckd from Caesars wing    Will make him fly an ordinary pitch,    Who else would soar above the view of men    And keep us all in servile fearfulness.',
          'Exeunt',
          '',
          'SCENE II. A public place.    Flourish. Enter CAESAR; ANTONY, for the course; CALPURNIA, PORTIA, DECIUS BRUTUS, CICERO, BRUTUS, CASSIUS, and CASCA; a great crowd following, among them a Soothsayer ',
          'CAESAR    Calpurnia!',
          'CASCA    Peace, ho! Caesar speaks.',
          'CAESAR    Calpurnia!',
          'CALPURNIA    Here, my lord.',
          'CAESAR    Stand you directly in Antonius way,    When he doth run his course. Antonius!',
          'ANTONY    Caesar, my lord?',
          'CAESAR    Forget not, in your speed, Antonius,    To touch Calpurnia; for our elders say,    The barren, touched in this holy chase,    Shake off their sterile curse.',
          'ANTONY    I shall remember:    When Caesar says do this, it is performd.',
          'CAESAR    Set on; and leave no ceremony out.    Flourish',
          'Soothsayer    Caesar!',
          'CAESAR    Ha! who calls?',
          'CASCA    Bid every noise be still: peace yet again!',
          'CAESAR    Who is it in the press that calls on me?    I hear a tongue, shriller than all the music,    Cry Caesar! Speak; Caesar is turnd to hear.',
          'Soothsayer    Beware the ides of March.',
          'CAESAR    What man is that?',
          'BRUTUS    A soothsayer bids you beware the ides of March.',
          'CAESAR    Set him before me; let me see his face.',
          'CASSIUS    Fellow, come from the throng; look upon Caesar.',
          'CAESAR    What sayst thou to me now? speak once again.',
          'Soothsayer    Beware the ides of March.',
          'CAESAR    He is a dreamer; let us leave him: pass.    Sennet. Exeunt all except BRUTUS and CASSIUS',
          'CASSIUS    Will you go see the order of the course?',
          'BRUTUS    Not I.',
          'CASSIUS    I pray you, do.',
          'BRUTUS    I am not gamesome: I do lack some part    Of that quick spirit that is in Antony.    Let me not hinder, Cassius, your desires;    Ill leave you.',
          'CASSIUS    Brutus, I do observe you now of late:    I have not from your eyes that gentleness    And show of love as I was wont to have:    You bear too stubborn and too strange a hand    Over your friend that loves you.',
          'BRUTUS    Cassius,   Be not deceived: if I have veild my look,    I turn the trouble of my countenance    Merely upon myself. Vexed I am    Of late with passions of some difference,    Conceptions only proper to myself,    Which give some soil perhaps to my behaviors;    But let not therefore my good friends be grieved--    Among which number, Cassius, be you one--    Nor construe any further my neglect,    Than that poor Brutus, with himself at war,    Forgets the shows of love to other men.',
          'CASSIUS    Then, Brutus, I have much mistook your passion;   By means whereof this breast of mine hath buried    Thoughts of great value, worthy cogitations.    Tell me, good Brutus, can you see your face?',
          'BRUTUS    No, Cassius; for the eye sees not itself,    But by reflection, by some other things',
          'CASSIUS    Tis just:    And it is very much lamented, Brutus    That you have no such mirrors as will turn    Your hidden worthiness into your eye,    That you might see your shadow. I have heard,    Where many of the best respect in Rome,    Except immortal Caesar, speaking of Brutus    And groaning underneath this ages yoke,    Have wishd that noble Brutus had his eyes.',
          'BRUTUS    Into what dangers would you lead me, Cassius,    That you would have me seek into myself    For that which is not in me?',
          'CASSIUS    Therefore, good Brutus, be prepared to hear:    And since you know you cannot see yourself    So well as by reflection, I, your glass,    Will modestly discover to yourself    That of yourself which you yet know not of.    And be not jealous on me, gentle Brutus:    Were I a common laugher, or did use    To stale with ordinary oaths my love    To every new protester; if you know    That I do fawn on men and hug them hard    And after scandal them, or if you know    That I profess myself in banqueting    To all the rout, then hold me dangerous.   Flourish, and shout',
          'BRUTUS    What means this shouting? I do fear, the people    Choose Caesar for their king.',
          'CASSIUS    Ay, do you fear it?    Then must I think you would not have it so.',
          'BRUTUS    I would not, Cassius; yet I love him well.    But wherefore do you hold me here so long?    What is it that you would impart to me?    If it be aught toward the general good,    Set honour in one eye and death i the other,    And I will look on both indifferently,    For let the gods so speed me as I love    The name of honour more than I fear death.',
          'CASSIUS    I know that virtue to be in you, Brutus,    As well as I do know your outward favour.    Well, honour is the subject of my story.    I cannot tell what you and other men    Think of this life; but, for my single self,    I had as lief not be as live to be    In awe of such a thing as I myself.    I was born free as Caesar; so were you:    We both have fed as well, and we can both    Endure the winters cold as well as he:    For once, upon a raw and gusty day,    The troubled Tiber chafing with her shores,    Caesar said to me Darest thou, Cassius, now    Leap in with me into this angry flood,    And swim to yonder point? Upon the word,    Accoutred as I was, I plunged in    And bade him follow; so indeed he did.    The torrent roard, and we did buffet it    With lusty sinews, throwing it aside    And stemming it with hearts of controversy;    But ere we could arrive the point proposed,    Caesar cried Help me, Cassius, or I sink!    I, as Aeneas, our great ancestor,    Did from the flames of Troy upon his shoulder    The old Anchises bear, so from the waves of Tiber    Did I the tired Caesar. And this man    Is now become a god, and Cassius is    A wretched creature and must bend his body,    If Caesar carelessly but nod on him.    He had a fever when he was in Spain,    And when the fit was on him, I did mark    How h did shake: tis true, this god did shake;    His coward lips did from their colour fly,    And that same eye whose bend doth awe the world    Did lose his lustre: I did hear him groan:    Ay, and that tongue of his that bade the Romans    Mark him and write his speeches in their books,    Alas, it cried Give me some drink, Titinius,    As a sick girl. Ye gods, it doth amaze me    A man of such a feeble temper should    So get the start of the majestic world    And bear the palm alone.    Shout. Flourish',
          'BRUTUS    Another general shout!    I do believe that these applauses are    For some new honours that are heapd on Caesar.',
          'CASSIUS    Why, man, he doth bestride the narrow world    Like a Colossus, and we petty men    Walk under his huge legs and peep about    To find ourselves dishonourable graves.    Men at some time are masters of their fates:    The fault, dear Brutus, is not in our stars,    But in ourselves, that we are underlings.    Brutus and Caesar: what should be in that Caesar?    Why should that name be sounded more than yours?    Write them together, yours is as fair a name;    Sound them, it doth become the mouth as well;    Weigh them, it is as heavy; conjure with em,    Brutus will start a spirit as soon as Caesar.    Now, in the names of all the gods at once,    Upon what meat doth this our Caesar feed,    That he is grown so great? Age, thouart shamed!    Rome, thou hast lost the breed of noble bloods!    When went there by an age, since the great flood,    But it was famed with more than with one man?    When could they say till now, that talkd of Rome,    That her wide walls encompassd but one man?    Now is it Rome indeed and room enough,    When there is in it bt one only man.    O, you and I have heard our fathers say,    There was a Brutus once that would have brookd    The eternal devil to keep his state in Rome    As easily as a king.',
          'BRUTUS    That you do love me, I am nothing jealous;    What you would work me to, I have some aim:    How I have thought of this and of these times,    I shall recount hereafter; for this present,    I would not, so with love I might entreat you,    Be any further moved. What you have said    I will consider; what you have to say    I will with patience hear, and find a time    Both meet to hear and answer such high things.    Till then, my noble friend, chew upon this:    Brutus had rather be a villager    Than to repute himself a son of Rome    Under these hard conditions as this time    Is like to lay upon us.',
          'CASSIUS    I am glad that my weak words    Have struck but thus much show of fire from Brutus.',
          'BRUTUS    The games are done and Caesar is returning.',
          'CASSIUS    As they pass by, pluck Casca by the sleeve;    And he will, after his sour fashion, tell you    What hath proceeded worthy note to-day.    Re-enter CAESAR and his Train',
          'BRUTUS    I will do so. But, look you, Cassius,    The angry spot doth glow on Caesars brow,    And all the rest look like a chidden train:    Calpurnias cheek is pale; and Cicero    Looks with such ferret and such fiery eyes    As we have seen him in the Capitol,    Being crossd in conference by some senators.',
          'CASSIUS    Casca will tell us what the matter is.',
          'CAESAR    Antonius!',
          'ANTONY    Caesar?',
          'CAESAR    Let me have men about me that are fat;    Sleek-headed men and such as sleep o nights:    Yond Cassius has a lean and hungry look;    He thinks too much: such men are dangerous.',
          'ANTONY    Fear him not, Caesar; hes not dangerous;    He is a noble Roman and well given.',
          'CAESAR    Would he were fatter! But I fear him not:    Yet if my name were liable to fear,    I do not know the man I should avoid    So soon as that spare Cassius. He reads much;    He is a great observer and he looks    Quite through the deeds of men: he loves no plays,    As thou dost, Antony; he hears no music;    Seldom he smiles, and smiles in such a sort    As if he mockd himself and scornd his spirit    That could be moved to smile at any thing.    Such men as he be never at hearts ease    Whiles they behold a greater than themselves,    And therefore are they very dangerous.    I rather tell thee what is to be feard    Than what I fear; for always I am Caesar.    Come on my right hand, for this ear is deaf,    And tell me truly what thou thinkst of him.    Sennet. Exeunt CAESAR and all his Train, but CASCA',
          'CASCA    You pulld me by the cloak; would you speak with me?',
          'BRUTUS    Ay, Casca; tell us what hath hanced to-day,    That Caesar looks so sad.',
          'CASCA    Why, you were with him, were you not?',
          'RUTUS    I should not then ask Casca what had chanced.',
          'CASCA    Why, there was a crown offered him: and being    offered him, he put it by with the back of his hand,    thus; and then the people fell a-shouting.',
          'BRUTUS    What was the second noise for?',
          'ASCA    Why, for that too.',
          'CASSIUS    They shouted thrice: what was the last cry for?',
          'CASCA    Why, for that too.',
          'BRUTUS    Was the crown offered him thrice?',
          'CASCA    Ay, marry, wast, and he put it by thrice, every    time gentler than other, and at every putting-by    mine honest neighbours shouted.',
          'CASSIUS    Who offered him the crown?',
          'CASCA    Why, Antony.',
          'BRUTUS    Tell us the manner of it, gentle Casca.',
          'CASCA    I can as well be hanged as tell the manner of it:    it was mere foolery; I did not mark it. I saw Mark    Antony offer him a crown;--yet twas not a crown    neither, twas one of these coronets;--and, as I told    you, he put it by once: but, for all that, to my    thnking, he would fain have had it. Then he    offered it to him again; then he put it by again:    but, to my thinking, he was very loath to lay his    fingers off it. And then he offered it the third    time; he put it the third time by: and still as he    refused it, the rabblement hooted and clapped their    chapped hands and threw up their sweaty night-caps    and uttered such a deal of stinking breath because    Caesar refused the crown that it had almost choked    Caesar; for he swounded and fell down at it: and    for mine own part, I durst not laugh, for fear of    opening my lips and receiving the bad air.',
          'CASSIUS    But, soft, I pray you: what, did Caesar swound?',
          'CASCA    He fell down in the market-place, and foamed at    mouth, and was speechless.',
          'BRUTUS    Tis very like: he hath the failing sickness.',
          'CASSIUS    No, Caesar hath it not; but you and I,    And honest Casca, we have the falling sickness.',
          'CASCA    I know not what you mean by that; but, I am sure,    Caesar fell down. If the tag-rag people did not    clap him and hiss him, according as he pleased and    displeased them, as they use to do the players in    the theatre, I am no true man.',
          'BRUTUS    What said he when he came unto himself?',
          'CASCA    Marry, before he fell down, when he perceived the    common herd was glad he refused the crown, he    plucked me ope his doublet and offered them his    throat to cut. An I had been a man of any    occupation, if I would not have taken him at a word,    I would I might go to hell among the rogues. And so    he fell. When he came to himself again, he said,    If he had done or said any thing amiss, he desired    their worships to think it was his infirmity. Three    or four wenches, where I stood, cried Alas, good    soul!and forgave him with all their hearts: but',
          '    theres no heed to be taken of them; if Caesar had    stabbed their mothers, they would have done no less.    And after that, he came, thus sad, away?',
          'CASCA    Ay.',
          'CASSIUS    Did Cicero say any thing?',
          'CASCA    Ay, he spoke Greek.',
          'CASSIUS    To what effect?',
          'CASCA    Nay, an I tell you that, Ill neer look you i the    face again: but those that understood him smiled at    one another and shook their heads; but, for mine own    part, it was Greek to me. I could tell you more    news too: Marullus and Flavius, for pulling scarfs    off Caesars images, are put to silence. Fare you    well. There was more foolery yet, if I could    remember it.',
          'CASSIUS    Will you sup with me to-night, Casca?',
          'CASCA    No, I am promised forth.',
          'CASSIUS    Will you dine with me to-morrow?',
          'CASCA    Ay, if I be alive and your mind hold and your dinner    worth the eating.',
          'CASSIUS    Good: I will expect you.',
          'CASCA    Do so. Farewell, both.    Exit',
          'BRUTUS    What a blunt fellow is this grown to be!    He was quick mettle when he went to school.',
          'CASSIUS    So is he now in execution    Of any bold or noble enterprise,    However he puts on this tardy form.    This rudeness is a sauce to his good wit,    Which gives men stomach to digest his words    With better appetite.',
          'BRUTUS    And so it is. For this time I will leave you:    To-morrow, if you please to speak with me,    I will come home to you; or, if you will,    Come home to me, and I will wait for you.',
          'CASSIUS    I will do so: till then, think of the world.    Exit BRUTUS    Well, Brutus, thou art noble; yet, I see,    Thy honourable metal may be wrought    From that it is disposed: therefore it is meet    That noble minds keep ever with their likes;    For who so firm that cannot be seduced?    Caesar doth bear me hard; but he loves Brutus:    If I were Brutus now and he were Cassius,    He should not humour me. I will this night,    In several hands, in at his windows throw,    As if they came from several citizens,    Writings all tending to the great opinion    That Rome holds of his name; wherein obscurely    Caesars ambition shall be glanced at:    And after this let Caesar seat him sure;    For we will shake him, or worse days endure.    Exit']

#Storyline from http://www.geekpreneur.com/the-best-spam-messages-ever
time_travel = ['From: Frank Young <fyoung32@skynet.com>', 'Subject: Time travelers PLEASE HELP!!!!!!', 'Date: 28 Feb 2002 20:43:53 +0100', 'If you are a time traveler or alien disguised as human and or have the technology to travel physically through time I need your help!',
               'My life has been severely tampered with and cursed!!', 'I have suffered tremendously and am now dying!', 'I need to be able to:', 'Travel back in time.', 'Rewind my life including my age back to 4.', 'Be able to remember what I know now so that I can prevent my life from being tampered with again after I go back.',
               'I am in very great danger and need this immediately!', 'I am aware that there are many types of time travel, and that humans do not do well through certain types.', 'I need as close to temporal reversion as possible, as safely as possible. To be able to rewind the hands of time in such a way that the universe of now will cease to exist.',
               'I know that there are some very powerful people out there with alien or government equipment capable of doing just that.', 'If you can help me I will pay for your teleport or trip down here, Along with hotel stay, food and all expenses. I will pay top dollar for the equipment. Proof must be provided.',
               'Also if you are one of the very few beings with the ability to edit the universe PLEASE REPLY!!!', 'Only if you have this technology and can help me please send me a (SEPARATE) email to:', 'timetravalerswanted@aol.com', 'Please do not reply if your an evil alien!',
               'Thanks']

#CONFIG
base_url = 'http://games.espn.com/second-chance-bracket/2017/en/api/sendGroupEmail'
group_id = '6128'
timeout = 20
storyline = time_travel

#You'll need the espn_s2 and espnAuth keyvalues from your logged in cookie. Use fiddler to grab them. 
my_cookies =  {
"espn_s2": "", 
"espnAuth": ''
}

line_index = 0

s=requests.session()
s.verify=False
requests.utils.add_dict_to_cookiejar(s.cookies, my_cookies)

s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36','Content-Type':'application/x-www-form-urlencoded'})

def send_line(play_line):
    data='groupID=%s&comments=%s' % (group_id, play_line)
    r=s.post(base_url,data=data)
    j=json.loads(r.content)
    global line_index
    if j['s']:
        line_index += 1
        print("Success! Sent message at index ", line_index)
        if(line_index == len(storyline)):
            print("Sent all spam, shutting down...")
            quit()
    else:
        print("Failed with error: %s" % j['e'][0])
    

def main():
    while(1):
        sending_line = storyline[line_index]
        print("Sending line: ", sending_line)
        send_line(sending_line)
        time.sleep(timeout)
    
if __name__ == '__main__':
    main()
