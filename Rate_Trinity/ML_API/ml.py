from hatesonar import Sonar
import json
class MessageScreenerResult :
    result = False
    hate = 0
    offence =0
    tips = ""

    def __init__(self,result, hate, offence,tips):
        self.result = result
        self.hate = hate
        self.offence = offence
        self.tips = tips

    def getHate(self) :
        return self.hate

    def getTips(self) :
        return self.tips

    def getOffence(self) :
        return self.offence

    def getResult(self) :
        return self.result


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
    #print("Hate ",hateConfidence, " || offenseConfidence ",offenseConfidence," || neither ",neitherConfidence)

    rez = False
    if neitherConfidence > 0.7:
        rez = False

    if hateConfidence > 0.6 :
        rez = True

    if offenseConfidence >0.55 :
        rez = True

    return MessageScreenerResult(rez,hateConfidence,offenseConfidence,"No Tips, Sorry!")

if __name__ == "__main__":
    #assert (isAbusiveComment("WHAT A PRICK").getResult()) == True
    assert (isAbusiveComment("cunt").getResult()) == True
    assert (isAbusiveComment("fuck you").getResult()) == True
    assert (isAbusiveComment("im going to kill you").getResult()) == True
    assert (isAbusiveComment("I dont like this module").getResult()) == False
    assert (isAbusiveComment("this module is bad").getResult()) == False
    assert (isAbusiveComment("i really dislike this module").getResult()) == False
    assert (isAbusiveComment("i like this module").getResult()) == False
    print('*** All tests passed ***')
