import yake
from craigslist_scraper.scraper import scrape_url
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
from transformers import pipeline, set_seed
# generator = pipeline('text-generation', model='gpt2')
sent_analysis = pipeline("sentiment-analysis")
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)
import gpt_2_simple as gpt2
import os
from keytotext import pipeline
import warnings
warnings.filterwarnings("ignore")
nlp = pipeline("k2t-new")  # loading the pre-trained model
import random
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar

def analyze_and_print(text, window):
    result = sent_analysis(text)[0]
    window.write_event_value('-THREAD-', f"\nLabel:  {result['label']}\n")
    window.write_event_value('-THREAD-', f"Confidence:  {result['score']}\n")
    return


def process_url(url, window):
    data = scrape_url(url)
    info = data.the_whole_post()
    window.write_event_value('-THREAD-', f"\n Cost: {data.price} ")
    analyze_and_print(info, window)

    model_name = "355M"
    if not os.path.isdir(os.path.join("models", model_name)):
        window.write_event_value('-THREAD-', f"Downloading {model_name} model...")
        gpt2.download_gpt2(model_name=model_name)  # model is saved into current directory under /models/124M/


    # my_words = info
    # sess = gpt2.start_tf_sess()

    # gpt2.finetune(sess,
    #               dataset=info,
    #               model_name='355M',
    #               steps=1000,
    #               restore_from='fresh',
    #               run_name='run1',
    #               print_every=10,
    #               sample_every=200,
    #               save_every=500,
    # 	          only_train_transformer_layers = True,
    #               )
    #
    # listing_response = gpt2.generate(sess)
    language = "en"
    max_ngram_size = 2
    deduplication_threshold = 0.90
    numOfKeywords = 3
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(info)
    window.write_event_value('-THREAD-', "\nKeywords from this post: \n")

    keyword_string = ""
    for kw in keywords:
        window.write_event_value('-THREAD-', f"{kw[0]}")
        keyword_string += (str(kw[0]) + " ")
    window.write_event_value('-THREAD-', "\nIn one sentence\n")
    # mygen = generator(keyword_string, length_penalty = 0.5, max_length=100, num_return_sequences=1)

    params = {"min_length": 50}  # decoding params
    response = nlp(keyword_string.split(), **params)
    window.write_event_value('-THREAD-', f"{response} \n")



    # add the EOS token as PAD token to avoid warnings
    # encode context the generation is conditioned on

    # input_ids = tokenizer.encode(info, return_tensors='tf')

    # generate text until the output length (which includes the context length) reaches 50
    # greedy_output = model.generate(input_ids, length_penalty=0.4, max_length=300)
    # listing_response = tokenizer.decode(greedy_output[0], skip_special_tokens=True)