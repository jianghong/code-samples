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
     5 more nested dictionaries as the value. Obtains the relevant
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
     bio = ''
     while line.strip() != "ENDBIO":
          bio += line
          line = data_file.readline()
     line = data_file.readline()
     follows = []
     while line.strip() != "END":
          follows.append(line.strip())
          line = data_file.readline() 
          
     return data_to_dict(info, bio, follows)

def total_data(data_file):
     '''Return a comprehensive and updated dictionary that contains
     every user in data_file as a key and 5 more nested dictionaries 
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
     '''xxx'''
     
     result = []
     for users in user_list:
          for user in FINAL_DATA:
               if users in FINAL_DATA[user]['follows']:
                    result.append(user)
     result = remove_duplicates(result)
     return result
  

def search_followed_by(user_list):
     '''xxx'''
     
     result = []
     for users in user_list:
          for followed in FINAL_DATA[users]['follows']:
               result.append(followed)
     result = remove_duplicates(result)
     return result

def filter_name(user_list, includes):
     '''xxx'''
     
     result = []
     for users in user_list:
          if includes.lower() in FINAL_DATA[users]['name'].lower():
               result.append(users)
     result = remove_duplicates(result)
     return result

def filter_location(user_list, includes):
     '''xxx'''
     
     result = []
     for users in user_list:
          if includes.lower() in FINAL_DATA[users]['location'].lower():
               result.append(users)
     result = remove_duplicates(result)
     return result

def filter_follows(user_list, includes):
     '''xxx'''
     
     
def read_query(q_file):
     '''xxx'''
     pass

    
#def open_filename(prompt, m):
     #'''Open the given filename and read its content.'''
     
     #filename = raw_input(prompt)
     
     #data_file = open(filename, m)     
    ## Erase any whitespace between line.
     #for line in data_file:
          #line = line.strip()
          #print line
        
     #data_file.close()

if __name__ == '__main__':
     #filename = open_filename("Enter Data file name: ", "r")
     data_file = open ("data.txt", "r")
     FINAL_DATA = total_data(data_file)
   
     