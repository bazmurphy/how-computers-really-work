# Chapter 11 - The Internet

## 11.01 - Networking Terms Defined

- **Computer Network Basics:**

  - Definition: A system facilitating communication between computing devices.
  - Connectivity: Wireless (e.g., Wi-Fi) or wired (e.g., copper wiring, fiber optics).
  - Communication Protocol: Rules governing information exchange.

- **The Internet:**

  - Definition: Globally connected network of networks.
  - Protocol Suite: Common protocols used across all connected networks.
  - Connectivity: Various organizations worldwide interconnected.

- **Host or Node:**

  - Definition: Single computing device on a network.
  - Roles: Can function as a server, client, or both.
  - Server: Listens for inbound connections, provides services (e.g., web, email).
  - Client: Makes outbound connections, requests services from servers (e.g., smartphones, laptops).

- **Server Types:**

  - General: Any device accepting inbound requests and providing services.
  - Specialized Hardware: Computers designed for network server tasks.
    - Characteristics: Physically designed for datacenters, often include redundancy and management features.
  - Software-Based Servers: Any device with suitable software can act as a server.

![](/images/11-01-01.png)

![](/images/11-01-02.png)

![](/images/11-01-03.png)

## 11.02 - The Internet Protocol Suite

- **Introduction to Internet Protocol Suite**:
  - Standardizes communication on the internet for all devices.
  - Foundational protocols: TCP and IP (TCP/IP).
  - Operates in a layered model known as a network stack.
  - Encapsulation simplifies overall design.
- **Four-Layer Model**:
  - The Internet Protocol Suite (TCP/IP) standardizes communication on the internet.
  - TCP/IP consists of foundational protocols: Transmission Control Protocol (TCP) and Internet Protocol (IP).
  - Network protocols operate in layered models, forming network stacks.
  - The TCP/IP model comprises four layers: link layer, internet layer, transport layer, and application layer.
  - The OSI model, with seven layers, is also used but TCP/IP is the basis for the internet.
  - Each layer in the TCP/IP model has specific responsibilities.
  - Protocols in adjacent layers communicate with each other.
  - Network transmissions pass through layers: application, transport, internet, and link.
  - Different networking hardware uses protocols from various layers.
  - A network request flows through layers from the client to the server.
  - The request is formatted and interpreted according to application layer protocols.

![](/images/11-02-01.png)

![](/images/11-02-02.png)

![](/images/11-02-03.png)

### 11.02.01 - Link Layer

- The link layer is the lowest level of the internet protocol suite.
- It deals with physical and logical connections between hosts known as network links.
- Link layer protocols facilitate communication between devices on the same network.
- Each device on a link has a unique network address, often referred to as a MAC address.
- Data at the link layer is divided into frames, consisting of a header, payload, and footer.
- Frame headers contain source and destination MAC addresses.
- Wi-Fi and Ethernet are notable link layer technologies.
- Wi-Fi enables wireless communication between devices, each with a MAC address.
- Ethernet is used for wired physical connections and utilizes IEEE 802.3 standards.
- All devices connected to the internet participate in the link layer for connectivity to a local network.
- Networking devices like hubs and switches operate at the link layer.
- Hubs transmit every frame it receives to all other ports without intelligence.
- Switches examine MAC addresses and send frames only to the port where the destination device is connected.

![](/images/11-02-04.png)

### 11.02.02 - Internet Layer

- Internet Layer:
  - Enables data transmission beyond local network
  - Primary protocol: Internet Protocol (IP)
  - IP addresses uniquely identify hosts on the internet
  - Private IP addresses exist, not directly exposed on the internet
  - IP packet carries data, enclosed in link layer frame
- Internet Protocol:
  - Header contains source and destination IP addresses
  - IP version and header length included in the header
  - Data section carries payload
- IPv4 and IPv6:
  - IPv4: Dominant version, 32-bit address
  - IPv6: 128-bit address, larger address space to accommodate shortage
- IP Address Notation:
  - IPv4 typically in dotted decimal notation
  - Example: 192.168.1.23
- Subnets:
  - Computers on same local network have similar IP addresses
  - Subnetting divides IP address into network prefix and host identifier
  - Subnet mask or CIDR notation used to represent subnet size
- Subnet Mask:
  - Binary representation for network prefix
  - Example: 255.255.255.0 for a 24-bit network prefix
