# Chapter 12 - The World Wide Web

## 12.01 - Overview of the World Wide Web

- The World Wide Web (WWW) is a collection of resources accessible through the internet.
- Resources are accessed using HyperText Transfer Protocol (HTTP).
- Web resources include documents, images, and other media.
- Web servers host these resources, while web browsers are used to access them.
- Web pages are viewed through browsers, and a group of related pages forms a website.
- Core attributes of the web include distribution, addressability, and interconnectedness.
- The web is distributed, meaning resources are spread across different servers globally.
- Addressability refers to the unique identification of resources through URLs.
- Interconnectedness highlights the linking of resources, allowing seamless navigation between them.

### 12.01.01 - The Distributed Web

- The World Wide Web operates on a distributed system, devoid of centralized control or governance over published content.
- Any computer connected to the internet can function as a web server, enabling individuals to share desired content without restrictions.
- While there's no overarching control, entities like organizations or countries can still impose access restrictions or block certain content.
- Governments retain the authority to shut down websites hosting illegal material, but outside such cases, the web remains an open platform for publishing diverse content.
- No single organization holds dominion over the content available on the web, emphasizing its decentralized nature.

### 12.01.02 - The Addressable Web

- The web utilizes Uniform Resource Locators (URLs) to assign unique addresses to resources, comprising both location and access information.
- URLs consist of several components: Scheme (identifying the protocol), Authority (containing the hostname or IP address), Path (location of the resource on the server), and Query (modifying the resource).
- A URL example: http://travel.example.com/destinations/carolinas?location=beach.
- The path part organizes resources into a logical hierarchy, analogous to a filesystem path.
- The query part modifies the resource returned to the client, with its format and meaning varying across sites.
- A URL may not include all elements shown in examples and can be valid with just scheme and authority.
- Browsers typically display the current URL in the address bar, with some simplifications such as excluding scheme and slashes.
- Examples of how Google Chrome displays URLs in its address bar are provided.
- URLs extend beyond web pages to other resources like images and scripts, each with its own URL.
- Relative URLs omit one or more elements (scheme, hostname, or full path), interpreted relative to the context they're found in, such as within a web page.

![](/images/12-01-01.png)

![](/images/12-01-02.png)

![](/images/12-01-03.png)

### 12.01.03 - The Linked Web

- URLs provide unique addresses for web resources, facilitating easy referencing.
- Hyperlinks, or links, connect web documents, allowing one-way referencing.
- Links do not require permission or reciprocal agreements to be established.
- The interconnectedness of web pages through links forms the basis of the World Wide Web.
- Documents linked via hyperlinks are termed hypertext documents.

### 12.01.04 - The Protocols of the Web

- The web is delivered using HyperText Transfer Protocol (HTTP), and its secure
  variant, HTTPS.

### 12.01.05 - HTTP

- **HTTP Basics:**
  - HTTP isn’t solely for hypertext transfer; it's used for various actions on web resources.
  - Relies on TCP/IP, where TCP ensures reliable data transfer and IP handles host addressing.
  - Operates on a request-response model.
- **HTTP Methods:**
  - Requests include an HTTP method, also known as an HTTP verb, indicating the action.
  - Common methods:
    - GET: Retrieve a resource.
    - PUT: Create or modify a resource.
    - POST: Create a resource.
    - DELETE: Remove a resource.
  - Servers may restrict certain methods on specific resources, often requiring permissions for deletion.
- **HTTP Response:**
  - Includes an HTTP status code indicating the server's response.
  - Status codes categorized:
    - 100s: Informational.
    - 200s: Success.
    - 300s: Redirection.
    - 400s: Client-side error.
    - 500s: Server-side error.
  - Common status codes:
    - 200: Success.
    - 301: Moved Permanently.
    - 401: Unauthorized.
    - 403: Forbidden.
    - 404: Not Found.
    - 500: Internal Server Error.
- **HTTP Request Format:**
  - Human-readable text format.
  - Request line includes method, URL, and HTTP version.
  - Followed by header fields providing additional information and an optional message body.
- **HTTP Response Format:**
  - Similar to request format.
  - First line includes HTTP version, status code, and response phrase.
  - May include header values and a message body.

![](/images/12-01-04.png)

### 12.01.06 - HTTPS

