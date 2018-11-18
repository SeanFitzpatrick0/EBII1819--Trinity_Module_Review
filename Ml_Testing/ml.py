
from hatesonar import Sonar
import json

sonar = Sonar()
a = sonar.ping(text="I hate this module, lecturer is crap and a real prick")

#obj = json.loads(a)
print(a)


hateSpeech = 1.0
offensiveLanguage =0.0

problimit = 0.6

if hateSpeech > problimit or offensiveLanguage >problimit :
    print("limit exceeded - do not post")
