package DFS;

public class Solution2 {
    public int solution(int n, int[][] computers) {
        int count = 0;
        boolean[] visited = new boolean[n+1];

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                network(n, i, computers, visited);
                count++;
            }
        }
        return count;
    }

    public static void network(int n, int idx, int[][] computers, boolean[] visited) {
        visited[idx] = true;

        for (int i = 0; i < n; i++) {
            if (!visited[i] && computers[idx][i] == 1)
                network(n, i, computers, visited);
        }
    }

}
