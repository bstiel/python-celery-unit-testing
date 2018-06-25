from unittest import TestCase, mock
from freezegun import freeze_time
import responses
import app
import tasks


class TestEndpoints(TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.client = app.app.test_client()
    
    @mock.patch('app.os.path.exists', return_value=False)
    def test_can_list_files(self, mock_path_exists):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    @mock.patch('app.fetch_data')
    def test_can_fetch_data(self, mock_fetch_data):
        response = self.client.post('/', json={'url': 'http://some-url'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'url': 'http://some-url'})
        mock_fetch_data.s.assert_called_once_with(url='http://some-url')

class TestTasks(TestCase):
    
    @responses.activate
    @freeze_time('2018-05-01T02:30:00')
    @mock.patch('tasks.os.makedirs')
    @mock.patch('tasks.os.path.exists', return_value=False)
    @mock.patch('tasks.open', new_callable=mock.mock_open)
    def test_fetch_data(self, mock_open, mock_path_exists, mock_makedirs):
        responses.add(responses.GET, 'http://some-url', body='0,1,2\n3,4,5', status=200)
        task = tasks.fetch_data.s(url='http://some-url').apply()
        self.assertEqual(task.status, 'SUCCESS')
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, 'http://some-url/')
        mock_makedirs.assert_called_once_with('./data')
        mock_open.assert_called_once_with('./data/20180501T023000000000', 'w')