- HTTPS (HyperText Transfer Protocol Secure) encrypts data sent over the internet to enhance security.
- Encryption encodes data into an unreadable format, while decryption reverses this process.
- Cryptographic algorithms use secret cryptographic keys for encryption and decryption.
- HTTPS employs symmetric encryption (using a single shared key) and asymmetric encryption (using a key pair).
- Asymmetric encryption involves a public key for encryption and a private key for decryption.
- HTTPS prevents interception or modification of web traffic, reducing risks associated with unencrypted transmission.
- Transport Layer Security (TLS) encrypts HTTP requests in HTTPS, replacing the deprecated Secure Sockets Layer (SSL).
- HTTPS sessions begin with a client hello message, server hello message, and exchange of digital certificates.
- Digital certificates contain the server's public cryptographic key for asymmetric encryption.
- HTTPS ensures secure communication by exchanging encrypted messages between the client and server.
- The use of HTTPS is becoming more widespread, driven by its security and privacy benefits.
- Google incentivizes HTTPS adoption by marking HTTP sites as "Not secure" and favoring HTTPS sites in search rankings.

### 12.01.07 - The Searchable Web

- The web often begins for users with a search rather than navigating to specific URLs.
- Browser design encourages this behavior, as browsers typically use the address bar as a search box.
- Users commonly search for a site rather than typing its full URL in the address bar.
- This design enhances browser usability but blurs the line between URLs and search terms, and between browsers and search engines.
- Despite its prevalence, searching isn't a native feature of the web, lacking a standard specification.
- Searching relies on nonstandard, proprietary search engines.
- Google dominates the web searching space, with alternative search engines having significantly less worldwide usage.

## 12.02 - The Languages of the Web

- Web browsers serve beyond file downloading, also rendering web pages.
- Three essential languages for constructing websites: HTML, CSS, JavaScript.
- **HTML (HyperText Markup Language):**
  - Defines page structure.
  - Specifies elements like buttons.
- **CSS (Cascading Style Sheets):**
  - Defines page appearance.
  - Specifies visual attributes like size and color.
- **JavaScript:**
  - Defines page behavior.
  - Enables interactive functions like button-click actions.
- Web browsers can also render image, video, and audio formats.
- The foundational languages of the web: HTML, CSS, JavaScript.

### 12.02.01 - Structuring the Web with HTML

- HTML is a markup language used for structuring web pages, not a programming language.
- HTML elements are enclosed in tags (<>) and include various components like paragraphs, headings, and images.
- Tags define the structure of an HTML document, with opening `<tag>` and closing `</tag>` tags for elements.
- Some elements like `<img>` do not require closing tags and are self-contained.
- HTML documents are rendered by web browsers based on their default settings if no styling information is provided.
- The structure of an HTML document includes a declaration, `<html>` as the top-level parent tag, `<head>` for document description, and `<body>` for content.
- Important elements in the `<head>` include meta tags for character encoding and a title tag for page description.
- The `<body>` section contains content elements like headings `<h1>-<h6>`, paragraphs `<p>`, and images `<img>`.
- Images in HTML are referenced by URLs and can include alternate text for accessibility.
- Indentation in HTML is for readability but is not mandatory as browsers ignore extra whitespace.
- HTML standards are maintained by organizations like the W3C and WHATWG, with the HTML Living Standard being the current version.
- Browsers strive to support both current and older HTML standards, leading to variations in rendering across browsers.
- Web developers test their creations on multiple browsers to ensure consistent behavior due to differences in rendering.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>A Cat</title>
  </head>
  <body>
    <h1>Thoughts on a Cat</h1>
    <p>This is a cat.</p>
    <img src="cat.jpg" alt="cat photo" />
  </body>
</html>
```

![](/images/12-02-01.png)

### 12.02.02 - Styling the Web with CSS

- HTML separates structure and style for flexibility in rendering content.
- CSS (Cascading Style Sheets) defines styling rules for web pages.
- Each CSS rule consists of a selector and styles to apply to selected elements.
- Multiple rules can apply to the same element (cascading).
- Example CSS rules for paragraphs and headings demonstrate font, size, margin, and color properties.
- Font-family property allows specifying multiple fonts to increase compatibility.
- CSS can be applied inline or via an external stylesheet.
- External stylesheets allow for better organization and consistency across multiple pages.
- Linking a CSS file to HTML is done using the <link> tag.
- CSS enables basic styling like font, color, and margin adjustments, as well as more advanced styling options.

```css
p {
font- family: Arial, Helvetica, sans- serif;
font- size: 11pt;
margin- left: 10px;
color: DimGray;
}

h1 {
font- family: 'Courier New', Courier, monospace;
font- size: 18pt;
font- weight: bold;
}
```

```html
<style>
  p {
    color: red;
  }
