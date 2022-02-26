package Hash;

public class Solution1 {

    public String solution(String[] participant, String[] completion) {
        String answer = "";
        String member = "";
        Boolean sameName = false;

        for (int i = 0; i < participant.length; i++) {
            for (int j = i+1; j < participant.length-1; j++) {
                if (participant[i] == participant[j]) {
                    sameName = true;
                }
            }

            int flag = 0;
            for (int j = 0; j < completion.length; j++) {
                if (participant[i] == completion[j]) {
                    flag = 1;
                }
            }
            if (flag == 0) {
                answer = participant[i] + "는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.";
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        String[] participant = {"leo", "kiki", "eden"};
        String[] completion = {"eden", "kiki"};
        Solution1 solution1 = new Solution1();
        System.out.println(solution1.solution(participant, completion));

    }

}
