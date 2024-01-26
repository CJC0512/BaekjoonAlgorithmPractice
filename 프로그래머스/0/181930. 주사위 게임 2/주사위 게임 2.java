
class Solution {
    public int solution(int a, int b, int c) {
        int answer = 1;
        int powNum = 1;
        if (a == b && b == c){
            powNum = 3;
        }    
        else{
            if (a == b || a == c || b == c) powNum = 2;
        }
        for (int i = 1; i <= powNum; i++){
            answer = answer * (int)(Math.pow(a,i) + Math.pow(b,i) + Math.pow(c,i));
        }
        return answer;
    }
}