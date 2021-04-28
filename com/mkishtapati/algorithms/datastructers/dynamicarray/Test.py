from com.mkishtapati.algorithms.datastructers.dynamicarray import DynamicArray

if __name__=='__main__':
    arr = DynamicArray.DynamicArray()
    for i in range(0,5):
        arr.add(i)  
    arr.add(16)
    print(arr.capacity)
    print(arr.removeAt(5))
    print(arr.capacity)
    arr.add(18)
    print(arr.capacity)