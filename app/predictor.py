import torch

from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_topic(text):
    labels = ["politics", "sports", "entertainment", "technology", "finance"]
    result = classifier(text, candidate_labels=labels)
    return result["labels"][0]


def predict_toxicity(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    score = torch.sigmoid(outputs.logits)[0][0].item()
    return score, score > 0.5