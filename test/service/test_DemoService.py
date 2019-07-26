from config import build_app
from main.service import DemoService

import unittest
from unittest.mock import Mock, patch


def test_index():
    DemoService.demo_service = Mock()
    assert 1 == 1

# class名は先頭に「test_」をつける必要はない
class DemoServiceTest(unittest.TestCase):

    def setUp(self):
        self.app = build_app()

    def tearDown(self):
        pass

    # @patchが複数存在する場合は、各モックのメソッド引数での順番に気をつける。
    # @patchの下から順にメソッド引数に定義する。
    @patch('main.service.DemoService.DemoHoge')
    @patch('main.service.DemoService.DemoFuga')
    def test_build_old_ss_target_local_yml(self, mock_DemoFuga, mock_DemoWriter):
        # current_appをテストでも利用したい場合は、withでアプリコンテキストを指定する。
        with self.app.app_context():
            DemoService.demo_service()
        assert 1 == 1
