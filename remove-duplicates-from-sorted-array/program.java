class Solution {
    public int removeDuplicates(int[] nums) 
    {
        int l=nums.length;
        int nums1[]=new int[l];
        int k=0;
        for(int i=0;i<l;i++)
        {
            nums1[i]=nums[i];
        }
        for(int i=0;i<l;i++)
        {
            if(nums.contains(nums[i]))
            {
                continue;
            }
            else
            {
                nums[i]=nums1[i];
                k++;
            }
        }
        return k;
    }
}