class Solution {
    public:
        int singleNumber(vector<int>& nums) {
            if(nums.size() == 1){
                return nums[0];
            }
            else {
                for(int i = 0; i<nums.size();i++){
                    int cont = count(nums.begin(),nums.end(),nums[i]);
                    if(cont == 1){
                        return nums[i];
                    }
                }
            }
            return 0;
        }
    };