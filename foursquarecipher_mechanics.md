# Mechanics 
The four-square cipher uses four 5 by 5 (5x5) matrices arranged in a square. Each of the 5 by 5 matrices contains the letters of the alphabet.
In general, the upper-left and lower-right matrices are the "plaintext squares" and each contain a standard alphabet. The upper-right and lower-left squares are the "ciphertext squares" and contain a mixed alphabetic sequence.


**Encryption and Decryption**

To encrypt a message is the same as decrypting it execpt doing the proccess in reverse. 
Let's say the word we are trying to encrpyt is Hello World.

1. Split the payload message into digraphs. (HELLO WORLD becomes HE LL OW OR LD)
2. Find the first letter in the digraph in the upper-left plaintext matrix.
3. Find the second letter in the digraph in the lower-right plaintext matrix.
4. The first letter of the encrypted digraph is in the same row as the first plaintext letter and the same column as the second plaintext letter. It is therefore in the upper-right ciphertext matrix.
5. The second letter of the encrypted digraph is in the same row as the second plaintext letter and the same column as the first plaintext letter. It is therefore in the lower-left ciphertext matrix.

![4 square cipher](https://crypto.interactive-maths.com/uploads/1/1/3/4/11345755/2024722_orig.jpg)

Using the four-square example given above, we can encrypt the following plaintext:

Plaintext:  he lp me ob iw an ke no bi
Ciphertext: FY GM KY HO BX MF KK KI MD


**Source**
https://en.wikipedia.org/wiki/Four-square_cipher

[Link to computer code!] (https://github.com/EPHS-CyberSecurity-2020-Hour1/CipherProject/blob/foursquarecipher/foursquarecipher_ComputerCode.md)
