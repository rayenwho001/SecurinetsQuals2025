This challenge consists of two main vulnerabilities: integer overflow and ret2win (return-to-win). We will explain both concepts and how they are exploited to gain control over the program.

**Understanding Integer Overflow**
Concept:
Integer overflow occurs when an arithmetic operation exceeds the maximum value that a data type can hold. This causes the value to wrap around, leading to unexpected behavior.
Example:
Consider an 8-bit unsigned integer that can hold values from 0 to 255.

![image](https://github.com/user-attachments/assets/b1172171-fc5c-425a-a981-27703db1d399)

Output = 4 , which is completly normal because an int is only an 8-bit unsigned integer that can hold values from 0 to 255. sowhen the value exceeds that it goes back to 0.


**Understanding ret2win**

Concept:
ret2win is a buffer overflow attack where we overwrite the return address of a function to redirect execution to a "win" function 

![image](https://github.com/user-attachments/assets/64dc20ac-570e-4b08-9c1a-2f5b2a073bf4)
So we'll be overflowing our input until we get to that return address. Per default it is set to **exit()** function we wanna change that and make it take us to the **win_function**

So we prepare our paylaod : payload = 32 (Number of bytes reserved for our input) + 8 (necessary always to jump over RBP) + win_address

where win_address is the pointer that will be taking us to the start of the win function : You can get it by just reading binary symbols where every function is carcterised by its own address :

**win_address = p64(binary.symbols['win'])** 

This successfully redirects execution to win(), granting us the flag!

![image](https://github.com/user-attachments/assets/279984e4-48a4-449e-a3ac-e5f281e19acb)
