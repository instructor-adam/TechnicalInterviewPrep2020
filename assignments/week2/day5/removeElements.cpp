class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *curr = head;
        ListNode *prev = curr;
        
        if(head==nullptr){
            return head;
        }
        
        ListNode *temp;
        while(curr){
          //cout << curr->val << " ";
           if(curr->val == val){
                temp = curr->next;
                prev->next = temp;
                curr = temp;
           } 
           else{
                temp = curr->next;
                prev = curr;
                curr = temp;             
           }
       }
       // if linked list is of size 1 e.g. 1->nullptr
       if(head->val == val){
           return head->next;
       }
       return head;
    }
};

// https://leetcode.com/problems/remove-linked-list-elements/submissions/