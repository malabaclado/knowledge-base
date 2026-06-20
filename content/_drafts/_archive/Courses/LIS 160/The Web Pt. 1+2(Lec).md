Tim Berners Lee 
- invented the Web
- knighted by Queen Elizabeth in 2013
- wrote HTTP, URL and HTML

Vinton Cerf - invented the internet

---
###### TCP/IP Network Model
![[Pasted image 20211015120535.png]]



###### Foundations of the Web
- Foundations: URL, HTTP, HTML
- The web resides in the Application layer


Overview of How the Web Works
![[Pasted image 20211015120807.png]]


Communication protocol - HTTP
Language - HTML
Way of identifying resources - URL

- HTML + HTTP: provides way for computers to communicate
- HTML + URL: provides a way to link together documents thru hyperlink
- HTTP + URL: a way of addressing web pages
---
Uniform Resource Locator (URL)


![[Pasted image 20211015121049.png]]
![[Pasted image 20211015121258.png]]

Top Level Domain - .com, .org, .edu

---
Domain Name System (DNS)
- are computers that maintain a table of domain names and their corresponding IP addresses.

![[Pasted image 20211015122014.png]]

- The browser sends the domain name to the DNS server. The DNS server sends back the IP address of that domain. The browser now searches that IP on the web server and the web server now sends back the information (web page) to your browser.

---
Client-Server Architecture
![[Pasted image 20211015122045.png]]

---
Hypertext Transfer Protocol (HTTP)
- Rules that web clients and servers need to follow to communicate with each other and exchange their resources.

![[Pasted image 20211015122326.png]]

![[Pasted image 20211015122401.png]]

HTTP requests start with a method (usually GET or POST)

GET method - requesting for something
POST method - sending/submitting data

![[Pasted image 20211015123135.png]]

---
HyperText Markup Language (HTML)

---
Content Management Systems
1. Google Sites
2. Weebly & Wix
3. Wordpress
4. Drupal



---
# The Web Pt 2
- Focus of discussion: how websites are created.
- HTML (Hyper-Text Markup Language) and CSS (Cascading Style Sheets) are text files
- Use IDEs to make life easier.


Anatomy of an HTML element
1. Opening/Closing Tag
2. Attributes
3. Enclosed content

Adding links
- Tag: `<a></a>`
- Attributes
	- `target` option to open in new tab
	- `href` houses the URL

Adding images
- Tag: `<img></img>`
- Attributes
	- `src`image source
	- `alt` adds alternative text


---
### Cascading Style Sheets

How CSS is used
1. Use as an attribute (placed inside HTML tags)
2. Coded after the HTML code
3. In a separate file


coolors.co