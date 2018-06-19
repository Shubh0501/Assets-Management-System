import auth

# if database requires authentication use username and password instead of None, None

newAuth = auth.Authentication('localhost', 27017, 'test-db', None, None)

if __name__ == '__main__':
    if newAuth.reg("Himanshu", "himanshu10nain@gmail.com", "7042856750", "password"):
        print("User Created")
    else:
        print("User Data Not Unique.")

    if newAuth.login("7042856750", "password"):
        print("Login Successful")
    else:
        print("Login Failed")


