"""автотест на заполнение и отправку формы
https://demoqa.com/automation-practice-form """
from qa_guru_hw_10.registration_page import RegistrationPage
import allure


def test_filling_and_send_form():
    allure.dynamic.title('Проверка формы регистрации: Student Registration Form')
    allure.dynamic.tag('Practice Form')
    allure.dynamic.severity(severity_level='Critical')
    allure.dynamic.feature('Регистрация студента')
    allure.dynamic.story('Создаем первую задачу Jenkins')

    registration_page = RegistrationPage()
    with allure.step('Открываем страницу c формой регистрации'):
        registration_page.open_form_page()

    with allure.step('Заполняем First Name'):
        registration_page.fill_first_name('Бобр')
    with allure.step('Заполняем Last Name'):
        registration_page.fill_last_name('Добр')
    with allure.step('Заполняем Email'):
        registration_page.fill_user_email('bobrdobr@test.ru')
    with allure.step('Выбираем Gender'):
        registration_page.fill_gender()
    with allure.step('Заполняем Mobile Number'):
        registration_page.fill_mobile_number('1234567890')
    with allure.step('Заполняем Date of Birth'):
        registration_page.fill_date_of_birth('2022', 'May', '12')
    with allure.step('Заполняем Subjects'):
        registration_page.fill_few_subjects(['English', 'Computer Science'])
    with allure.step('Заполняем Hobbies'):
        registration_page.fill_hobbies('Reading')
    with allure.step('Выбираем и загружаем Picture'):
        registration_page.add_picture('bobr.jpg')
    with allure.step('Заполняем Current Address'):
        registration_page.fill_current_address('Бобриное Болото')
    with allure.step('Выбираем State and City'):
        registration_page.fill_state_and_city('Haryana', 'Karnal')
    with allure.step('Нажимаем кнопку Submit'):
        registration_page.press_submit()

    with allure.step('Выполняем проверку заполнения полей'):
        registration_page.assert_have_registered_user('Бобр Добр',
                                                       'bobrdobr@test.ru',
                                                       'Male',
                                                       '1234567890',
                                                       '12 May,2022',
                                                       'English, Computer Science',
                                                       'Reading',
                                                       'bobr.jpg',
                                                       'Бобриное Болото',
                                                       'Haryana Karnal')
