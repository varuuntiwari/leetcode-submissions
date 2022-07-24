class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i, j;
        for(i = 0; i < nums.size(); i++) {
            for(j = 0; j < nums.size(); j++) {
                if(j == i) continue;
                if(nums[j] == target - nums[i]) {
                    return vector<int>{i, j};
                }
            }
        }
        return vector<int>{};
    }
};