import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
import string


# todo 1 :  setting the maximun number of columns

pd.set_option("display.max_columns",100)
#  pd.get_option("display.max_columns")exit()

# todo 2 : remove stop words !!
stopwords = stopwords.words('english')
ps = nltk.PorterStemmer()


# todo 3 : read the file content into data variable and give it a heading
data = pd.read_csv("sms.tsv",sep='\t',header=None)
data.columns = ['label','body']
# print(data)

# todo 4 : clean the text
# todo : remove punctuation, tokenize, stopword and stem
def clean_text(text):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('W+',text)
    text = [ps.stem(word) for word in tokens if word not in stopwords]
    return text


# todo 5 : perform count vectorization
# Vector :  convert data into a binary form
# Encode Text Data for Machine Learning with scikit-learn
from sklearn.feature_extraction.text import CountVectorizer
# create the transform
count_vectorizer = CountVectorizer(analyzer = clean_text)
# tokenize and build vocab
x_count = count_vectorizer.fit_transform(data['body'])

# todo : print no of text data as rows and no of words in vocab as column
# print(x_count.shape)
# print(count_vectorizer.get_feature_names())
# print(x_count)


# todo 6 : seperating dependent and independent variable
x = x_count.toarray()
y = data.iloc[:,0].values  # first column of data frame (values)
# print(y)

# todo 7 : encoding dependant variable
from sklearn.preprocessing import LabelEncoder
# to deal with categorical data we have to convert it into number
labelencoder_y = LabelEncoder()
# covert first column into integer values
y = labelencoder_y.fit_transform(y)
# print(y)



# todo 8 : splitting the dataset
# splitting the data set into train and test set

# x = feature
# y = dependent variable or outccome
# test_size = 20% of data is used for testing
# random state = take same row each time for training and testing


from sklearn.model_selection import train_test_split
x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=0)


# todo : 9  using Naive Bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train,y_train)

# todo : 10 predicting the result
y_pred = classifier.predict(x_test)

# todo 11 : confusuion matrix
from sklearn.metrics import confusion_matrix
result = confusion_matrix(y_test,y_pred)
# the primary diagonal op are the correct ones
# print(result)

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
print('Accuracy Score :',accuracy_score(y_test,y_pred))
print('Report : ')
print(classification_report(y_test,y_pred))



