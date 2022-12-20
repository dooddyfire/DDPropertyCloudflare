#import cloudscraper

#scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
#print(scraper.get("https://animekimi.co/").text) 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
from selenium import webdriver
import pandas as pd 
from selenium.webdriver.common.by import By

# "https://animekimi.co/page/4/"
if __name__ == '__main__':
    df = pd.DataFrame()
    options = webdriver.ChromeOptions() 
    options.headless = True
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    url = "https://www.ddproperty.com/%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A8%E0%B8%82%E0%B8%B2%E0%B8%A2?region_code=TH10&freetext=%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E&listing_posted=7&market=residential&maxPricePerArea=400000&ps=1"
    driver = uc.Chrome()
    
    driver.get(url)

    #current_url = driver.current_url


    for i in range(0,6):
        driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(3)
            # print(driver.page_source)  # results


    soup = BeautifulSoup(driver.page_source,'html.parser')
    print(soup.prettify())
    list_url =[ x['href'] for x in soup.find_all("a",{'class':'nav-link'})]
    print(list_url)

    prop_name_lisx = []
    sell_price_lis = []
    bed_lis = []
    baht_lis = []
    province_lis = []
    distrinct_lis = []
    property_eng_lis = []
    area_code_lis = []
    address_lis = []
    unit_lis = []
    price_per_sqm_lis = []

    lat_lis = []
    long_lis = []

    for i in list_url:
        urlx = i 

        driver.get(urlx)
        soup = BeautifulSoup(driver.page_source,'html.parser')

        lat = soup.find('meta',{'itemprop':'latitude'})
        long = soup.find('meta',{'itemprop':'longitude'})


        print("lat-long")
        print(lat['content'])
        print(long['content'])

        try:
            prop_name = soup.find('div',{'class':'listing-title'}).text.strip()
            print(prop_name)
            prop_name_lisx.append(prop_name)
        except: 
            prop_name_lisx.append("ไม่มี")
            print("ไม่มี")

        try:
            sell_price = soup.find('span',{'itemprop':'price'}).text.strip()
            print(sell_price)
            sell_price_lis.append(sell_price)
        except: 
            sell_price_lis.append("ไม่มี") 
            print("ไม่มี")

        try:
            bed = driver.find_element(By.XPATH,'//*[@id="overview"]/div/div/div/section/div[1]/div[2]/div[1]/span').text.strip()
            bed_lis.append(bed)
            print(bed)
        except: 
            bed_lis.append("0")
            print(0)

        try:
            baht = driver.find_element(By.XPATH,'//*[@id="overview"]/div/div/div/section/div[1]/div[2]/div[2]/span').text.strip()
            baht_lis.append(baht)
            print(baht)
        except: 
            baht_lis.append("0")
            print(0)
        try:
            province = driver.find_element(By.XPATH,'//*[@id="overview"]/div/div/div/section/div[1]/div[4]/div/div[1]').text.strip()
            province_lis.append(province)
            print(province)
        except: 
            province_lis.append("ไม่มี")
            print("ไม่มี")

        try:
            distrinct = driver.find_element(By.XPATH,'//*[@id="overview"]/div/div/div/section/div[1]/div[4]/div/div[2]/div[1]/span').text.strip()
            distrinct_lis.append(distrinct)
            print(distrinct)
        except: 
            distrinct_lis.append("ไม่มี")
            print("ไม่มี")

        try:
            area_code = driver.find_element(By.XPATH,'//*[@id="details"]/div/div[1]/table/tbody[7]/tr/td[2]').text.strip()
            area_code_lis.append(area_code)
            print(area_code)
        except: 
            area_code_lis.append("ไม่มี")

        try:
            price_per_sqm = driver.find_element(By.XPATH,'//*[@id="overview"]/div/div/div/section/div[1]/div[2]/div[4]/div/span[2]').text.strip()
            print(price_per_sqm)
            price_per_sqm_lis.append(price_per_sqm) 
        except: 
            price_per_sqm_lis.append("ไม่มี")
            print('ไม่มี')

        try:
            lat_lis.append(lat['content'])
        except: 
            lat_lis.append("ไม่มี")
        
        try:
            long_lis.append(long['content'])
        except: 
            long_lis.append("ไม่มี")


    df = pd.DataFrame()
    df['property_name'] = prop_name_lisx
    df['sell_price'] = sell_price_lis        #https://animekimi.co/
    df['property_code'] = area_code 
    df['url'] = list_url 
    df['price_per_sqm'] = price_per_sqm_lis 
    df['bed'] = bed_lis 
    df['baht'] = baht_lis 
    df['latitude'] = lat_lis 
    df['longitude'] = long_lis 
    df['province'] = province_lis
    df['district'] = distrinct_lis 

    df.to_excel("Test.xlsx")