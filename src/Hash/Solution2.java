package Hash;

import java.util.HashMap;

// 전화번호 목록
public class Solution2 {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> map = new HashMap<>();
        for (String num : phone_book) {
            map.put(num, map.get(num));
        }

        for (int i = 0; i < phone_book.length; i++) {
            for (int j = 0; j < phone_book[i].length(); j++) {
                if (map.containsKey(phone_book[i].substring(0, j)))
                    answer = false;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        String[] phone_book = {"123","456","789"};
        Solution2 sol = new Solution2();
        System.out.println(sol.solution(phone_book));
    }
}
