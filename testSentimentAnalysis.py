from SentimentAnalysis import load_models, get_sentiments
from sklearn.metrics import confusion_matrix, classification_report

sentences = [
    'we lost ๐ ๐ ๐ <img>https://media.giphy.com/media/2rtQMJvhzOnRe/giphy.gif</img>',
    'wow you are so funny ๐ฎ <img>https://media.giphy.com/media/13mPGyNp9otvyg/giphy.gif</img>',
    'you suck ๐',
    'hell yeah <img>https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif</img>',
    '<img>https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif</img>',
    '<img>https://media.giphy.com/media/l1KVaj5UcbHwrBMqI/giphy.gif</img>',
    '<img>https://media1.giphy.com/media/a9xhxAxaqOfQs/giphy.gif</img>',
]

# obtained from https://www.kaggle.com/rexhaif/emojifydata-en
evaluation = {
    "I get in my moods where I donโt be wanting to talk and thatโs when everybody got a question ๐ค": 0,
    "THANKS GOD FOR WAKING ME UP TODAY. ๐๐": 1,
    "i love this sweatshirt so much :,) ๐ค๐๐๐งก": 1,
    "Itโs Official This Weekend Iโm Going To Knoxville Tennessee !!! ๐ง๐ฝโโ๏ธ": 1,
    "3/4 of the team is ๐": 0,
    "literally ovr math ๐": 0,
    "OH MYY GOSHHH๐ฉ๐๐๐": 1,
    "Nice to meet you, Jimu! ๐ Yay I really looking forward for your next concert experience ๐๐ Have fun! ๐๐": 1,
    "I can't stand it's not that funny kind of people, like okay I'm sorry with your amargada no sense of humor having ass ๐": 0,
    "Cavs look terrible Lebron ainโt making it out the first round with these niggas๐คฆ๐ฟโโ๏ธ": 0,
    "It was funny when we were like 12๐ญ": 0,
    "Thatโs your headline? ๐How about crazed man throws car in reverse &amp; hits patrol car. Assault on officersโฆ": 0,
    "I thought it looked familiar ๐": 1,
    "BEAUTIFUL ๐๐ congratulations!!": 1,
    "This episode ๐ฅ": 1,
    "can school be done already?๐": 0,
    "God has brought me such a loooong way and heโs nowhere near done โค๏ธ thank you Lord!!": 1,
    "Okaaaay. I donโt mean to be head ass but I mean to be head ass. ๐คง๐๐ and thank you bb ๐": 1,
    "EPIC. You actually look really pretty w/the hairstyle &amp; earrings ๐ฉ๐   Twinning ๐๐ฝ๐๐ฝ": 1,
    "I donโt care who drops what or when! Weโre climbing the chart or weโre going down swinging HARD! ๐๐ฅ๐ค๐ฝ": 1,
    "You remind me of a cupcake. Cute and sweet. ๐๐ with an adorably fitting gif to go with it ๐๐": 1,
    "I took an amazing nap ๐ค": 1,
    "Yes I luv u too ๐": 1,
    "Happiest birthday, ! God bless you always! ๐๐  CTTO": 1,
    "Wow RIP ๐ฅ": 0,
    "I should be packing for my house sitting job.....but I donโt want tooooo. ๐ฉ": 0,
    "Theyโre signed to the same label &amp; both have ghost writers. ๐คท๐พโโ๏ธ": 0,
    "THIS IS GOLD ๐๐๐": 1,
    "New blessings are coming your way ๐": 1,
    "I want a nigga geeked about me.๐๐๐๐๐คช": 1,
    "Finding both love and friendship in the same person &gt;&gt;&gt; ๐๐ญ": 1,
    "Right!! Cuz everyone knows he got those medals at the Dollar Store! ๐": 0,
    "Damn coach popโs wife died ๐ญ๐คง I couldnโt imagine whatโs heโs feeling rn": 0,
    "HELLL YESSS QUEEN๐๐": 1,
    "I've felt this kinda pain before...๐ญ๐๐": 0,
    "๐ข rt if you cried.": 0,
    "I just love her ๐โค๏ธ": 1,
    "Chaela just told me i canโt wear a sweat suit to her baby shower ๐๐ ok": 0,
    "Coolโฅ": 1,
    "i just ๐ช": 0,
    "Could watch still game aww day, unreal๐": 1,
    "Thank you for putting me on your Insta Story!!  ๐๐๐": 1,
    "American๐บ๐ธ guys hate my face": 0,
    "Stop recycling old skins pls ๐๐ฝ": 0,
    "๐คฆโโ๏ธ....๐คซ Says the guy who delayed our first fight by 5 months because of injury. ๐๐คทโโ๏ธ": 0,
    "Happy 28th birthday to you, ๐": 1,
    "YALL WRONG FOR THIS ๐๐": 1,
    "Dude ๐๐๐": 1,
    "My dainty friends don't like beef ๐คฆ๐ฟโโ๏ธ๐คฆ๐ฟโโ๏ธ": 0,
    "Is it men that are trash or is it your perception of men that is trash? ๐ค": 0,
    "Love Tennessee โฅ๏ธ": 1,
    "Thanks same to you ๐ท":
        1,
    "Y'all be so consumed in everyone else's business, but y'all forget to tend to your own. That shit baffles me. ๐คฆ๐ฝโโ๏ธ๐ญ": 0,
    "My favorite person everโค๏ธ": 1,
    "LMFAOOO YOOO IT ALL MAKES SENSE NOW๐ญ๐ญ๐ญ": 0,
    "I made it to my interview 7 minutes early. I'm proud of myself ๐ค": 1,
    "I still respect your opinion ๐": 1,
    "When women support other women, incredible things happen๐๐": 1,
    "Iโm always here for you too!!!!! Ilysmm! ๐โบ๏ธ๐": 1,
    "they're at a .30 ๐": 0,
    "Oh my word this gauche wee turd ๐": 0,
    "Life is amazing when you're surrounded by good people and positive vibes โบ๐ด": 1,
    "Stop it ๐": 1,
    "He should leave USA ๐บ๐ธ stupid unprofessional bonehead!": 0,
    "Yea this how I know Iโm grown now ... too much sweets like this makes my stomach hurt just watching it ๐คข โฆ": 0,
    "The more immoral Trump becomes, the more white Evangelicals approve. Hmmm ๐ค": 0,
    "Need everyone to be on this level when they see me ๐โค๏ธ": 1,
    "Amazing picture ๐": 1,
    "She good. She donโt need no help โ๐พ": 1,
    "Still can't get enough of his accent at 9:30 ๐": 1,
    "The fact that this was a true story was sad af.๐ข": 0,
    "Sheโs So Adorable ใ?ใ?ใ?ใ?โจ": 1,
    "This shit too clean ๐ฉ": 1,
    "ION WANNA SEE NONE OF YALL TWEET HIS LYRICS WHEN YALL WAS CALLIN HIM TRASH FOR YEARS ๐?๐?๐?๐?": 0,
    "Hey, guess who officially a Flight Attendant ๐๐พ": 1,
    "๐ค...and I know without a shadow of a fuxking doubt,you always meant so well...๐ค Presbyteria ๐ญ๐ญ๐ญ": 1,
    "OMG! We LOVE your Memes. ๐๐๐๐๐๐ $OOT $KMD": 1,
    "Got a KFC and Iโve actually not been this full in such a long time ๐๐๐คค๐คค": 1,
    "Feel like dude treats all his hoes like princesses. Then thereโs me, the queen, treated like a side piece ๐": 0,
    "I got the job ๐": 1,
    "Very sad to hear about  RIP ๐ข": 0,
    "I definitely learnt my lesson on that one ๐ฉ๐คฌ": 0,
    "That looks ugly and sooooo not very tasty ๐ฑ๐ฑ๐ฑ": 0,
    "๐ foo Ian made not one joke today you jus be trippin": 0,
    "Social media is so bad for the mind n soul. Seriously thinking about deleting it๐ด๐๐ฝ": 0,
    "Bitch slapped the blunt out of my mouth, She done fucked up Iโm cooking her ass tonight ๐ค๐": 0,
    "This just adds fuel to the โ niggas ainโt shit โ saying ๐คฆ๐ฝโโ๏ธ": 0,
    "I go back to work tonight and I dread it so much. ๐": 0,
    "Itโs because we are counting down until graduation๐ญ itโs torture": 0,
    "gotta love an infected piercing ๐ค.": 0,
    "Mentally exhausted ๐ค": 0,
    "I am SO scared of birds๐คง": 0,
    "i got you bbyโค๏ธ๐": 1,
    "Denzel is the Goat for this๐๐": 1,
    "Iโm going to hell and Rosas following ๐๐": 0,
    "Studying Midwifery๐ฃ๐": 0,
    "i love it when it rain outside ๐ค": 0,
    "wow you are so amazing lol ๐คฌ": 0,
    "wow that move was ๐ฉ": 0,
    "that is disgusting ๐คฎ": 0
}


def test_model():
    """
    Print predictions for test media containing emojis, text and images
    :return: none
    """
    image_model, text_model_ensemble = load_models()
    sentiments = get_sentiments(sentences, image_model, text_model_ensemble)
    for i in range(len(sentences)):
        print(sentences[i], " | ", sentiments[i])


def evaluate_model():
    """
    Evaluate model performance on emoji and text combinations from Twitter
    :return:
    """
    image_model, text_model_ensemble = load_models()
    sentiments = get_sentiments(evaluation, image_model, text_model_ensemble)

    predicted = []
    actual = []

    for k, v in evaluation.items():
        actual.append(v)

    for sentiment in sentiments:
        if sentiment > 0:
            predicted.append(1)
        elif sentiment < 0:
            predicted.append(0)

    confusion_matrix(actual, predicted)
    print("\n", "Confusion Matrix: \n", confusion_matrix(actual, predicted))
    print("\n", "Classification Report: \n", classification_report(actual, predicted))


test_model()
