from transformers import pipeline 
from transformers import AutoModelForSequenceClassification 
from transformers import BertJapaneseTokenizer 
 
TARGET_TEXT = "すっごく楽しい。幸せだ"
 
model = AutoModelForSequenceClassification.from_pretrained('cl-tohoku/bert-large-japanese') 
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking') 
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer) 
 
print(nlp(TARGET_TEXT))