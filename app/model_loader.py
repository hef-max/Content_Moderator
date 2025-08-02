from transformers import AutoTokenizer, AutoModelForSequenceClassification

def load_toxicity_model():
    tokenizer = AutoTokenizer.from_pretrained("unitary/toxic-bert")
    model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert")
    return tokenizer, model
