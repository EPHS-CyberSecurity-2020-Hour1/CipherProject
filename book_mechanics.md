###### Mechanics
## * How does the cipher work?
   * main strength of a book cipher is the key
   * sender and receiver of encoded messages can agree to use any book or other publication available to both of them as the key to their cipher
   * drawback to a book cipher is that both parties have to possess an identical copy of the key
## * Demo of encryption and decryption
   * Key Index: Use this index to specify a starting point in the key file for encoding. The final ciphertext will not include any index references that occur before this point in the file. This gets around the problem of using a key file that may have similar opening text to many other files, such as an HTML heading, email signature or publisher title page
   * Encrypt Spaces: Give the whitespace in the original message corresponding index references in the ciphertext. Uncheckingthisoptionwillmakethedecodedtextlooklikethis, and will also cut down on the size of the ciphertext.
   * Ignore Case: Check this option to match characters regardless of case. Use this to preserve the text when the message includes rarely used capitals that might not be found in the key file. Some letter use frequency information might be useful.
   * Example implementation
    1. Here we encode some of Polonius’s advice using a small key file just a few lines. We start by defining the key index as 3:13, meaning the first character we could possibly encode is the thirteenth character of the third line. Note that lines are defined by their paragraph break rather than their displayed word wrap, and that all characters in the line receive an index, including the quotation marks and spaces.
                  ![picture of Polonius's advice](https://sites.google.com/site/brutenorhuman/_/rsrc/1472689476287/book-cipher/Example1.png)   
    2. Next we need to search the key text for the letters in the message. Here’s a visualization of the search process for just the first word. Notice that the algorithm encodes the two lowercase e characters as two separate indexes:
                  ![picture 2 of Polonius's advice](https://sites.google.com/site/brutenorhuman/_/rsrc/1472689480337/book-cipher/Example2.png)   
    3. Each character is encoded according to its line number and character index as a colon-separated tuple. For instance, the Capital N character is found in the fourth line as the second character, and will be encoded as 4:2. Each tuple is demarcated by a single space. Following this procedure the entire first word becomes 4:2 3:15 3:18 3:13 3:14 3:22 3:30.
                  ![picture 3 of Polonius's advice](https://sites.google.com/site/brutenorhuman/_/rsrc/1472689476559/book-cipher/Example3.png) 
    4. Here are the selected indices for the messages remaining characters. Notice that for messages containing common language the cipher is able make matches largely within a single line, only occasionally searching farther for less common letters. For such a short message the second half of the key is hardly required. A single character, the semicolon at the tail of the message, was not found in the key file. Characters not in the key will be given random line assignments with character indexes outside the range of that line. They will decode as the pound sign (#).
                  ![picture 4 of Polonius's advice](https://sites.google.com/site/brutenorhuman/_/rsrc/1472689476800/book-cipher/Example4.png)
    5. The final encoded message is: 4:2 3:15 3:18 3:13 3:14 3:22 3:30 3:17 3:25 3:20 3:102 3:39 3:30 3:31 3:50 3:21 3:76 3:81 3:70 3:23 3:16 3:65 5:22 3:27 3:29 3:34 3:88 3:77 3:26 3:38 3:85 5:62 3:37 3:143 3:89 4:10
    6. Which would decode with the loss of one character as: Neither a borrower, nor a lender be#
