#Adya Aggarwal, Chahat Ahuja, Kushagra Gupta
import requests
import webbrowser
flag=False
def genrecheck(list):
    global genre
    for j in range (0,len(list)):
        genreid=list[j]
        url="https://api.themoviedb.org/3/genre/movie/list?api_key=9ed6b0b603ee6fee3631125b0c7cb133"
        response2=requests.get(url)
        tocheckin=response2.json()
        tocheckin=(tocheckin["genres"])
        for i in range (0,len(tocheckin)):
            if genreid==tocheckin[i]['id'] and tocheckin[i]['name']==genre:
                return True
def findtrailer(index):
    global idlist
    idtocheck=idlist[index-1]
    url=f"https://api.themoviedb.org/3/movie/{idtocheck}/videos?api_key=9ed6b0b603ee6fee3631125b0c7cb133&language=en-US"
    response=requests.get(url)
    response=response.json()
    for i in range (0,len(response["results"])):
        if(response["results"][i]['type'])=="Trailer":
            key=response["results"][i]['key']
            break
    return(key)
def findyoutubevideo(key):
    url=f"https://www.youtube.com/watch?v={key}"
    webbrowser.open_new(url)

actorname2=input("please enter actor name")
actorname=(actorname2).split()
genre=input("please enter genre:").capitalize()

#for actor movies
act=''
for i in range (len(actorname)):
    act=act+actorname[i]+"%20"
actor=(act[0:-3])

url = f"https://actor-movie-api1.p.rapidapi.com/getid/{actor}"
querystring = {"apiKey":"62ffac58c57333a136053150eaa1b587"}
headers = {
    "X-RapidAPI-Key": "bf354052b7msh580effee1ffda44p124802jsn8ca383675295",
    "X-RapidAPI-Host": "actor-movie-api1.p.rapidapi.com"
}
flag2=True
response = requests.request("GET", url, headers=headers, params=querystring)
data=response.json()
filmlist=[]
overviewlist=[]
yearlist=[]
idlist=[]
if len(data)<2:
    flag2=False
if (flag2==False):
    print("actor not found in database")
else:
    for i in range (0,len(data)):
        film=data[i]["original_title"]
        overview=data[i]["overview"]
        year=data[i]["release_date"]
        id=data[i]["id"]
        genreidlist=data[i]["genre_ids"]
        if genrecheck(genreidlist)==True:     
            filmlist.append(film)
            overviewlist.append(overview)
            yearlist.append(year)
            idlist.append(id)
            flag=True
    if flag2==True and flag==False:
        print("genre not found")
        print(f"here are all movies starring {actorname2} ")
        for i in range (0,len(data)):
            film=data[i]["original_title"]
            print(film)
    if flag==True and flag2==True:
        for i in range (0,len(filmlist)):
            print(str(i+1)+".")
            print(filmlist[i])
            print(yearlist[i])
            print(overviewlist[i])
            print()

        x=[1]
        while len(x)!=0:
            indexnumber=int(input("please enter index no. of movie you want a trailer to"))
            values=list(str(indexnumber))
            youtubekey=findtrailer(indexnumber)
            findyoutubevideo(youtubekey)
            if len(values)==0:
                break