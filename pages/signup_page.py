from pages.base_page import BasePage

class SignupPage(BasePage):
    URL = "https://automationexercise.com/login"

    def __init__(self, page):
            super().__init__(page)
            self.name_input = page.locator("[data-qa='signup-name']")
            self.email_input = page.locator("[data-qa='signup-email']")
            self.signup_button = page.locator("[data-qa='signup-button']")
            self.error_message_exsist_email = page.get_by_text("Email Address already exist!")
            self.password = page.get_by_role("textbox", name="Password *")
            self.first_name = page.get_by_role("textbox", name="First name *")
            self.last_name = page.get_by_role("textbox", name="Last name *")
            self.address = page.get_by_role("textbox", name="Address * (Street address, P.")
            self.country = page.get_by_label("Country *")
            self.state = page.get_by_role("textbox", name="State *")
            self.city = page.get_by_role("textbox", name="City * Zipcode *")
            self.zipcode = page.locator("#zipcode")
            self.phone_number = page.get_by_role("textbox", name="Mobile Number *")
            self.create_button = page.get_by_role("button", name="Create Account")
            self.success_message = page.get_by_text("Account Created!")

    def open_signup_page(self): 
        self.open(self.URL)
    
    def enter_name(self, name): 
            self.name_input.fill(name)
        
    def enter_email(self, email): 
            self.email_input.fill(email)

    def click_signup_button(self): 
            self.signup_button.click()
    #test
    
    def enter_password(self, password): 
        self.password.fill(password)
    
    def enter_first_name(self, first_name): 
        self.first_name.fill(first_name)

    def enter_last_name(self, last_name): 
        self.last_name.fill(last_name)

    def enter_address(self, address): 
        self.address.fill(address)

    def select_country(self, country): 
        self.country.select_option(country)

    def enter_state(self, state): 
        self.state.fill(state)

    def enter_city(self, city): 
        self.city.fill(city)

    def enter_zipcode(self, zipcode): 
        self.zipcode.fill(zipcode)

    def enter_phone_number(self, phone_number): 
        self.phone_number.fill(phone_number)

    def click_create_button(self): 
        self.create_button.click()
    
    def signup_firts_step(self, name, email):
        self.enter_name(name)
        self.enter_email(email)
        self.click_signup_button()


    def signup_finished(self, password, first_name, last_name, address, country, state, city, zipcode, phone_number):
        self.enter_password(password)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_address(address)
        self.select_country(country)
        self.enter_state(state)
        self.enter_city(city)
        self.enter_zipcode(zipcode)
        self.enter_phone_number(phone_number)
        self.click_create_button()


    