def dot(x,y):
    ans = 0
    for i in range(len(x)):
        ans+=(x[i]*y[i])
    return ans


def root_sum(x):
    ans = 0
    for i in x:
        ans += i*i
    
    return pow(ans,0.5)

def cosine_sim(x,y):
    return dot(x,y)/(root_sum(x)*root_sum(y))

def pearson(x,y):
    pass


