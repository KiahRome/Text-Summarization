from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import heapq

class NewAlgorithmProcessor:
    def __init__(self):
        self.content = ""

    def set_content(self, content):
        self.content = content

    def generate_summary(self):
        if not self.content:
            return "No content available for summarization."

        # Tokenize content into sentences
        sentences = sent_tokenize(self.content)

        # Tokenize content into words and count word frequencies
        word_frequencies = Counter(word_tokenize(self.content.lower()))
        
        # Normalize frequencies
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] /= max_frequency

        # Score sentences by summing the frequencies of words they contain
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]

        # Select the top N sentences as the summary
        summary_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary
