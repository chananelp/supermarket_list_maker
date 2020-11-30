# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import os

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import csv
import traceback

from collections import OrderedDict
from pprint import pprint

from config_file import *

import statistics
import math


def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]


#https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser(description="Create supermarket products list by scannig barcodes",
                             epilog="Written by Chananel Perel - Nov. 2020 ")
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
                help="path to output CSV file containing barcodes")
ap.add_argument("-i", "--inputfile", type=str, # default=None,
                help="input list of \"barcode, local price and department\" from file")

ap.add_argument("-m", "--manual", action="store_true",
                help="manual barcode typing and do not use camera")
ap.add_argument("-s", "--skip", action="store_true",
                help="skip user unput of local price and department")


ap.add_argument("-t", "--type", type=int, choices=[0, 1, 2],
                    help="what type to use")
ap.add_argument("-d", "--debug", action="store_true",
                help="debug mode")
ap.add_argument("-v", "--verbosity", action="count", default=0,
                help="increase output verbosity")

#args_old = vars(ap.parse_args())
args = ap.parse_args()
print(args)


print(city_names)
cities_enc = []

for city in city_names:
    cities_enc.append( urllib.parse.quote(city) )

if not args.manual:
    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    # vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
found = set()

filepath = args.output #args_old["output"]
#csv = open(args["output"], "w")

if os.path.isfile(filepath):
    write_header = False
else:
    write_header = True

