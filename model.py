import yake
from transformers import pipeline
from craigslist_scraper.scraper import scrape_url


text_list = [
    "microsoft/DialoGPT-medium",
    "microsoft/DialoGPT-large",
    "gpt2"
]

moods = [
    "normal, reserved, friendly",
    "spontaneous, random, assertive",
]

mood_levels = {
    1: "normal, reserved, friendly",
    2: "spontaneous, random, assertive",
}

sent_analysis = pipeline("sentiment-analysis")


def analyze_and_print(text, window):
    result = sent_analysis(text)[0]
    window.write_event_value('-THREAD-', f"\n\nLabel:  {result['label']}\n")
    window.write_event_value('-THREAD-', f"Confidence:  {result['score']}\n\n")
    return


def process_url(url, window):
    data = scrape_url(url)
    info = data.the_whole_post()
    window.write_event_value('-THREAD-', f"\n Cost: {data.price} \n")
    analyze_and_print(info, window)

    language = "en"
    max_ngram_size = 1
    deduplication_threshold = 0.9
    numOfKeywords = 10
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                     top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(info)
    window.write_event_value('-THREAD-', "\n Keywords from this post \n")

    for kw in keywords:
        window.write_event_value('-THREAD-', f"{kw[0]}")


