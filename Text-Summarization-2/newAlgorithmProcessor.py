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

    def generate_summary(self, text_type="article"):
        if not self.content:
            return "No content available for summarization."

        # Choose the summarization strategy based on the text type
        if text_type == "short_story":
            chunks = self.segment_text_short_story(self.content)
        elif text_type == "article":
            chunks = self.segment_text_article(self.content)
        else:
            return "Invalid text type specified."

        full_summary = []
        for chunk in chunks:
            chunk_summary = self._generate_chunk_summary(chunk)
            full_summary.append(chunk_summary)

        return self._shorten_summary(' '.join(full_summary).strip(), text_type)

    def segment_text_short_story(self, text, max_chunk_size=2000):
        sentences = self.tokenize_sentences(text)
        return self._segment_text(sentences, max_chunk_size)

    def segment_text_article(self, text, max_chunk_size=4000):
        sentences = self.tokenize_sentences(text)
        return self._segment_text(sentences, max_chunk_size)

    def _segment_text(self, sentences, max_chunk_size):
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
        headings = r'\b(Abstract|Keywords|Introduction|Literature Review|Methodology|Results|Discussion|Conclusion)\b'
        text = re.sub(headings, '', text, flags=re.IGNORECASE)
        text = re.sub(r'\b\d+(\.\d+)?\b\s*', '', text)
        text = re.sub(r'(\u2022|\u25AA|\u25CF)\s*', '', text)
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'[^\w\s.,!?-]', '', text)
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
        
        threshold = 0.2 * max_score if len(sentences) > 10 else 0.3 * max_score
        
        filtered_scores = {sentence: score for sentence, score in sentence_scores.items() if score > threshold}

        return filtered_scores

    def select_top_sentences(self, sentences, sentence_scores):
        top_n = min(5, len(sentences)) if len(sentences) <= 10 else min(8, len(sentences))
        ranked_sentences = heapq.nlargest(top_n, sentence_scores.items(), key=lambda x: x[1])
        best_sentences = [sentence for sentence, _ in ranked_sentences]
        best_sentences.sort(key=lambda sentence: sentences.index(sentence))
        return best_sentences

    def _shorten_summary(self, summary, text_type):
        words = summary.split()
        if text_type == "short_story":
            return ' '.join(words[:150])  # Limit to a specific word count for short stories
        elif text_type == "article":
            return ' '.join(words[:250])  # Limit to a specific word count for articles
        return summary
