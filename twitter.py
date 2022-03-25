from socialmedia import socialMedia

class Twitter(socialMedia):
    def __init__(self , name  ):
        super().__init__(name)
        self.tweets = []

    def getTweets(self):
        return self.tweets


    def createNewTweet(self ):
        create = False
        body = input("enter your tweet body:")
        if( len(body)<=280):
            create = True
            self.tweets.append(body)
            print("your tweet was accepted :)")
        else:
            print(" not valid tweet body")

        return create



