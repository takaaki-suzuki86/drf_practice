from rest_framework.test import APITestCase


class TestCheckMain(APITestCase):
    def test_main(self):
        expected = True
        result = True
        self.assertEqual(result, expected, "テスト動作確認")
