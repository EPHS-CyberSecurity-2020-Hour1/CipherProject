###### Mechanics
By: Sarah Sumrall and Sudeeksha Nooka
## How does the cipher work?
   * main strength of a book cipher is the key
   * sender and receiver of encoded messages can agree to use any book or other publication available to both of them as the key to their cipher
   * drawback to a book cipher is that both parties have to possess an identical copy of the key
## Demo of encryption and decryption
   * Key Index: Use a specific text (book) to specify the starting point of your key for encoding. After you choose the spot in the text, it is important to remember that the final ciphertext will not include any index references that are before this point. 
   * Encrypt Spaces: Give the whitespace in the original message corresponding index references in the ciphertext; this will also cut down on the size of the ciphertext.
   * Ignore Case: Make sure that case doesn't matter, so the key will match characters regardless of case. This will preserve the text when the message includes capitals, since they might not be found in the key. 
   
   * Example Implementation:
   
   1. Here we will use a few lines of Polonius’s advice as our key. Let's start by defining the key index as 3:13, meaning the first character we could possibly encode is the thirteenth character of the third line. 
   
   ![picture 1 of Polonius's advice](https://sites.google.com/site/brutenorhuman/_/rsrc/1472689476287/book-cipher/Example1.png)                                      
   2. Next we need to search our key for the letters that correspond to the letters in the message. Here’s a visualization of the search process for just the first word. 
   
   ![picture 2 of Polonius's advice](https://sites.google.com/site/brutenorhuman/_/rsrc/1472689480337/book-cipher/Example2.png)                                       
   3. Each character is encoded according to its line number and character (line number:character). For instance, the Capital N character is found in the fourth line as the second character, and will be encoded as 4:2. Following this procedure the entire first word becomes 4:2 3:15 3:18 3:13 3:14 3:22 3:30.                                
   ![picture 3 of Polonius's advice](https://sites.google.com/site/brutenorhuman/_/rsrc/1472689476559/book-cipher/Example3.png)                                      
   4. Here are the selected indices for the messages remaining characters. The coded message will appear in all numbers. If the character is not given in the key, when decoded it will output pound sign (#). 
   
   ![picture 4 of Polonius's advice](https://sites.google.com/site/brutenorhuman/_/rsrc/1472689476800/book-cipher/Example4.png)
   
   5. The final encoded message is: 4:2 3:15 3:18 3:13 3:14 3:22 3:30 3:17 3:25 3:20 3:102 3:39 3:30 3:31 3:50 3:21 3:76 3:81 3:70 3:23 3:16 3:65 5:22 3:27 3:29 3:34 3:88 3:77 3:26 3:38 3:85 5:62 3:37 3:143 3:89 4:10
   
   6. Which would decode with the loss of one character as: Neither a borrower, nor a lender be#

## Reference: 
https://sites.google.com/site/brutenorhuman/book-cipher 

### [Next Page: Math Analysis](https://github.com/EPHS-CyberSecurity-2020-Hour1/CipherProject/blob/BookCipher/book_mathanalysis.md)
