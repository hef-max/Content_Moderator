import pandas as pd
from datetime import datetime

def log_toxic(text, score):
    df = pd.DataFrame([[datetime.now(), text, score]], columns=["timestamp", "text", "toxicity_score"])
    df.to_csv("data/toxic_log.csv", mode="a", header=False, index=False)
