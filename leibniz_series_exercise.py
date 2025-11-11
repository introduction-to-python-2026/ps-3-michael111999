def approximate_pi(n_terms):
    lst=[]
    for i in range(n_terms):
        if i%2==0:
            lst.append(1/(i*2+1))
        else:
            lst.append(-1/(i*2+1))
        
    return 4*sum(lst)

        
    
    
