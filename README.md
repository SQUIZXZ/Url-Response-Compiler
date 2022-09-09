# Url-Response-Compiler

Developed using Python 3.10.5

<h2>Getting Started</h2>

Step 1: Clone the git repo<br /> 

Step 2: cd into app folder<br />

Step 3: Run <b>source venv/bin/activate</b> to start python virtual env<br />

Step 4: run <b>python url_request_properties.py</b><br />

Step 5:	Copy and paste line separated urls with no spaces, for example:<br />
	
http://www.bbc.co.uk/iplayer<br />
https://google.com<br />
http://www.bbc.co.uk/missing/thing<br />
http://not.exists.bbc.co.uk/<br />
http://www.oracle.com/technetwork/java/javase/downloads/index.html<br />
https://ichef.bbci.co.uk/news/976/cpsprodpb/0DAA/production/_107889430_kittensthree.jpg<br />
http://site.mockito.org/<br />
bad://address
	
Step 6: To run unit tests run <b>python test_url_request_properties.py</b>


<h2>Future Works</h2>
When storing the urls and their response property objects, instead of using a list, use a dictionary O(1) so it's possible to search a response to a url without having the search the entire list of urls O(n)

Conform to PEP8

Add type hints to function params for maintainability

Implemnent the solution using classes to make it more organised and easier to test even though it was a smaller project

Add test and src files for best practise

Minimise any dependency

Considering the validateUrls() function to detect illegal chars in urls, an encoding library could be used in a separate function to detect illegal chars. Doing this, it would be possible to detect any urls that need encoding and removing them before later use in the algorithm.
 
getUrlRequestProperties() function could to be split up into separated functions with params to make testing more transparent and clear and to reduce the responsiblity of a single function 

getUrlsRequestProperties() complies with rfc 2616: https://stackoverflow.com/questions/53001960/rfc-2616-http-content-length-and-transfer-encoding-compatibility

- Make sure no spaces in urls
- Sepearated line format only 



