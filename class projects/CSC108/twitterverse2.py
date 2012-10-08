'''FINAL DATA will end up being the twitter dictionary. A twitter dictionary 
contains a person's twitter username as a key and 5 nested dictionaries as 
their value. The nested dictionaries contain their real name, location, 
website, bio, and people followed by the person. '''
FINAL_DATA = None

def data_to_dict(L, s, f):
     '''Return a dictionary that uses a person's username as the key and
     5 more nested dictionaries as the value. The nested dictionaries contain
     the name, location, website, bio, and people followed by the person.
     L is a list that contains username, name, location, website
     s is the bio of the person
     f is a list of people followed by the person'''
     
     data = {}
     inner_data = {}
     inner_data['name'] = L[1]
     inner_data['location'] = L[2]
     inner_data['website'] = L[3]
     inner_data['bio'] = s
     inner_data['follows'] = f
     data[L[0]] = inner_data
     
     return data
     
def store_data(data_file):
     '''Return a dictionary that uses a person's username as the key and
     5 more nested dictionaries as the value. Obtains the relevant information
     from data_file to pass as paramters for data_to_dict'''
     
     info = []
     line = data_file.readline()
     if len(line) == 0:
          return ''
     for i in range(4):
          if line.strip() != '':
               info.append(line.strip())
               line = data_file.readline()
          else:
               info.append('')
               line = data_file.readline()
     bio = '\n'
     while line.strip() != "ENDBIO":
          bio += line
          line = data_file.readline()
     line = data_file.readline()
     follows = []
     while line.strip() != "END":
          follows.append(line.strip())
          line = data_file.readline() 
          
     return data_to_dict(info, bio.rstrip(), follows)

def total_data(data_file):
     '''Return a comprehensive and updated dictionary that contains
     every username in data_file as a key and 5 more nested dictionaries 
     as the value. The nested dictionaries contain
     the name, location, website, bio, and people followed by the user. '''
     
     data = {}
     divided_data = None
     while divided_data != '':
          divided_data = store_data(data_file)
          data.update(divided_data)
     return data

def remove_duplicates(L):
     '''Return a new list that has any duplicates in list L removed. '''
     
     new_l = []
     for item in L:
          if item not in new_l:
               new_l.append(item)
     return new_l

def search_follows(user_list):
     '''Return a new list containing usernames who follow the 
     usernames in user_list. user_list is a list of usernames'''
     
     result = []
     for users in user_list:
          for user in FINAL_DATA:
               if users in FINAL_DATA[user]['follows']:
                    result.append(user)
     result = remove_duplicates(result)
     return result
  

def search_followed_by(user_list):
     '''Return a new list containing usernames that are followed by the 
     usernames in user_list. user_list is a list of usernames'''
     
     result = []
     for users in user_list:
          for followed in FINAL_DATA[users]['follows']:
               result.append(followed)
     result = remove_duplicates(result)
     return result

def filter_name(user_list, includes):
     '''Return a new list containing usernames from user_list that have 
     includes as part of their name. includes is a string'''
     
     result = []
     for users in user_list:
          if includes.lower() in FINAL_DATA[users]['name'].lower():
               result.append(users)
     result = remove_duplicates(result)
     return result

def filter_location(user_list, includes):
     '''Return a new list containing usernamess from user_list that have
     includes as part of their location. includes is a string'''
     
     result = []
     for users in user_list:
          if includes.lower() in FINAL_DATA[users]['location'].lower():
               result.append(users)
     result = remove_duplicates(result)
     return result

def filter_follows(user_list, includes):
     '''Return a new list containing usernamess from user_list that follow 
     includes. includes is a username'''
     
     result = []
     for user in user_list:
          if includes in FINAL_DATA[user]['follows']:
               result.append(user)
     result = remove_duplicates(result)
     return result

def filter_followed_by(user_list, includes):
     '''Return a new list containing users from user_list that are followed by
     includes. includes is a username'''
     
     result = []
     for user in user_list:
          if user in FINAL_DATA[includes]['follows']:
               result.append(user)
     result = remove_duplicates(result)
     return result
     
def sort_username(uname1, uname2):
     '''uname1 and uname2 are usernames. Return -1 if uname1 comes before
     uname2 alphabetically. Return 1 if uname1 comes after uname2 
     alphabetically, Return 0 if their position doesn't matter'''
     
     if uname1.lower() < uname2.lower():
          return -1
     elif uname1.lower() > uname2.lower():
          return 1
     else:
          return 0

def sort_name(uname1, uname2):
     '''Return -1 if uname1's name comes before uname2's alphabetically. Return
     1 if uname1's name comes after uname2's alphabetically. sort by 
     sort_username if their names are identical'''
     
     name1 = FINAL_DATA[uname1]['name']
     name2 = FINAL_DATA[uname2]['name']
     
     if name1.lower() < name2.lower():
          return -1
     elif name1.lower() > name2.lower():
          return 1
     else:
          return sort_username(uname1, uname2)
     
def sort_popularity(uname1, uname2):
     '''Return -1 if number of uname1's followers are less than uname2's.
     Return 1 if number of uname1's followers are more than uname2's
     Sort by sort_username if they are identical'''
     
     followers1 = len(search_follows([uname1]))
     followers2 = len(search_follows([uname2]))
     
     if followers1 < followers2:
          return 1
     elif followers1 > followers2:
          return -1
     else:
          return sort_username(uname1, uname2)

def present_long_format(user_list):
     '''Print all the relevant information of the usernames in user_list
     separated by 10 -'s'''
     
     for user in user_list:
          print '----------'
          print user
          print 'name:', FINAL_DATA[user]['name']
          print 'location:', FINAL_DATA[user]['location']
          print 'website:', FINAL_DATA[user]['website']
          print 'bio:', FINAL_DATA[user]['bio']
          print 'follows:', FINAL_DATA[user]['follows']
     print '----------'
     
def read_query(q_file):
     '''Read q_file and perform indicated queries on the twitter dictionary
     FINAL_DATA'''
     
     line = q_file.readline().strip()
     line = q_file.readline().strip()
     user_list = [line]
     while line != 'FILTER':
          if line == 'followed-by':
               user_list = search_followed_by(user_list)
          elif line == 'follows':
               user_list = search_follows(user_list)
          line = q_file.readline().strip()
     line = q_file.readline().strip()
     while line != 'PRESENT':
          line_split = line.split()
          if 'follows' in line:
               user_list = filter_follows(user_list, line_split[1])
          elif 'followed-by' in line:
               user_list = filter_followed_by(user_list, line_split[1])
          elif 'name-includes' in line:
               user_list = filter_name(user_list, line_split[1])
          elif 'location-includes' in line:
               user_list = filter_location(user_list, line_split[1])
          line = q_file.readline().strip()
     line = q_file.readline().strip()
     if 'username' in line:
          user_list.sort(sort_username)
     elif 'name' in line:
          user_list.sort(sort_name)     
     elif 'popularity' in line:
          user_list.sort(sort_popularity)
     line = q_file.readline().strip()
     if 'long' in line:
          present_long_format(user_list)
     elif 'short' in line:
          print user_list
          

if __name__ == '__main__':
  
     data = raw_input("Data file: ")
     query = raw_input("Query file: ")
     data_file = open (data, "r")
     q_file = open (query, "r")
     FINAL_DATA = total_data(data_file)
     read_query(q_file)
   
     