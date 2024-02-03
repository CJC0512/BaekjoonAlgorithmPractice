class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int temp;
        for (int k = 0; k < queries.length; k++){
            temp = arr[queries[k][0]];
            arr[queries[k][0]] = arr[queries[k][1]];
            arr[queries[k][1]] = temp;
        }
        return arr;
    }
}