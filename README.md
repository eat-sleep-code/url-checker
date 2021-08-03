# URL Checker 

This simple Python3 script that will intake a text list of URLs and check their response status.

## Prerequisites

- Python3
- The requests library.   This can be installed using `pip3 install requests`


## Getting started

- Create a text file named **urls.txt** that contains one URL per line.   
- Place this file in the same directory as the **check.py** Python script.
- Run the following command to make the Python script executable.:  `sudo chmod +x check.py`
- Run the following command to begin checking the list of URLs: `./check.py`


## Understanding the output

After the script completes a series of **.log** files may be created.

- **success.log** - URLs that returned a status code of 200 through 299.
- **redirect.log** - URLs that returned a status code of 300 through 399.   
- **error-client.log** - URLs that returned a status code of 400 through 499.   These may include URLs that are not found or URLs that are prohibited.
- **error-server.log** - URLs that returned a status code of 500 and above.   These indicate errors that are raised by the web servers itself.   These may be temporary errors or malformed URLs.
- **error-request.log** - Requests that fail completely due invalid schemas, invalid domains, or network errors.
