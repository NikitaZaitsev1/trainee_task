from innotter.aws_service import AwsService

from unittest import TestCase
from unittest.mock import patch


class TestCaseAwsS3(TestCase):

    @patch('innotter.aws_service.AwsService.upload_to_s3')
    def test_upload_to_s3(self, upload_to_s3_mock):
        upload_to_s3_mock.return_value = True
        self.assertEqual(True, AwsService().upload_to_s3("image.jpg", folder="user"))
