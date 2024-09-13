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

        sentences = self.tokenize_sentences(self.content)
        word_frequencies = self.get_word_frequencies()
        sentence_scores = self.score_sentences(sentences, word_frequencies)
        summary_sentences = self.select_top_sentences(sentences, sentence_scores)
        return ' '.join(summary_sentences)

    def tokenize_sentences(self, text):
        text = self._normalize_text(text)
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s+(?=[A-Z])', text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def _normalize_text(self, text):
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'(\d+\.\s)', r'\n\1', text)  # Handle numbered lists
        text = re.sub(r'(\u2022|\u25AA|\u25CF)\s', r'\n- ', text)  # Handle bullet points
        return text

    def get_word_frequencies(self):
        if not self.word_frequencies_cache:
            words = re.findall(r'\w+', self.content.lower())
            word_frequencies = Counter(words)
            max_frequency = max(word_frequencies.values(), default=1)
            self.word_frequencies_cache = {word: freq / max_frequency for word, freq in word_frequencies.items()}
        return self.word_frequencies_cache

    def score_sentences(self, sentences, word_frequencies):
        sentence_scores = {}
        max_score = 0
        
        for sentence in sentences:
            words = re.findall(r'\w+', sentence.lower())
            score = sum(word_frequencies.get(word, 0) for word in words)
            sentence_scores[sentence] = score
            max_score = max(max_score, score)
        
        # Adjusted threshold for more relevant sentences
        threshold = 0.15 * max_score
        filtered_scores = {sentence: score for sentence, score in sentence_scores.items() if score > threshold}

        # Enhance representation from different sections
        total_sentences = len(sentences)
        if total_sentences > 5:
            min_sentences = max(1, total_sentences // 6)
            for idx, sentence in enumerate(sentences):
                if idx < min_sentences or idx > total_sentences - min_sentences:
                    filtered_scores[sentence] = filtered_scores.get(sentence, 0) + 0.2

        return filtered_scores

    def select_top_sentences(self, sentences, sentence_scores):
        top_n = min(7, len(sentences))  # Increase the number of top sentences
        ranked_sentences = heapq.nlargest(top_n, sentence_scores.items(), key=lambda x: x[1])
        
        # Ensure the selected sentences maintain the original order
        best_sentences = [sentence for sentence, _ in ranked_sentences]
        best_sentences.sort(key=lambda sentence: sentences.index(sentence))
        
        return best_sentences
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

        # Segment long texts into chunks if necessary
        chunks = self.segment_text(self.content)
        summary_chunks = [self._generate_chunk_summary(chunk) for chunk in chunks]
        full_summary = ' '.join(summary_chunks)
        return full_summary

    def segment_text(self, text, max_chunk_size=5000):
        sentences = self.tokenize_sentences(text)
        chunks = []
        current_chunk = []

        chunk_size = 0
        for sentence in sentences:
            sentence_size = len(sentence)
            if chunk_size + sentence_size > max_chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                chunk_size = 0
            current_chunk.append(sentence)
            chunk_size += sentence_size
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))

        return chunks

    def _generate_chunk_summary(self, chunk):
        sentences = self.tokenize_sentences(chunk)
        word_frequencies = self.get_word_frequencies()
        sentence_scores = self.score_sentences(sentences, word_frequencies)
        summary_sentences = self.select_top_sentences(sentences, sentence_scores)
        return ' '.join(summary_sentences)

    def tokenize_sentences(self, text):
        text = self._normalize_text(text)
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s+(?=[A-Z])', text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def _normalize_text(self, text):
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'(\d+\.\s)', r'\n\1', text)  # Handle numbered lists
        text = re.sub(r'(\u2022|\u25AA|\u25CF)\s', r'\n- ', text)  # Handle bullet points
        return text

    def get_word_frequencies(self):
        if not self.word_frequencies_cache:
            words = re.findall(r'\w+', self.content.lower())
            word_frequencies = Counter(words)
            max_frequency = max(word_frequencies.values(), default=1)
            self.word_frequencies_cache = {word: freq / max_frequency for word, freq in word_frequencies.items()}
        return self.word_frequencies_cache

    def score_sentences(self, sentences, word_frequencies):
        sentence_scores = {}
        max_score = 0
        
        for sentence in sentences:
            words = re.findall(r'\w+', sentence.lower())
            score = sum(word_frequencies.get(word, 0) for word in words)
            sentence_scores[sentence] = score
            max_score = max(max_score, score)
        
        # Adjusted threshold for more relevant sentences
        threshold = 0.15 * max_score
        filtered_scores = {sentence: score for sentence, score in sentence_scores.items() if score > threshold}

        # Enhance representation from different sections
        total_sentences = len(sentences)
        if total_sentences > 5:
            min_sentences = max(1, total_sentences // 6)
            for idx, sentence in enumerate(sentences):
                if idx < min_sentences or idx > total_sentences - min_sentences:
                    filtered_scores[sentence] = filtered_scores.get(sentence, 0) + 0.2

        return filtered_scores

    def select_top_sentences(self, sentences, sentence_scores):
        top_n = min(10, len(sentences))  # Increase the number of top sentences
        ranked_sentences = heapq.nlargest(top_n, sentence_scores.items(), key=lambda x: x[1])
        
        # Ensure the selected sentences maintain the original order
        best_sentences = [sentence for sentence, _ in ranked_sentences]
        best_sentences.sort(key=lambda sentence: sentences.index(sentence))
        
        return best_sentences
