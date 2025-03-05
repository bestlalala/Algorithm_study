package BruteForce;

import java.util.HashSet;
import java.util.Iterator;

// 완전 탐색 - 소수 찾기
public class Solution2 {
    HashSet<Integer> nums = new HashSet<>();

    public int solution(String numbers) {

        // 모든 조합의 수를 만든다.
        allNum("", numbers);

        // 소수의 개수만 센다.
        int cnt = 0;
        Iterator<Integer> it = nums.iterator();
        while (it.hasNext()) {
            // 소수인지 판별하는 메서드 만들어서 이용
            if (isPrime(it.next()))
                cnt++;
        }
        return cnt;
    }

    // 재귀 함수
    public void allNum(String comb, String others) {
        // 현재 조합을 set 에 추가한다.
        if (!comb.equals(""))
            nums.add(Integer.valueOf(comb));

        // 남은 숫자 중 한 개를 더해 새로운 조합을 만든다.
        for (int i = 0; i < others.length(); i++)
            allNum(comb + others.charAt(i), others.substring(0, i) + others.substring(i+1));
    }

    public boolean isPrime(int num) {
        // 0과 1은 소수가 아님.
        if (num == 0 || num == 1)
            return false;

        // 에라토스테네스의 체에 따라 lim 까지 배수 여부 확인
        for (int i = 2; i <= (int) Math.sqrt(num); i++) {
            if (num%i == 0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution2 sol = new Solution2();
        String numbers = "011";
        System.out.println(sol.solution(numbers));
    }
}
