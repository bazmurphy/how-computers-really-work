# Chapter 02 - Binary In Action

## 02.01 - Representing Data Digitally

- Data in computers is stored as bits, including not only numbers but also various forms of data like text, images, audio, etc.

### 02.01.01 - Digital Text

- Text can be represented in binary using a character set, typically including alphanumeric symbols and punctuation marks.
- For English text, around 100 characters need representation, including uppercase and lowercase letters, punctuation marks, spaces, and digits.
- Using 8 bits (1 byte) per character allows for the representation of 256 unique characters, which is sufficient for most text encoding needs.
- While there are standard ways of representing text in binary (like ASCII or Unicode), custom encoding schemes can also be devised as long as the software understands them.
- Encoding involves translating data into a digital format, while decoding involves interpreting that digital data.

### 02.01.02 - ASCII

- ASCII (American Standard Code for Information Interchange) is a standard format for representing text digitally.
- It represents 128 characters using 7 bits per character, commonly stored using a full byte (8 bits).
- ASCII handles characters needed for English, while Unicode handles characters for various languages.
- ASCII includes control codes for device control, such as carriage return and form feed.
- Text representation in ASCII involves mapping each character to a unique sequence of bits.
- Computing devices interpret these bit sequences to display the corresponding symbols to users.

#### Exercise 2-2: Encode and Decode ASCII

Hello = 48 65 6C 6C 6F = 01001000 01100101 01101100 01101100 01101111
5 cats = 35 20 63 61 74 73 = 00110101 00100000 01100011 01100001 01110100 01110011

01000011 01101111 01100110 01100110 01100101 01100101 = 43 6F 66 66 65 65 = Coffee
01010011 01101000 01101111 01110000 = 53 68 6F 70 = Shop

43 6C 61 72 69 6E 65 74 = Clarinet

![](/images/02-01-01.png)

### 02.01.03 Digital Colors and Images

- Introduction to digital representation of colors and images
- Comparison to representing text and numbers in binary
- Exploration of grayscale as a limited color range
- Decision to represent grayscale with black, white, dark gray, and light gray
- Determining the number of bits needed to represent four grayscale colors (2 bits)
- Explanation of how an image is arranged in a grid of pixels
- Example of a simple grayscale image with 4x4 pixel dimensions
- Note on modern displays being composed of grids of pixels, with examples of resolutions

![](/images/02-01-02.png)

### 02.01.04 Approaches for Representing Colors and Images

- Grayscale images commonly use 8 bits per pixel, allowing for 256 shades of gray, ranging from 0 (black) to 255 (white).
- RGB (Red, Green, Blue) is a method used for representing colors beyond shades of gray, with each color component represented by 8 bits, totaling 24 bits for the overall color.
- RGB is based on an additive color model, where colors are composed of varying intensities of red, green, and blue light.
- In RGB representation, each component color can range from 0 (dark) to 255 (bright), allowing for a wide range of color variations.
- Bitmap images store RGB color data for each pixel individually, while formats like JPEG and PNG use compression techniques to reduce storage space.

![](/images/02-01-03.png)

![](/images/02-01-04.png)

### 02.01.05 - Interpreting Binary Data

- Binary value: 011000010110001001100011
- Potential interpretations: ASCII text string "abc", 24-bit RGB color, positive integer (6,382,179)
- Interpretation depends on context
- Different programs interpret data differently
- Binary data can represent numbers, text, colors, and images
- Other types of data like video or audio can also be stored digitally
- Digital representation may not be a perfect replica but is still useful
- Binary data allows for adaptability through software to handle various data types

![](/images/02-01-05.png)

## 02.02 - Binary Logic

- Computers process data using binary logic
- Binary logic represents logical statements with true (1) or false (0)
- Logical operators like AND and OR are fundamental in binary logic
- AND requires all conditions to be true for the result to be true
- OR requires at least one condition to be true for the result to be true
- Truth tables illustrate all possible combinations of inputs and outputs for logical statements
- Logical operators include NOT, NAND, NOR, and XOR
- Boolean algebra, described by George Boole in the 1800s, forms the foundation of digital electronics

![](/images/02-02-01.png)

![](/images/02-02-02.png)

![](/images/02-02-03.png)

![](/images/02-02-04.png)

![](/images/02-02-05.png)

![](/images/02-02-06.png)

![](/images/02-02-07.png)

![](/images/02-02-08.png)

![](/images/02-02-09.png)

- NOT (OPPOSITE) - if input is true, the result is false

- NAND (NOT AND) - if both inputs are true, the result is false

- NOR (NOT OR) - if both inputs are false, the result is true

- XOR (EXCLUSIVE OR) - only a single input can be true, for result to be true

![](/images/02-02-10.png)

![](/images/02-02-11.png)

![](/images/02-02-12.png)

![](/images/02-02-13.png)

## Exercise

The table shows three inputs for a logical expression.
Complete the truth table output for the expression (A OR B) AND C

| A   | B   | C   | Output |
| --- | --- | --- | ------ |
| 0   | 0   | 0   | 0      |
| 0   | 0   | 1   | 0      |
| 0   | 1   | 0   | 0      |
| 0   | 1   | 1   | 1      |
| 1   | 0   | 0   | 0      |
| 1   | 0   | 1   | 1      |
| 1   | 1   | 0   | 0      |
| 1   | 1   | 1   | 1      |

## 02.03 - Summary

- Binary representation: Explained its use for data and logical states
- Versatility of 0s and 1s: Demonstrated their application in representing various types of data including text, colors, and images
- Logical operators: Introduced concepts like AND and OR, and their relevance in expressing logical statements
- Importance of understanding logic: Crucial for comprehending the functioning of modern computer processors
- Future chapters: Binary's significance will be revisited in the context of digital circuits in Chapter 4
- Preparation for upcoming topics: Chapter 3 will delve into fundamentals of electrical circuits to pave the way for understanding digital circuits
- Topics to be covered: Electricity laws, workings of electrical circuits, basic components, and practical circuit building opportunities
