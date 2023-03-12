nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
sentences="""Machine learning (ML) is a field of inquiry devoted to understanding and building methods that "learn" – that is, methods that leverage data to improve performance on some set of tasks.[1] It is seen as a part of artificial intelligence.Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so.[2] Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, agriculture, and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks.[3][4] A subset of machine learning is closely related to computational statistics, which focuses on making predictions using computers, but not all machine learning is statistical learning. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a related field of study, focusing on exploratory data analysis through unsupervised learning.[6][7]Some implementations of machine learning use data and neural networks in a way that mimics the working ."""


import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 
ps=PorterStemmer()
lemma=WordNetLemmatizer()
sent_lst=nltk.sent_tokenize(sentences)
stop_words= stopwords.words('english')
corpus=[]
for i in range(len(sent_lst)):
    tokens= nltk.word_tokenize(re.sub('[^a-zA-Z0-9]',' ',sent_lst[i])) 
    tokens=[lemma.lemmatize(token.lower()) for token in tokens if not tokens in stop_words]
    corpus.append(tokens)




print(corpus)
