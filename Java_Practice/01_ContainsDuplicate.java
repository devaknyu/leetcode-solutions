class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> res = new HashSet<>();
        for (int n: nums){
            res.add(n);
        }
        return res.size() != nums.length;
    }
}