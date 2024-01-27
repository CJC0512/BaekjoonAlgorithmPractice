class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        int result = 0;
        int idx = 0;
        while(numLog.length -1 > idx){
            result = numLog[idx+1] - numLog[idx];
            switch(result){
                case 1:
                    answer += "w";
                    break;
                case -1:
                    answer += "s";
                    break;
                case 10:
                    answer += "d";
                    break;
                case -10:
                    answer += "a";
                    break;
            }
            idx++;
        }
        return answer;
    }
}