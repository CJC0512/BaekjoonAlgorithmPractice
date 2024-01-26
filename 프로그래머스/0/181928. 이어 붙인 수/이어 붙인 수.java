class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String hol = "";
        String jjack = "";
        for(int num : num_list){
            if (num % 2 == 0) jjack += num;
            else hol += num;
        }
        answer = Integer.parseInt(hol)+Integer.parseInt(jjack);
        return answer;
    }
}