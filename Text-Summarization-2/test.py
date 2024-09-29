import nltk
from nltk.chunk import ne_chunk
from nltk.tokenize import word_tokenize

nltk.download('averaged_perceptron_tagger_eng')  # Corrected the download

nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
sentence = "John lives in New York and works at Google."
tokens = word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
chunked = ne_chunk(tagged)

print(chunked)
