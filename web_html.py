import urllib.request
import urllib.parse

from bs4 import BeautifulSoup


city_name = input("Please enter city (hebrew): ")
#print(f'You entered {value}')
if not city_name:
    city_name = 'אריאל'
print(city_name)
city_enc = urllib.parse.quote(city_name)

#city = "%D7%90%D7%A8%D7%99%D7%90%D7%9C"   # Ariel city
#print(urllib.parse.unquote(city))

barcode_num = input("Please enter city (number/hebrew): ")
if not barcode_num:
    barcode_num = "7290000523811"
print(barcode_num)
barcode_enc = urllib.parse.quote(barcode_num)

link = "https://chp.co.il/{}/0/0/{}/0".format(city_enc, barcode_enc)
print(link)


with urllib.request.urlopen(link) as f:
    my_web = f.read().decode('utf-8')

#print(my_web)
#print(type(my_web))

soup = BeautifulSoup(my_web, 'html.parser')
#title = soup.select('h3')[1].select('span')[0].text.replace('\n', ' ').strip()
title = soup.select('h3')[1].text.replace('\n', ' ').replace('הוסף לרשימה','').strip()
print(title)

# <h3>מלח גס בצנצנת הארץ, 1 ק"ג <span style="color:grey">(יצרן/מותג: תעשיות מלח לישראל, ברקוד: 7290000523811)</span>
#   <BR><a href="#" onclick="add_to_list_from_compare_results()">הוסף לרשימה</a></h3>

hh = soup.select('h4')
for h in hh:
    print( h.text.replace('\n', ' ').strip() )
