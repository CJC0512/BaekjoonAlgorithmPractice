class Solution {
    public int solution(int n, String control) {
        int answer = n;
        int index = 0;
        while(index < control.length()){
            switch (control.charAt(index)){
                case 'w':   answer++; break;
                case 's':   answer--; break;
                case 'd':   answer+=10; break;
                case 'a':   answer-=10; break;
            }
            index++;
        }
        return answer;
    }
}