---
doc_type: hypothesis-highlights
url: 'https://www.scrapingbee.com/blog/web-scraping-101-with-python/'
---


## Metadata
- Author: [scrapingbee.com]()
- Title: Web Scraping 101 with Python
- Reference: https://www.scrapingbee.com/blog/web-scraping-101-with-python/
- Category: #article

## Page Notes
## Highlights
- HTTP is called a stateless protocol because each transaction (request/response) is independent. FTP, for example, is stateful because it maintains the connection. — [Updated on 2023-02-28 17:17:50](https://hyp.is/xiV71rdIEe2VUPN6NhIH0Q/www.scrapingbee.com/blog/web-scraping-101-with-python/) — Group: #Just-Me

- HyperText Transfer Protocol (HTTP) uses a client/server model. An HTTP client (a browser, your Python program, cURL, libraries such as Requests...) opens a connection and sends a message (“I want to see that page : /product”) to an HTTP server (Nginx, Apache...). Then the server answers with a response (the HTML code for example) and closes the connection. — [Updated on 2023-02-28 17:17:58](https://hyp.is/ys7yNLdIEe2aj0cWNS77RQ/www.scrapingbee.com/blog/web-scraping-101-with-python/) — Group: #Just-Me

- User-Agent: This contains information about the client originating the request, including the OS. In this case, it is my web browser (Chrome) on macOS. This header is important because it is either used for statistics (how many users visit my website on mobile vs desktop) or to prevent violations by bots. — [Updated on 2023-02-28 17:19:25](https://hyp.is/_rq08rdIEe2Z9l8IqqxL1A/www.scrapingbee.com/blog/web-scraping-101-with-python/) — Group: #Just-Me

- Cookies are one way how websites can store data on your machine. This could be either up to a certain date of expiration (standard cookies) or only temporarily until you close your browser (session cookies). Cookies are used for a number of different purposes, ranging from authentication information, to user preferences, to more nefarious things such as user-tracking with personalised, unique user identifiers. — [Updated on 2023-02-28 17:19:56](https://hyp.is/ENlDVrdJEe2ZkXcZtEJfNA/www.scrapingbee.com/blog/web-scraping-101-with-python/) — Group: #Just-Me

- Referer: The referrer header (please note the typo) contains the URL from which the actual URL has been requested. This header is important because websites use this header to change their behavior based on where the user came from. For example, lots of news websites have a paying subscription and let you view only 10% of a post, but if the user comes from a news aggregator like Reddit, they let you view the full content. They use the referrer to check this. Sometimes we will have to spoof this header to get to the content we want to extract. — [Updated on 2023-02-28 17:21:26](https://hyp.is/Rm8zfLdJEe2NAN95HrYa4Q/www.scrapingbee.com/blog/web-scraping-101-with-python/) — Group: #Just-Me

- Urllib3 is a high-level package that allows you to do pretty much whatever you want with an HTTP request. With urllib3, we could do what we did in the previous section with way fewer lines of code. — [Updated on 2023-02-28 17:26:52](https://hyp.is/CQFRVLdKEe2_Sm-3U9wWrQ/www.scrapingbee.com/blog/web-scraping-101-with-python/) — Group: #Just-Me

- XPath is a technology that uses path expressions to select nodes or node-sets in an XML document (or HTML document). If you are familiar with the concept of CSS selectors, then you can imagine it as something relatively similar. — [Updated on 2023-02-28 17:28:15](https://hyp.is/OqeRZLdKEe2tfvP0AWXwrQ/www.scrapingbee.com/blog/web-scraping-101-with-python/) — Group: #Just-Me

- To extract data from an HTML document with XPath we need three things — [Updated on 2023-02-28 17:28:57](https://hyp.is/U2RB1LdKEe27DxvsABvx4g/www.scrapingbee.com/blog/web-scraping-101-with-python/) — Group: #Just-Me
    - Annotation: * an HTML document
* some XPath expressions
* an XPath engine that will run those expressions
- The easiest way to speed up this process is to make several calls at the same time. This means that instead of sending every request sequentially, you can send requests in batches of five. In that case, each batch will handle five URLs simultaneously, which means you'll scrape five URLs in 10 seconds, instead of 50, or the entire set of 25 URLs in 50 seconds instead of 250. Not bad for a time-saver 🥳. — [Updated on 2023-02-28 17:37:00](https://hyp.is/c2XvaLdLEe2thesmx2__dQ/www.scrapingbee.com/blog/web-scraping-101-with-python/) — Group: #Just-Me



