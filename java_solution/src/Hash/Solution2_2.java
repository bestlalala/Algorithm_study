package Hash;

import java.util.Arrays;

// 전화번호 목록 _ 참고하
public class Solution2_2 {
    // O(n^2) => 시간 초과 뜸
    public boolean solution1(String[] phoneBook) {
        for (int i = 0; i < phoneBook.length; i++) {
            for (int j = i+1; j < phoneBook.length; j++) {
                if (phoneBook[i].startsWith(phoneBook[j])) return false;
                if (phoneBook[j].startsWith(phoneBook[i])) return false;
            }
        }
        return true;
    }

    public boolean solution2(String[] phoneBook) {
        Arrays.sort(phoneBook);
        for (int i = 0; i < phoneBook.length-1; i++) {
            if (phoneBook[i+1].contains(phoneBook[i])) {
                return false;
            }
        }
        return true;
    }
}
