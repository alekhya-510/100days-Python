def calculate_love_score(name1,name2):
    
    name= (name1+name2).lower()
    
    t= name.count("t")
    r= name.count("r")
    u= name.count("u")
    e= name.count("e")
    
    first_digit = t+r+u+e
    
    l= name.count("l")
    o= name.count("o")
    v= name.count("v")
    e= name.count("e")
    
    second_digit= l+o+v+e
    
    score=str(first_digit)+str(second_digit)
    print(score)

calculate_love_score("Alekhya", "Trinadha Chandra Mouli")    
    
