
from hatesonar import Sonar
import json



def isAbusiveComment(x):
    sonar = Sonar()
    a = sonar.ping(text=x)
    #print(x)
    #print(a)

    hateConfidence = 0.0
    offenseConfidence = 0.0
    neitherConfidence = 0.0


    for result in a['classes'] :
        #print(result)
        #print(result['confidence'])
        #print(result["class_name"])
        if result["class_name"] == "hate_speech" :
            hateConfidence = result['confidence']
        if result["class_name"] == "offensive_language" :
            offenseConfidence = result['confidence']
        if result["class_name"] == "neither" :
            neitherConfidence = result['confidence']

    if neitherConfidence > 0.7:
        return False

    if hateConfidence > 0.4 and offenseConfidence >0.4 :
        return True

    if hateConfidence > 0.6 and offenseConfidence >0.3 :
        return True

    if hateConfidence > 0.7 :
        return True

    if offenseConfidence >0.6 :
        return True

    return False
    #print("Hate ",hateConfidence, " || offenseConfidence ",offenseConfidence," || neither ",neitherConfidence)

print(isAbusiveComment("hey"))
