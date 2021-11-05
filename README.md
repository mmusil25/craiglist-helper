# craiglist-helper synopsis
Perform sentiment analysis and keyword extraction on Craigslist listings 

# Background

I love Craigslist. I've found most of my housing situations through Craigslist and despite the occasional mix up with a 
stranger[^1] I always find better prices there and interesting individuals. However, I find it exhausting to browse Craigslist
and parse the sometimes poorly written or overly lengthy postings. I don't mind reading someone's well-thought-out
description of their home and ideal roommate, but I do mind wasting time reading aggressive posts clearly written by 
emotionally distant landlords. 

So I came up with the idea of using sentiment analysis in order to determine whether the author of the posting is
positive. I only want to live with positive people so this helps me greatly. In addition, this program gathers keywords from 
the listing to help you get a sense of what they are describing. It also shows you the price for reference. 

I will be adding more features such as an email drafter to further automate the process of setting up transactions. 

Enjoy!

[^1]: I wore a mask to my meeting with the landlord and was immediately cussed out because of the mask and told to 
leave. Too bad it was such a great deal :(

## Examples

[A positive listing (scroll right)](media/Positive.PNG)

## Usage 


Install dependencies via requirements.txt

```
pip install -r requirements.txt
```

Run!

```
python3 controller.py
```
