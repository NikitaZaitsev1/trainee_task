import os
from unittest import TestCase
from unittest.mock import patch

from innotter.email_service import EmailService


class TestCaseAwsSES(TestCase):

    @patch('innotter.email_service.EmailService.notify_by_mail')
    def test_notify_by_mail(self, notify_by_mail_mock):
        notify_by_mail_mock.return_value = None
        self.assertEqual(None, EmailService().notify_by_mail([os.getenv("ADMIN_EMAIL")]))
