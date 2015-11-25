import requests
import json
import random

url = "https://hooks.slack.com/services/your/api/endpoint"

messages = [
	"I put a 100,000 pictures of my ass on the internet so the NSA could spy on it",
	":wave: HIT IT WITH THE LEFT :wave:",
	":birthday: It's Lee's birthday so do one handed pushups :birthday:",
	":muscle: :muscle: P U S H U P B O Y S :muscle: :muscle:",
	":ghost: I'm just here for the boos :ghost:",
	":spaghetti: I am Gino Musclerino, you are doing my clients pushups please no pasterino :spaghetti:",
	":dansgame: :dansgame: :dansgame: :dansgame: :dansgame: :dansgame: :dansgame: :dansgame: :dansgame: :dansgame: :dansgame:",
	":grimacing: WHY DID NO ONE TELL ME IT WAS RICH'S BIRTHDAY :grimacing:",
	"Suns out buns out :hamburger:",
	"Yo momma so good at pushups they renamed them yomommaups",
	":sparrow: Meek Mill said on twitter that Nas ghostwrote your pushups :sparrow:",
	":pig: :pig: GO HAM :pig: :pig:",
	":tng: :tng: Push or push not, there is no try :tng: :tng:",
	":muscle: :muscle: P U S H U P B O Y S A N D G I R L S :muscle: :muscle:",
	"time for pushups",	
	":bomb: Dr. Balanced recommends a minimum of seven pushups an hour :bomb:",
	"last name boys / first name pushups / like a dictionary I got all the lookups",
	":2chainz: I had a dreeeeeam / pushups didn't work / woke up on the rug / had to hit it with the planks :2chainz:",
	":ramen: Mr. Noodlearms please report to the pushup area :ramen:",
	":thugger: Put my biceps in your cup / they might not melt / oh my push brah :thugger:",
	"GET P NINETY EXED",
	":computer: ...he'll try to persuade me to squash it / I'll say nah, he forgot what a hardcore programmer is / a hardcore programmer is a dangerous man / such as myself / trained to do twenty pushups in soft carpet :computer:",
	":fire: :boom: COP THE ALBUM #PUSHUPBOYS OUT TOMORROW 100% FIRE 200% PLANKS :boom: :fire:",
	"I heard that Torri can lift a tank above her head",
	"I head that Tom can't lift a toy tank abouve his head",
	"I'm the neighborhood Pusha / call me subwoofer / cuz I pump arms like that / jack", 
	"From pushup to pushup / plank to plank",
	"I put numbers on the (white) boards",
	":100: Do 12 pushups :100:",
	"I might do :100: pushups on my birthday / 30 years of doing reps like it's workout day",
	"I'm pretty much just a Pusha T quote bot now",
	"Yung Tookie is always late",
	":star: Check out my Spark video it's just Tookie being late for pushup time :star:",
	":2chainz: Bought a new crib just to pushup in / I've been doing planks where the rep you been? :2chainz:", 
	"Some people call me the space cowboy / some people call me the gangster of hugs",
	":triangular_ruler: it's the roc :triangular_ruler: ",
	":chart_with_downwards_trend: super-push-ups / planka-genesis / when I was dead weak / I couldn't picture this :chart_with_upwards_trend:",
	":spaghetti: :spaghetti: :spaghetti: mom's :spaghetti: :spaghetti: :spaghetti:",
	":kappa: I'm sorry Tookie it was only because you were in the hot seat :kappa:",
	"There's a horse in the hospital",
	"re-frag your hard drive",
	"http://bfy.tw/14VG",
	":meat_on_bone: Drake and Meek Mill both can't pushup for shit :meat_on_bone:", 
	"http://bfy.tw/15Js",
	"Meek Mill rap like he on his fifteenth pushup",
	":trophy: Yo momma so good at pushups she got the town record. The mayor even gave her a trophy! It was at the carnival and everyone saw! :trophy:",
	"What if Homer Simpson did pushups? It's not that hard to imagine",
	":chocolate_bar: :candy: M&M's are the Budweiser of candy :candy: :chocolate_bar:",
	":chocolate_bar: :candy: M&M's and Budweiser are products of the oppressive capitalist system :candy: :chocolate_bar:",
	":japanese_ogre: pushup god demands a sacrifice :japanese_ogre:",
]

message = random.choice(messages)

avatars = [
	":arnold:",
	":candlejack:",
	":drboom:",
	":failfish:",
	":kappa:",
	":thugger:",
	":dropmicani:",
	":octopus:",
	":muscle:",
	":mega:",
	":nut_and_bolt:",
	":syringe:",
	":pill:",
	":santa:",
	":japanese_ogre:",
	":japanese_goblin:",
	":skull:",
]

avatar = random.choice(avatars)

payload = {
	"channel":"#pushupboys",
	"username":"pushupbots",
	"text":message,
	"icon_emoji":avatar,
}

a = requests.post(url, data=json.dumps(payload), verify=True)
