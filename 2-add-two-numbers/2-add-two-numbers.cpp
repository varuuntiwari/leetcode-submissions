/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode();
        ListNode* tmp = res;
        int x, y, sum, carry = 0;
        while(l1 != NULL || l2 != NULL || carry != 0) {
            if(l1)
                x = l1 -> val;
            else
                x = 0;
            //////////////////
            if(l2)
                y = l2 -> val;
            else
                y = 0;
            
            sum = carry + x + y;
            carry = sum/10;
            tmp -> next = new ListNode(sum%10);
            tmp = tmp -> next;
            
            if(l1)
                l1 = l1 -> next;
            else
                l1 = nullptr;
            ////////////////////
            if(l2)
                l2 = l2 -> next;
            else
                l2 = nullptr;
            
        }
        return res -> next;
    }
};