package Hash;

import java.util.HashMap;

// 위장
public class Solution3 {
    public int solution(String[][] clothes) {
        // key : value = 종류 : 의상 개수
        HashMap<String, Integer> map = new HashMap<>();

        for (int i = 0; i < clothes.length; i++) {
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1], 0)+1);
        }

        int cnt = 1;
        for (String cloth : map.keySet()) {
            cnt *= map.get(cloth)+1;
        }

        return cnt-1;

    }

    public static void main(String[] args) {
        String[][] clothes = {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
        Solution3 sol = new Solution3();
        System.out.println(sol.solution(clothes));
    }
}
