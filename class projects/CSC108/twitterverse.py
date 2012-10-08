'''FINAL DATA will end up being the twitter dictionary. A twitter dictionary 
contains a person's twitter username as a key and 5 nested dictionaries as 
their value. The nested dictionaries contain the labels: name, location,
website, bio, and follows as keys and their respective info as values.'''
FINAL_DATA = None

def data_to_dict(uname, name, location, website, bio, follows):
     '''Return a dictionary that uses uname as the key and
     5 more nested dictionaries as the value. The nested dictionaries contain
     the name, location, website, bio, and people followed by the person 
     obtained from parameter. uname, name, location, wbesite, bio are strings.
     follows is a list.'''
     
     data = {}
     inner_data = {}
     inner_data['name'] = name
     inner_data['location'] = location
     inner_data['website'] = website
     inner_data['bio'] = bio
     inner_data['follows'] = follows
     data[uname] = inner_data
     
     return data
     
def store_data(data_file):
     '''Return a dictionary that uses a person's username as the key and
     5 more nested dictionaries as the value. Obtains the relevant information
     from data_file to pass as paramters for data_to_dict. data_file
     is a plain text document.'''
     
     line = data_file.readline()
     # Return empty string if data_file.readline() has reached the end
     # This will affect the next function
     if len(line) == 0:
          return ''
     uname = line.strip()
     line = data_file.readline()
     name = line.strip()
     line = data_file.readline()
     location = line.strip()
     line = data_file.readline()
     website = line.strip()
     line = data_file.readline()
     bio = '\n'
     # Add lines to bio until data_file.readline() reaches ENDBIO
     while line.strip() != "ENDBIO":
          bio += line
          line = data_file.readline()
     line = data_file.readline()
     follows = []
     # Append lines to follows until data_file.readline() reaches END
     while line.strip() != "END":
          follows.append(line.strip())
          line = data_file.readline() 
          
     return data_to_dict(uname, name, location, website, bio.rstrip(), follows)

def total_data(data_file):
     '''Return a comprehensive and updated dictionary that contains
     every username in data_file as a key and 5 more nested dictionaries 
     as the value. The nested dictionaries contain
     the name, location, website, bio, and people followed by the user.
     data_file is a plain text document.'''
     
     data = {}
     divided_data = None
     # Updates data until divided_data reaches the end of data_file
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
     # Iterate through keys in FINAL_DATA to check if they follow the users 
     # in user_list
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
     
     # Convert everything to lowercase to make filters case-insensitive
     result = []
     for users in user_list:
          if includes.lower() in FINAL_DATA[users]['name'].lower():
               result.append(users)
     result = remove_duplicates(result)
     return result

def filter_location(user_list, includes):
     '''Return a new list containing usernames from user_list that have
     includes as part of their location. includes is a string'''
     
     result = []
     for users in user_list:
          if includes.lower() in FINAL_DATA[users]['location'].lower():
               result.append(users)
     result = remove_duplicates(result)
     return result

def filter_follows(user_list, includes):
     '''Return a new list containing usernames from user_list that follow 
     includes. includes is a username'''
     
     result = []
     # Obtain a list of who follows includes and check if usernames in 
     # user_list are in that list
     for user in user_list:
          if user in search_follows([includes]):
               result.append(user)
     result = remove_duplicates(result)
     return result

def filter_followed_by(user_list, includes):
     '''Return a new list containing users from user_list that are followed by
     includes. includes is a username'''
     
     result = []
     # Obtain a list of who is followed by includes and check if usernames
     # in user_list are in that list
     for user in user_list:
          if user in search_followed_by([includes]):
               result.append(user)
     result = remove_duplicates(result)
     return result
     
def sort_username(uname1, uname2):
     '''uname1 and uname2 are usernames. Return -1 if uname1 comes before
     uname2. Return 1 if uname1 comes after uname2. Return 0 if their 
     position doesn't matter'''
     
     if uname1 < uname2:
          return -1
     elif uname1 > uname2:
          return 1
     else:
          return 0

def sort_name(uname1, uname2):
     '''Return -1 if uname1's name comes before uname2's Return
     1 if uname1's name comes after uname2's. Sort by 
     sort_username if their names are identical'''
     
     name1 = FINAL_DATA[uname1]['name']
     name2 = FINAL_DATA[uname2]['name']
     
     if name1 < name2:
          return -1
     elif name1 > name2:
          return 1
     else:
          return sort_username(uname1, uname2)
     
def sort_popularity(uname1, uname2):
     '''Return 1 if number of uname1's followers are less than uname2's.
     Return -1 if number of uname1's followers are more than uname2's
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
     separated by 10 -'s.'''
     
     # Ensure 10 -'s at top of output if user_list is empty
     if len(user_list) == 0:
          print '----------'
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
     '''Read q_file and perform each indicated query using the twitter 
     dictionary FINAL_DATA. q_file is a plain text document.'''
     
     line = q_file.readline().strip()
     line = q_file.readline().strip()
     user_list = [line]
     # Perform  respective search functions depending on keyword in q_file
     # until readline is at FILTER
     while line != 'FILTER':
          if line == 'followed-by':
               user_list = search_followed_by(user_list)
          elif line == 'follows':
               user_list = search_follows(user_list)
          line = q_file.readline().strip()
     # Perform respective filter functions depending on keyword in q_file
     # until readline is at PRESENT
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
     # Perform respective sort functions depending on keyword in q_file
     if 'username' in line:
          user_list.sort(sort_username)
     elif 'name' in line:
          user_list.sort(sort_name)     
     elif 'popularity' in line:
          user_list.sort(sort_popularity)
     line = q_file.readline().strip()
     # Print an output depending on keyword in q_file
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
   
     