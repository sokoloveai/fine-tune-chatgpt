import pandas as pd
import json

# загрузка CSV файла с вопросами и ответами
df = pd.read_csv("your-file.csv", sep=';')

# создание списка пар вопрос-ответ
pairs = []
for i, row in df.iterrows():
    pairs.append({"prompt": row["Question"], "completion": row["Answer"]})

# экспорт списка в JSON файл
with open("pairs.json", "w", encoding="utf-8") as f:
    json.dump(pairs, f, indent=4, ensure_ascii=False)

# Сгенерировано с помощью @gptscience