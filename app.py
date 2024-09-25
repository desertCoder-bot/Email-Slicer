def email_slicer():
    print("Welcome to the Email Slicer!")
    
    while True:
        email = input("Enter an email address (or 'quit' to exit): ").strip()
        
        if email.lower() == 'quit':
            print("Thank you for using Email Slicer!")
            break
        
        if '@' not in email:
            print("Invalid email address. Please try again.")
            continue
        
        username, domain = email.split('@')
        
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        print()

if __name__ == "__main__":
    email_slicer()
