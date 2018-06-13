import scrape as s
import pandas as pd
import numpy as np
import csv


def write_image_csv():
    csvfile = pd.read_csv('docs/one_shot_data_anime.csv', sep='\t', encoding = 'utf-8', error_bad_lines = False)

    imagefile = pd.read_csv('image_links.csv', sep='\t', encoding = 'utf-8', error_bad_lines = False)
    ids = csvfile.iloc[:, 1]

    image_ids = []

    for item in imagefile.iloc[:, 0]:
        val = int(item.split(',')[0])
        print val
        image_ids.append(val)


        progress = 1
        for i in ids:
            print str(progress)  + ' / ' + str(len(ids))
            progress+= 1
            if (i not in image_ids):
                with open('image_links.csv', 'a') as imgfile:
                    wr = csv.writer(imgfile, quoting=csv.QUOTE_ALL)
                    image_link = s.get_image_link(i)
                    print image_link, i
                    wr.writerow([str(i) , image_link])

def add_image_link_to_datafile():
    imagefile = pd.read_csv('docs/image_links.csv', sep='\t', encoding = 'utf-8', error_bad_lines = False)  
    csvfile = pd.read_csv('docs/one_shot_data_anime.csv', sep='\t', encoding = 'utf-8', error_bad_lines = False)
    data = csvfile.iloc[:, 1:3].values
    image_data = imagefile.values
    ids = [int(val[0].split(',')[0]) for val in image_data]
    image_links = [str(val[0].split(',')[1][1:-1]) for val in image_data]
    anime_names = []

    for item in ids:
        val = data[np.where(data[:,0] == item)][0][1]
        val = val.encode('utf-8')
        anime_names.append(val)

    ids = np.asarray(ids, dtype = int)
    image_links = np.asarray(image_links, dtype = str)
    anime_names = np.asarray(anime_names, dtype = str)

    new_data = pd.DataFrame({"id" : ids, "name" : anime_names, "image_links" : image_links})

    new_data.to_csv('docs/image_data.csv', sep='\t')

# add_image_link_to_datafile()