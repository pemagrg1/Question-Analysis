import nltk
from modules.info_extraction import getContinuousChunk

def determineAnswerType(text):
    word = nltk.word_tokenize(text)
    pos_tag = nltk.pos_tag(word)
    chunk = nltk.ne_chunk(pos_tag)
    ne_list = []
    for ele in chunk:
        if isinstance(ele, nltk.Tree):
            ne_list.append(ele.label())
    if len(ne_list)>1:
        return ne_list
    else:
        questionTaggers = ['WP', 'WDT', 'WP$', 'WRB', 'VBZ']

        qPOS = nltk.pos_tag(nltk.word_tokenize(text))
        qTag = None

        for token in qPOS:
            if token[1] in questionTaggers:
                qTag = token[0].lower()
                break

        if qTag == None:
            if len(qPOS) > 1:
                if qPOS[0][0].lower() in ['is', 'are', 'can', 'should','will']:
                    qTag = "YESNO"
                    return "YESNO"

        if qTag != "YESNO":
            # who/where/what/why/when/is/are/can/should
            if qTag == "who":
                return "PERSON"
            elif qTag == "where":
                return "LOCATION"
            elif qTag == "when":
                return "DATE"
            elif qTag == "which":
                if len(qPOS) > 1:
                    t2 = qPOS[1]
                    if t2[0].lower() in ["year", "day", "date", "week", "month"]:
                        return "DATE"
                    elif t2[0].lower() in ["city", "state", "country"]:
                        return "LOCATION"
                    elif t2[0].lower() in ["person", "man", "women", "uncle", "aunt", "male", "female"]:
                        return "PERSON"
            elif qTag == "what":
                qTok = getContinuousChunk(text)
                '''if len(qTok) > 1:
                    if qTok[1][1] in ['is', 'are', 'was', 'were'] and qTok[2][0] in ["NN", "NNS", "NNP", "NNPS"]:
                        text = " ".join([qTok[0][1], qTok[2][1], qTok[1][1]])
                        print("DEFINITION")'''
                for token in qPOS:
                    if token[0].lower() in ["city", "place", "country", "capital", "state", "location", "area","route"]:
                        return "LOCATION"
                    elif token[0].lower() in ["company", "industry", "organization"]:
                        return "ORGANIZATION"
                    elif token[0].lower() in ["cost", "area", "number"]:
                        return "NUMBER"
            elif qTag == "how":
                t2 = qPOS[1]
                if t2[0].lower() in ["few", "great", "little", "many", "much"]:
                    return "QUANTITY"
                elif t2[0].lower() in ["tall", "wide", "big", "far"]:
                    return "LINEAR_MEASURE"
                return "1FULL"
            else:
                return "FULL"