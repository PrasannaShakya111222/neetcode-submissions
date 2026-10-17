class Twitter {

    private int time;
    private Map<Integer, Set<Integer>> following;
    private Map<Integer, List<int[]>> tweets;

    public Twitter() {
        time = 0;
        following = new HashMap<>();
        tweets = new HashMap<>();
    }

    public void postTweet(int userId, int tweetId) {
        tweets.computeIfAbsent(userId, k -> new ArrayList<>())
              .add(new int[]{time++, tweetId});
    }

    public List<Integer> getNewsFeed(int userId) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(b[0], a[0])
        );

        // Include the user's own tweets
        addTweets(userId, maxHeap);

        // Include tweets from followed users
        for (int followeeId :
                following.getOrDefault(userId, Collections.emptySet())) {
            addTweets(followeeId, maxHeap);
        }

        List<Integer> feed = new ArrayList<>();

        // Return the 10 most recent tweets
        while (!maxHeap.isEmpty() && feed.size() < 10) {
            feed.add(maxHeap.poll()[1]);
        }

        return feed;
    }

    private void addTweets(int userId, PriorityQueue<int[]> maxHeap) {
        List<int[]> userTweets = tweets.get(userId);

        if (userTweets == null) {
            return;
        }

        for (int[] tweet : userTweets) {
            maxHeap.offer(tweet);
        }
    }

    public void follow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return;
        }

        following.computeIfAbsent(followerId, k -> new HashSet<>())
                 .add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        following.getOrDefault(followerId, Collections.emptySet())
                 .remove(followeeId);
    }
}
