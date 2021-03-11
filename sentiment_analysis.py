# Daya Mann
# Sentiment Analysis

# define main function for sentiment analysis
def compute_tweets(tweet_file,keyword_file):

    # use try and except to ensure function returns a valid result (i.e. even if invalid file name is given)
    try:

        # define function to obtain needed values from keyword file
        def keyword_unpacker(keyword_file):
            keyword_dict = {}

            # open file and create list of each line
            with open(keyword_file, encoding='utf-8', errors='ignore') as f:
                list1 = f.readlines()

            # separate each word from its value and append to a dictionary
            for x in range(len(list1)):
                str1 = list1[x]
                key_value = int(str1[-2:])
                keyword = str1[0:-3]
                if key_value == 0:
                    key_value = 10
                    keyword = str1[0:-4]
                keyword_dict[keyword] = key_value

            # return final dictionary
            return keyword_dict

        final_keyword_dict = keyword_unpacker(keyword_file)

        # create empty list for each region's set of scores
        pacific_scores = []
        mountain_scores = []
        central_scores = []
        eastern_scores = []

        # define function that obtains needed information from each tweet
        def tweet_unpacker(tweet_file):
            pacific_tweets = 0
            mountain_tweets = 0
            central_tweets = 0
            eastern_tweets = 0

            # open file and iterate through each line
            with open(tweet_file, encoding='utf-8', errors='ignore') as t:
                for line in t:
                    line = line.split()
                    # obtain just the float value of latitude and longitude and compare to check what region the tweet is from
                    line[0] = float(line[0][1:-1])
                    line[1] = float(line[1][0:-1])
                    lat = line[0]
                    long = line[1]
                    if (lat > 49.189787) or (lat < 24.660845):
                        continue
                    if (long > -67.444574) or (long < -125.242264):
                        continue
                    if (long <= -67.444574) and (long >= -87.518395):
                        zone = 'eastern'
                    elif (long < -87.518395) and (long >= -101.998892):
                        zone = 'central'
                    elif (long < -101.998892) and (long >= -115.236428):
                        zone = 'mountain'
                    else:
                        zone = 'pacific'

                    # delete every item in the 'list' of the line except for the actual tweet
                    del line[0]
                    del line[0]
                    del line[0]
                    del line[0]
                    del line[0]

                    # iterate through each word, and each letter within each word to check that there is at least one letter in the word; if not, delete the 'word'
                    for n in range(len(line)):
                        counter = 0
                        for x in range(len(line[n])):
                            if line[n][x].isalpha() == True:
                                counter +=1
                            else:
                                continue

                        if counter == 0:
                            line[n] = ' '

                    while ' ' in line:
                        line.remove(' ')

                    # remove any punctutation on the outside of each word
                    for x in range(len(line)):
                        while line[x][-1].isalpha() == False:
                            line[x] = line[x][0:-1]
                        while line[x][0].isalpha() == False:
                            line[x] = line[x][1:]

                    # convert every word to lowercase to be able to match to dictionary
                    for x in range(len(line)):
                        line[x] = line[x].lower()

                    happ_score = 0
                    keywords = 0

                    # search through remaining words for keywords; if keyword is found, add that value to the tweet's total score and increment
                    # number of keywords for given tweet
                    for x in range(len(line)):
                        if line[x] in final_keyword_dict:
                            happ_score += final_keyword_dict[line[x]]
                            keywords += 1
                        else:
                            continue

                    # if the tweet had keywords, find average score for the tweet and add it to the respective region list
                    # also, increment number of tweets in the region
                    if keywords != 0:
                        if zone == 'eastern':
                            happ_score = happ_score/keywords
                            eastern_scores.append(happ_score)
                            eastern_tweets += 1
                        elif zone == 'central':
                            happ_score = happ_score/keywords
                            central_scores.append(happ_score)
                            central_tweets += 1
                        elif zone == 'mountain':
                            happ_score = happ_score/keywords
                            mountain_scores.append(happ_score)
                            mountain_tweets += 1
                        else:
                            happ_score = happ_score/keywords
                            pacific_scores.append(happ_score)
                            pacific_tweets += 1

                    # if the tweet had no keywords, increment total tweets from the region
                    else:
                        if zone == 'eastern':
                            eastern_tweets += 1
                        elif zone == 'central':
                            central_tweets += 1
                        elif zone == 'mountain':
                            mountain_tweets += 1
                        else:
                            pacific_tweets += 1

            # if a region had no keyword tweets, set appropriate values to 0
            # otheriwse, calculate average for the region and number of keyword tweets
            if sum(eastern_scores) == 0:
                eastern_avg = 0
                eastern_key_tweets = 0
            else:
                eastern_avg = sum(eastern_scores) / len(eastern_scores)
                eastern_avg = round(eastern_avg,2)
                eastern_key_tweets = len(eastern_scores)

            if sum(central_scores) == 0:
                central_avg = 0
                central_key_tweets = 0
            else:
                central_avg = sum(central_scores) / len(central_scores)
                central_avg = round(central_avg,2)
                central_key_tweets = len(central_scores)

            if sum(mountain_scores) == 0:
                mountain_avg = 0
                mountain_key_tweets = 0
            else:
                mountain_avg = sum(mountain_scores) / len(mountain_scores)
                mountain_avg = round(mountain_avg,2)
                mountain_key_tweets = len(mountain_scores)

            if sum(pacific_scores) == 0:
                pacific_avg = 0
                pacific_key_tweets = 0
            else:
                pacific_avg = sum(pacific_scores) / len(pacific_scores)
                pacific_avg = round(pacific_avg,2)
                pacific_key_tweets = len(pacific_scores)

            # return final list of tuples and return
            final_list = [(eastern_avg, eastern_key_tweets, eastern_tweets), (central_avg, central_key_tweets, central_tweets), (mountain_avg, mountain_key_tweets, mountain_tweets), (pacific_avg, pacific_key_tweets, pacific_tweets)]
            return final_list

        final_analysis = tweet_unpacker(tweet_file)
        return final_analysis

    #if invalid file names were entered, return an empty list
    except:
        empty_list = []
        return empty_list
