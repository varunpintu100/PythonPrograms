
class Movie:
    def __init__(self,MId,MName,TCost,CCategory="Default"):
        self.Movie_1id=MId
        self.Movie_Name=MName
        self.Ticket_Cost=TCost
        self.Cost_Category=CCategory
            
    def Assign_Price_Category(self):
        Category=["General","Silver","Gold","Platinum"]
        if self.Ticket_Cost in range(0,150):
            self.Cost_Category=Category[0]
        elif self.Ticket_Cost in range(150,250):
            self.Cost_Category=Category[1]
        elif self.Ticket_Cost in range(250,350):
            self.Cost_Category=Category[2]
        elif(self.Ticket_Cost>=350):
            self.Cost_Category=Category[3]
                
class Movie_Ticket:
    def __init__(self,CName,MName,VCount,TTCost):
        self.Customer_Name=CName
        self.Movie_Name=MName
        self.Viewer_Count=VCount
        self.Total_Ticket_Cost=TTCost
def getCategoryWiseCount(List_Movie_Objects): 
    for obj in List_Movie_Objects:
        obj.Assign_Price_Category()
    Dictionary={}
    for Obj in List_Movie_Objects:
        Cost_Cat=Obj.Cost_Category
        if Cost_Cat not in Dictionary.keys():
            Dictionary[Cost_Cat]=1
        else:
            Dictionary[Cost_Cat]=Dictionary[Cost_Cat]+1
    return Dictionary
def bookMovieTicket(MObjects,CName,MName,VCount):
    for Object in Movie_Objects:
        val=Object.Movie_Name.lower()==MName.lower()
        if(val):
            Total_Ticket_Cost=Object.Ticket_Cost*VCount 
            return Total_Ticket_Cost
   
if __name__=="__main__":    
    Movie_Objects=[] 
    Num=int(input())
    for i in range(Num):
        mid=int(input())#taking movie id as input 
        mname=input()#taking movie name as input 
        tcost=int(input())#taking ticket cost 
        M = Movie(mid,mname,tcost)#making m as the object of the class Movie
        Movie_Objects.append(M)#appending the class object to the string 
    CName=input() 
    MName=input() 
    VCount=int(input())
    Dictionary=getCategoryWiseCount(Movie_Objects)
    B=bookMovieTicket(Movie_Objects,CName,MName,VCount) 
    print('Category wise ticket count:')
    for i in Dictionary:
        print('{}:{}'.format(i,Dictionary[i]))
    print(CName,B)

