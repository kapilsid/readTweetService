from firebase import firebase

class MyFirebase():
    
    def __init__(self,fireURL):
        self.fireURL = fireURL
        self.firebase = firebase.FirebaseApplication(fireURL, None)
 

    def save(self,key,data):
        result = self.firebase.post (key, data)
        return(result)     

def main():
    fb = MyFirebase('https://maclea-fb3c6.firebaseio.com/')
    #x = {}
    #x["term1"] ={"name":"Google Home"}
    #x["term2"] ={"name":"Alexa Home"}
    #x["term2"] ="Alexa Echo"
    #fb.save('/queries', x)
    #result = fb.firebase.get('/queries','-LMHtZ5RR85VWdOHtNbZ/0')
    #result.post(['txt:asasdasdadsads,date:23424'])
    #x = ['txt:asasdasdadsads,date:23424','txt:3443,date:43534']
    #result = fb.firebase.post('/queries/-LMHtZ5RR85VWdOHtNbZ/term2/q',x)
    k = '-LMSV4Lo-uNseK4W3cQ-'
    q = 'term1'
    count = 10 
    result = fb.firebase.put('/queries/'+ k +'/'+q, 'count' ,count)        
    #q = result.child("0").push()
    #q.setValue('txt:asasdasdadsads,date:23424')
    #fb.save('/queries/LMHhVBcjfVr1xPZuhmY','txt:asasdasdadsads,date:23424')
    #fb.save('/queries', '{term1: "Google Home", term2:"Alexa Echo"}')
    #tweets2 = api.getTweets(query = '"Alexa Echo"',mnth=2)
   

if __name__ == "__main__":
    # calling main function
    main()     