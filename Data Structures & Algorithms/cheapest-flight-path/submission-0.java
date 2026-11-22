class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] price = new int[n];
        Arrays.fill(price, Integer.MAX_VALUE);
        price[src] = 0;
        // At most k stops means at most k+1 flights
        for (int i = 0; i <= k; i++) {
            int[] temp = price.clone();
            for (int[] flight : flights) {
                int u = flight[0];
                int v = flight[1];
                int cost = flight[2];
                if (price[u] != Integer.MAX_VALUE) {
                    temp[v] = Math.min(temp[v], price[u] + cost);
                }
            }
            price = temp;
        }
        return price[dst] == Integer.MAX_VALUE ? -1 : price[dst];
    }
}
