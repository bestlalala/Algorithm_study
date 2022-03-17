package DFS;

import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

// 인접 행렬로 구현한 DFS
public class DFS_Array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // 정점의 개수
        int m = sc.nextInt(); // 간선의 개수
        int v = sc.nextInt(); // 탐색을 시작할 정점의 번호

        boolean visited[] = new boolean[n+1]; // 방문 여부를 검사할 배열
        int[][] adjArray = new int[n+1][n+1];

        // 두 정점 사이에 여러 개의 간선이 있을 수 있다.
        // 입력으로 주어지는 간선은 양방향이다.
        for (int i = 0; i < m; i++) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();

            adjArray[v1][v2] = 1;
            adjArray[v2][v1] = 1;
        }

        System.out.println("DFS- 인접행렬 / 재귀로 구현");
        dfs_array_recursion(v, adjArray, visited);

        Arrays.fill(visited, false); // 스택 DFS를 위해 visited 배열 초기화
    }

    public static void dfs_array_recursion(int v, int[][] adjArray, boolean[] visited) {
        int l = adjArray.length - 1;
        visited[v] = true;
        System.out.println(v + " ");

        for (int i = 1; i <= l; i++) {
            if (adjArray[v][i] == 1 && !visited[i]) {
                dfs_array_recursion(i, adjArray, visited);
            }
        }
    }

    public static void dfs_array_stack(int v, int[][] adjArray, boolean[] visited, boolean flag) {
        int l = adjArray.length-1;
        Stack<Integer> stack = new Stack<>();
        stack.push(v);
        visited[v] = true;
        System.out.println(v + " ");

        while (!stack.isEmpty()) {
            int w = stack.peek();
            flag = false;

            for (int i = 1; i <= l; i++) {
                if (adjArray[w][i] == 1 && !visited[i]) {
                    stack.push(i);
                    System.out.println(i + " ");
                    visited[i] = true;
                    flag = true;

                    break;
                }
            }
            if (!flag) {
                stack.pop();
            }
        }
    }
}
