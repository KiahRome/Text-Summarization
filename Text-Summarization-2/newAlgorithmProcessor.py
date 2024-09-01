import re
from collections import Counter
import heapq

class NewAlgorithmProcessor:
    def __init__(self):
        self.content = ""
        self.word_frequencies_cache = {}
        self.sentence_scores_cache = {}

    def set_content(self, content):
        self.content = content
        self.word_frequencies_cache = {}  # Reset cache
        self.sentence_scores_cache = {}  # Reset cache

    def generate_summary(self):
        if not self.content:
            return "No content available for summarization."

        sentences = self.tokenize_sentences(self.content)  # Shallow Parsing
        word_frequencies = self.get_word_frequencies()  # Memoization
        sentence_scores = self.score_sentences(sentences, word_frequencies)  # Memoization
        summary_sentences = self.select_top_sentences(sentences, sentence_scores)  # Branch and Bound
        return ' '.join(summary_sentences)

    def tokenize_sentences(self, text):
        # Shallow Parsing: Split text into sentences
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def get_word_frequencies(self):
        # Selective Memoization: Cache word frequencies
        if not self.word_frequencies_cache:
            word_frequencies = Counter(re.findall(r'\w+', self.content.lower()))
            max_frequency = max(word_frequencies.values(), default=1)
            self.word_frequencies_cache = {word: freq / max_frequency for word, freq in word_frequencies.items()}
        return self.word_frequencies_cache

    def score_sentences(self, sentences, word_frequencies):
        # Selective Memoization: Cache sentence scores
        sentence_scores = {}
        for sentence in sentences:
            if sentence not in self.sentence_scores_cache:
                words = re.findall(r'\w+', sentence.lower())
                score = sum(word_frequencies.get(word, 0) for word in words)
                self.sentence_scores_cache[sentence] = score
            sentence_scores[sentence] = self.sentence_scores_cache[sentence]
        return sentence_scores

    def select_top_sentences(self, sentences, sentence_scores):
        # Branch and Bound: Efficiently select top N sentences
        top_n = 5
        ranked_sentences = heapq.nlargest(top_n, sentence_scores.items(), key=lambda x: x[1])
        ranked_sentences.sort(key=lambda x: sentences.index(x[0]))  # Maintain original order
        return [sentence for sentence, _ in ranked_sentences]
