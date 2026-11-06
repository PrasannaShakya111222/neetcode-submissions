class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        boolean[][] isPrerequisite =
            new boolean[numCourses][numCourses];
        // Mark direct prerequisites
        for (int[] p : prerequisites) {
            isPrerequisite[p[0]][p[1]] = true;
        }
        // Floyd-Warshall
        for (int k = 0; k < numCourses; k++) {
            for (int i = 0; i < numCourses; i++) {
                for (int j = 0; j < numCourses; j++) {
                    if (isPrerequisite[i][k] &&
                        isPrerequisite[k][j]) {
                        isPrerequisite[i][j] = true;
                    }
                }
            }
        }
        // Ans queries
        List<Boolean> result = new ArrayList<>();

        for (int[] q : queries) {
            result.add(isPrerequisite[q[0]][q[1]]);
        }
        return result;
    }
}
