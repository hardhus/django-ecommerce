from django.test import TestCase
from rest_framework import serializers
from main.models import StatusReport
from users.models import User
from main.serializers import StatusReportSerializer
from rest_framework.renderers import JSONRenderer
from collections import OrderedDict
from rest_framework.parsers import JSONParser
from io import BytesIO


class StatusReportSerializer_Tests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()

        cls.u = User(name="ŞEYMA", email="şeyma@nerede.com")
        cls.u.save()

        cls.new_status = StatusReport(user=cls.u, status="ŞEYMA NEREDE?")
        cls.new_status.save()

        when = cls.new_status.when.isoformat()
        if when.endswith("+00:00"):
            when = when[:-6] + "Z"
        cls.expected_dict = dict(OrderedDict([
            ("id", cls.new_status.id),
            ("user", cls.u.email),
            ("when", when),
            ("status", "ŞEYMA NEREDE?"),
        ]))

    def test_model_to_dictionary(self):
        serializer = StatusReportSerializer(self.new_status)
        self.assertEquals(self.expected_dict, serializer.data)

    def test_dictionary_to_json(self):
        serializer = StatusReportSerializer(self.new_status)
        content = JSONRenderer().render(serializer.data)
        expected_json = JSONRenderer().render(self.expected_dict)
        self.assertEquals(expected_json, content)

    def test_json_to_StatusReport(self):
        json = JSONRenderer().render(self.expected_dict)
        stream = BytesIO(json)
        data = JSONParser().parse(stream)

        serializer = StatusReportSerializer(self.new_status, data=data)
        self.assertTrue(serializer.is_valid())

        status = serializer.save()
        self.assertEqual(self.new_status.id, status.id)
        self.assertEqual(self.new_status.status, status.status)
        self.assertEqual(self.new_status.when, status.when)
        self.assertEqual(self.new_status.user, status.user)
        self.assertEqual(self.new_status, status)

    def test_json_to_new_StatusReport(self):
        json = JSONRenderer().render(self.expected_dict)
        stream = BytesIO(json)

        data = JSONParser().parse(stream)
        serializer = StatusReportSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        status = serializer.save()
        self.assertEqual(self.new_status.status, status.status)
        self.assertIsNotNone(status.when)
        self.assertEqual(self.new_status.user, status.user)