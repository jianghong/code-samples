def get_password (max_attempts):
  '''Prompt the user for a valid password until a valid one is given
  or they have entered max_attempts invalid passwords.
  A valid password is one that is at least length 6 and is not the word "password".
  Each time the user gives an invalid password, tell them that it
  was invalid and prompt again if they have not reached max_attempts tries.
  If the user gives max_attempts invalid passwords, return the empty string;
  otherwise return the valid password they gave.'''
  
  counter = 0
  valid = False
  while counter < max_attempts and not valid:
    pw = raw_input ("Valid password: ")
    if len(pw) < 6 or pw == 'password':
      print "Invalid!"
      counter += 1
    else:
      valid = True
  if valid:
    return pw
  else:
    return ''
    