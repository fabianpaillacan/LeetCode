#include <string>
class Solution {
public:
    bool isPalindrome(int x) {
        string b = to_string(x);
        string reversa = b;
        reverse(reversa.begin(), reversa.end());
        if (b == reversa){
            return true;
        }
        else{
            return false;
        }  
    }
};