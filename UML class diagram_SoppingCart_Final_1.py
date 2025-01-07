class Customer:
    __customers = []  # List to store all customer objects

    # Constructor: constructs objects with values
    def __init__(self, customerName, email, password, address: dict = None, creditCardInfo: dict = None, accountBalance: float = 0.0) -> None:
        # Default values for address and credit card info
        if address is None:
            address = {
                "Street": "",
                "House Number": "",
                "City": "",
                "State": "",
                "Zip Code": "",
                "Country": ""
            }
        if creditCardInfo is None:
            creditCardInfo = {
                "Type": "",
                "Card Number": "",
                "CVV": "",
                "Expiry": "",
                "Currency": ""
            }
        # Assigning instance variables
        self.__customerName = customerName
        self.__email = email
        self.__password = password
        self.__address = address
        self.__creditCardInfo = creditCardInfo
        self.__accountBalance = accountBalance
        self.__carts = []

    def signup(self) -> None:
        # Check if the email is already in use
        for customer in Customer.__customers:
            if customer.__email == self.__email:
                raise ValueError("Email already in use.")
        # Add the customer to the list
        Customer.__customers.append(self)
        print("Signup successful!")

    def signin(self, email, password):
        # Searching for the customer with the provided email and password
        for customer in Customer.__customers:
            if customer.__email == email and customer.__password == password:
                print("Signin successful!")
                return customer
        # If no customer found with the provided email and password
        print("Invalid email or password.")
        return None

    def updateProfile(self, newCustomerName=None, newEmail=None, newPassword=None, newAddress=None, newCreditCardInfo=None):
        # Updating profile attributes if new values are provided
        if newCustomerName:
            self.__customerName = newCustomerName
        if newEmail:
            # Checking if the new email is already in use
            for customer in Customer.__customers:
                if customer.__email == newEmail:
                    raise ValueError("Email already in use.")
            self.__email = newEmail
        if newPassword:
            self.__password = newPassword
        if newAddress:
            self.__address = newAddress
        if newCreditCardInfo:
            self.__creditCardInfo = newCreditCardInfo
        print("Profile updated successfully!")

    def getCustomerDetails(self):
        print("Name:", self.__customerName)
        print("Email:", self.__email)
        print("Address:", self.__address)
        print("Card Details:", self.__creditCardInfo)
        print("Account Balance:", self.__accountBalance)

    def getCustomerName(self):
        return self.__customerName

    def createCart(self, cartId):
        cart = ShoppingCart(cartId)
        self.__carts.append(cart)
        print(f"Cart {cartId} created successfully.")
        return cart

    def getCart(self, cartId):
        for cart in self.__carts:
            if cart.cartId == cartId:
                return cart
        print(f"No cart found with ID {cartId}.")
        return None

class ShoppingCart:
    def __init__(self, cartId: int):
        self.cartId = cartId
        self.products = []
        self.quantities = []
        self.dateAdded = None

    def addCartItem(self, productId: int, quantity: int, dateAdded: str):
        self.products.append(productId)
        self.quantities.append(quantity)
        self.dateAdded = dateAdded
        print(f"Added product {productId} with quantity {quantity} to cart {self.cartId} on {self.dateAdded}")

    def updateQuantity(self, productId: int, newQuantity: int):
        if productId in self.products:
            index = self.products.index(productId)
            self.quantities[index] = newQuantity
            print(f"Updated product {productId} quantity to {newQuantity}")
        else:
            print(f"Product {productId} not found in cart.")

    def viewCartDetails(self):
        print(f"Cart ID: {self.cartId}")
        for product, quantity in zip(self.products, self.quantities):
            print(f"Product ID: {product}, Quantity: {quantity}")

    def checkOut(self):
        print(f"Checking out cart {self.cartId} with items: {self.products}")

