class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] minArr = new int[queries.length];
        for (int i = 0; i < queries.length; i++){
            int temp = -1;
            int k = queries[i][2];
            for (int j = queries[i][0]; j <= queries[i][1]; j++){
                if (k < arr[j]){
                    if (temp == -1) temp = arr[j];
                    else{
                        if(temp > arr[j])   temp = arr[j];
                    }
                    
                }
            }
            minArr[i] = temp;
              
        }
        return minArr;
    }
}