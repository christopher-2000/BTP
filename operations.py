import plotly.express as px

def dot(x,y,d1,d2):
    ans = 0
    for i in range(len(x)):
        ans+=((x[i]-d1)*(y[i]-d2))
    return ans

def euclidean(x,y):
    ans=0
    div = root_sum([40,40,5,3])

    for i,j in zip(x,y):
        ans+=pow(i-j,2)
    return 1 - (pow(ans,0.5)/div)

def root_sum(x,d=0):
    ans = 0
    for i in x:
        ans += pow(i-d,2)
    ans = pow(ans,0.5)
    if ans==0:
        return 1
    else:
        return ans

def avg(x):
    return sum(x)/len(x)

def cosine_sim(x,y):
    val = dot(x,y,0,0)/(root_sum(x,0)*root_sum(y,0))
    return val

def pearson(x,y):
    return dot(x,y,avg(x),avg(y))/(root_sum(x,avg(x))*root_sum(y,avg(y)))

def type_change(s):
        
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            return 10
        

def drawGraph(d,x,y,c=None):
    graph = px.bar(d,x=x,y=y,color=c)
    graph.update_xaxes(showgrid=False)
    graph.update_yaxes(showgrid=False)
    graph.update_layout(xaxis_range=[0,1])
    return graph
    



