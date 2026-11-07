class Solution {
    int[] parent;
    int[] rank;
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        int n = accounts.size();
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
        // Map each email to account index.
        Map<String, Integer> emailToId = new HashMap<>();
        // Connect accounts having common emails.
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < accounts.get(i).size(); j++) {
                String email = accounts.get(i).get(j);
                if (emailToId.containsKey(email)) {
                    union(i, emailToId.get(email));
                } else {
                    emailToId.put(email, i);
                }
            }
        }
        // Group emails according to their parent.
        Map<Integer, TreeSet<String>> groups = new HashMap<>();
        for (String email : emailToId.keySet()) {
            int root = find(emailToId.get(email));
            groups.putIfAbsent(root, new TreeSet<>());
            groups.get(root).add(email);
        }
        // Build final result.
        List<List<String>> result = new ArrayList<>();
        for (int root : groups.keySet()) {
            List<String> account = new ArrayList<>();
            account.add(accounts.get(root).get(0));
            account.addAll(groups.get(root));
            result.add(account);
        }
        return result;
    }
    // Find with path compression.
    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    // Union by rank.
    private void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY) return;
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        }
        else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        }
        else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }
}