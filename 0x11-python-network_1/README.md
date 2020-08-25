# Python - Network #1
Urllib module is the URL handling module for python. It is used to fetch URLs (Uniform Resource Locators). It uses the urlopen function and is able to fetch URLs using a variety of different protocols.

Urllib is a package that collects several modules for working with URLs, such as:

    urllib.request for opening and reading.
    urllib.parse for parsing URLs
    urllib.error for the exceptions raised
    urllib.robotparser for parsing robot.txt files

If urllib is not present in your environment, execute the below code to install it.
``` pip install urllib ```

### Example
```
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   ```