from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob, Word
import random
import time

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse',methods = ['POST'])
def analyse():
    # start the system timer
    start = time.time()
    if request.method == 'POST':
        # take raw text from html form
        rawtext = request.form['rawtext']
        print("the raw text is : ",rawtext)
        # convert raw text into blob format
        blob = TextBlob(rawtext)
        print("the blob is: ",blob)
        # make a copy of blob text
        received_text = blob
        # calculate sentiment and sensitivity
        blob_sentiment , blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
        number_of_token = len(list(blob.words))
        print("the blob tag is: ",blob.tags)

        nouns = list()
        for word,tag in blob.tags:
            # check if the tag is a Noun
            if tag =='NN':
                nouns.append(word.lemmatize)
                print("the nouns are: ",nouns)
                # count the number of nouns
                len_of_words = len(nouns)
                # random words: genrate random mnumber form list with len of noun
                rand_words = random.sample(nouns,len_of_words)
                print("the random words generated are",rand_words)

                final_words = list()
                for items in rand_words:
                    word = word(items).pluralize()
                    print("the words are: ",word)
                    final_words.append(word)
                    print("the final words are: ",final_words)
                    summary = final_words
                    end = time.time()
                    total_time = end - start

    return render_template('index.html',received_text = received_text, number_of_token = number_of_token,
                           blob_sentiment = blob_sentiment, blob_subjectivity = blob_subjectivity,
                           summary = summary , final_time = total_time)

if __name__ == '__main__':
    app.run(debug = True)


