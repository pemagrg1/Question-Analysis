import nltk
from nltk.tree import Tree
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
stem = ps.stem
grammar = "NE:{<NN.*><.*><NN.*>| <NN.*><VB.*>}"
chunk_parser=nltk.RegexpParser(grammar)

#------------------QUESTION CLASSIFICATION--------

def getphrase(text):
    q1_tokens = nltk.word_tokenize(text)
    q1_pos = nltk.pos_tag(q1_tokens)
    grammar = "NE:{<NN.*><.*><VBG>|<VB.*><.*><RP.*>|<NN.*><.*><NN.*>}"
    chunk_parser = nltk.RegexpParser(grammar)
    chunk_tree = chunk_parser.parse(q1_pos)

    phrase_list = []
    for subtree in chunk_tree.subtrees(filter=lambda t: t.label() == 'NE'):
        w = (subtree.leaves())
        for a, b in w:
            phrase_list.append(a)
    phrase = " ".join(phrase_list)
    return (phrase)


def getContinuousChunk(text):
    chunks = []
    answerToken = nltk.word_tokenize(text)
    nc = nltk.pos_tag(answerToken)

    prevPos = nc[0][1]
    entity = {"pos": prevPos, "chunk": []}
    for c_node in nc:
        (token, pos) = c_node
        if pos == prevPos:
            prevPos = pos
            entity["chunk"].append(token)
        elif prevPos in ["DT", "JJ"]:
            prevPos = pos
            entity["pos"] = pos
            entity["chunk"].append(token)
        else:
            if not len(entity["chunk"]) == 0:
                chunks.append((entity["pos"], " ".join(entity["chunk"])))
                entity = {"pos": pos, "chunk": [token]}
                prevPos = pos
    if not len(entity["chunk"]) == 0:
        chunks.append((entity["pos"], " ".join(entity["chunk"])))
    return chunks

def getNamedEntity(answers):
    chunks = []
    for answer in answers:
        answerToken = nltk.word_tokenize(answer)
        nc = nltk.ne_chunk(nltk.pos_tag(answerToken))
        entity = {"label":None,"chunk":[]}
        for c_node in nc:
            if(type(c_node) == Tree):
                if(entity["label"] == None):
                    entity["label"] = c_node.label()
                entity["chunk"].extend([ token for (token,pos) in c_node.leaves()])
            else:
                (token,pos) = c_node
                if pos == "NNP":
                    entity["chunk"].append(token)
                else:
                    if not len(entity["chunk"]) == 0:
                        chunks.append((entity["label"]," ".join(entity["chunk"])))
                        entity = {"label":None,"chunk":[]}
        if not len(entity["chunk"]) == 0:
            chunks.append((entity["label"]," ".join(entity["chunk"])))
    if len(chunks) == 0:
        answerToken = nltk.word_tokenize(answers)
        nc = nltk.ne_chunk(nltk.pos_tag(answerToken))
        for word,pos in nc:
            if pos == "NNP" or pos == "NN" or pos == "VB":
                chunks.append(word)
    return chunks
