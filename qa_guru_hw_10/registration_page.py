"""Класс для страницы регистрации https://demoqa.com/automation-practice-form"""
from pathlib import Path
from selene import have, command


class RegistrationPage:

    def __init__(self, browser):
        self.browser = browser

    def open_form_page(self) -> None:
        self.browser.open('/automation-practice-form')
        self.browser.config.driver.maximize_window()
        self.browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(have.size_greater_than_or_equal(3))
        self.browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value: str) -> None:
        self.browser.element('#firstName').type(value)

    def fill_last_name(self, value: str) -> None:
        self.browser.element('#lastName').type(value)

    def fill_user_email(self, value: str) -> None:
        self.browser.element('#userEmail').type(value)

    def fill_gender(self) -> None:
        self.browser.element('[for="gender-radio-1"]').click()

    def fill_mobile_number(self, value: str) -> None:
        self.browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year: str, month: str, day: str) -> None:
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__month-select').type(month)
        self.browser.element('.react-datepicker__year-select').type(year)
        self.browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_few_subjects(self, value: list) -> None:
        self.browser.element('#subjectsInput').type(value[0]).press_enter().type(value[1]).press_enter()

    def fill_hobbies(self, value) -> None:
        self.browser.all('.custom-control').element_by(have.exact_text(value)).click()

    def add_picture(self, value: str) -> None:
        self.browser.element("#uploadPicture").send_keys(str(Path(__file__).parent.joinpath(f'data/pictures/{value}')))

    def fill_current_address(self, value: str) -> None:
        self.browser.element('#currentAddress').type(value)

    def fill_state_and_city(self, state: str, city: str) -> None:
        self.browser.element("#state").perform(command.js.scroll_into_view)
        self.browser.element("#state").click()
        self.browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(state)).click()
        self.browser.element("#city").click()
        self.browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(city)).click()

    def press_submit(self) -> None:
        self.browser.element('#submit').perform(command.js.click)

    def assert_have_registered_user(self, full_name, email, gender, mobile_number, date_of_birth, subjects,
                                     hobbies, picture, current_address, state_and_city):
        self.browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )
