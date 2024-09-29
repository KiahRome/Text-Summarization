from transformers import BartTokenizer, BartForConditionalGeneration

class NewAlgorithmProcessor:
    def __init__(self):
        self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
        self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
        self.content = ""

    def set_content(self, content):
        self.content = content

    def generate_summary(self):
        if not self.content:
            return "No content available for summarization."

        inputs = self.tokenizer.encode("summarize: " + self.content, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = self.model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
