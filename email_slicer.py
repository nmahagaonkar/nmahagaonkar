email = input("enter your email:").strip()

username = email[:email.index('@')]
domain = email.index('@')+1:]
print(f"your username is {username} and domain is {domain}")
