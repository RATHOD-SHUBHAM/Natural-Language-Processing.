# -*- coding: utf-8 -*-
"""RuleBased-Spacy-V01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a-jvbk0UdhL21elDdDR-Ce4Tl4PRHp1s

# Phrase Matcher
"""

import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab,attr = "LOWER")

terms = ["Barack Obama", "Angela Merkel", "washington"]
# Only run nlp.make_doc to speed things up
patterns = [nlp.make_doc(text) for text in terms]
matcher.add("TerminologyList", patterns)

doc = nlp("German Chancellor Angela Merkel and US President Barack Obama "
          "converse in the Oval Office inside the White House in Washington, D.C.")
matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)

"""# Token Matcher"""

import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)


# Only run nlp.make_doc to speed things up
patterns = [
    [{'IS_DIGIT':True,}],
    [{'IS_DIGIT':True,},{"IS_PUNCT": True,'OP':'*'},{"LOWER": "barack"}, {"IS_PUNCT": True,'OP':'*'}, {"LOWER": "obama"}],
    [{'IS_DIGIT':True},{"IS_SPACE": True},{"IS_PUNCT": True},{"LOWER": "barack"}, {"IS_PUNCT": True,'OP':'*'}, {"LOWER": "obama"}]
    # [{"LOWER": "barack"}, {"LOWER": "obama"}]
]
matcher.add("HelloWorld", patterns)

doc = nlp("German Chancellor Angela Merkel and US President 1992 - Barack Obama "
          "1992 -"
          "BARACK-OBAMA converse in the Oval Office inside the White House in Washington, D.C.")
matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)

import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Add match ID "HelloWorld" with no callback and one pattern
# pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]
# matcher.add("HelloWorld", [pattern])

patterns = [
    [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}],
    [{"LOWER": "hello"}, {"LOWER": "world"}]
]
matcher.add("HelloWorld", patterns)

doc = nlp("Hello, world! Hello world!")
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # 'HelloWorld'
    span = doc[start:end]

