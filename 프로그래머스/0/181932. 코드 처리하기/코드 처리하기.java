class Solution {
    public String solution(String code) {
        String answer = "";
        String ret = "";
        int mode = 0;
        int idx = 0;
        
        while(idx < code.length()){
            if (code.charAt(idx) == '1'){
                    mode = (mode == 1) ? 0 : 1;
                    idx++;
                    continue;
                }
            switch (mode){
                case 0: 
                    if (idx % 2 == 0) 
                        ret += code.charAt(idx); 
                    break;
                case 1: 
                    if (idx % 2 == 1) 
                        ret +=code.charAt(idx); 
                    break;
            }
            idx++;
        }
        if (ret == "")
            return "EMPTY";
        else
            return ret;
    }
}