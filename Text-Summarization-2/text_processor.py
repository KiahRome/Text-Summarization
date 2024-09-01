import re
from collections import Counter

class TextProcessor:
    def __init__(self):
        self.fileContent = ''
        self.memo = {}  # Memoization table to store sentence scores

    def set_content(self, content):
        """Sets the content of the text processor."""
        self.fileContent = content
        self.memo = {}  # Reset memoization table

    def tokenize_sentences(self, text):
        """Splits text into sentences using regular expressions."""
        # Regex to split text by periods, exclamation marks, and question marks
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\!|\?)\s', text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def tokenize_words(self, text):
        """Splits text into words using regular expressions."""
        return re.findall(r'\w+', text.lower())  # Convert to lowercase and extract words

    def get_word_frequencies(self):
        """Calculates word frequencies and normalizes them."""
        words = self.tokenize_words(self.fileContent)
        word_frequencies = Counter(words)
        max_frequency = max(word_frequencies.values(), default=1)
        return {word: freq / max_frequency for word, freq in word_frequencies.items()}

    def get_sentence_score(self, sentence, freq_dist):
        """Returns the score of a sentence based on word frequency, using memoization."""
        if sentence in self.memo:
            return self.memo[sentence]
        
        words = self.tokenize_words(sentence)
        score = sum(freq_dist.get(word, 0) for word in words)
        self.memo[sentence] = score
        return score

    def generate_summary(self, num_sentences=3):
        """Generates a summary by selecting the top scoring sentences."""
        if not self.fileContent:
            return "No content available to summarize."
        
        sentences = self.tokenize_sentences(self.fileContent)
        freq_dist = self.get_word_frequencies()

        sentence_scores = {sentence: self.get_sentence_score(sentence, freq_dist) for sentence in sentences}
        summarized_sentences = sorted(sentences, key=lambda s: sentence_scores[s], reverse=True)[:num_sentences]

        return ' '.join(summarized_sentences)

    def display_memo(self):
        """Displays the memoization table containing sentence scores."""
        return self.memo
