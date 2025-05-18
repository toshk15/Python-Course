from queue import Queue  
  
def Print(queue): 
    while (not queue.empty()): 
        print(queue.queue[0], end = ", ")  
        queue.get() 
  

def reversequeue(queue): 
    Stack = []  
    while (not queue.empty()): 
        #print("Que tiene la cola", queue)
        Stack.append(queue.queue[0])  
        print("que tiene la cola", queue.queue[0])
        print("Que tiene la Pila ",Stack)
        queue.get() 
    while (len(Stack) != 0):  
        queue.put(Stack[-1]) 
        #print("que tiene la cola en el segundo ciclo", queue.put(Stack[-1]) )
        Stack.pop()
        print("Pop sobre la pila ",Stack) 
  

if __name__ == '__main__': 
    queue = Queue() 
    queue.put(10)  
    queue.put(20)  
    queue.put(30)  
    queue.put(40)  
    queue.put(50)  
     
  
    reversequeue(queue)  
    Print(queue) 