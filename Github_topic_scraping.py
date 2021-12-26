# %% [markdown]
# ## Web Scraping using python

# %%
%pip install requests --upgrade

# %%
#use for fetching url  
import requests

#now we need to download the page
topic_url = 'https://github.com/topics'
response = requests.get(topic_url);

# %%
#status code will let us know if the data is downloaded or not
response.status_code

len(response.text)  #174167 to much big file 

#to see some rows
view_page = response.text
view_page[:1000]

# %% [markdown]
# ## Using Beautiful Soup 

# %%
from bs4 import BeautifulSoup as bs
doc = bs(view_page,'html.parser')

# %%
type(doc)

# %%
#grabing content of a page
p_tag = doc.find_all('p')

len(p_tag)

p_tag[0:5]

# %%
#find specific syntax
#Getting title
selection_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'
topic_title_tag = doc.find_all('p', {'class': selection_class})

len(topic_title_tag)

topic_title_tag[:5]

# %%
#Getting Description
topic_desc_tag = doc.find_all('p', {'class':'f5 color-fg-muted mb-0 mt-1'})

topic_desc_tag[0:5]

# %%
#fetching a url
topic_link_tag = doc.find_all('a',{'class':'no-underline flex-1 d-flex flex-column'})
len(topic_link_tag)

topic_link_tag[0]['href']

# %%
#Creating a url syntax
topic0_url = "https://github.com" + topic_link_tag[0]['href']

print(topic0_url)


topic_title_tag[:5]

# %%
#Now taking all the topic titles in a list
topic_title_tag[0].text # to get the value 


#creating title list
topic_titles = []

for tag in topic_title_tag:
    topic_titles.append(tag.text)

print(topic_titles)

# %%
#Creating description list
topic_desc_tag[:5]

topic_desc = []

for tag in topic_desc_tag:
    topic_desc.append(tag.text.strip())

print(topic_desc[:5])

# %%
#Creating url list
topic_urls = []
base_url = "https://github.com"

for tag in topic_link_tag:
    topic_urls.append(base_url+tag['href'])

topic_urls[:5]

# %% [markdown]
# ### Creating CSV from mulitple list 

# %%
import pandas as pd

# %%
#creating dictionary

topic_dic = {
    'title': topic_titles,
    'description': topic_desc,
    'Urls': topic_urls
}


# %%
topic_df  = pd.DataFrame(topic_dic)

# %%
topic_df

# %%
topic_df.to_csv('topics.csv')

# to remove the row numbers

topic_df.to_csv('topics.csv', index= None)


# %% [markdown]
# # Getting information out of a topic 

# %%
topic_page_url = topic_urls[0]
topic_page_url

# %%
response = requests.get(topic_page_url)

response.status_code

# %%
len(response.text)

# %%
topic_doc = bs(response.text,'html.parser')

# %%
#getting name of the author
repo_tag =topic_doc.find_all('h3', {'class':'f3 color-fg-muted text-normal lh-condensed'})

a_tag=repo_tag[0].find_all('a')

a_tag[0].text.strip()

# %%
#repo name
a_tag[1].text.strip()

# %%
#repo url
repo_url = base_url + a_tag[1]['href']
repo_url

# %%
#stars
star_repo = topic_doc.find_all('span',{'class':'Counter js-social-count'})

star=star_repo[0].text.strip()

# %%
#converting into to anumber

def parse_star_count(star_str):
    star_str= star_str.strip()
    if star_str[-1] == 'k':
       return  int (float(star_str[:-1]) * 1000)
    else:
        return int(star_str)

# %%
parse_star_count(star)

# %%
#Returing all the information 
def get_repo_info(h1_tag, star_tag):
    a_tag = h1_tag.find_all('a')
    user_name = a_tag[0].text.strip()
    repo_name = a_tag[1].text.strip()
    reo_url = base_url + a_tag[1]['href']
    stars = parse_star_count(star_tag.text.strip())
    return user_name, repo_name, stars, reo_url


# %%
get_repo_info(repo_tag[0], star_repo[0])

# %%
topic_repo_dict ={

    'username' : [],
    'repo_name' : [],
    'stars':[],
    'repo_urls':[]
}



for i in range(len(repo_tag)): 
    repo_info=get_repo_info(repo_tag[i], star_repo[i])
    topic_repo_dict['username'].append(repo_info[0])
    topic_repo_dict['repo_name'].append(repo_info[1])
    topic_repo_dict['stars'].append(repo_info[2])
    topic_repo_dict['repo_urls'].append(repo_info[3])

# %%
topic_repo_dict

# %%
topic_repo_df = pd.DataFrame(topic_repo_dict)

# %%
topic_repo_df

topic_repo_df.to_csv('topics_repo.csv', index= None)


# %%



