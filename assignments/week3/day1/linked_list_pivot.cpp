SinglyLinkedListNode* linked_list_pivot(SinglyLinkedListNode* lst, int key) {
    // arrange nodes
    SinglyLinkedList *prev_aft = new SinglyLinkedList();
    SinglyLinkedList *prev_bef = new SinglyLinkedList();
    SinglyLinkedList *pivot_ = new SinglyLinkedList();
    SinglyLinkedListNode *curr_ = lst;
    while(curr_){
    // if key is greater than pivot
        if(curr_->data<key){
            SinglyLinkedListNode *temp = curr_;
            // insert into prev_aft list
            prev_aft->insert_node(temp->data);
            // release memory
            temp = nullptr;
            delete temp;
        }
        else if(curr_->data>key){
            SinglyLinkedListNode *temp = curr_;
            prev_bef->insert_node(temp->data);
            temp = nullptr;
            delete temp;
        }
        else{
            SinglyLinkedListNode *temp = curr_;
            pivot_->insert_node(temp->data);
            temp = nullptr;
            delete temp;
        }
        curr_ = curr_->next;
    }
    // sorted result list
    SinglyLinkedList *res_ = new SinglyLinkedList();
    curr_ = prev_aft->head;
    while(curr_){
        SinglyLinkedListNode *temp = curr_;
        res_->insert_node(temp->data);
        temp = nullptr;
        delete temp;
        curr_ = curr_->next;
    }
    curr_ = pivot_->head;
    while(curr_){
        SinglyLinkedListNode *temp = curr_;
        res_->insert_node(temp->data);
        temp = nullptr;
        delete temp;
        curr_ = curr_->next;
    }
    curr_ = prev_bef->head;
    while(curr_){
        SinglyLinkedListNode *temp = curr_;
        res_->insert_node(temp->data);
        temp = nullptr;
        delete temp;
        curr_ = curr_->next;
    }

    return res_->head;
}