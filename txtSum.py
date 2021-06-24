from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
# input text, I put the 'BASIC' portion of Microsoft history from Bill Gates Wiki page...
text = "Gates read the January 1975 issue of Popular Electronics which demonstrated the Altair 8800, and he contacted Micro Instrumentation and Telemetry Systems (MITS) to inform them that he and others were working on a BASIC interpreter for the platform. In reality, Gates and Allen did not have an Altair and had not written code for it; they merely wanted to gauge MITS's interest. MITS president Ed Roberts agreed to meet them for a demonstration, and over the course of a few weeks they developed an Altair emulator that ran on a minicomputer, and then the BASIC interpreter. The demonstration was held at MITS's offices in Albuquerque, New Mexico; it was a success and resulted in a deal with MITS to distribute the interpreter as Altair BASIC. MITS hired Allen, and Gates took a leave of absence from Harvard to work with him at MITS in November 1975. Allen named their partnership Micro-Soft, a combination of microcomputer and software, and their first office was in Albuquerque. The first employee Gates and Allen hired was their high school collaborator Ric Weiland. They dropped the hyphen within a year and officially registered the trade name Microsoft with the Secretary of the State of New Mexico on November 26, 1976. Gates never returned to Harvard to complete his studies. Microsofts Altair BASIC was popular with computer hobbyists, but Gates discovered that a pre-market copy had leaked out and was being widely copied and distributed. In February 1976, he wrote an Open Letter to Hobbyists in the MITS newsletter in which he asserted that more than 90% of the users of Microsoft Altair BASIC had not paid Microsoft for it and the Altair hobby market was in danger of eliminating the incentive for any professional developers to produce, distribute, and maintain high-quality software.This letter was unpopular with many computer hobbyists, but Gates persisted in his belief that software developers should be able to demand payment. Microsoft became independent of MITS in late 1976, and it continued to develop programming language software for various systems. The company moved from Albuquerque to Bellevue, Washington on January 1, 1979. Gates said he personally reviewed and often rewrote every line of code that the company produced in its first five years. As the company grew, he transitioned into a manager role, then an executive. DONKEY.BAS, is a computer game written in 1981 and included with early versions of the PC DOS operating system distributed with the original IBM PC. It is a driving game in which the player must avoid hitting donkeys. The game was written by Gates and Neil Konzen."

# python dict. to keep a record of how many times a word appears.
stopWordz = set(stopwords.words("english"))
words = word_tokenize(text)
# create a feq table
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWordz:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# assign score to each sentence depending on the words it contains
# sent_tokenize() method will ceate an array of sentence.
sentences = sent_tokenize(text)
sentenceValue = dict()
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq


# assign a certain score to compare sentences within the feedback
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
# avg value of a sentence from og text
avg = int(sumValues / len(sentenceValue))

# sentences stored in summary.
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * avg)):
        summary += " " + sentence
print(summary)