class Menu:
    def __init__(self):
        self.current_customer = None

    def display_menu(self):
        while True:
            if self.current_customer is None:
                print("\nMenu:")
                print("1. Sign Up")
                print("2. Sign In")
                print("3. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.signup()
                elif choice == '2':
                    self.signin()
                elif choice == '3':
                    print("Exiting the menu.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("\nMenu:")
                print("1. Update Profile")
                print("2. View Customer Details")
                print("3. Create Shopping Cart")
                print("4. Add Item to Cart")
                print("5. Update Item Quantity")
                print("6. View Cart Details")
                print("7. Check Out")
                print("8. Sign Out")
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.update_profile()
                elif choice == '2':
                    self.view_customer_details()
                elif choice == '3':
                    self.create_cart()
                elif choice == '4':
                    self.add_item_to_cart()
                elif choice == '5':
                    self.update_item_quantity()
                elif choice == '6':
                    self.view_cart_details()
                elif choice == '7':
                    self.check_out()
                elif choice == '8':
                    self.signout()
                else:
                    print("Invalid choice. Please try again.")

    def signup(self):
        while True:
            customerName = input("Enter Customer Name: ")
            if customerName.strip() == "":
                print("Customer name is required.")
                continue
            else:
                break

        while True:
            email = input("Enter Email: ")
            if email.strip() == "":
                print("Email is required.")
                continue
            else:
                break

        while True:
            password = input("Enter Password: ")
            if password.strip() == "":
                print("Password is required.")
                continue
            else:
                break

        address = {
            "Street": input("Enter Street: "),
            "House Number": input("Enter House Number: "),
            "City": input("Enter City: "),
            "State": input("Enter State: "),
            "Zip Code": input("Enter Zip Code: "),
            "Country": input("Enter Country: ")
        }
        creditCardInfo = {
            "Type": input("Enter Card Type: "),
            "Card Number": input("Enter Card Number: "),
            "CVV": input("Enter CVV: "),
            "Expiry": input("Enter Expiry: "),
            "Currency": input("Enter Currency: ")
        }

        while True:
            try:
                accountBalance = float(input("Enter Account Balance: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the account balance.")

        customer = Customer(customerName, email, password, address, creditCardInfo, accountBalance)
        try:
            customer.signup()
        except ValueError as e:
            print(e)

    def signin(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        customer = Customer("", email, password).signin(email, password)
        if customer:
            self.current_customer = customer

    def signout(self):
        print(f"Customer {self.current_customer.getCustomerName()} signed out successfully.")
        self.current_customer = None

    def update_profile(self):
        if self.current_customer:
            newCustomerName = input("Enter New Customer Name (leave blank to keep current): ")
            newEmail = input("Enter New Email (leave blank to keep current): ")
            newPassword = input("Enter New Password (leave blank to keep current): ")
            
            # Validate yes/no input for address change
            while True:
                change_address = input("Change address? (y/n): ").lower()
                if change_address in ('y', 'n'):
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

            newAddress = {
                "Street": input("Enter New Street (leave blank to keep current): "),
                "House Number": input("Enter New House Number (leave blank to keep current): "),
                "City": input("Enter New City (leave blank to keep current): "),
                "State": input("Enter New State (leave blank to keep current): "),
                "Zip Code": input("Enter New Zip Code (leave blank to keep current): "),
                "Country": input("Enter New Country (leave blank to keep current): ")
            } if change_address == 'y' else None
            
            # Validate yes/no input for credit card info change
            while True:
                change_credit_info = input("Change credit card info? (y/n): ").lower()
                if change_credit_info in ('y', 'n'):
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

            newCreditCardInfo = {
                "Type": input("Enter New Card Type (leave blank to keep current): "),
                "Card Number": input("Enter New Card Number (leave blank to keep current): "),
                "CVV": input("Enter New CVV (leave blank to keep current): "),
                "Expiry": input("Enter New Expiry (leave blank to keep current): "),
                "Currency": input("Enter New Currency (leave blank to keep current): ")
            } if change_credit_info == 'y' else None

            try:
                self.current_customer.updateProfile(newCustomerName or None, newEmail or None, newPassword or None, newAddress, newCreditCardInfo)
            except ValueError as e:
                print(e)
        else:
            print("No customer signed in.")

    def view_customer_details(self):
        if self.current_customer:
            self.current_customer.getCustomerDetails()
        else:
            print("No customer signed in.")

    def create_cart(self):
        if self.current_customer:
            cartId = int(input("Enter Cart ID: "))
            self.current_customer.createCart(cartId)
        else:
            print("No customer signed in.")

    def add_item_to_cart(self):
        if self.current_customer:
            cartId = int(input("Enter Cart ID: "))
            cart = self.current_customer.getCart(cartId)
            if cart:
                productId = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))
                dateAdded = input("Enter Date Added (YYYY-MM-DD): ")
                cart.addCartItem(productId, quantity, dateAdded)
        else:
            print("No customer signed in.")

    def update_item_quantity(self):
        if self.current_customer:
            cartId = int(input("Enter Cart ID: "))
            cart = self.current_customer.getCart(cartId)
            if cart:
                productId = int(input("Enter Product ID: "))
                newQuantity = int(input("Enter New Quantity: "))
                cart.updateQuantity(productId, newQuantity)
        else:
            print("No customer signed in.")

    def view_cart_details(self):
        if self.current_customer:
            cartId = int(input("Enter Cart ID: "))
            cart = self.current_customer.getCart(cartId)
            if cart:
                cart.viewCartDetails()
        else:
            print("No customer signed in.")

    def check_out(self):
        if self.current_customer:
            cartId = int(input("Enter Cart ID: "))
            cart = self.current_customer.getCart(cartId)
            if cart:
                cart.checkOut()
        else:
            print("No customer signed in.")

# Running the Menu
menu = Menu()
menu.display_menu()
