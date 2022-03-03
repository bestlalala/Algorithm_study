package BruteForce;

// 완전탐색 - 
public class Solution3 {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int m, n;

        for (m = 3; m <= 5000; m++) {
            for (n = 3; n <= 2000000; n++) {
                if (m < n) break;
                if ((brown == m*n-(m-2)*(n-2)) && (yellow == (m-2)*(n-2))) {
                    answer[0] = m;
                    answer[1] = n;
                }
            }
        }
        return answer;
    }
}
