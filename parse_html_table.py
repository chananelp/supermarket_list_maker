
#https://stackoverflow.com/questions/51657000/how-to-convert-an-html-table-into-a-python-dictionary
#https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table

from bs4 import BeautifulSoup
from collections import OrderedDict
from pprint import pprint
import urllib.request
import urllib.parse

import statistics
import math
#import numpy as np
import math

def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]


data = """<h4>מחירים בקרבת אריאל <span style="font-size:80%"> (פער בין היקר ביותר לזול ביותר: <b>6%</b>)</span></h4><table class="table results-table" id="results-table" data-product_search_total_num_results="1"> <thead> <tr> <th>רשת</th> <th>שם החנות</th> <th class="dont_display_when_narrow">כתובת החנות</th> <th>מבצע</th> <th>מחיר</th> </tr> </thead> <tbody> <tr class="line-odd"><td>רמי לוי</td><td>אריאל</td><td class="dont_display_when_narrow">קניון מגה אור, שדרות ירושלים, אריאל</td><td>&nbsp;</td><td>6.90</td></tr><tr class="line-odd display_when_narrow"><td colspan="5" style="border-top:none;">קניון מגה אור, שדרות ירושלים, אריאל</td></tr><tr ><td>שופרסל דיל</td><td>דיל אריאל</td><td class="dont_display_when_narrow">רחוב מוריה , אריאל</td><td>&nbsp;</td><td>7.20</td></tr><tr class="display_when_narrow"><td colspan="5" style="border-top:none;">רחוב מוריה , אריאל</td></tr><tr class="line-odd"><td>מגה בעיר</td><td>אריאל א'</td><td class="dont_display_when_narrow">הנחשונים 37, אריאל</td><td>&nbsp;</td><td>7.30</td></tr><tr class="line-odd display_when_narrow"><td colspan="5" style="border-top:none;">הנחשונים 37, אריאל</td></tr></tbody></table><h4>תוצאות מחנויות באינטרנט<span style="font-size:80%"> (פער בין היקר ביותר לזול ביותר: <b>27%</b>)</span></h4><table class="table results-table"> <thead> <tr> <th class="dont_display_when_narrow">רשת</th> <th>שם החנות</th> <th>אתר אינטרנט</th> <th>מבצע</th> <th>מחיר</th> </tr> </thead> <tbody> <tr class="line-odd"><td class="dont_display_when_narrow">ישיר למהדרין</td><td><a href="https://www.lamehadrin.co.il" target="_blank">ישיר למהדרין</a></td><td>https://www.lamehadrin.co.il</td><td>&nbsp;</td><td>5.90</td></tr><tr ><td class="dont_display_when_narrow">חצי חינם אונליין</td><td><a href="https://shop.hazi-hinam.co.il/" target="_blank">חצי חינם אונליין</a></td><td>https://shop.hazi-hinam.co.il/</td><td>&nbsp;</td><td>6.90</td></tr><tr class="line-odd"><td class="dont_display_when_narrow">שופרסל אונליין</td><td><a href="https://www.shufersal.co.il" target="_blank">שופרסל אונליין</a></td><td>https://www.shufersal.co.il</td><td>&nbsp;</td><td>7.20</td></tr><tr ><td class="dont_display_when_narrow">מגה אונליין</td><td><a href="https://www.mega.co.il" target="_blank">מגה אונליין</a></td><td>https://www.mega.co.il</td><td>&nbsp;</td><td>7.20</td></tr><tr class="line-odd"><td class="dont_display_when_narrow">יינות ביתן אונליין</td><td><a href="https://www.ybitan.co.il" target="_blank">יינות ביתן אונליין</a></td><td>https://www.ybitan.co.il</td><td>&nbsp;</td><td>7.20</td></tr><tr ><td class="dont_display_when_narrow">רמי לוי באינטרנט</td><td><a href="https://www.rami-levy.co.il" target="_blank">רמי לוי באינטרנט</a></td><td>https://www.rami-levy.co.il</td><td>&nbsp;</td><td>7.30</td></tr><tr class="line-odd"><td class="dont_display_when_narrow">ויקטורי אונליין</td><td><a href="https://www.victoryonline.co.il" target="_blank">ויקטורי אונליין</a></td><td>https://www.victoryonline.co.il</td><td>&nbsp;</td><td>7.50</td></tr> </tbody> </table>
"""


