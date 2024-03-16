import java.util.*;

class Solution {
    public int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
    
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        
        int newNumer = numer1 * denom2 + numer2 * denom1;
        int newDenom = denom1 * denom2;
        
        int divisor = gcd(newNumer, newDenom);
        
        
        newNumer /= divisor;
        newDenom /= divisor;
        
        answer[0] = newNumer;
        answer[1] = newDenom;
        
        return answer;
    }
}