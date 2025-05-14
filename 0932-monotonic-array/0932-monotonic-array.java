class Solution {
    public boolean isMonotonic(int[] nums) {
        boolean ase = true;
        boolean des = true;

        for(int i = 0; i < nums.length -1;i++){
            if(nums[i] < nums[i+1]){
                des = false ;      
            }
            else if(nums[i] > nums[i+1]){
                ase = false ;
            }          
        }
        return ase || des;
    }
}