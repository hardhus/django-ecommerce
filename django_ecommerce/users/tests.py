from django.test import TestCase, RequestFactory
from unittest import TestCase as UTestCase
from .models import User
from .forms import SigninForm, UserForm
from django import forms
from django.shortcuts import render
from django.urls import resolve
from users.views import register
import mock

# TotalTest 7

########################
#### Testing Models ####
########################


class UserModelTest(TestCase):

    # TODO burada cls.cls_atomics i setUpClass ta tek bir kere yap
    @classmethod
    def setUpClass(cls) -> None:
        cls.cls_atomics = cls._enter_atomics()
        cls.test_user = User(email="j@j.com", name="test user")
        cls.test_user.save()

    # @classmethod
    # def setUp(cls):
    #     cls.test_user = User(email="j@j.com", name="test user")
    #     cls.test_user.save()
    
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

    def test_create_user_function_stores_in_database(self):
        user = User.create("test", "test@t.com", "1234")
        self.assertEquals(User.objects.get(email="test@t.com"), user)

    def test_create_user_allready_exists_throws_IntegrityError(self):
        from django.db import IntegrityError
        self.assertRaises(
            IntegrityError,
            User.create,
            "test user",
            "j@j.com",
            "1234",
            
        )

#######################
#### Testing Forms ####
#######################

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

# class ViewTesterMixin():
#     @classmethod
#     def setupViewTester(cls,
#                         url,
#                         view_func,
#                         expected_html,
#                         status_code=200,
#                         session={}):
#         cls.request = RequestFactory().get(url)
#         cls.request.session = session
#         cls.status_code = status_code
#         cls.url = url
#         cls.view_func = view_func
#         cls.expected_html = expected_html
    
#     def test_resolves_to_correct_view(self):
#         test_view = resolve(self.url)
#         self.assertEquals(test_view.func, self.view_func)
    
#     def test_returns_appropriate_respose_code(self):
#         resp = self.view_func(self.request)
#         self.assertEquals(resp.status_code, self.status_code)
    
#     def test_returns_correct_html(self):
#         resp = self.view_func(self.request)
        

# TODO view testleri yazmayı çöz
class ViewTesterMixin(object):

    @classmethod
    def setupViewTester(cls, url, view_func,
                        status_code=200,
                        session={}):
        request_factory = RequestFactory()
        cls.request = request_factory.get(url)
        cls.request.session = session
        cls.status_code = status_code
        cls.url = url
        cls.view_func = staticmethod(view_func)
    
    @classmethod
    def set_expected_html(cls, expected_html):
        cls.expected_html = expected_html

    def test_resolves_to_correct_view(self):
        test_view = resolve(self.url)
        self.assertEquals(test_view.func, self.view_func)

    def test_returns_appropriate_respose_code(self):
        resp = self.view_func(self.request)
        self.assertEquals(resp.status_code, self.status_code)

    def test_returns_correct_html(self):
        resp = self.view_func(self.request)
        print("------------------------------------------")
        print(resp.content)
        print("------------------------------------------")
        print(self.expected_html)
        print("------------------------------------------")
        self.assertEquals(resp.content, self.expected_html)

# FIXME render_to_response yerine render kullanıldığı için sarmal bağımlılık oluyor
class RegisterPageTests(TestCase, ViewTesterMixin):

    @classmethod
    def setUpClass(cls):
        cls.cls_atomics = cls._enter_atomics()
        # request_factory = RequestFactory().get("/register")
        
        ViewTesterMixin.setupViewTester(
            "/register/",
            register,
        )
        
        html = render(
            cls.request,
            'register.html',
            {
                'form': UserForm(),
                'months': range(1, 12),
                'user': None,
                'years': range(2011, 2036),
            }
        )
        ViewTesterMixin.set_expected_html(html.content)
    

    def test_(self):
        pass

    # def setUp(self):
    #     request_factory = RequestFactory()
    #     self.request = request_factory.get('/register')

    # def test_invalid_form_returns_registration_page(self):
    #     with mock.patch('users.forms.UserForm.is_valid') as user_mock:

    #         user_mock.return_value = False

    #         self.request.method = 'POST'
    #         self.request.POST = None
    #         resp = register(self.request)
    #         print(self.expected_html)
    #         self.assertEquals(resp.content, self.expected_html)
    #         # make sure that we did indeed call our is_valid function
    #         self.assertEquals(user_mock.call_count, 1)

#     # def test_registering_new_user_returns_successfully(self):
        
#     #     self.request.session = {}
#     #     self.request.method = "POST"
#     #     self.request.POST = {
#     #         "email": "python@rocks.com",
#     #         "name": "pyRock",
#     #         "password": "bad_password",
#     #         "ver_password": "bad_password",
#     #     }

#     #     resp = register(self.request)
#     #     self.assertEquals(resp.status_code, 200)
#     #     self.assertEquals(self.request.session, {})