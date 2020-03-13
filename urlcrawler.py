#-*- coding:utf-8 -*-
import requests
import bs4
import argparse
from fake_useragent import UserAgent
try:
    # python2
    from urllib.parse import urlparse
except ImportError:
    # python3
     from urlparse import urlparse

class Node:
    pNode = None
    data = list()
    count = 0
    
    def previous_node(self):
        return self.pNode
    def insert(self, url, content_len, status_code):
        self.data.append({'url' : url, 'content_len' : content_len, 'status_code' : status_code, 'link' : None})
        self.count += 1
    def getData(self, index):
        return self.data[index]
    def getLength(self):
        return self.count
    def modifyData(self, index, key, value):
        self.data[index][key] = value

def command_parser():
    parser = argparse.ArgumentParser(description = "URL crawler")
    
    parser.add_argument("--url", required=True, help="Input url or --url [Parent url] [Sub url (option)], --url http://test.com http://test.com/board/news/")
    parser.add_argument("--agent", required=False, default=None, action='store_true', help="Random User-agent, --agent")
    parser.add_argument("--excloud", required=False, default=None, nargs='+', help="Input exclouded url, --excloud http://test.com/logout http://test.com/login")
    parser.add_argument("--depth", required=False, default=3, help="Set parsing depth, --depth 4 (max = 10)")
    parser.add_argument("--nocontent", required=False, default=None, action='store_true', help="Whether to collect image, css, js url, --nocontent")
    parser.add_argument("--timeout", required=False, type=int, default=10, help="Set timeout. Default=10s, --timeout [time]")
    
    return parser.parse_args()

# Generate fake user-agent
def generateUserAgent():
    print("[*] Generating fake user-agent...")
    useragent = UserAgent().chrome
    print("[*] Done.")
    return useragent
    
def request(url, header):
    try:
        if len(header) == 0:
            r = requests.get(url)
        else:
            r = requests.get(url, headers = header)
    except requests.exceptions.MissingSchema as e:
        # Need scheme
        print("[!] "+str(e))
        exit()
    except requests.exceptions.ConnectionError as e:
        # Domain name error
        print("[!] "+str(e))
        return None
    
    return r

# parameter: bs >> beautifulSoup object (type = object)
#            arg >> user defined command 
#            url_table >> this variable stores all url list (type = list)
#            url >> user defined url (type = string)
def url_parser(bs, arg, url_table, url):
    tag_list = {"a" : "href", "img" : "src", "iframe" : "src", "form" : "action", "script" : "src", "link" : "href"}
    result_list = list()
    
    # Parsing js, css, img or not
    if arg.nocontent:
        del tag_list["img"]
        del tag_list["script"]
        del tag_list["link"]
    
    for key in tag_list.keys():
        link_list = bs.find_all(key)        
        
        for l in link_list:
            link = l.get(tag_list[key])
            
            if link is None or len(link) == 1 or link == "" or link[0] == '#':
                # Useless data
                # ex) #, #content, /, None ...
                continue
            
            if link[0] == '/' or link[0] == '?':
                result_list.append(url + link)
            else:
                result_list.append(link)
    
    # Delete duplicate url 
    result_list = set(result_list)
    result_list = list(result_list - set(url_table))
    url_table += result_list
    
    return insertData(result_list), url_table
    
# Insert in Node 
# parameter: data >> url data. (type = list) ["https://test.com", "http://aa.com", ...]
def insertData(data):
    node = Node()
    for d in data:
        node.insert(d, None, None)
        
    return node

def showToHTML(url_table):
    template = '''
    <html>
        <head>
            <title>
                URL cralwer result
            </title>
        </head>
        <body>
            {}
        </body>
    </html>
    '''.format("<br>".join(url_table))
    
    f = open("./result.html", "w")
    # data = template.encode("utf8")
    f.write(template)
    f.close()

def nodeToString(node):
    result = list()
        
    for index in range(node.getLength()):
        result.append(node.getData(index))
        
    for index in range(node.getLength()):
        link = node.getData(index)['link']
        if link is not None:
            result.append(nodeToString(link))
    
    return result
    
if __name__ == "__main__":
    url_table = list()
    arg = command_parser()
    user_url = arg.url
    
    header = ''
    
    if arg.agent is not None:
        header = {"User-agent" : generateUserAgent()}
    print("[*] URL crawling in {}".format(user_url))
    r = request(user_url, header)
    
    if r is None:
        exit()
    bs = bs4.BeautifulSoup(r.text, "html.parser")
    node, url_table = url_parser(bs, arg, url_table, user_url)
    
    for index in range(node.getLength()):
        
        d = node.getData(index)
        
        # print(d["url"], user_url)
        parsed_uri_1 = urlparse(d["url"]).netloc
        parsed_uri_2 = urlparse(user_url).netloc
        
        if parsed_uri_1 != parsed_uri_2:
            continue
        r = request(d["url"], header)
        
        if r is None:
            continue
        status_code = r.status_code
        bs = bs4.BeautifulSoup(r.text, "html.parser")
        node_link, url_table = url_parser(bs, arg, url_table, user_url)
        
        node.modifyData(index, "link", node_link)
        node.modifyData(index, "status_code", status_code)
    
    showToHTML(url_table)
    
    result = nodeToString(node)
    
    for i in result:
        print(i["url"] + " " + i["status_code"])
    
    # f = open("./test.txt", "a")
    # data = "\n".join(url_table).encode("utf8")
    # f.write(data+"\n\n\n")
    # f.close()