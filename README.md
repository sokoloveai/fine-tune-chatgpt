# How to fine-tune ChatGPT?
## Installation
Version of **openai==0.25** is more stable.

``` pip install -r requirements.txt ```


Set your **OPENAI_API_KEY** environment variable by adding the following line into your shell initialization script (e.g. .bashrc, zshrc, etc.) or running it in the command line before the fine-tuning command:

``` export OPENAI_API_KEY="<OPENAI_API_KEY>" ```

## Create data in .json format

``` {"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
... 
```

If you have your data in .csv format, use **converter.py** and pass it though.

## CLI data preparation tool

This tool validates, gives suggestions and reformats your data:

``` openai tools fine_tunes.prepare_data -f <LOCAL_FILE> ``` 

## Create fine-tuned model
You can choose between 3 Base models: *Curie*, *Ada*, *Baddage*

*Curie* is the most powerful model, with the largest size and highest computational power.

*Ada* is a medium-power model that can generate texts of moderate complexity and quality. Less time and resources to train than Curie.

*Babbage* is the lowest-power model, with the smallest size and computational power. It can generate texts of low complexity and quality, but requires the least amount of time and resources to train.

``` openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL> ```
