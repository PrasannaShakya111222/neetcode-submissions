class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet<>(Arrays.asList(deadends));
        // Starting state is blocked
        if (dead.contains("0000")) return -1;
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.offer("0000");
        visited.add("0000");
        int turns = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String current = queue.poll();
                // Target reached
                if (current.equals(target)) {
                    return turns;
                }
                char[] wheels = current.toCharArray();
                // Try rotating each of 4 wheels
                for (int j = 0; j < 4; j++) {
                    char original = wheels[j];
                    // Rotate forward
                    wheels[j] = (char) (original == '9'
                            ? '0' : original + 1);

                    String next = new String(wheels);
                    if (!dead.contains(next) &&
                        visited.add(next)) {
                        queue.offer(next);
                    }
                    // Rotate backward
                    wheels[j] = (char) (original == '0'
                            ? '9' : original - 1);

                    next = new String(wheels);
                    if (!dead.contains(next) &&
                        visited.add(next)) {
                        queue.offer(next);
                    }
                    // Restore original wheel
                    wheels[j] = original;
                }
            }
            turns++;
        }
        return -1;
    }
}