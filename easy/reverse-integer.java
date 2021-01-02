class Solution {
    public int reverse(int x) {
        final long max = Integer.MAX_VALUE;
        final long min = Integer.MIN_VALUE;
       String str = Integer.toString(x);
        String rev = "";
        int goal = 0;
        
        if(x >= 0){
            for(int i = str.length() - 1; i > -1; i--){
                rev += str.charAt(i);
                
            }try{
                goal = Integer.parseInt(rev);
            }catch(NumberFormatException e){
                goal = 0;
            }
        }else if(x < 0){
            x = Math.abs(x);
            rev += "-";
            for(int i = str.length() - 1; i > 0; i--){
                rev += str.charAt(i);
                
            }
            }try{
                goal = Integer.parseInt(rev);
            }catch(NumberFormatException e){
                goal = 0;
            }
            
        
       // System.out.println(rev);
        
       
        return goal;
    }
}
