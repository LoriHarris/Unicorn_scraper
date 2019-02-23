

from splinter import Browser
from bs4 import BeautifulSoup
import time
import pymongo
import requests
from splinter.exceptions import ElementDoesNotExist
import pandas as pd

def init_browser():

        executable_path = {"executable_path": "chromedriver.exe"}
        return Browser("chrome", **executable_path, headless=False)

def data_scrape():
        conn = "mongodb://localhost:27017"
        client = pymongo.MongoClient(conn)
        db = client.mars_app
        browser = init_browser()
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')


        results = soup.find_all("div", class_="content_title")
        for result in results:

                title = result.find('a').text
        
                link = result.a['href']
                paragraph=soup.find("div", class_="article_teaser_body").text
                if (title and paragraph and link):
                        db.img_dict.insert_many(
                                [
                                        {
                                                "News_Title": title,
                                                "News_Paragraph": paragraph,
                                                "News_Link": link,
                                        }
                                ]
                        )
                



        # #I used Splinter as the assignment dictated in the boxes below
        # # however I was was able to pull the link for the featured image with BS from home page
        # # so I included that too, here:
        # url_pic = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        # browser.visit(url_pic)
        # html_pic = browser.html
        # soup_pic = BeautifulSoup(html_pic, 'html.parser')
        # results1 = soup_pic.find('a', class_="button fancybox")['data-fancybox-href']
        # featured_image_url=("https://www.jpl.nasa.gov"+results1)
        # print(featured_image_url)


        # #Now to get splinter results which were the same end result
        url_pic = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url_pic)
        browser.click_link_by_partial_text('FULL')
        html_f_pic = browser.html
        soup_f_pic= BeautifulSoup(html_f_pic, 'html.parser')
        results1 = soup_f_pic.find('a', class_="button fancybox")['data-fancybox-href']
        # featured_image_url=("https://www.jpl.nasa.gov"+results1)




        browser.visit("https://twitter.com/marswxreport?lang=en")
        html_tweets = browser.html
        soup_tweets = BeautifulSoup(html_tweets, 'html.parser')
        mars_weather = soup_tweets.find('p', class_='TweetTextSize').text
        print(mars_weather)

        pandas_url = ("http://space-facts.com/Mars/")
        tables = pd.read_html(pandas_url)
        tables

        df = tables[0]
        html_table = df.to_html()
        html_table.replace('\n', '')
        df_html = df.to_html('table.html')

        db.img_dict.insert_many(
                                        [
                                                {
                                                        "Featured_Image": results1,
                                                        "Mars_Weather": mars_weather,
                                                        "Mars_Table": df_html,
                                                }
                                        ]
                                )
        
        browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
        browser.click_link_by_partial_text('Cerberus')
        time.sleep(5)
        html_mars_img = browser.html
        soup_mars_img = BeautifulSoup(html_mars_img, 'html.parser')
        cerberus_img = soup_mars_img.find('a', target='_blank')['href']
        cerberus_title= soup_mars_img.find('h2', class_='title').text
        browser.click_link_by_partial_text('Back')
        time.sleep(5)
        browser.click_link_by_partial_text('Schiaparelli')
        time.sleep(5)
        html_mars_img1 = browser.html
        soup_mars_img1 = BeautifulSoup(html_mars_img1, 'html.parser')
        schia_img = soup_mars_img1.find('a', target='_blank')['href']
        schia_title= soup_mars_img1.find('h2', class_='title').text
        browser.click_link_by_partial_text('Back')
        time.sleep(5)
        browser.click_link_by_partial_text('Syrtis')
        time.sleep(5)
        html_mars_img2 = browser.html
        soup_mars_img2 = BeautifulSoup(html_mars_img2, 'html.parser')
        syrtis_img = soup_mars_img2.find('a', target='_blank')['href']
        syrtis_title= soup_mars_img2.find('h2', class_='title').text
        browser.click_link_by_partial_text('Back')
        time.sleep(5)
        browser.click_link_by_partial_text('Valles')
        time.sleep(5)
        html_mars_img3 = browser.html
        soup_mars_img3 = BeautifulSoup(html_mars_img3, 'html.parser')
        valles_img = soup_mars_img3.find('a', target='_blank')['href']
        valles_title= soup_mars_img3.find('h2', class_='title').text
       
        
        
        db.img_dict.insert_many(
                [
                {
                        "img_url": cerberus_img,
                        "img_Title": cerberus_title,
                
                },
                {
                        "img_url": schia_img,
                        "img_Title": schia_title,
                },
                {
                        "img_url": syrtis_img,
                        "img_Title": syrtis_title,
                },
                {
                        "img_url": valles_img,
                        "img_Title": valles_title,
                }
                ]
        )
        




# In[ ]:




