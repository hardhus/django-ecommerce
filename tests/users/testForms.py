from django.test import TestCase
from users.forms import UserForm, SigninForm
from tests.testutils import FormTesterMixin


class FormTests(TestCase, FormTesterMixin):

    def test_signin_form_data_validation_for_invalid_data(self):
        invalid_data_list = [
            {'data': {'email': 'j@j.com'},
             'error': ('password', ['This field is required.'])},
            {'data': {'password': '1234'},
             'error': ('email', ['This field is required.'])}
        ]

        for invalid_data in invalid_data_list:
            self.should_have_form_error(
                SigninForm,
                invalid_data['error'][0],
                invalid_data['error'][1],
                invalid_data["data"]
            )

    def test_user_form_passwords_match(self):
        form = UserForm(
            {
                'name': 'jj',
                'email': 'j@j.com',
                'password': '1234',
                'ver_password': '1234',
                'last_4_digits': '3333',
                'stripe_token': '1'}
        )
        # Is the data valid?
        if form.is_valid():
            # Is the data clean?
            self.assertTrue(form.cleaned_data)

    def test_user_form_passwords_dont_match_throws_error(self):
        form = UserForm(
            {
                'name': 'jj',
                'email': 'j@j.com',
                'password': '234',
                'ver_password': '1234',  # bad password
                'last_4_digits': '3333',
                'stripe_token': '1'
            }
        )

        # Is the data valid?
        self.assertFalse(form.is_valid())


# TotalTest 3