</style>
```

```html
<link rel="stylesheet" type="text/css" href="style.css" />
```

![](/images/12-02-02.png)

### 12.02.03 - Scripting the Web with JavaScript

- The web initially aimed for sharing hypertext documents, but evolved into an interactive platform.
- JavaScript became pivotal for web interactivity, allowing browsers to function as application development platforms.
- JavaScript is interpreted, not compiled to machine code, though some browsers use JIT compilers for performance.
- Minification reduces JavaScript size for faster website loading without compiling it to machine code.
- JavaScript syntax resembles C, but it fundamentally differs, especially in its reliance on prototypes over classes.
- JavaScript interacts with HTML pages via the Document Object Model (DOM), a hierarchical structure of page elements.
- JavaScript can modify DOM elements and respond to page events like clicks using DOM manipulation methods.
- A simple script example demonstrates adding text to a paragraph upon clicking a photo using event handling and DOM manipulation.
- HTML elements can be referenced programmatically by assigning them IDs.
- JavaScript applications can be built within web browsers, adhering to the ECMAScript standard.
- Browsers implement script engines to interpret JavaScript according to the ECMAScript standard, updated regularly.

```js
document.getElementById("cat-photo").onclick = function () {
  document.getElementById("cat-para").innerHTML += " Meow!";
};
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>A Cat</title>
    <link rel="stylesheet" type="text/css" href="style.css" />
    <script src="cat.js"></script>
  </head>
  <body>
    <h1>Thoughts on a Cat</h1>
    <p id="cat- para">This is a cat.</p>
    <img id="cat- photo" src="cat.jpg" alt="cat photo" />
  </body>
</html>
```

![](/images/12-02-03.png)

### 12.02.04 - Structuring the Web's Data with JSON and XML

- Websites vs. web services: Websites provide HTML content for user consumption, while web services deliver data programmatically.
- Web services' significance: Often underpin websites and apps, providing data for various purposes.
- Scenario: Consider running a website about local bands; an app developer wants to integrate your data but needs it in a different format.
- Web service solution: Provide data in a format other than HTML, facilitating easier access and integration.
- XML overview: Introduced in the 1990s, text-based markup language, allows custom tags for data description.
- XML example: Describing a band with custom tags like `<band>` and `<concert>`.
- XML's flexibility: Custom tags require agreement between data producer and consumer.
- XML's popularity: Widely used but verbose; parsing can be complex.
- JSON overview: Describes data similar to JavaScript's syntax, concise and easy to parse.
- JSON example: Same band data represented in JSON format, utilizing objects and arrays.
- Advantages of JSON over XML: Terser syntax, preferred format for new web services in the 2010s.
- Rendering compactness: Both XML and JSON can be compactly rendered by removing extra whitespace.
- Usage in browsers: XML and JSON not directly rendered in browsers but consumed by code for various purposes.
- Example applications: Smartphone apps displaying nearby bands or client-side JavaScript transforming JSON into HTML for browser display.

```xml
<band name="The Highbury Musical Club">
  <bandMembers>
    <member name="Jane Fairfax" instrument="Piano" />
    <member name="Emma Woodhouse" instrument="Guitar" />
    <member name="Harriet Smith" instrument="Percussion" />
    <member name="Frank Churchill" instrument="Vocals" />
  </bandMembers>
  <upcomingConcerts>
    <concert location="Donwell Abbey" date="August 14, 2020" />
    <concert location="Hartfield" date="November 20, 2020" />
  </upcomingConcerts>
