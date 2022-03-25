from socialmedia import socialMedia

class Instagram(socialMedia):
    def __init__(self , name  ):
        super().__init__(name)
        self.postList = []

    def getPosts(self):
        return self.postList


    def publishNewPost(self ):
        publish = False
        body = input("enter your Instagram post body:")
        if( len(body)<=2200):
            publish = True
            self.postList.append(body)
            print("your post was accepted  *_*")

        else:
            print(" not valid post body")

        return publish



