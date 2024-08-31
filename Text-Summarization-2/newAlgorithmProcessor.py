from transformers import BartTokenizer, BartForConditionalGeneration
import torch  # Ensure you have PyTorch installed

class NewAlgorithmProcessor:
    def __init__(self):
        self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
        self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
        self.content = ""
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def set_content(self, content):
        self.content = content

    def generate_summary(self):
        if not self.content:
            return "No content available for summarization."

        inputs = self.tokenizer.encode("summarize: " + self.content, return_tensors="pt", max_length=1024, truncation=True).to(self.device)


        summary_ids = self.model.generate(
            inputs,
            max_length=150,
            min_length=40,
            length_penalty=2.0,
            num_beams=2,  # Reduced beams for faster generation
            early_stopping=True
        )
        
        # Move summary_ids to CPU before decoding
        summary_ids = summary_ids.cpu()
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
