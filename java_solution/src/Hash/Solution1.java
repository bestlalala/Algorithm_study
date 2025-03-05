package Hash;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

// 완주하지 못한 선수
public class Solution1 {

    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        for (String player : participant)
            map.put(player, map.getOrDefault(player, 0) + 1);
        for (String player : completion)
            map.put(player, map.get(player) - 1);

        for (String key : map.keySet()) {
            if (map.get(key) != 0) {
                answer = key;
                break;
            }
        }

//        Iterator<Map.Entry<String, Integer>> iter = map.entrySet().iterator();
//
//        while (iter.hasNext()) {
//            Map.Entry<String, Integer> entry = iter.next();
//            if (entry.getValue() != 0) {
//                answer = entry.getKey();
//                break;
//            }
//        }
        return answer;
    }

    public static void main(String[] args) {
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};
        Solution1 solution1 = new Solution1();
        System.out.println(solution1.solution(participant, completion));
    }

}
