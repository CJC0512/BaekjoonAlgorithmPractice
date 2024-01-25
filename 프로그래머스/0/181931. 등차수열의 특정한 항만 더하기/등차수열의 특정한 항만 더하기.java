class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int stack = 0;
        for (int i = 0; i < included.length; i++){
            stack = stack + (included[i] == true ? i : 0);
            answer = answer + (included[i] == true ? a : 0);
        }
        return answer + d * stack;
    }
}