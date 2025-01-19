def authuser():
    setUser = "astro"
    setPass = "astro123"
    username = input("Enter username : ")
    password = input("Enter password : ")
    if username == setUser and password == setPass:
        return True
    else:
        return False
    
    