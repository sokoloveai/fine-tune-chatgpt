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

``` openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL> ```
