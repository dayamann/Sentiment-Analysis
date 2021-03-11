# Sentiment-Analysis
With the emergence of Internet companies such as Google, Facebook, and Twitter, more and more data accessible online is comprised of text.  Textual data and the computational means of processing it and extracting information is also increasingly more important in areas such as business, humanities, social sciences, etc.  In this assignment, you will deal with textual analysis.

Twitter has become very popular, with many people “tweeting” aspects of their daily lives.  This “flow of tweets” has recently become a way to study or guess how people feel about various aspects of the world or their own life.  For example, analysis of tweets has been used to try to determine how certain geographical regions may be voting – this is done by analyzing the content, the words, and phrases, in tweets.  Similarly, analysis of keywords or phrases in tweets can be used to determine how popular or unpopular a movie might be.  This is often referred to as sentiment analysis.

# Functionality
This repository contains a Python module, called sentiment_analysis.py and a main program, main.py, that uses the module to analyze Twitter information.  In the module sentiment_analysis.py, there is a function that performs simple sentiment analysis on Twitter data.  The Twitter data contains comments from individuals about how they feel about their lives and comes from individuals across the continental United States.  The objective is to determine which timezone (Eastern, Central, Mountain, Pacific) is the “happiest”.  To do this, the program:

- Analyzes each individual tweet to determine a score – a “happiness score” – for the individual tweet.
- The “happiness score” for a single tweet is found by looking for certain keywords (which are given) in a tweet and for each keyword found in that tweet totaling their “sentiment values”. Each value is an integer from 1 to 10.
- The happiness score for the tweet is simply the sum of the “sentiment values” for keywords found in the tweet divided by the number of keywords found in the tweet. 
- If there are none of the given keywords in a tweet, it is just ignored, i.e., you do NOT count it.

A file called tweets.txt contains the tweets and a file called keywords.txt contains keywords and scores for determining the “sentiment” of an individual tweet.  These files are described in more detail below.
