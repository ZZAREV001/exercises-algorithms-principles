# Multinomial Naive Bayes applied to newspapers articles and their tags
import math
from collections import defaultdict


class MultinomialNB:
    def __init__(self, articles_per_tag):
        self.alpha = 1
        self.priors_per_tag = {}
        self.likelihood_per_word_per_tag = {}
        self.articles_per_tag = articles_per_tag  # dictionary in which the key is tag and the value is the list of articles associated with that tag
        self.tags = self.articles_per_tag.keys()
        self.train()

    def train(self):
        tag_counts_map = {tag: len(self.articles_per_tag[tag]) for tag in
                          self.tags}  # we create the dictionaries as indicated in the Naive Bayes formulas.
        self.priors_per_tag = {tag: tag_counts_map[tag] / sum(tag_counts_map.values()) for tag in self.tags}
        self.likelihood_per_word_per_tag = self.__get_word_likelihoods_per_tag()

    def predict(self, article):
        posteriors_per_tag = {tag: math.log(prior) for tag, prior in self.priors_per_tag.items()}
        # Iterate through each words in the article.
        for word in article:
            for tag in self.tags:
                posteriors_per_tag[tag] = posteriors_per_tag[tag] + math.log(
                    self.likelihood_per_word_per_tag[word][tag]
                )
        return posteriors_per_tag

    def __get_word_likelihoods_per_tag(self):  # find the word frequencies first
        word_frequencies_per_tag = defaultdict(lambda: {tag: 0 for tag in self.tags})
        total_word_count_per_tag = defaultdict(int)
        for tag in self.tags:
            for article in self.articles_per_tag[tag]:
                for word in article:
                    word_frequencies_per_tag[word][tag] += 1  # assign word frequencies per tag at each iteration
                    total_word_count_per_tag[tag] += 1  # increment the total number of words in this tag
        word_likelihoods_per_tag = defaultdict(lambda: {tag: 0.5 for tag in
                                                        self.tags})  # recall: we add 1 to the numerator and 2 to the denominator. That's why we have 0.5 here (1/2=0.5)
        for word, tags_map in word_frequencies_per_tag.items():
            for tag in tags_map.keys():  # here we have the formula Naive Bayes model
                word_likelihoods_per_tag[word][tag] = (word_frequencies_per_tag[word][tag] + 1 * self.alpha) \
                                                      / (total_word_count_per_tag[tag] + 2 * self.alpha)
        return word_likelihoods_per_tag





    

