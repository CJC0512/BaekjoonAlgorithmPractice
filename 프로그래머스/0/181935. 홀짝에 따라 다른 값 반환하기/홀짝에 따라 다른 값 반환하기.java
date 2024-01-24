class Solution {
    public int solution(int n) {
        int answer = 0;
        int num = 1;
        if (n % 2 != 0){
            while(num <= n){
                answer += num;
                num+=2;
            }            
        }
        else {
            num ++;
            while(num <= n){
                answer += num*num;
                num+=2;
            }       
        }
        return answer;
    }
}