link = "https://chp.co.il/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D/0/0/7290104067198/0"
#link=  "https://chp.co.il/%D7%A2%D7%9C%D7%99/9000/3765/7290104067198/0"
with urllib.request.urlopen(link) as f:
    data = f.read().decode('utf-8')


dl_all = []
prices = []
soup = BeautifulSoup(data, 'html.parser') ##'lxml')
tables = soup.find_all('table', attrs={'class': 'results-table'})
for table in tables:
    table_head = table.find('thead')
    row_header = table_head.find('tr')  # we should have one tr
    cols_header = row_header.find_all('th')
    cols_header = [ele.text.replace('\n', ' ').strip() for ele in cols_header]

    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    #, class_= lambda c: (print(c) if c else print("DD:",c)))
    # the above lines can not filter
    # we must use this: https://stackoverflow.com/questions/51189822/beautifulsoup-find-class-names-and-not
    rows = [r for r in rows if 'display_when_narrow' not in (r.get('class') if r.get('class') else []) ]
    #pprint(rows)
    print('================')
    # exit()
    selected_d = {}
    for row in rows:
        d = {} ##OrderedDict()
        cols = row.find_all('td')
        cols = [ele.text.replace('\n', ' ').strip() for ele in cols]  ##.splitlines()
        for h,c in zip(cols_header, cols):
            d[h] = c
        #print(d)
        if d.get('מחיר'):
            prices.append( float(d.get('מחיר').strip()) )
        dl_all.append(d)
        if d.get('רשת').strip() in ['אושר עד','רמי לוי','מעיין 2000', 'שופרסל דיל', 'שוק מהדרין', 'קואופ שופ', 'זול ובגדול', 'רמי לוי באינטרנט', 'שופרסל אונליין', '', '', ''] and \
              d.get('שם החנות').strip() in ['אריאל', 'שער בנימין', 'דיל אריאל', 'כוכב יעקב', 'בית אל', 'ירום- פסגת זאב', 'פסגת זאב ירושלים', 'פסגת זאב יקותאל אדם', 'גבעת שאול', 'רמי לוי באינטרנט',
                                            'שופרסל אונליין', '', '', '']:

            print(d)
            selected_d[d.get('רשת').strip() + " - " + d.get('שם החנות').strip()] = float(d.get('מחיר').strip())

    print('================')
    pprint(selected_d)
    print(list(selected_d.keys()))
    # ['', 'רמי לוי - אריאל', 'מעיין 2000 - שער בנימין', 'רמי לוי - שער בנימין', 'שופרסל דיל - דיל אריאל', 'שוק מהדרין - בית אל', 'שוק מהדרין - כוכב יעקב']
    # ['', 'אושר עד - גבעת שאול', 'מעיין 2000 - שער בנימין', 'רמי לוי - גבעת שאול', 'רמי לוי - שער בנימין', 'זול ובגדול - פסגת זאב יקותאל אדם', 'שופרסל דיל - ירום- פסגת זאב', 'קואופ שופ - פסגת זאב ירושלים']
    # ['', 'שופרסל אונליין - שופרסל אונליין', 'רמי לוי באינטרנט - רמי לוי באינטרנט']


#pprint(dl_all)
print(prices)
print(max(prices),min(prices),sum(prices),len(prices))
print("mean", "median", statistics.mean(prices), statistics.median(prices))
print("pstdev", "pvariance", statistics.pstdev(prices), statistics.pvariance(prices))
#print("quantiles", statistics.quantiles(prices, n=4))
#print("percentile", np.percentile(prices,5), np.percentile(prices,25), np.percentile(prices,50), np.percentile(prices,75), np.percentile(prices,95))
print("percentile", percentile(prices,5), percentile(prices,25), percentile(prices,50), percentile(prices,75), percentile(prices,95))
