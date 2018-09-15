from urllib.request import Request, urlopen,quote
import urllib
from http.cookiejar import CookieJar
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import json
#from pyquery import PyQuery
import re
from bs4 import BeautifulSoup
from postTweets import TweetPost


class TwitterQuery():
    
    def __init__(self,key,term):
        self.db = TweetPost()
        self.key = key
        self.ttype = term 
    
    def getTweets(self,query,maxTweets=0,mnth=6):
        refreshCursor = ''
        results = []
        #resultsAux = []
        #cookieJar = http.cookiejar.CookieJar()
        cookieJar = CookieJar()
        lang = 'en'
        totalTweet = 0
        active = True
        while active:
            json = TwitterQuery.getTweetPage(query,refreshCursor, cookieJar,lang)
            if len(json['items_html'].strip()) == 0:
                break

            refreshCursor = json['min_position']
            
            soup = BeautifulSoup(json['items_html'],"html.parser")
            #scrapedTweets = PyQuery(json['items_html'])
            #tweets = scrapedTweets('div.js-stream-tweet')
            tweets = soup.find_all('li','js-stream-item')

            if len(tweets) == 0:
                break

            totalTweet += len(tweets)
            print(totalTweet)

            # for tweetHTML in tweets:
            #     #tweetPQ = PyQuery(tweetHTML)
            #     tweet = {}
            #     pT = tweetHTML.find('p','js-tweet-text').get_text()
            #     dateSec = int(tweetHTML.find('span','js-short-timestamp')['data-time'])
            #     txt =  re.sub(r"\s+", " ", pT.replace('# ', '#').replace('@ ', '@'))
            #     #txt = re.sub(r"\s+", " ", tweetPQ("p.js-tweet-text").text().replace('# ', '#').replace('@ ', '@'))
            #     #dateSec = int(tweetPQ("small.time span.js-short-timestamp").attr("data-time"))    
            #     tweet['text'] = txt
            #     tweet['date'] = datetime.datetime.fromtimestamp(dateSec)
            #     results.append(tweet)
            #     if maxTweets > 0 and len(results) >=maxTweets:
            #         active = False
            #         break
            self.db.addCount(self.key,totalTweet, self.ttype)
            results = []

        #return results

    def getTweetPage(querySearch,refreshCursor,cookieJar,lang,mnth=1):
        now = datetime.datetime.now() 
        today = date.today()
        #sixmonth = today + relativedelta(months=-mnth)
        sixmonth = today + relativedelta(days=-15)
        #q = quote(query,safe='')
        since = sixmonth.strftime("%Y-%m-%d") 
        until = now.strftime("%Y-%m-%d")

        url = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&%smax_position=%s"
        urlGetData = ''
        if since:
            urlGetData += ' since:' + since

        if until:
            urlGetData += ' until:' + until

        if querySearch:
            urlGetData += ' ' + querySearch

        if lang:
            urlLang = 'lang=' + lang + '&'
        else:
            urlLang = 'lang=en&'

        url = url % (urllib.parse.quote(urlGetData), urlLang, refreshCursor)

        print(url)
        
        #url = "https://twitter.com/search?q=" + q +"%20since%3A"+since+"%20until%3A"+ until +"&amp;amp;amp;amp;amp;amp;lang=en"
        headers = [
                    ('Host', "twitter.com"),
                    ('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"),
                    ('Accept', "application/json, text/javascript, */*; q=0.01"),
                    ('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
                    ('X-Requested-With', "XMLHttpRequest"),
                    ('Referer', url),
                    ('Connection', "keep-alive")
                ]
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJar))

        opener.addheaders = headers

        response = opener.open(url)
        jsonResponse = response.read()

        dataJson = json.loads(jsonResponse.decode())
        return dataJson

def main():
    api = TwitterQuery()
    tweets1 = api.getTweets(query = '"Google Home"',mnth=1)
    #tweets2 = api.getTweets(query = '"Alexa Echo"',mnth=2)
   

if __name__ == "__main__":
    # calling main function
    main()            
