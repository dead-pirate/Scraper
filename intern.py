from bs4 import BeautifulSoup
import requests
import pandas as pd

#uss3541

url = requests.get("https://internshala.com/internships")
con = url.content

soup = BeautifulSoup(con, "html.parser")

num =int(soup.find("span",{"id":"total_pages"}).text)
print( 'file will be created after : ',num)

"""
for item in all:
    print(item.find("div",{"class":"heading_4_5 profile"}).text)
    print(item.find("div",{"class":"heading_6 company_name"}).text.strip())
    print(item.find("span").text.strip())
    print(item.find("span",{"class":"start_immediately_desktop"}).text)
    print(item.find_all("div",{"class":"item_body"})[1].text.strip())
    print(item.find("span",{"class":"stipend"}).text.replace(" ",""))
    print(item.find("div",{"class":"apply_by"}).find("div",{"class":"item_body"}).text)
"""
"""    
profile=[]
company=[]
locations=[]
start_date=[]
duration=[]
stipend=[]
last_date=[]
"""
addr="https://internshala.com/internships/page-"
l=[]

print('counting pages : ')
for i in range(1,num+1):  
    print(str(i))
    url = requests.get(addr + str(i))
    con = url.content
    

    soup = BeautifulSoup(con, "html.parser")

    all = soup.find_all("div",{"class":"internship_meta"})
    for item in all:
        d={}
        try:
            d["Profile"]=item.find("div",{"class":"heading_4_5 profile"}).text.strip()
        except:
            d["profile"]=None
        try:
            d["Company"]=item.find("div",{"class":"heading_6 company_name"}).text.strip()
        except:
            d["Company"]=None
        try:
            d["Location"]=item.find("span").text.strip()
        except:
            d["Location"]=None
        try:
            d["Start Date"]=item.find("span",{"class":"start_immediately_desktop"}).text
        except:
            d["Start Date"]=None    
        try:    
            d["Duration"]=item.find_all("div",{"class":"item_body"})[1].text.strip()
        except:
            d["Duration"]=None 
        try:   
            d["Stipend"]=item.find("span",{"class":"stipend"}).text.replace(" ","")
        except:
            d["Stipend"]=None     
        try:    
            d["Apply By"]=item.find("div",{"class":"apply_by"}).find("div",{"class":"item_body"}).text
        except:
            d["Apply By"]=None 
        l.append(d)

print('Creating the file .......')
#columns=["Profile","Company","Locations","Start Date","Duration","Stipend","Last Date"],
#index=[i+1 for i in range(len(profile))]
#"Locations":locations
#"Start Date":start_date,

#data = pd.DataFrame({"Profile": profile,"Company":company,"Locations":locations,
#                     "Duration":duration,"Stipend":stipend,"Last Date":last_date})
data = pd.DataFrame(l,index=[i+1 for i in range(len(l))])
data.to_csv("internships.csv")

print('All Done')