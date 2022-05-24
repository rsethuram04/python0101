class game():
 def __init__(self) :
     self.stonePaperScissor()
 
 def stonePaperScissor(self):
   import random 
   p1=0
   p2=0
   list=["stone","paper","scissor"]
   for i in range(0,100):
     no1=random.randrange(0,3)
     no2=random.randrange(0,3)
     #print(list[no1] ,"-",list[no2])
   
     if (list[no1]=="stone" and list[no2]=="stone"):
         continue
     elif ((list[no1]=="stone") and (list[no2]=="paper")):
         p2+=1
         
     elif ((list[no1]=="stone") and (list[no2]=="scissor")):
         p1+=1
   
   
   
     elif (list[no1]=="paper" and list[no2]=="stone"):
         p1+=1
     elif ((list[no1]=="paper") and (list[no2]=="paper")):
         continue
         
     elif ((list[no1]=="paper") and (list[no2]=="scissor")):
         p2+=1    
   
   
   
     elif (list[no1]=="scissor" and list[no2]=="stone"):
         p2=p2+1
     elif ((list[no1]=="scissor") and (list[no2]=="paper")):
        p1+=1
         
     elif ((list[no1]=="scissor") and (list[no2]=="scissor")):
         continue
   
     print("Person 1 scores", p1)
     print("Person 2 scores", p2)
     
     if(p1>p2):
         print("player 1 won the match")
     elif (p1<p2):
         print("player 2 won the match")   
     elif(p1==p2):
         print("Match draw")    
g1=game()
