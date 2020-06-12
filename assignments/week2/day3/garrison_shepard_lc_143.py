 def reorderList(self, head):
        if not head: 
            return    
        if not head.next:
            return 
        if not head.next.next:
            return 
        
        prev = head
        cur = head.next
        tail = prev
        
        while cur:
            tail = prev
            if not tail.next.next:
                break
            
            while tail.next.next:
                tail = tail.next   
            
            end = tail
            tail = tail.next
            end.next = None  
            
            prev.next = tail 
            tail.next = cur
			
            prev = cur;
            cur = cur.next