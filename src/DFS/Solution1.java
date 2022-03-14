package DFS;

// 타겟 넘버
public class Solution1 {

    // idx: 몇 번째 인덱스인지. sum: idx까지 누적된 값
    public int dfs(int[] numbers, int target, int idx, int sum) {
        // 모든 정수를 탐색했을 때
        if (idx == numbers.length) {
            if (sum == target) {
                return 1;
            }
            return 0;
        }

        return dfs(numbers, target, idx+1, sum+numbers[idx]) + dfs(numbers, target, idx+1, sum-numbers[idx]);

    }

    public int solution(int[] numbers, int target) {
        int answer = 0;
        answer = dfs(numbers, target, 0, 0);

        return answer;
    }

    public static void main(String[] args) {
        Solution1 sol = new Solution1();
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;
        System.out.println(sol.solution(numbers, target));
    }
}
