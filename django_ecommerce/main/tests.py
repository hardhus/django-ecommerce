from django.test import TestCase, RequestFactory
from django.urls import resolve
from django.shortcuts import render
from .views import index
from users.models import User
import mock


class MainPageTests(TestCase):

    #############
    ### Setup ###
    #############

    @classmethod
    def setUpClass(cls) -> None:
        cls.cls_atomics = cls._enter_atomics()
        request_factory = RequestFactory()
        cls.request = request_factory.get("/")
        cls.request.session = {}

    ########################
    #### Testing routes ####
    ########################

    def test_root_resolves_to_main_view(self):
        main_page = resolve("/")
        self.assertEqual(main_page.func, index)
    
    def test_returns_appropriate_html_response_code(self):
        resp = index(self.request)
        self.assertEquals(resp.status_code, 200)

    #####################################
    #### Testing templates and views ####
    #####################################
    
    def test_returns_exact_html(self):
        resp = index(self.request)
        self.assertEquals(
            resp.content,
            render(self.request, "index.html").content,
        )

    def test_index_handles_logged_in_user(self):
        user = User(
            name="JJ",
            email="j@j.com",
        )
        self.request.session = {"user": "1"}
        with mock.patch("main.views.User.get_by_id") as get_mock:
            get_mock.return_value = user
            resp = index(self.request)
            self.request.session = {}
            expected_html = render(self.request, "user.html", {"user": user}).content
            self.assertEquals(resp.content, expected_html)
        # # Create the user needed for user lookup from index page
        # user = User(
        #     name="jj",
        #     email="j@j.com",
        # )
        # user.save()

        # self.request.session = {"user": "1"}

        # # Request the index page
        # resp = index(self.request)

        # # ensure we return the state of the session back to normal so
        # # we don't affect other tests
        # self.request.session = {}

        # # Verify it returns the page for the logged in user
        # expected_html = render(self.request, "user.html", {"user": User.get_by_id(uid="1")}).content
        # self.assertEquals(resp.content, expected_html)