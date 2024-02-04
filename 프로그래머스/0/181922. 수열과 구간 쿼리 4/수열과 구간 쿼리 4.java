class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for (int j = 0; j < queries.length; j++){
            for(int i = queries[j][0]; i <= queries[j][1]; i++){
                if (i % queries[j][2] == 0){
                    arr[i]++;
                }
            }
        }
        return arr;
    }
}