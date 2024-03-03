import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n, int k) {
        int[] answer = {};
        List<Integer> resultList = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                resultList.add(i);
            }
        }
        
        answer = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            answer[i] = resultList.get(i);
        }
        
        return answer;
    }
}