SinglyLinkedListNode* linked_list_pivot(SinglyLinkedListNode* lst, int key) {
    /* If(node > k)
    If (node < k)
    If (node == k)*/
    SinglyLinkedListNode* greaterHead = NULL;
    SinglyLinkedListNode* greaterLast = NULL;
    SinglyLinkedListNode* smallerHead = NULL;
    SinglyLinkedListNode* smallerLast = NULL;
    SinglyLinkedListNode* eqlHead = NULL;
    SinglyLinkedListNode* eqlLast = NULL;
    /*Create a new list for each set of nodes*/
    while(lst != NULL){
        if(lst->data>key){
            if(greaterHead == NULL){
                greaterHead = greaterLast;
                greaterLast = lst;
            } else{
                greaterLast->next = lst;
                greaterLast = lst;
            }
        } else if (lst->data<key) {
            if(smallerHead == NULL){
                smallerHead = smallerLast;
                smallerLast = lst;
            } else {
                smallerLast->next = lst;
                smallerLast = lst;
            }
        } else if (lst->data==key) {
            if(eqlHead == NULL){
                eqlHead = eqlLast;
                eqlLast = lst;
            } else {
                eqlLast->next = lst;
                eqlLast = lst;
            }
        }
    }
    lst = lst->next;
    //Put the lists together
    if(smallerHead != NULL){
        if(eqlHead!=NULL)
            return eqlHead;
        eqlLast->next = greaterHead;
        return eqlHead;
    }
    if(eqlHead == NULL){
        smallerLast->next = greaterHead;
        return smallerLast;
    }
    smallerLast->next = eqlHead;
    eqlLast->next = greaterHead;
    return smallerHead;
}
