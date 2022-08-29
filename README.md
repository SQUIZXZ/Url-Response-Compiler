# Url-Response-Compiler

<h2>Getting Started</h2>

Step 1: Clone the git repo<br /> 

Step 2: cd into app folder<br />

Step 3: Run source venv/bin/activate to start python virtual env<br />

Step 4: run: python url_request_properties.py<br />

Step 5:	Copy and paste line separated urls with no spaces, for example:<br />
	
http://www.bbc.co.uk/iplayer<br />
https://google.com<br />
http://www.bbc.co.uk/missing/thing<br />
http://not.exists.bbc.co.uk/<br />
http://www.oracle.com/technetwork/java/javase/downloads/index.html<br />
https://ichef.bbci.co.uk/news/976/cpsprodpb/0DAA/production/_107889430_kittensthree.jpg<br />
http://site.mockito.org/<br />
bad://address
	
Step 6: To run unit tests run: python test_url_request_properties.py


<h2>Future Works</h2>
When storing the urls and their response property objects, instead of using a list, use a dicntionary O(1) so a it's possible to search a response to a url without having the search the entire list of urls O(n)


Conform to PEP8

Implemnent the solution using classes to make it more organised and easier to test even though it was a smaller project

Add test and src files for best practise

Minimise any dependency

Considering the time complexity of validateUrls() 0(n2) function to detect illegal chars in urls, an encoding library could be used in a sperate function to detect illgal chars in urls in which would reducuce the complexity to worst case 0(n). Doing this, it would be possbile to detect any urls that need encoding and removing before being later used in the algorithm.

On that note, the getUrlRequestProperties() function needs to be split up into separated functions with params to make testing more transparent and clear 

getUrlsRequestProperties() complies with rfc 2616: https://stackoverflow.com/questions/53001960/rfc-2616-http-content-length-and-transfer-encoding-compatibility

- Make sure no spaces in urls
- Sepearated line format only 



