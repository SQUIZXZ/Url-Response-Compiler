import json
import unittest
import url_request_properties
from unittest.mock import MagicMock, patch
import datetime

class TestUrlRequestProperties(unittest.TestCase):

    def test_remove_duplicate_urls(self):

        # Checks if removeDuplicateUrls() removes duplicate urls
        result = url_request_properties.removeDuplicateUrls(['http://www.bbc.co.uk/iplayer', 'http://www.bbc.co.uk/iplayer'])
        self.assertEqual(result, ['http://www.bbc.co.uk/iplayer'])

    def test_validate_urls(self):

        # Checks removeDuplicateUrls() returns only urls with "http"
        result = url_request_properties.validateUrls(['httsp://www.bbc.co.uk/iplayer', 'https://www.bbc.co.uk/iplayer'])
        self.assertEqual(result, ['https://www.bbc.co.uk/iplayer'])

        # Checks removeDuplicateUrls() returns nothing if inputs are invalid
        result = url_request_properties.validateUrls(['httsp://www.bbc.co.uk/iplayer', 'httsp://www.bbc.co.uk/iplayer'])
        self.assertEqual(result, [])

        # Checks if removeDuplicateUrls() removes duplicates in return
        result = url_request_properties.validateUrls(['http://www.bbc.co.uk/iplayer', 'http://www.bbc.co.uk/iplayer'])
        self.assertEqual(result, ['http://www.bbc.co.uk/iplayer'])

        # Checks if removeDuplicateUrls() returns only urls without forbidden characters
        result = url_request_properties.validateUrls(['http://www.bbc.co.uk/<iplayer>', 'http://www.bbc.co.uk/ iplayer','http://www.bbc.co.uk/iplayer'])
        self.assertEqual(result, ['http://www.bbc.co.uk/iplayer'])
    
    
    @patch('url_request_properties.requests')
    def test_get_url_request_properties(self, mock_requests):

        # Creating mock of requests.get()
        mock_response = MagicMock()

        # Mocking request attributes
        mock_response.status_code = 200
        mock_response.headers = {'Content-length': '517710', 'Date': 'Sun, 28 Aug 2022 11:57:23 GMT'}
        mock_response.elapsed = datetime.timedelta(seconds=0.466)
        mock_requests.get.return_value = mock_response

        # Checks if function correctly returns json for url
        self.assertEqual(url_request_properties.getUrlRequestProperties(['http://www.bbc.co.uk/iplayer']), json.dumps([{'url': 'http://www.bbc.co.uk/iplayer', 'statusCode': 200, 'contentLength': '517710', 'requestDuration': '466ms', 'date': 'Sun, 28 Aug 2022 11:57:23 GMT'}, [{"statusCode": 200, "numberOfResponses": 1}]]))

        # Checks getUrlRequestProperties() correctly returns content length header if request returns a transfer encoding header 
        mock_response.headers = {'Date': 'Sun, 28 Aug 2022 11:57:23 GMT', 'Transfer-encoding': 'chuncked'}
        self.assertEqual(url_request_properties.getUrlRequestProperties(['https://google.com']), json.dumps([{'url': 'https://google.com', 'statusCode': 200, 'contentLength': 'None', 'requestDuration': '466ms', 'date': 'Sun, 28 Aug 2022 11:57:23 GMT'}, [{"statusCode": 200, "numberOfResponses": 1}]]))
     
        # Checks if getUrlRequestProperties() returns a json object which correctly counts number of responses for urls with status_code 400
        mock_response.status_code = 400
        mock_response.headers = {'Content-length': '517710', 'Date': 'Sun, 28 Aug 2022 11:57:23 GMT'}
        self.assertEqual(url_request_properties.getUrlRequestProperties(['http://www.bbc.co.uk/iplayer']), json.dumps([{'url': 'http://www.bbc.co.uk/iplayer', 'statusCode': 400, 'contentLength': '517710', 'requestDuration': '466ms', 'date': 'Sun, 28 Aug 2022 11:57:23 GMT'}, [{"statusCode": 400, "numberOfResponses": 1}]]))
        
        # Create test to check if exception is raised appropriate function output is returned


if __name__ == '__main__':
    unittest.main()

