Created Date: 27 May 2019

# Question-Analysis

Based on the question, analyse what to reply back like: Person name, Location, date etc.

# To run the code:
run main.py

# Question Analysis
Question Analysis for Question Answering System.<br>
In a question answering system, it is important to know the type of question so as to get the answer. For example, "who is Pema?" we can obviously say that it's asking about a person. So how can we make the machine understand that too?
 
 
 As said in the paper <i>"Information Retrieval: Improving Question Answering Systems by Query Reformulation and Answer Validation" </i>by Mohammad Reza Kangavari, Samira Ghandchi, Manak Golpour[1], there are two important components which are the bases of the question processing. The first component is the question classification that specifies types of question and answer.
 
 ![alt text](https://cdn-images-1.medium.com/max/800/1*fADmgfyF8ar9Y5rdm6-g1g.png)<br>
Table 1 Classification of question and answer

Referring to the paper and also applying some other methods, what I did was firstly get NER using NLTK such as:

![alt text](https://cdn-images-1.medium.com/max/800/1*ulQKSrU8cPU_luD8we-9QA.png)<br>
Fig: question analysis using NLTK library

We can automatically tell that the question is about "PERSON". But if the question is "where should I come?" NLTK library returns null, for such cases,  I applied the rules from the paper. The output generated:

![alt text](https://cdn-images-1.medium.com/max/800/1*Cv1wGEcQhGjRupdzXeJnDg.png)<br>
Fig: question analysis referring to the paper


Referrence:
[1] http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.193.1603&rep=rep1&type=pdf