- Calculating Subnets:
  - Subnetting divides IP address into network prefix and host identifier
  - Example calculation provided for a subnet with a 24-bit network prefix
  - Subnet mask or CIDR notation used to represent subnet size
  - Example calculation shows how to determine if two computers are on the same subnet using bitwise logical AND operation
- Range of Addresses on a Subnet:
  - Network prefix bits followed by host identifier determine range
  - First and last addresses have special meanings
  - Calculation of available host addresses on a subnet provided

![](/images/11-02-05.png)

![](/images/11-02-06.png)

![](/images/11-02-07.png)

![](/images/11-02-08.png)

![](/images/11-02-09.png)

### 11.02.03 - Transport Layer

- Transport Layer Overview:
  - Provides communication channel for data exchange between applications.
  - Common protocols: TCP and UDP.
- TCP (Transmission Control Protocol):
  - Ensures reliability, error minimization, in-order data delivery.
  - Segments data.
- UDP (User Datagram Protocol):
  - "Best effort" protocol, prioritizing speed over reliability.
  - Data sent as datagrams.
- Focus on TCP for simplicity.
- Packet Delivery Path:
  - Link layer: MAC address for local network interface.
  - Internet layer: IP address for host identification.
  - Transport layer: Destination network port number for specific service/process.
- Analogy: IP Address vs. Network Port Number:
  - IP address: Street address of an office building.
  - Port number: Office number of a worker in the building.
- Packet Delivery Process:
  - Operating system delivers inbound data to the process listening on specified port.
- Port Classification:
  - Well-known ports (0-1023).
  - Registered ports (1024-49151).
  - Dynamic ports (greater than 49151).
- Standardization of Port Numbers:
  - Web servers typically listen on port 80 and 443.
- Client-Server Communication:
  - Servers use well-known ports for ease of connection.
  - Clients open ephemeral ports for receiving server responses.
- Endpoint and Socket:
  - IP address and port number form an endpoint.
  - Instance of an endpoint is a socket.
  - Sockets can listen for new connections or represent established connections.

![](/images/11-02-10.png)

### 11.02.04 - Application Layer

- Application layer is the topmost layer of the internet protocol suite
- Focuses on specific tasks for communication over the internet
- Protocols at this layer include HTTP for web servers, SMTP for email servers, and FTP for file transfer
- Describes the behavior of applications
- Lower layers enable applications to function
- Figure 11-12 illustrates the data contained in the application layer segment
- Figure 11-13 shows a frame containing an IP packet, TCP segment, and application data
- Process of assembling layers: application data -> segment -> packet -> frame
- Frames are processed in reverse order when sent from a host

![](/images/11-02-11.png)

![](/images/11-02-12.png)

## 11.03 - A Trip Through the Internet

- **Scenario Setup**:
  - Client device connected to Wi-Fi network.
  - Client connected to internet via router.
  - Server connected to internet via switch and router.
  - Client requests web page hosted on server.
- **Data Transmission from Client to Server**:
  - Client's web browser forms HTTP request for server.
  - HTTP request handed to TCP/IP software stack.
  - HTTP payload encapsulated in TCP segment.
  - TCP segment encapsulated in IP packet.
  - IP packet encapsulated in frame with local router's MAC address.
  - Frame transmitted wirelessly by client's Wi-Fi hardware.
- **Routing through Internet**:
  - Frame received by wireless access point, sent to router.
  - Router examines packet, determines destination IP.
  - Packet encapsulated in new frame, sent to next router.
  - Routing continues through multiple routers until reaching server's subnet router.
- **Reaching the Server**:
  - Last router encapsulates packet with server's MAC address.
  - Switch forwards frame based on MAC address.
  - Server receives frame, passes TCP/IP packet to software stack.
  - HTTP data handed to process listening on TCP port 80.
- **Server Response and Reverse Transmission**:
  - Web server software handles request, replies to client.
  - Process repeats in reverse order for response transmission.

![](/images/11-02-13.png)

## 11.04 - Foundational Internet Capabilities

- TCP/IP serves as the foundational framework for data transfer on the internet.
- Additional protocols complement TCP/IP by providing essential internet capabilities.
- DHCP (Dynamic Host Configuration Protocol) is crucial for dynamically assigning IP addresses to devices on a network.
- DNS (Domain Name System) is pivotal for translating domain names into IP addresses, enabling users to access websites via memorable names.
- NAT (Network Address Translation) is a system that facilitates the translation of private IP addresses within a local network to a single public IP address for internet communication.
- These protocols and systems operate at the application layer of the internet protocol suite.
- Together, they enhance the functionality and accessibility of the internet for users and devices.

