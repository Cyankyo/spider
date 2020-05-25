import re
if __name__ == '__main__':
    str="document.write(\'<li class=\"next\">\');					 document.write(\'<a class=\"btn btn-info\" href=\"\');					 document.write(\'/203/\');					 document.write(\'203886/46166387-2.html\');					 document.write(\'\"><img src=\"/web/np.gif\"></a>\');					 document.write(\'</li>\');"
    pattern = re.compile(r'11([0-9]|-)+.html')
    a = re.search(pattern, str)
    if a:
        print(a.group())