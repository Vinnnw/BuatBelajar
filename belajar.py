def is_prime(bilangan):
    if bilangan < 2:
        return "bukan prima"
        
    else:
        for i in range(2, int(bilangan**0.5) + 1):
            if bilangan % i == 0:
                return "bukan prima"
        return "prima"
            
            
    
    
