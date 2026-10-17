class Twitter:

    def __init__(self):
        self.userFollowSet = {}
        self.postTimeStamp = {}
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userFollowSet:
            self.userFollowSet[userId] = set()
        self.userFollowSet[userId].add(userId)

        self.time += 1
        userText = tweetId
        self.postTimeStamp[self.time] = {userId: userText}
        #print("post")
        #print(self.postTimeStamp)
        #print()

        

    def getNewsFeed(self, userId: int) -> List[int]:
        followee = self.userFollowSet[userId]

        res = []
        for t in range(self.time, 0, -1):
            if len(res) == 10:
                break

            posterList = self.postTimeStamp[t]
            for poster in posterList:
                if poster in followee:
                    post = self.postTimeStamp[t][poster]
                    res.append(post)

        #print("get")
        #print(res)
        #print()

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowSet:
            self.userFollowSet[followerId] = set()
        self.userFollowSet[followerId].add(followeeId)
        #print("follow")
        #print(self.userFollowSet)
        #print()




    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowSet:
            return

        if followeeId not in self.userFollowSet[followerId]:
            return

        self.userFollowSet[followerId].remove(followeeId)
        #print("unfollow")
        #print(self.userFollowSet)
        #print()