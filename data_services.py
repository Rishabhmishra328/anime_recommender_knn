import pandas as pd
import numpy as np

def get_data():
  csvfile = pd.read_csv('docs/one_shot_data_anime.csv', sep='\t', encoding = 'utf-8', error_bad_lines = False)
  csvfile = csvfile.iloc[:, 1:]
  
  data = csvfile.values
  data[:, 3] = data[:, 3] / 10 # rating
  # data = np.delete(data, np.s_[4], axis=1) #removing members
  # data[:, 4] = data[:, 4] / 1e+2 # members
  # data[:, 4] = data[:, 4] / data[:, 4].max(axis=0) #normalizing members
  data[:, 4] = norm_members(data[:,4]) #normalizing members

  labels = np.asarray(csvfile.columns.values, dtype = str)

  return data, labels

def get_recom(suggestions = 10, ids = [20], strength = [1.0]):
  data, labels = get_data()
  val = [0.0] * len(get_value(ids[0])) 
  for index in range(len(ids)):
    val = val + (get_value(ids[index]) * strength[index])
  
  val = val / len(ids)
  
  print suggestions
  suggestions = int(suggestions)

  recom = [[0, 100]] * suggestions
  for index in range(len(data)):
    recom = sorted(recom, key = lambda recom: recom[1])
    item_val = data[index][3:]
    item_id = data[index][0]
    if(item_id not in ids):
      diff = np.linalg.norm(item_val - val)
      if(index < suggestions):
        recom[index] = [item_id, diff]
      if(recom[-1][1] > diff):
        recom[-1] = [item_id, diff]
   
  recom = np.array(recom)
  names = get_names(recom[:,0])
  img_url = []
  for name in names:
    img_url.append(get_image_link(name))

  recom_score = []
  for val in recom[:,1]:
    recom_score.append(int((1/(val)) * (1e+3)))
  
  res = []
  for index in range(len(names)):
    res_val = [recom[index][0], names[index], recom_score[index], img_url[index]]
    res.append(res_val)
    
  return res

def get_value(id = 20):
  data, labels = get_data()
  val = np.where(data[:, 0] == id)
  return data[val[0][0], 3:]

def get_names(ids):
  names = []
  data, labels = get_data()
  for item in ids:
    val = np.where(data[:, 0] == item)
    names.append(data[val[0][0], 1])
  return np.asarray(names).reshape(len(ids),)

def get_image_link(name = 'Naruto'):
  csvfile = pd.read_csv('docs/image_data.csv', sep='\t', encoding = 'utf-8', error_bad_lines = False)
  data = csvfile.values
  try:
    val = np.where(data[:, 3] == name)[0][0]
    url = data[val][2]
  except:
    url = 'https://i0.wp.com/bradan.co/wp-content/uploads/2017/01/Video-Reel-and-Film-Canister2.png?ssl=1'

  if(isinstance(url, float)):
    url = 'https://i0.wp.com/bradan.co/wp-content/uploads/2017/01/Video-Reel-and-Film-Canister2.png?ssl=1'
  return url

def get_id(name = 'Naruto'):
  csvfile = pd.read_csv('docs/image_data.csv', sep='\t', encoding = 'utf-8', error_bad_lines = False)
  data = csvfile.values
  try:
    val = np.where(data[:, 3] == name)[0][0]
    id_val = data[val][1]
  except:
    id_val = 0
  return id_val

def norm_members(mem):
  res = []
  for item in mem:
    factor = 1
    tenth = 0
    hunredth = 0
    while(len(str(item / factor)) > 1):
      tenth = len(str(factor))
      hunredth = item / factor
      factor *= 10
    new_val = (float(tenth)/10) + float(float(hunredth)/100)
    res.append(new_val)

  res = np.asarray(res, dtype = np.float32)
  # print res[10:20]
  return res

# data, labels = get_data()
# print get_id()
# print get_image_link()
# print get_recom(suggestions = 5, id = 20)