/* 206. Reverse Linked List */

ListNode* reverseList(ListNode* head) {
    if(head == NULL){
        return head;
    }

    ListNode* curr_ptr = head->next; // start at second element
    ListNode* temp; // 'reverse' element 


    head->next = NULL; // point first element to NULL (new tail)

    while(curr_ptr != NULL){
        temp = curr_ptr;
        curr_ptr = curr_ptr->next; // get next element before pointer reverses
        temp->next = head; // point to prev_element
        head = temp;
    }

    return head;
}

/* 203. Remove Linked List Element: Incomplete */

ListNode* removeElements(ListNode* head, int val) {
    ListNode* curr_ptr = head;
    ListNode* prev_ptr = head;


    if(head == nullptr){
        return head;
    }

    if(head->next == nullptr && head->val == val){ // single element
        delete head;
        head = NULL;
        return head;
    }

    while(curr_ptr->next != nullptr){
        ListNode* remove;

        if(curr_ptr->val == val){
            remove = curr_ptr;
            prev_ptr->next = curr_ptr->next;
            curr_ptr = curr_ptr->next;

            delete remove;
            remove = NULL;
        }else{
            prev_ptr = curr_ptr;
            curr_ptr = curr_ptr->next;
        }

    }

    if(curr_ptr->next == nullptr && curr_ptr->val == val){
        prev_ptr->next = NULL;
        delete curr_ptr;
        curr_ptr = NULL;
    }

    return head;
}
