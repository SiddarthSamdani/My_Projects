import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

import nltk
nltk.download('movie_reviews')

def extract_features(word_list):
    return  dict([(word, True) for word in word_list])

if __name__ == '__main__':
    # Load positive and negative reviews
    positive_fields = movie_reviews.fileids('pos')
    negative_fields = movie_reviews.fileids('neg')

features_positive = [(extract_features(movie_reviews.words(fileids = [f])), 'Positive') for f in positive_fileids]
features_negative = [(extract_features(movie_reviews.words(fileids = [f])), 'Negative') for f in negative_fileids]

# Split the data into train and test (80/20)
threshold_factor = 0.8
threshold_positive = int(threshold_factor * len(features_positive))
threshold_negative = int(threshold_factor * len(features_negative))

features_train = features_positive[:threshold_positive] + features_negative[:threshold_negative]
features_test = features_positive[threshold_positive:] + features_negative[threshold_negative:]
print("\n Number of training datapoints:", len(features_train))
print("Number of test datapoints:", len(features_test))

# Train a Naive Bayes Classifier
Classifier = NaiveBayesClassifier.train(features_train)
print("\n Accuracy of the classifier:", nltk.classify.util.accuracy(Classifier, features_test))

print("\n Top 10 most informative words:")
for item in Classifier.most_informative_features()[:10]:
    print(item[0])

# Sample input reviews
input_reviews = [
                "It is an amazing movie",
                "This movie is really thrilling",
                "This movie was totally boring",
                "Such a waste of time this movie is",
                "This movie is pretty good",
                "The plot of the movie was scattered"
]

print("\n Predictions:")
for review in input_reviews:
    print("\n Review:",review)
    probdist = Classifier.prob_classify(extract_features(review.split()))
    pred_sentiment = probdist.max()
    print("Predicted Sentiment:",pred_sentiment)
    print("Probability:", round(probdist.prob(pred_sentiment),2))