
# coding: utf-8

# In[16]:

while True:
    x=(input("insert gender(boy=1,girl=2):"))
    y=int(input("insert age (0 to exit ):"))

    if y == 0 :
        break
   
    else:
        x = int
       
        
        if(x==1):
           
            if (y>=1)and(y<=3):
                print("calorie intake 1000 cals/day")
            elif(y>3)and(y<=8):
                print("calorie intake 1200 - 1400 cals/day")
            elif(y>8)and(y<=13):
                print("calorie intake 1600 - 2000 cals/day")
            elif(y>13)and(y<=18):
                print("calorie intake 2000 - 2400 cals/day")
            elif(y>18)and(y<=30):
                print("calorie intake 2400 - 2600 cals/day")
            elif(y>30)and(y<=50):
                print("calorie intake 2200 - 2400 cals/day")
            else: 
                print("calorie intake 2000 - 2200 cals/day")
        else:
            
            if (y>=1)and(y<=3):
                print("calorie intake 1000 cals/day")
            elif (y>3)and(y<=8):
                print("calorie intake 1200 - 1400 cals/day")
            elif(y>8)and(y<=13):
                print("calorie intake 1400 - 1600 cals/day")
            elif(y>13)and(y<=18):
                print("calorie intake 1800 cals/day")
            elif(y>18)and(y<=30):
                print("calorie intake 1800 - 2000 cals/day")
            elif(y>30)and(y<=50):
                print("calorie intake 1800 cals/day")
            else: 
                print("calorie intake 1600 cals/day")
    
        


# In[ ]:



