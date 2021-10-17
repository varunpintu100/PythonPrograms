#this is the class of the node
class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
    def get_data(self):
        return self.val
    def put_data(self,val):
        self.val=val
    def get_next(self):
        return self.next
    def set_next(self,next):
        self.next=next
#class of linked list
class Linkedlist(object):
    def __init__(self,head=None):
        self.head=head
        self.count=0
    def get_count(self):
        return self.count
    def insert(self,data):
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node
        self.count +=1
    def find(self,val):
        item =self.head
        while (item != None):
            if item.get_data()==val:
                return item
            else:
                item = item.get_next()
        return None
    def del_idx(self,idx):
        if idx > self.count-1:
            return 
    def dump_list(self):
        tempnode=self.head
        while (tempnode != None):
            print("Node :", tempnode.get_data())
            tempnode=tempnode.get_next()
itemlist=Linkedlist()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()
print(itemlist)
print("item count : ",itemlist.get_count())
print(itemlist.del_idx(0))
        
                
        