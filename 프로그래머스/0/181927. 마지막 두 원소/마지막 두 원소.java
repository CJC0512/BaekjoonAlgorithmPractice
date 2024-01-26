class Solution {
    public int[] solution(int[] num_list) {
        int len = num_list.length;
        int[] answer = new int[(len + 1)];
        for(int i = 0; i < len; i++){
            answer[i] = num_list[i];
        }
        if (num_list[len-1] > num_list[len-2])
            answer[len] = num_list[len-1] - num_list[len-2];
        else
            answer[len] = 2*num_list[len-1];
        return answer;
    }
}