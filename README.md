# OpenAI gpt2 twitter bot

A simple twitter bot, trained on [this](https://github.com/zarveyy/openai-gtp2-twitter-bot/blob/main/Train_a_GPT_2_Model_on_Tweets.ipynb) openai gpt-2-simple model.

## Requirements
Create a Twitter application and generate a Consumer Key, Consumer Secret, Access Token, and Access Token Secret.
## Installation
### tweepy
An easy-to-use Python library for accessing the Twitter API

The easiest way to install the latest version from PyPI is by using pip:

```shell
pip install tweepy
```

 ### gpt-2-simple
A simple Python package that wraps existing model fine-tuning and generation scripts for [OpenAI](https://openai.com)'s [GPT-2 text generation model](https://openai.com/blog/better-language-models/)

You can use gpt-2-simple to retrain a model using a GPU **for free** in [this Colaboratory notebook](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce)

**only required if you don't want to use the Colaboratory notebook**

gpt-2-simple can be installed [via PyPI](https://pypi.org/project/gpt_2_simple/):

```shell
pip3 install gpt-2-simple
```

You will also need to install the corresponding TensorFlow for your system (e.g. `tensorflow` or `tensorflow-gpu`). **TensorFlow 2.0 is currently not supported** and the package will throw an assertion if loaded, so TensorFlow 1.14/1.15 is recommended.

For more info about gpt-2-simple, go [here](https://github.com/minimaxir/gpt-2-simple)

## Usage
Just change the value "TwitterUsername" in download_tweets.py by the name of the account you want to download the tweets from.
```python
if __name__ == "__main__":
    for user in ["TwitterUsername"]:
        download_all_tweets(user)
```
Output goes in downloaded_tweets

## Contributing
Pull requests are welcome. This is a very simple "template"



## License
[MIT](https://choosealicense.com/licenses/mit/)
