package BruteForce;

import java.util.ArrayList;

// 완전탐색 - 모의고사
public class Solution1 {

    public int[] solution(int[] answers) {

        int n = answers.length; // 문제 수
        int[] person1 = {1, 2, 3, 4, 5};
        int[] person2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] score = new int[3];

        for (int i = 0; i < n; i++) {
            if (person1[i%person1.length] == answers[i]) score[0]++;
            if (person2[i%person2.length] == answers[i]) score[1]++;
            if (person3[i%person3.length] == answers[i]) score[2]++;
        }

        int max = Math.max(Math.max(score[0], score[1]), score[2]);

        ArrayList<Integer> maxList = new ArrayList<>();
        if (max == score[0]) maxList.add(1);
        if (max == score[1]) maxList.add(2);
        if (max == score[2]) maxList.add(3);

        int[] answer = new int[maxList.size()];
        for (int i = 0; i < maxList.size(); i++) {
            answer[i] = maxList.get(i);
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] answers = {1, 2, 3, 4, 5, 2, 4};
        Solution1 sol = new Solution1();
        int[] answer = sol.solution(answers);

        for (int i = 0; i < answer.length; i++) {
            System.out.println(answer[i]);
        }
    }
}
