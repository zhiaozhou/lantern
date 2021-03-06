from mock import MagicMock, patch


class TestConfig:
    def setup(self):
        pass
        # setup() before each test method

    def teardown(self):
        pass
        # teardown() after each test method

    @classmethod
    def setup_class(cls):
        pass
        # setup_class() before any methods in this class

    @classmethod
    def teardown_class(cls):
        pass
        # teardown_class() after any methods in this class

    def test_ll(self):
        from lantern.live import LanternLive
        live = LanternLive(MagicMock(), 'test', MagicMock())
        assert live.path() == 'test'

    def test_ll2(self):
        with patch('lantern.live.utils.get_ipython') as m:
            m.return_value = MagicMock()
            m.return_value.kernel = MagicMock()
            m.return_value.kernel.session = MagicMock()
            m.return_value.kernel.session.config = {'IPKernelApp': {'connection_file': '/'}}

            from lantern.live import run
            run(MagicMock())

    def test_ll3(self):
        with patch('lantern.live.utils.get_ipython') as m:
            m.return_value = MagicMock()
            m.return_value.kernel = MagicMock()
            m.return_value.kernel.session = MagicMock()
            m.return_value.kernel.session.config = {'IPKernelApp': {'connection_file': '/'}}

            from lantern.live import pipeline
            pipeline(MagicMock(), [], [])
