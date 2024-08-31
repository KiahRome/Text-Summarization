from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import FreqDist
import nltk

nltk.download('punkt')  # Corrected the download

class TextProcessor:
    def __init__(self):
        self.fileContent = ''
        self.memo = {}  # Memoization table to store sentence scores

    def set_content(self, content):
        """Sets the content of the text processor."""
        self.fileContent = content

    def get_sentence_score(self, sentence, freq_dist):
        """Returns the score of a sentence based on word frequency, using memoization."""
        # Check if the sentence's score is already computed and stored in memo
        if sentence in self.memo:
            return self.memo[sentence]
        
        # Calculate the score by summing up the frequency of each word in the sentence
        score = sum(freq_dist.get(word.lower(), 0) for word in word_tokenize(sentence))
        
        # Store the computed score in the memo table
        self.memo[sentence] = score
        
        return score

    def generate_summary(self, num_sentences=3):
        """Generates a summary by selecting the top scoring sentences."""
        # Handle case where file content might be empty
        if not self.fileContent:
            return "No content available to summarize."
        
        sentences = sent_tokenize(self.fileContent)
        words = word_tokenize(self.fileContent)
        freq_dist = FreqDist(word.lower() for word in words if word.isalpha())

        # Score each sentence and store it in the memoization table
        sentence_scores = {sentence: self.get_sentence_score(sentence, freq_dist) for sentence in sentences}
        
        # Select the top sentences based on their scores
        summarized_sentences = sorted(sentences, key=lambda s: sentence_scores[s], reverse=True)[:num_sentences]

        return ' '.join(summarized_sentences)

    def display_memo(self):
        """Displays the memoization table containing sentence scores."""
        return self.memo
