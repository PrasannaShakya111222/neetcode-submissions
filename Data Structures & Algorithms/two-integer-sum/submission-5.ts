class Solution {
    /**
     * @param nums Array of numbers
     * @param target Target sum
     * @return Indices of the two numbers
     */
    twoSum(nums:number[],target:number):number[]{
        const map =new Map<number,number>();
        for (let i = 0;i<nums.length;i++){
            const complement= target-nums[i];
            if (map.has(complement)){
                return [map.get(complement)!,i];
            }
            map.set(nums[i],i);
        }
        return [];
    }
}