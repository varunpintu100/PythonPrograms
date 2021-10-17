# class Movie:
#     def __init__(self,mov_id,mov_name,tick_cost,M_catageory='Default'):
#         self.mov_id=mov_id
#         self.mov_name=mov_name
#         self.tick_cost=tick_cost
#         self.M_catageroy=M_catageory
#     def Price_category(self):
#         cat=['General','Silver','Gold','Platinum']
#         if self.tick_cost in range(0,150):
#             self.M_catageroy = cat[0]
#         elif self.tick_cost in range(150,250):
#             self.M_catageroy = cat[1]
#         elif self.tick_cost in range(250,350):
#             self.M_catageroy = cat[2]
#         elif self.tick_cost >=350:
#             self.M_catageroy = cat[3]
#
# class Movie_Ticket:
#     def __init__(self,cust_name,mov_name,viewer_count,tot_cost):
#         self.cust_name=cust_name
#         self.mov_name=mov_name
#         self.viewer_count=viewer_count
#         self.tot_cost=tot_cost
# def cat_count(list_movies):
#     for i in list_movies:
#         i.Price_category()
#         for 
class Movie:
        def __init__(self,MId,MName,TCost,CCategory="Default"):
            self.Movie_1id=MId
            self.Movie_Name=MName
            self.Ticket_Cost=TCost
            self.Cost_Category=CCategory
        def __str__(self):
            return (str(self.__dict__))
if __name__=="__main__":    
        Movie_Objects=[] 
        Num=int(input("enter the number of test cases : "))
        for i in range(Num):
            mid=int(input("enter the movie ID : "))#taking movie id as input 
            mname=input("Enter movie name : ")#taking movie name as input 
            tcost=int(input("Enter ticket cost : "))#taking ticket cost 
            M = Movie(mid,mname,tcost)#making m as the object of the class Movie
            Movie_Objects.append(M)#appending the class object to the string 
        print(Movie_Objects.__getitem__(1))