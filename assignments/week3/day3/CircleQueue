/* https://leetcode.com/problems/design-circular-queue/ */

class MyCircularQueue {
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        for(int i = 0; i < k; ++i){
          circleQueue.push_back(-1)  ;
        }
        queueSize = k;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
    // 6 % 5
        
        if(numElements == 0){
            front = front%queueSize; // new front index
        } 
        
        if(numElements < queueSize){
            rear = (rear + 1);
            circleQueue[rear%queueSize] = value;
            
            cout << "currRear: " << circleQueue[rear%queueSize] << ", " << rear<< endl;
            numElements++;
            return true;
        }else{
            return false;
        }
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if(numElements > 0){
            front = front + 1;
            circleQueue[front % queueSize] == -1;
            cout << circleQueue[front % queueSize] << ", " << front%queueSize << endl;
            
            
            numElements--;
            
//             if(numElements < 0){
                
//             }
            return true;
        }else{
            return false;
        }
    }
    
    /** Get the front item from the queue. */
    int Front() {
        return circleQueue[front%queueSize];
    }
    
    /** Get the last item from the queue. */
    int Rear() {
        return circleQueue[rear%queueSize];
    }
    
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return numElements == 0;
    }
    
    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return numElements == queueSize;
    }
    
private:
    vector<int> circleQueue;
    int queueSize = 0;
    int numElements = 0;
    int front = -1, rear = -1; // indices to front and rear
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
