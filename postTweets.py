from postFirebase import MyFirebase

class TweetPost():
    
    def __init__(self):
        self.db = MyFirebase('https://maclea-fb3c6.firebaseio.com/')
    
    def addTweetReq(self,q):
        x = {}
        x["term1"] ={"name":q["term1"]}
        x["term2"] ={"name":q["term2"]}
        self.key = self.db.save('/queries', x) 

    def addCount(self,k,count,q):
        fb.firebase.put('/queries/'+ k +'/'+q, 'count' ,count)    
    
    def addList(self,k,q,t):
        result = self.db.post('/queries/'+ k +"/" + q + '/q',t)     

def main():
    tp = MyFirebase('https://maclea-fb3c6.firebaseio.com/')
    
if __name__ == "__main__":
    # calling main function
    main()     