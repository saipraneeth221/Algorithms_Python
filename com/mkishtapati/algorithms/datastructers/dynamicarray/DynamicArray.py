import ctypes

class DynamicArray(object):
    
    def __init__(self):
        self.length=0;
        self.capacity=16;
        self.Arr=self.make_array()
        
    def make_array(self):
        """
        Returns a new array with new_cap capacity
        """
        return (self.capacity * ctypes.py_object)()
    
    def size(self):
        """
        Return number of elements sorted in array
        """
        return self.length
    
    def isEmpty(self):
        """
        check if the array is empty or not
        """
        return self.size()==0;
    
    def get(self,index):
        if (index >= self.length or index < 0):
            raise IndexError
        return self.Arr[index]
    
    def set(self,index,element):
        if (index >= self.length or index < 0):
            raise IndexError
        self.Arr[index]=element
        
    def clear(self):
        for i in range(0,self.Arr.length):
            self.Arr[i]=None
        
        self.length=0
        
    def add(self,element):
        if(self.length+1>=self.capacity):
            if(self.capacity==0):
                self.capacity=1
            else:
                self.capacity=self.capacity*2
            
            arr1=self.make_array()   
            for i in range(0,self.length):
                arr1[i]=self.Arr[i]
                
            self.Arr=arr1    
        
        self.Arr[self.length]=element    
        self.length=self.length+1  
        
    def removeAt(self,rm_index):
        if (rm_index >= self.length or rm_index < 0):
            raise IndexError
        data=self.Arr[rm_index]
        arr1=((self.length-1) * ctypes.py_object)()
        temp=False
        for i in range(0,self.length):
            if i == rm_index:
                temp=True
            else:
                if temp==False:
                    arr1[i]=self.Arr[i]
                else:
                    arr1[i-1]=self.Arr[i]
        
        self.Arr=arr1
        self.length=self.length-1
        self.capacity= self.length
        return data
    
    def remove(self,element):
        index=self.indexOf(element)
        if index==-1: 
            return False
        self.removeAt(index)
        return True
    
    def indexOf(self,element):
        for i in range(0,self.length):
            if element is None:   
                if self.arr[i]==None:
                    return i
            else:
                if self.arr[i]==element:
                    return i
                
        return False
    
    def contains(self,element):
        return self.indexOf(element) != -1
    
    
    
        
    
        


    