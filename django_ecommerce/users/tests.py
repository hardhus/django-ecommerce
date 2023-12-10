from django.test import TestCase
from unittest import TestCase as UTestCase
from .models import User
from .forms import SigninForm, UserForm
from django import forms



# Create your tests here.

class UserModelTest(TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.cls_atomics = cls._enter_atomics()
    #     cls.test_user = User(email="j@j.com", name="test user")
    #     cls.test_user.save()
    #     print("setUpClass")
    
    # safer setUpClass
    @classmethod
    def setUp(cls):
        cls.cls_atomics = cls._enter_atomics()
        cls.test_user = User(email="j@j.com", name="test user")
        cls.test_user.save()
    
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     pass

    # @classmethod
    # def tearDown(cls):
    #     pass

    def test_user_to_string_print_email(self):
        self.assertEquals(str(self.test_user), "j@j.com")

    def test_get_by_id(self):
        self.assertEquals(User.get_by_id(1), self.test_user)

class FormTesterMixin():
    def assertFormError(self, form_cls, expected_error_name, expected_error_msg, data):
        from pprint import pformat
        test_form = form_cls(data=data)
        # if we get an error then the form should not be valid
        self.assertFalse(test_form.is_valid())
        self.assertEquals(
            test_form.errors[expected_error_name],
            expected_error_msg,
            msg="Expected {} : Actual {} : using data {}".format(
                test_form.errors[expected_error_name],
                expected_error_msg, pformat(data)
            )
        )

class UFormTest(UTestCase, FormTesterMixin):
    # TODO UTestCase hata vermiyor TestCase hata veriyor neden? ve Şeyma Nerede?
    def test_signin_form_data_validation_for_invalid_data(self):
        invalid_data_list = [
            {'data': {'email': 'j@j.com'},
            'error': ('password', [u'This field is required.'])},
            {'data': {'password': '1234'},
            'error': ('email', [u'This field is required.'])}
        ]

        for invalid_data in invalid_data_list:
            self.assertFormError(
                SigninForm,
                invalid_data["error"][0],
                invalid_data["error"][1],
                invalid_data["data"],
            )

class FromTest(TestCase, FormTesterMixin):

    def test_user_form_passwords_match(self):
        form = UserForm(
            {
                "name": "jj",
                "email": "j@j.com",
                "password": "1234",
                "ver_password": "1234",
            }
        )
        # Is the data valid? -- if not print out the errors
        self.assertTrue(form.is_valid(), form.errors)

        # this will throw an error if the form doesn't clean correctly
        self.assertIsNotNone(form.clean())
    
    def test_user_form_passwords_dont_match_throws_error(self):
        form = UserForm(
            {
                "name": "jj",
                "email": "j@j.com",
                "password": "234", # bad password
                "ver_password": "1234",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(
            forms.ValidationError,
            "Passwords do not match",
            form.clean,
        )