with open(filepath, 'a', encoding='utf-8', newline='') as csv_file:
    try:

        # writer = csv.writer(csv_file, dialect=csv.excel)
        writer = csv.DictWriter(csv_file, restval='', extrasaction='ignore', dialect=csv.excel, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()

        # loop over the frames from the video stream
        while True:
            try:
                # grab the frame from the threaded video stream and resize it to
                # have a maximum width of 400 pixels
                if not args.manual:

                    frame = vs.read()
                    frame = imutils.resize(frame, width=400)
                    # find the barcodes in the frame and decode each of the barcodes
                    barcodes = pyzbar.decode(frame)
                else:
                    barcode_manual = input("Please enter Barcode: ")
                    if barcode_manual == "q":
                        break

                    barcodes =[barcode_manual]
                    # [
                    #     pyzbar.Decoded(
                    #         data=barcode_manual, #b'Foramenifera',
                    #         type='_MANUAL_',
                    #         rect=None,
                    #         polygon=None
                    #     )
                    # ]

                # loop over the detected barcodes
                for barcode in barcodes:

                    if not args.manual:
                        # extract the bounding box location of the barcode and draw
                        # the bounding box surrounding the barcode on the image
                        (x, y, w, h) = barcode.rect
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        # the barcode data is a bytes object so if we want to draw it
                        # on our output image we need to convert it to a string first
                        barcodeData = barcode.data.decode("utf-8")
                        barcodeType = barcode.type
                        # draw the barcode data and barcode type on the image
                        text = "{} ({})".format(barcodeData, barcodeType)
                        cv2.putText(frame, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    else:
                        barcodeData = barcode
                        barcodeType = '_MANUAL_'

                    # if the barcode text is currently not in our CSV file, write
                    # the timestamp + barcode to disk and update the set
                    if barcodeData not in found:
                        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

                        #os.system("open platform-game-beeping--2-sound-effect-22351075.mp3")
                        os.system(' osascript -e "beep 1" ')

                        dl_all = []     # dict of all data
                        selected_d = {} # dict of only selected place and only prices
                        all_prices_dict = {}
                        prices = []     # just prices list

                        for city_enc in cities_enc:

                            link = base_link.format(city_enc, barcodeData)
                            print(link)

                            with urllib.request.urlopen(link) as f:
                                my_web = f.read().decode('utf-8')

                            #print(my_web)
                            #print(type(my_web))

                            write_filename = "item__{}_{}.htm".format(barcodeData,city_enc)
                            with open(write_filename, 'w') as f2:
                                f2.write(my_web)

                            soup = BeautifulSoup(my_web, 'html.parser')
                            #title = soup.select('h3')[1].select('span')[0].text.replace('\n', ' ').strip()
                            title = soup.select('h3')[1].text.replace('\n', ' ').replace(remove_str,'').strip()
                            print(title)
                            # <h3>מלח גס בצנצנת הארץ, 1 ק"ג <span style="color:grey">(יצרן/מותג: תעשיות מלח לישראל, ברקוד: 7290000523811)</span>
                            #   <BR><a href="#" onclick="add_to_list_from_compare_results()">הוסף לרשימה</a></h3>
                            hh = soup.select('h4')
                            for h in hh:
                                if args.verbosity >= 1:
                                    print( "===   ", h.text.replace('\n', ' ').strip() )
                                pass

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
                                # pprint(rows)
                                #print('================')
                                # exit()

                                for row in rows:
                                    d = {} ##OrderedDict()
                                    cols = row.find_all('td')
                                    cols = [ele.text.replace('\n', ' ').strip() for ele in cols]  ##.splitlines()
                                    for h,c in zip(cols_header, cols):
                                        d[h] = c

                                    if args.verbosity >= 1:
                                        print(d)

                                    dl_all.append(d)

                                    all_prices_dict[d.get(allowed_chain_key).strip() + " - " + d.get(allowed_stores_key).strip()] = float(d.get(price_key).strip())

                                    if d.get(price_key):
                                        prices.append( float(d.get(price_key).strip()) )

                                    if d.get(allowed_chain_key).strip()  in allowed_chain  and  \
                                       d.get(allowed_stores_key).strip() in allowed_stores :
                                            #print(d)
                                            selected_d[d.get(allowed_chain_key).strip() + " - " + d.get(allowed_stores_key).strip()] = float(d.get(price_key).strip())



                                #print('================')

                        # here we have prices in all locations

                        #print('dl_all', dl_all)
                        #print('set_selected', set(selected_d.keys()))
                        #print('selected_d', selected_d)
                        #print('prices', prices)

                        #print("max", "min", max(prices),min(prices),sum(prices),len(prices))
                        #print("mean", "median", statistics.mean(prices), statistics.median(prices))
                        #print("pstdev", "pvariance", statistics.pstdev(prices), statistics.pvariance(prices))
                        #print("percentile", percentile(prices,5), percentile(prices,25), percentile(prices,50), percentile(prices,75), percentile(prices,95))
                        if args.skip:
                            local_price = ""
                            department_id = ""
                        else:
                            local_price = input("Please enter Price at your Local Super Market: ")
                            print(local_price)

                            department_id = input("Please enter Department ID: ")
                            print(department_id, departments.get(str(department_id)))

                        # csv.write("{},{},{},{}\n".format(datetime.datetime.now(), barcodeData,title,str(local_price)))
                        # csv.flush()
                        #one_line = [ datetime.datetime.now(), barcodeData, title, str(local_price) ]
                        #writer.writerow(one_line)
                        one_dict = {
                            field_time: str(datetime.datetime.now()),
                            field_barcode: str(barcodeData),
                            field_department_id: str(department_id),
                            field_department_name: departments.get(str(department_id),''),

                            field_title: title,
                            field_link: link,  # will put the last city
                            field_comments: '',

                            field_local_price: local_price,
                            max_price: max(prices),
                            min_price: min(prices),

                            mean_price: round(statistics.mean(prices),3),
                            median_price: round(statistics.median(prices),3),

                            pstdev_price: round(statistics.pstdev(prices),3),
                            pvariance_price: round(statistics.pvariance(prices),3),

                            p5_price: percentile(prices,5),
                            p25_price: percentile(prices,25),
                            p50_price: percentile(prices,50),
                            p75_price: percentile(prices,75),
                            p95_price: percentile(prices,95),

                            sum_prices_list: round(sum(prices),3),
                            len_prices_list: len(prices),
                            prices_list: str(prices),
                            # sorted dict by val: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
                            all_prices_data: str({k: v for k, v in sorted(all_prices_dict.items(), key=lambda item: item[1])})

                        }

                        one_dict.update(selected_d)

                        pprint(one_dict)
                        writer.writerow(one_dict)

                        found.add(barcodeData)
                        print('================\n\n')

                if not args.manual:
                    # show the output frame
                    cv2.imshow("Barcode Scanner", frame)
                    key = cv2.waitKey(1) & 0xFF

                    # if the `q` key was pressed, break from the loop
                    if key == ord("q"):
                        break

            except Exception as e:  # catch all errors:  # try2 - for re-run
                print("ERR:" + str(e.__class__) + str(e))
                print(traceback.format_exc())
            #finally:
            #    print("Finally..")
    finally:
        print("Finally..")

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
# csv.close()
if not args.manual:
    cv2.destroyAllWindows()
    vs.stop()

print("Done!")
