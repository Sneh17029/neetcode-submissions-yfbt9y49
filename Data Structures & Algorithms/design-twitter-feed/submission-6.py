class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(  self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        if userId not in self.follows.keys():
            self.follows[userId] = set()
        
        users = self.follows[userId] | {userId}
        heap = []

        for user in users:
            if user in self.tweets:
                i = len(self.tweets[user]) - 1
                time, tweet = self.tweets[user][i]

                heapq.heappush(heap, (-time, tweet, user, i - 1))
        while heap and len(res)<10:
            time, tweet, user, index = heapq.heappop(heap)
            res.append(tweet)
            if index >= 0:
                ntime, ntweet = self.tweets[user][index]
                heapq.heappush(heap, (-ntime, ntweet, user, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
