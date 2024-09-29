import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.chunk import ne_chunk
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Download NLTK data
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

class TextProcessor:
    def __init__(self):
        self.fileContent = ''
        self.memo = {}  # Memoization table to store sentence scores

    def set_content(self, content):
        self.fileContent = content

    def shallow_parse(self):
        sentences = sent_tokenize(self.fileContent)
        chunks = []
        for sentence in sentences:
            tokens = word_tokenize(sentence)
            tagged = nltk.pos_tag(tokens)
            chunked = ne_chunk(tagged)
            chunks.append(chunked)
        return chunks

    def get_chunk_text(self, chunk):
        return ' '.join(c[0] for c in chunk if isinstance(c, tuple))

    def generate_summary(self, num_sentences=3):
        sentences = sent_tokenize(self.fileContent)
        # For simplicity, we’ll just return the first few sentences as summary
        return ' '.join(sentences[:num_sentences])

class BERTProcessor:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
    
    def summarize_with_bert(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        outputs = self.model(**inputs)
        # For demonstration, we'll just return the raw model output
        return outputs

def process_text_with_bert(text):
    # Initialize processors
    text_processor = TextProcessor()
    bert_processor = BERTProcessor()

    # Set content and perform shallow parsing
    text_processor.set_content(text)
    chunks = text_processor.shallow_parse()

    # Process chunks with BERT
    summaries = []
    for chunk in chunks:
        chunk_text = text_processor.get_chunk_text(chunk)
        summary = text_processor.generate_summary()
        bert_summary = bert_processor.summarize_with_bert(chunk_text)
        summaries.append(summary)
    
    # Return summarized results
    return summaries

# Example usage
if __name__ == "__main__":
    sample_text = ("John lives in New York and works at Google. "
                   "He enjoys programming and working on AI projects. "
                   "In his free time, John likes to read books on technology.")
    results = process_text_with_bert(sample_text)
    print(results)
