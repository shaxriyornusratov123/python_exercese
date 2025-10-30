class Pizza:
    def PizzaClices(p_clices,num_people):
        if num_people==0:
            return "bunaday bo'la olmaydi"
        return p_clices/num_people
    
print(Pizza.PizzaClices(8,2))