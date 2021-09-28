def dot(x,y,d1,d2):
    ans = 0
    for i in range(len(x)):
        ans+=((x[i]-d1)*(y[i]-d2))
    return ans


def root_sum(x,d):
    ans = 0
    for i in x:
        ans += (i-d)*(i-d)
    
    return pow(ans,0.5)

def avg(x):
    return sum(x)/len(x)

def cosine_sim(x,y):
    val = dot(x,y,0)/(root_sum(x,0)*root_sum(y,0))

def pearson(x,y):
    return dot(x,y,avg(x),avg(y))/(root_sum(x,avg(x))*root_sum(y,avg(y)))



    



