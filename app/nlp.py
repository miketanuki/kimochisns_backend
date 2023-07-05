from transformers import pipeline 
from transformers import AutoModelForSequenceClassification 
from transformers import BertJapaneseTokenizer

model = AutoModelForSequenceClassification.from_pretrained('cl-tohoku/bert-large-japanese') 
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking') 
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer) 

def get_sentiment(text):
    result = nlp(text)[0]
    # sentiment_score = result['score'] if result['label'] == 'LABEL_1' else -result['score']
    sentiment_score = result['score']
    return sentiment_score