
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses, 0);
        // Build graph
        for (auto& p : prerequisites) {
            int a = p[0];
            int b = p[1];
            adj[b].push_back(a);
            indegree[a]++;
        }
        // Add courses with no prerequisites.
        queue<int> q;

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        int completed = 0;
        // BFS
        while (!q.empty()) {
            int course = q.front();
            q.pop();
            completed++;
            for (int next : adj[course]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    q.push(next);
                }
            }
        }
        // If all courses completed, no cycle exists.
        return completed == numCourses;
    }
};
