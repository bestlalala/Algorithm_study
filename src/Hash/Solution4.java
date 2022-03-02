package Hash;

import java.util.*;

// 베스트앨범
public class Solution4 {

    static class Music {
        String genre;
        int play;
        int idx;

        public Music(String genre, int play, int idx) {
            this.genre = genre;
            this.play = play;
            this.idx = idx;
        }
    }

    public int[] solution(String[] genres, int[] plays) {

        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            map.put(genres[i], map.getOrDefault(genres[i], 0) + plays[i]);
        }

        // 장르별 내림차순으로 정렬
        List<String> genres_ordered = new ArrayList<>(map.keySet());
        Collections.sort(genres_ordered, (v1, v2) -> map.get(v2) - map.get(v1));

        ArrayList<Music> result = new ArrayList<>(); // 최종 결과를 담을 리스트
        for (String genre : genres_ordered) {
            ArrayList<Music> list = new ArrayList<>();
            for (int i = 0; i < genres.length; i++) {
                if (genres[i].equals(genre)) {
                    list.add(new Music(genre, plays[i], i));
                }
            }
            Collections.sort(list, (o1, o2) -> o2.play - o1.play);
            result.add(list.get(0)); // 1개는 무조건 수록
            if (list.size()!=1)
                result.add(list.get(1));
        }

        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i).idx;
        }

        return answer;
    }

    public static void main(String[] args) {
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};
        Solution4 sol = new Solution4();
        int[] result = sol.solution(genres, plays);
        for (int i = 0; i < result.length; i++) {
            System.out.println(result[i]);
        }
    }
}
