# Topic Modeling - Natural Language Processing(NLP).

I recently began learning about Latent Dirichlet Allocation (LDA) for topic modeling and was astounded by how effective it can be while yet being simple to use.
Introduction
Text analytics is all about extracting high-quality information from data. 
It's tough to find relevant and desired information in today's world, since the majority of data is "unstructured".

However, with technological advancements, data can be retrieved.
Text mining is an artificial intelligence (AI) technology that uses natural language processing (NLP) to transform the free (unstructured) text in documents and databases into normalized, structured data suitable for analysis or to drive machine learning (ML) algorithms.

# What is Text Mining?
The technique of reviewing vast collections of documents in order to find new information or answer is known as text mining.

Text mining uncovers facts, connections, and statements that would otherwise be lost in a sea of textual large data. After being extracted, the data is turned into a structured format that can be further examined or displayed in a variety of ways. To process the text, text mining uses a range of approaches, one of the most essential of which being "Natural Language Processing (NLP)".

# What is Natural Language Processing (NLP)?
NLP is an important component in a wide range of software applications that we use
in our daily lives.
Natural Language Processing or NLP is a field of Artificial Intelligence that gives the machines the ability to read, understand and derive meaning from human languages.

# NLP Tasks
These are some of the fundamental tasks that appear frequently across  NLP.

1. Language modeling
This is the task of predicting what the next word in a sentence will be based on
the history of previous words. 

2. Text classification
This is the task of bucketing the text into a known set of categories based on its
content. 

3. Information extraction
As the name indicates, this is the task of extracting relevant information from
text, such as calendar events from emails or the names of people mentioned in a
social media post.

4. Information retrieval
This is the task of finding documents relevant to a user query from a large collec‐
tion. 

5. Conversational agent
This is the task of building dialogue systems that can converse in human lan‐
guages. Alexa, Siri, etc., are some common applications of this task.

6. Text summarization
This task aims to create short summaries of longer documents while retaining the
core content and preserving the overall meaning of the text.

7. Question answering
This is the task of building a system that can automatically answer questions
posed in natural language.

8. Machine translation
This is the task of converting a piece of text from one language to another. Tools
like Google Translate are common applications of this task.

9. Topic modeling
This is the task of uncovering the topical structure of a large collection of docu‐
ments. Topic modeling is a common text-mining tool.


# What is unsupervised learning?
Unsupervised learning, also known as unsupervised machine learning, analyzes and clusters "unlabeled datasets" using machine learning techniques. Without the need for human intervention, these algorithms uncover hidden patterns or data groupings.

# Topic modeling
A topic model is a form of statistical model used in machine learning and natural language processing to find abstract "topics" that appear in a collection of documents.
Topic Modeling is an unsupervised learning method for clustering documents and identifying topics based on their contents. It works in the same way as the K-Means algorithm and Expectation-Maximization. We will have to evaluate individual words in each document to uncover topics and assign values to each depending on the distribution of these terms because we are clustering texts.
Latent Dirichlet Allocation is one of the approaches to topic modeling.
Latent Dirichlet Allocation (LDA) is used to classify text in a document to a certain topic. It creates a Dirichlet distribution-based on topic per document and word per topic model.

Latent Dirichlet Allocation (LDA):
The Latent Dirichlet Allocation (LDA) is a generative statistical model used in natural language processing that allows sets of observations to be explained by unobserved groups that explain why some sections of the data are similar.
LDA, or Latent Derelicht Analysis, is a probabilistic model that employs two probability values to determine cluster assignments: P(words | topics) and P(topics|documents). To determine their topic assignment, these values are generated based on an initial random assignment, then repeated for each word in each document. These probabilities are calculated several times in an iterative method until the algorithm converges.

# How does LDA Work?
1) LDA assigns words at random to k topic for each document, where k is the number of pre-defined topics.
2) LDA computes for each document 'd' and each word 'w' in the text.
a. P(topic(t) | document(d)): Proportion of words allocated to subject t in document d.
b. P(word(w) | topic(t)): Proportion of topic t assignment over all documents derived from w.
3) Given all of the other words and their topic assignments, reassign topic t to word w with probability p.
4) Iterate multiple times until the topic assignment remains the same.

# Example:
Lets say i have 5 document:

Document 1 : I like mongo and apple.
Document 2 : Crab and fish live in water.
Document 3 : Puppies and kittens are fluffy.
Document 4 : I had spinach and berry smoothie.
Document 5 : My pup loves mango.

So if i take this corpus and apply LDA on it. As a example, model might output something like this.

Then i would get this as output:
Document 1 : 100% Topic A.

Document 2 : 100% Topic B.

Document 3 : 100% Topic B.

Document 4 : 100% Topic A.

Document 5 : 60% Topic A, 40% Topic B.

Now if a take a look at topic in detail, we can say that
Topic A: 40% apple, 20% mango, 10% breakfast..
Topic B: 60% pup, 40% kitten, 30% dog, 15% cute..

Now that we know what our topic is about we can know that
Document 1 is talking about Food.

Document 2 is talking about Animals.

Document 3 is talking about Animals.

Document 4 is talking about Food.

Document 5 is talking about Food + Animals.

# Topic Modelling Using LDA in Python:
Task: 
Given the abstract and title for a set of research articles, predict the topics for each article included in the test set.

The Data:
I have used Kaggle Topic Modeling for Research Articles data set.

Data Pre-processing:

    * Check for missing values.
    
    * Toeknization: Split the text into sentences and the sentences into words. Convert the upper case into lower case and remove the punctuations.
    
    * Remove stop Words.
    
    * Lemmatizing: Words are transformed to original form.
    
Word Vectorizer:

    * Count Vectorizer.
    
    * TF - IDF.
    
Running LDA using TF-IDF.

Performance Evaluation.

Testing Model on unseen document.

# Check out my [article](https://www.linkedin.com/pulse/introduction-topic-modeling-latent-dirichlet-lda-natural-shankar/) for detailed explanation.
