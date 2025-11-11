def approximate_pi(n_terms):
    n_terms=10
    lst=[]
    for i in n_terms:
        if i%2==0:
            lst.append(1)
        else:
            lst.append(2)
    
