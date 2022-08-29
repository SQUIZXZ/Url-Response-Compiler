# Developed using Python 3.10.5

import sys
import requests 
import json

def getUserInput(): 
    print("Copy and paste the list of urls here, press enter. Then press CTRL+D to submit") 
    urls = sys.stdin.read().splitlines()
    return urls

def removeDuplicateUrls(urls):
    urls = urls
    urls = list(dict.fromkeys(urls))
    return urls 

def validateUrls(urls):
    urls = removeDuplicateUrls(urls)
    validUrls = []
    invalidUrls = []
    
    forbiddenChar = [",", "<", ">", "{", "}", " " ] 
    
    # Checks url for illegal characters in url
    for url in urls:
        if "http" in url:
            if any(char in url for char in forbiddenChar):
                invalidUrls.append(url)
            else: 
                validUrls.append(url)
        else:
            invalidUrls.append(url)
    
    print("These urls are invalid: ", invalidUrls)
    return validUrls

def getUrls():
    urls = validateUrls(removeDuplicateUrls(getUserInput()))
    return urls

def getUrlRequestProperties(urls):

    # List of all urls
    urls = urls

    # List of server response objects for each url
    responses = []

    print("Processing url requests (below)...")

    # Dict storing count of unique status_code responses
    statusCodeCount = {}

    # List of statusCodeCount objects
    allStatusCodeCount = []

    # Performing url response operations
    for url in urls:
        try:
            # GET request to url, storing response object 
            resGet = requests.get(url, headers={'Accept-Encoding': None}, timeout=3)

            # Stores response status_code
            status_code = resGet.status_code

            # Elapsed request time
            requestDuration = resGet.elapsed.total_seconds() * 1000
            
            # Checking if response header 'Transfer-encoding' exists
            if 'Transfer-encoding' in resGet.headers:
                contentLength = "None"
            else: 
                contentLength = resGet.headers['Content-length']

            # Stores response date
            date = resGet.headers['Date']

            # Creating server response object
            response = {
                "url" : url,
                "statusCode" : status_code,
                "contentLength" : contentLength,
                "requestDuration" : str(round(requestDuration)) + "ms",
                "date" : date
            }

            # Checking if reponse status code already exist
            if status_code not in statusCodeCount:
                statusCodeCount[status_code] = 0
            # Incrementing count for status_code if already exists
            if status_code in statusCodeCount:
                statusCodeCount[status_code] = statusCodeCount.get(status_code) + 1
                
            # Saving server response
            responses.append(response)
            
        except requests.exceptions.RequestException:
            
            # Creating object for invalid url
            response = {
                    "url" : url,
                    "error" : "invalid url"
                }

            responses.append(response)
            continue
    
    # Creates object containing count of all status_code responses
    for status in statusCodeCount:
        statusCount = {
            "statusCode": status,
            "numberOfResponses": statusCodeCount[status]
        }
        allStatusCodeCount.append(statusCount)

    responses.append(allStatusCodeCount)
    print(responses)
    return json.dumps(responses)



if __name__ == '__main__':
    getUrlRequestProperties(getUrls())


