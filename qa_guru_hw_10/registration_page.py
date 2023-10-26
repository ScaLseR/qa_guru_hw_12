"""Класс для страницы регистрации https://demoqa.com/automation-practice-form"""
from pathlib import Path
from selene import have, command
from selene.support.shared import browser


class RegistrationPage:

    def open_form_page(self) -> None:
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_first_name(self, value: str) -> None:
        browser.element('#firstName').type(value)

    def fill_last_name(self, value: str) -> None:
        browser.element('#lastName').type(value)

    def fill_user_email(self, value: str) -> None:
        browser.element('#userEmail').type(value)

    def fill_gender(self) -> None:
        browser.element('[for="gender-radio-1"]').click()

    def fill_mobile_number(self, value: str) -> None:
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year: str, month: str, day: str) -> None:
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_few_subjects(self, value: list) -> None:
        browser.element('#subjectsInput').type(value[0]).press_enter().type(value[1]).press_enter()

    def fill_hobbies(self, value) -> None:
        browser.all('.custom-control').element_by(have.exact_text(value)).click()

    def add_picture(self, value: str) -> None:
        browser.element("#uploadPicture").send_keys(str(Path(__file__).parent.joinpath(f'data/pictures/{value}')))

    def fill_current_address(self, value: str) -> None:
        browser.element('#currentAddress').type(value)

    def fill_state_and_city(self, state: str, city: str) -> None:
        browser.element('[id="state"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(state)).click()
        browser.element('[id="city"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(city)).click()

    def press_submit(self) -> None:
        browser.element('#submit').perform(command.js.click)

    def assert_have_registered_user(self, full_name, email, gender, mobile_number, date_of_birth, subjects,
                                     hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
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
