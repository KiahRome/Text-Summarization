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

        sentences = self.tokenize_sentences(self.content)  # Shallow Parsing: Basic Tokenization
        word_frequencies = self.get_word_frequencies()  # Selective Memoization
        sentence_scores = self.score_sentences(sentences, word_frequencies)  # Enhanced Scoring
        summary_sentences = self.select_top_sentences(sentences, sentence_scores)  # Improved Selection
        return ' '.join(summary_sentences)

    def tokenize_sentences(self, text):
        # Shallow Parsing: Enhanced sentence split to handle edge cases
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s+(?=[A-Z])', text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def get_word_frequencies(self):
        # Selective Memoization: Cache word frequencies efficiently
        if not self.word_frequencies_cache:
            words = re.findall(r'\w+', self.content.lower())
            word_frequencies = Counter(words)
            max_frequency = max(word_frequencies.values(), default=1)
            self.word_frequencies_cache = {word: freq / max_frequency for word, freq in word_frequencies.items()}
        return self.word_frequencies_cache

    def score_sentences(self, sentences, word_frequencies):
        # Enhanced sentence scoring with improved threshold
        sentence_scores = {}
        max_score = 0
        
        for sentence in sentences:
            words = re.findall(r'\w+', sentence.lower())
            score = sum(word_frequencies.get(word, 0) for word in words)
            sentence_scores[sentence] = score
            max_score = max(max_score, score)
        
        # Adjusted pruning threshold based on max score
        threshold = 0.1 * max_score
        filtered_scores = {sentence: score for sentence, score in sentence_scores.items() if score > threshold}

        # Ensure representation from different sections (beginning, middle, end)
        total_sentences = len(sentences)
        if total_sentences > 5:
            min_sentences = max(1, total_sentences // 6)  # Ensure representation from each part
            for idx, sentence in enumerate(sentences):
                if idx < min_sentences or idx > total_sentences - min_sentences:
                    filtered_scores[sentence] = filtered_scores.get(sentence, 0) + 0.1
        
        return filtered_scores

    def select_top_sentences(self, sentences, sentence_scores):
        # Improved sentence selection
        top_n = min(5, len(sentences))  # Ensure we do not select more sentences than available
        ranked_sentences = heapq.nlargest(top_n, sentence_scores.items(), key=lambda x: x[1])
        
        # Maintain original order
        best_sentences = [sentence for sentence, _ in ranked_sentences]
        best_sentences.sort(key=lambda sentence: sentences.index(sentence))
        
        return best_sentences
