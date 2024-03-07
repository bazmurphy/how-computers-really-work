# Chapter 01 - Computing Concepts

## 01.01 - Defining a Computer

- The term "computer" extends beyond traditional laptops and desktops to encompass various electronic devices, including smartphones, servers, video game consoles, fitness trackers, smartwatches, and smart televisions.
- Smartphones, increasingly becoming primary computing devices for many people, perform similar operations to PCs.
- The internet, powered by servers, is integral to modern computing, with every online interaction involving connections to servers.
- A computer is defined as any electronic device capable of executing a programmed set of logical instructions.
- Modern devices exhibit computer-like functionalities, emphasizing the broad scope of what constitutes a computer in contemporary contexts.

## 01.02 - Analog and Digital

- Computers are described as digital devices, contrasting with analog devices like mechanical clocks.
- Understanding the difference between analog and digital is crucial for understanding computing.
- Analog approach involves describing attributes of objects with potentially infinite variations.
- Analog measuring tools represent data through analogies, such as a needle on a scale or mercury in a thermometer.
- Analog storage methods include phonograph records and film-based cameras.
- Computers find it challenging to deal with analog data due to variability and difficulty in precise measurement.
- Digital systems represent data as a sequence of symbols, typically 0s and 1s, offering simplified hardware and improved reliability.
- All data in modern computers is represented as sequences of 0s and 1s.
- Despite the seeming limitation, digital systems can express complex ideas through sequences of 0s and 1s.
- 0s and 1s are not literally stored as numbers but as sequences where each entry has two possible states, represented differently in various storage mediums.
- The term "analog" is often used to mean "not digital" but doesn't always imply analogy to something else.

## 01.03 - Number Systems

- Computers operate in binary, dealing with 0s and 1s, unlike the decimal system most people are accustomed to.
- Decimal numbers are based on place-value notation, with each position representing a different order of magnitude, and each place having one of ten symbols (0 through 9).
- Decimal numbers follow the base 10 system, where each place is a power of ten.
- Binary numbers, on the other hand, use only two symbols (0 and 1) and follow the base 2 system.
- In binary, each place represents a power of 2, starting from 2^0, and the weights of each place determine the value of the number.
- To avoid confusion, binary numbers in the book are written with a "0b" prefix, indicating binary representation (e.g., 0b10 represents two in binary, while 10 without a prefix represents ten in decimal).

![](/images/01-03-01.png)

![](/images/01-03-02.png)

![](/images/01-03-03.png)

### Exercise

#### Exercise 1-2: Binary to Decimal

- 10 (binary) = 2 (decimal)
- 111 (binary) = 7 (decimal)
- 10101 (binary) = 21 (decimal)

#### Exercise 1-3: Decimal to Binary

- 3 (decimal) = 11 (binary)
- 8 (decimal) = 100 (binary)
- 14 (decimal) = 1110 (binary)

## 01.04 - Bits and Bytes

- A digit in a decimal number corresponds to a single place or symbol, while a bit in a binary number is a single place or symbol representing either 0 or 1.
- Bits are grouped into sets of eight called bytes for easier management.
- A 4-bit number is sometimes called a nibble.
- Each byte can represent 256 unique combinations of 0s and 1s.
- By raising 2 to the power of the number of bits, you can calculate the total combinations of 0s and 1s a binary number can represent.
- Understanding the number of bits or bytes required for data storage is crucial for computer engineers, as it impacts the capacity to represent information accurately.

![](/images/01-04-01.png)

![](/images/01-04-02.png)

## 01.05 - Prefixes

- Complex data types require a large number of bits for representation.
- Prefixes like giga- and mega- are used to communicate the size of data more easily.
- The International System of Units (SI) provides standard prefixes for quantifiable entities.
- SI prefixes are also used in electrical circuits.
- SI prefixes can represent quantities of bits and bytes, e.g., 3GB for 3 billion bytes.
- Conventionally, uppercase B denotes bytes, while lowercase b denotes bits.
- Most software works in base 2 when dealing with bytes, not base 10.
- Internet service providers advertise transfer rates in bits per second, leading to confusion when converting to bytes.
- IEEE 1541 introduced new prefixes for binary scenarios to address confusion caused by multiple meanings of prefixes.
- New prefixes (kibi-, mebi-, etc.) correspond to base 2 values and are intended for binary scenarios.
- These new prefixes haven't been widely adopted yet.
- Manufacturers advertise storage device capacities using base 10, while software calculates size using base 2.
- Lack of standard adoption of new prefixes leads to inconsistencies in file size representation.

![](/images/01-05-01.png)

![](/images/01-05-02.png)

![](/images/01-05-03.png)

## 01.06 - Hexadecimal

- Hexadecimal is a base-16 number system used in computing.
- Each place in hexadecimal represents a power of 16, with symbols ranging from 0 to F.
- A through F represent decimal values 10 to 15 respectively.
- The prefix "0x" is often used to indicate hexadecimal.
- Hexadecimal simplifies binary conversions due to its clear representation.
- Converting between binary and hexadecimal is more straightforward compared to binary and decimal.
- Hexadecimal can represent groups of four bits, making it convenient for byte-level representation.
- Engineers often use hexadecimal and binary together, resorting to decimal only when necessary.

### Exercise

#### Exercise 1-4: Binary to Hexadecimal

10 (binary) = 2 (hexadecimal)

8+4+2+1 = 15 = F or 1111 = F
0+0+0+0 = 0 = 0 or 0000 = 0
11110000 (binary) = F0 (hexadecimal)

![](/images/01-06-01.png)

![](/images/01-06-02.png)

![](/images/01-06-03.png)

![](/images/01-06-04.png)

## 01.07 - Summary

- Introduction to computing fundamentals
- Definition of a computer as an electronic device programmed for logical instructions
- Distinction between digital and analog systems: digital systems use 0s and 1s, while analog systems use varying values
- Explanation of binary system: data represented as sequences of 0s and 1s
- Introduction to bits and bytes
- Overview of standard SI prefixes (giga-, mega-, kilo-, etc.) for describing data size
- Utilization of hexadecimal system for binary work
