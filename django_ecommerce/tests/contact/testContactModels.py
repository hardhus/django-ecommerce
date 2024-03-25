from django.test import TestCase, SimpleTestCase
import time
from contact.models import ContactForm
from contact.forms import ContactView
from datetime import datetime, timedelta

class UserModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(UserModelTest, cls).setUpClass()
        ContactForm(email="seyma@seyma.seyma1", name="seyma1").save()
        ContactForm(email="seyma@seyma.seyma2", name="seyma2").save()
        time.sleep(0.01)
        cls.firstUser = ContactForm(
            email="seyma@seyma.seyma0",
            name="seyma0",
        )
        cls.firstUser.save()

    def test_contactform_str_returns_email(self):
        self.assertEquals("seyma@seyma.seyma0", str(self.firstUser))

    # ŞEYMA
    def test_ordering(self):
        contacts = ContactForm.objects.all().order_by('-timestamp')
        self.assertEquals(self.firstUser, contacts[0])

class ContactViewTests(SimpleTestCase):

    def test_displayed_fields(self):
        expected_fields = ['name', 'email', 'topic', 'message']
        self.assertEqual(ContactView.Meta.fields, expected_fields)


# TotalTest 3