from django.test import TestCase
from users.models import User
from django.db import IntegrityError


class UserModelTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super(UserModelTest, cls).setUpClass()
        # cls.cls_atomics = cls._enter_atomics() Buna gerek kalmadı ama bi süre dursun burada
        # cls.test_user = User(email="j@j.com", name="test user")
        # cls.test_user.save()
        pass

    @classmethod
    def setUpTestData(cls):
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

    # ŞEYMA
    # def test_get_by_id(self):
    #     self.assertEquals(User.get_by_id(1), self.test_user)

    def test_create_user_function_stores_in_database(self):
        user = User.create("test", "test@t.com", "1234")
        self.assertEquals(User.objects.get(email="test@t.com"), user)

    def test_create_user_allready_exists_throws_IntegrityError(self):
        self.assertRaises(
            IntegrityError,
            User.create,
            "test user",
            "j@j.com",
            "1234",
            
        )


# TotalTest 4