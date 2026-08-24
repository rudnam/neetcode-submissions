class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indices = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            if (indices.containsKey(target - num)) {
                return new int[]{indices.get(target - num), i};
            }

            indices.put(num, i);
        }

        throw new IllegalArgumentException("There are no pair of indices that satisfy the condition");
    }

}
