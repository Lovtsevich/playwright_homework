from playwright.sync_api import expect
from conftest import REGISTER_USER_FIRST_STEP
from conftest import REGISTER_USER_SECOND_STEP
from pages.signup_page import SignupPage


def test_open_signup_page(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    assert "login" in signup_page.get_url()

def test_name_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    expect(signup_page.name_input).to_be_visible()

def test_email_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    expect(signup_page.email_input).to_be_visible()

def test_signup_first_step(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    assert "signup" in signup_page.get_url()

def test_exsist_email_signup(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step("Anna", "test@test.com")
    expect(signup_page.error_message_exsist_email).to_be_visible()

def test_password_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    expect(signup_page.password).to_be_visible()

def test_first_name_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    expect(signup_page.first_name).to_be_visible()

def test_last_name_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    expect(signup_page.last_name).to_be_visible()

def test_address_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    expect(signup_page.address).to_be_visible()

def test_country_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    expect(signup_page.country).to_be_visible()

def test_state_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    expect(signup_page.state).to_be_visible()

def test_city_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    expect(signup_page.city).to_be_visible()

def test_zipcode_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    expect(signup_page.zipcode).to_be_visible()

def test_phone_number_field_visible(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    expect(signup_page.phone_number).to_be_visible()

def test_signup(page):
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.signup_firts_step(**REGISTER_USER_FIRST_STEP)
    signup_page.signup_finished(**REGISTER_USER_SECOND_STEP)

    assert "/account_created" in signup_page.get_url()