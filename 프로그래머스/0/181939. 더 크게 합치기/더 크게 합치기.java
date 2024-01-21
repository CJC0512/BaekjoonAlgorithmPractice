class Solution {
    public int solution(int a, int b) {
        int aPlusb = Integer.parseInt((Integer.toString(a)+Integer.toString(b)));
        int bPlusa = Integer.parseInt((Integer.toString(b)+Integer.toString(a)));
        return (aPlusb >= bPlusa) ? aPlusb : bPlusa ;
    }
}