### 11.04.01 - Dynamic Host Configuration Protocol

- **IP Addressing Basics**:
  - Every host on the internet requires an IP address, subnet mask, and router IP (default gateway) for communication.
  - IP addresses can be assigned statically or dynamically.
- **Static vs. Dynamic IP Assignment**:
  - Static IP: Manual configuration, requiring expertise and validation.
  - Dynamic IP: Utilizes DHCP for automatic assignment without user intervention.
- **Dynamic Host Configuration Protocol (DHCP)**:
  - DHCP automates IP address assignment.
  - DHCP server on the network manages a pool of IP addresses for assignment.
- **DHCP Workflow**:
  - Device connects to the network and broadcasts DHCP discovery message.
  - DHCP server responds with an offer of an IP address.
  - Client device accepts the offered IP address and requests it from the server.
  - DHCP server acknowledges the request and assigns the IP address to the client.
  - The assigned IP address is leased to the client and expires if not renewed.

![](/images/11-02-14.png)

### 11.04.02 - Private IP Address and Network Address Translation

- The limitation of available IP addresses leads ISPs to assign a single public IP address to customers, typically linked to a router.
- Private IP addresses are designated for use within private networks, such as those in homes or offices, and include ranges like 10.x.x.x, 172.16.x.x, or 192.168.x.x.
- Private IP addresses are nonroutable on the public internet but can be used simultaneously on multiple private networks.
- Network Address Translation (NAT) allows devices on a private network to share a single public IP address on the internet.
- NAT routers modify IP address information in packets, replacing private IP addresses with the router's public IP address.
- NAT ensures that all traffic from the home network appears to originate from the same public IP address, enhancing security by not exposing devices directly to the internet.
- Most consumer routers for home use incorporate NAT functionality, often with built-in wireless access points.
- Private IP addresses are also used in business settings to protect computers from exposure to the public internet.
- Corporate networks may employ proxy servers instead of NAT routers, offering additional features such as user authentication, traffic logging, and content filtering.

![](/images/11-02-15.png)

### 11.04.03 - The Domain Name System

- Domain Name System (DNS) maps names to IP addresses for user-friendly internet navigation.
- Fully Qualified Domain Names (FQDNs) consist of a local hostname and a domain suffix.
- Hosts query DNS servers to resolve hostnames into IP addresses.
- DNS servers maintain lists of IP addresses and respond to client queries accordingly.
- DNS facilitates distributing loads across multiple servers and allows multiple names to map to the same IP address.
- DNS records include A records (mapping hostnames to IP addresses), CNAME records (mapping one hostname to another), and MX records (used for email services).
- DNS hierarchy allows for shared responsibility in managing records across different levels.
- Root domain, top-level domains (TLDs), and second-level domains are integral parts of the DNS hierarchy.
- DNS servers cache records for faster responses and update them periodically to ensure recent data.

![](/images/11-02-16.png)

![](/images/11-02-17.png)

## 11.05 - Networking is Computing

- Internet is an integral part of computing, not a separate entity.
- Composed of hardware and software facilitating communication between devices.
- Data transmitted over the internet is ultimately represented as 0s and 1s.
- Networking interfaces (e.g., Wi-Fi, Ethernet adapters) are treated as I/O devices by computers.
- Operating systems interact with networking adapters through device drivers.
- OS includes software libraries enabling applications to communicate over the internet.
- Networking devices like routers and switches are specialized computers.
- Internet extends local computing capabilities, enabling data transfer and processing across multiple devices.

## 11.06 - Summary

- The internet is a globally connected set of computer networks using common protocols.
- Four layers of the internet protocol suite: link layer, internet layer, transport layer, application layer.
- Understanding data transmission and device interaction across these layers.
- DHCP provides networking configuration data.
- NAT facilitates devices on private networks to connect to the internet.
- DNS provides friendly names in place of IP addresses.

## 11.07 - Project 29: Examine the Link Layer

## 11.08 - Project 30: Examine the Internet Layer

## 11.09 - Project 31: Examine Port Usage

## 11.10 - Project 32: Trace the Route to a Host on the Internet

## 11.11 - Project 33: See your Leased IP Address

## 11.12 - Project 34: Is Your Device's IP Public or Private?

## 11.13 - Project 35: Find Information in DNS
