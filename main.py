# Daya Mann
# Sentiment Analysis

# import main funtion
from sentiment_analysis import compute_tweets

# obtain file names from user
user_tweet_file = input('Please input a file name for the tweets you would like to analyze (please include the .txt in the name): ')
user_keyword_file = input('Please input a file name for the keywords and their respective scores (please include the .txt in the name): ')

# run main function
sent_analysis = compute_tweets(user_tweet_file,user_keyword_file)
print()

# if the returned result was not an empty list, format and return results to user
if sent_analysis != []:
    eastern_tuple = sent_analysis[0]
    central_tuple = sent_analysis[1]
    mountain_tuple = sent_analysis[2]
    pacific_tuple = sent_analysis[3]

    score_dict = {eastern_tuple[0]:'Eastern',central_tuple[0]:'Central',mountain_tuple[0]:'Mountain',pacific_tuple[0]:'Pacific'}
    winner_score = max(score_dict)
    winner = score_dict[winner_score]

    print('ANALYSIS RESULTS')
    print('The Eastern timezone has an average happiness score of',eastern_tuple[0],'- with',eastern_tuple[1],
          'tweets containing keywords and',eastern_tuple[2],'tweets overall.')
    print('The Central timezone has an average happiness score of',central_tuple[0],'- with',central_tuple[1],
          'tweets containing keywords and',central_tuple[2],'tweets overall.')
    print('The Mountain timezone has an average happiness score of',mountain_tuple[0],'- with',mountain_tuple[1],
          'tweets containing keywords and',mountain_tuple[2],'tweets overall.')
    print('The Pacific timezone has an average happiness score of',pacific_tuple[0],'- with',pacific_tuple[1],
          'tweets containing keywords and',pacific_tuple[2],'tweets overall.')
    print()
    print('The happiest timezone in this analysis is',winner+', with a score of',str(winner_score)+'!')

# otherwise, return an error message
else:
    print('The file name(s) entered are invalid. Feel free to try again or have a nice day!')

