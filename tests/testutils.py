class FormTesterMixin():
    def should_have_form_error(self, form_cls, expected_error_name, expected_error_msg, data):
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

