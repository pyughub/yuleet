#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> res;
        const int n = static_cast<int>(nums.size());

        for (int i = 0; i < n - 2; ++i) {
            const int ni = nums[i];
            if (ni > 0) {
                break;
            }
            if (i > 0 && ni == nums[i - 1]) {
                continue;
            }
            if (ni + nums[i + 1] + nums[i + 2] > 0) {
                break;
            }
            if (ni + nums[n - 1] + nums[n - 2] < 0) {
                continue;
            }

            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                const int s = ni + nums[j] + nums[k];
                if (s < 0) {
                    ++j;
                } else if (s > 0) {
                    --k;
                } else {
                    res.push_back({ni, nums[j], nums[k]});
                    ++j;
                    --k;
                    while (j < k && nums[j] == nums[j - 1]) {
                        ++j;
                    }
                    while (j < k && nums[k] == nums[k + 1]) {
                        --k;
                    }
                }
            }
        }

        return res;
    }
};