</band>
```

```json
{
  "name": "The Highbury Musical Club",
  "bandMembers": [
    {
      "name": "Jane Fairfax",
      "instrument": "Piano"
    },
    {
      "name": "Emma Woodhouse",
      "instrument": "Guitar"
    },
    {
      "name": "Harriet Smith",
      "instrument": "Percussion"
    },
    {
      "name": "Frank Churchill",
      "instrument": "Vocals"
    }
  ],
  "upcomingConcerts": [
    {
      "location": "Donwell Abbey",
      "date": "August 14, 2020"
    },
    {
      "location": "Hartfield",
      "date": "November 20, 2020"
    }
  ]
}
```

## 12.03 - Web Browsers

- Web browsers are software on the client side of the web.
- The first web browser was called WorldWideWeb, developed by Tim Berners-Lee in 1990, and was the first client for the first web server CERN httpd.
- WorldWideWeb was supplanted by Mosaic, a browser that popularized the web.
- Netscape Navigator was another major browser release with a large following.
- Microsoft entered the browser market in 1995 with Internet Explorer, becoming dominant.
- Currently, dominant browsers include Google Chrome, Apple Safari, and Mozilla Firefox.

### 12.03.01 - Rendering a Page

- **Initial Request**:
  - A user requests a webpage either by typing the URL or following a link.
  - Browser sends a request to the specified URL.
  - Server responds with HTML.
- **HTML Parsing and DOM Construction**:
  - Browser constructs a Document Object Model (DOM) from the HTML received.
  - HTML may contain references to other resources like images, scripts, and style sheets.
  - Browser makes separate requests for each resource.
- **Resource Retrieval**:
  - Browser fetches additional resources (images, scripts, style sheets) referenced in the HTML.
  - These resources have their own URLs.
- **Rendering Process**:
  - Browser displays the HTML, utilizing CSS for presentation.
  - JavaScript code, if present, is executed by a JavaScript engine.
  - JavaScript may manipulate the page immediately or register event handlers for later execution.
  - It can also request data from web services to update the page.
- **Components of Web Browsers**:
  - Rendering engine (for HTML and CSS).
  - JavaScript engine.
  - User interface.
  - Rendering engine and JavaScript engine determine page presentation and behavior.
  - Different browsers may render pages differently due to variations in rendering and JavaScript engines.
- **Rendering Engines**:
  - WebKit: Used in Apple's Safari browser and iOS applications.
  - Blink: Fork of WebKit, used in Chromium project (Google Chrome, Opera).
  - Gecko: Used in Mozilla Firefox.
- **Impact of Engine Choice**:
  - Safari, Chrome, Opera, and Edge (post-2018) use WebKit or Blink.
  - Firefox uses Gecko.
  - Microsoft Edge transitioned to Chromium-based, abandoning its own engines.

![](/images/12-03-01.png)

### 12.03.02 - The User Agent String

- **User Agent String Overview:**
  - The user agent string is a header value sent by web browsers to describe themselves when making requests to web servers.
  - It includes information about the browser, platform, rendering engine, and sometimes additional details.
- **Mozilla Identifier:**
  - The initial part of the user agent string, "Mozilla/5.0", originated from Netscape Navigator and was used by various browsers to receive the best website versions.
  - Currently, most browsers identify themselves as Mozilla, rendering this part of the string somewhat meaningless.
- **Platform Specification:**
  - The section within parentheses indicates the platform on which the browser is operating, such as "Windows NT 10.0; Win64; x64".
- **Rendering Engine:**
  - The rendering engine, indicated by "AppleWebKit/537.36", denotes the underlying technology responsible for displaying web content.
  - In the case of Chrome, it's a fork of WebKit, with a mention of KHTML, a legacy engine WebKit was based on.
- **Browser Name and Version:**
  - This section specifies the browser name and version, such as "Chrome/71.0.3578.98".
- **Compatibility Measures:**
  - Some user agent strings include references to other browsers, like Safari, to ensure compatibility with websites designed specifically for them.
  - Browsers employ such tactics due to historical fragmentation in browser capabilities and websites tailored for specific browsers.
- **Continued Complexity:**
  - Despite advancements in browser capabilities, many websites still send tailored content based on specific browsers, necessitating modern browsers to maintain compatibility measures.
  - This complexity persists due to the lack of evolution in certain websites' approaches to content delivery.

```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/71.0.3578.98 Safari/537.36
```

## 12.04 - Web Servers

- Web servers are powered by various programming languages and technologies that can communicate over HTTP and return data in a client-understandable format.
- Websites can be static or dynamic; static sites return pre-built HTML, CSS, or JavaScript files without modification, while dynamic sites perform server-side processing to generate HTML.
- Dynamic websites typically involve server-side processing where the server queries a database, retrieves data, formats it as HTML, and responds to client requests.
- Static websites handle requests by simply returning the corresponding static file, reducing complexity and resulting in simpler, faster, and more secure sites.
- The terms "static" and "dynamic" in this context refer to how content is served from the server, not the user experience. Both types of sites can offer interactive experiences using JavaScript.
- Hosting a static site requires web server software configured to serve static files, without the need for custom code.
- For dynamic websites, developers can use existing software or write custom code in various programming languages such as Python, C#, JavaScript, Java, Ruby, or PHP.
- Server-side development often involves interfacing with databases, with flexibility in choosing the database technology.

![](/images/12-04-01.png)

## 12.05 - Summary

- The web is a collection of distributed, linked resources accessible via HTTP over the internet.
- HTML structures web pages, CSS styles them, and JavaScript adds interactivity and functionality.
- Web browsers are used to access web content and display it to users.
- Web servers are software applications that host and serve web resources.

## 12.06 - Project 36: Examine HTTP Traffic

## 12.07 - Project 37: Run Your Own Web Server

## 12.08 - Project 38: Return HTML from Your Web Server

## 12.09 - Project 39: Add CSS to Your Website

## 12.10 - Project 40: Add JavaScript to Your Website
