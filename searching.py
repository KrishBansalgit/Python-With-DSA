class search:
    def searhing(self,target):
        li=[1,4,5,6,7,8,89,56,34,23,6,7,44,2,4,5,3,4,5,45,234,5456,234,56,34,54,2234,556]
        for index,value in enumerate(li):
            if value == target:
                print("the target number is find succesfully ")
                return index                
        return -1
            
s=search()
print(s.searhing(56))
              