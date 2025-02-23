**#Securinets ISI Qualifications 2025**

Challenge name : Burried Treasure 
Description : A long-lost treasure is hidden somewhere on this mysterious map, but no one has been able to uncover its exact location. The coordinates are there, buried deep within the data—
Only the smartest treasure hunters will succeed. Will you be one of them? 🌍🔎

You were provided with an executable file to solve locally then solve the challenge remotely.

First thing we can do is run our program , and as we can see it's asking for an input so we try to see if it's vulnrable to Buffer Overflow by sending bunch of A's.
: ![image](https://github.com/user-attachments/assets/d7583050-4033-497f-86d4-874b3b811b31)
As you can see this input isn't vulnrable to BoF so we try to check our binary using Ghidra or Cutter . 
![image](https://github.com/user-attachments/assets/cd4d723b-6fdd-4cef-9789-624f1c60cce1)
We found a function called find_treasure so after seeing its content what we can see : 
      - our input function is called correctly with fgets and limited number of bytes
      yet we can see that : printf function doesnt have any parameters to it , so we can abuse a **Format String Vunlarability** 

But first what is Format String Vulnrability : it's a mis-use of the print function whenever it's called without any format specifiers. 
Normally when we call printf function we choose one format specifier for it :
![image](https://github.com/user-attachments/assets/5a829ca8-bfaf-4565-a9fd-6908a2df0688)
For a string it would be like this :
![image](https://github.com/user-attachments/assets/4b2c3747-0810-44b0-a811-670a112b8905)

But what will happen if we dont call any format specifier in our printf? 
The printf function start to read values from the stack FROM the TOP to the Bottom because that's the way our memory writes .

![image](https://github.com/user-attachments/assets/ab7d0b21-c211-45e1-8e19-f8c1c84e5a06)

**Are you saying that we can continue leaking stuff until we get to the x and y variables? But how much do i have to leak ? and how can i leak them? 
**
Exactly that's what we're about to do , since x and y are integers so the printf format specifier we we'll be using is %ld : that stands for a long integer. 
Let's see what does this give us : 

![image](https://github.com/user-attachments/assets/ada66b3f-0d1f-4b33-bba7-305e80951fa2)

And here we are we got the leaks and surely since our input is limited so is our numbers of values leaked : 
![image](https://github.com/user-attachments/assets/91d73ee6-e43e-499e-a364-27837cf76767)

for example the numbers we're seeing are integers saved in our stack going From TOP to Bottom.
**But unfortunatly we cant seem to find any number between 2003 and 2999 in these leaked numbers ,so how can i go deeper than just the 8 values printed?
**
That's why we will be using this format **%x$ld** where x is the number of offset we want to be looking at. (Offset is the distance between a certain variable and the top of our stack called also RSP:Stack Pointer .
So for example if we want to see the variable at Offset number 9 from the top of our stack we'll just use : **%9$ld**

so we prepare our second payload :  %9$ld %10$ld  %11$ld %12$ld %13$ld  %14$ld %15$ld and we send it :
![image](https://github.com/user-attachments/assets/838e9d0c-4ca0-41c4-827e-483832710ba8)

Ohh!! it looks like we found something intresting :** 2675173794341204017 3541272297679892785  13833094912812082 2050 2036 1**
As we can see we got two numbers that satisfy the conditions of x and y. 

the normal thing to do now is submit x = 2050 and y = 2036 ! yet not so fast because that's not the correct answer.
Remember how i told you that our leaking goes from top to the bottom so the first number we're seeing is for the y variable since it has been called last , and x variable is the second one . So if we submit x = 2036 and y = 2050 

![image](https://github.com/user-attachments/assets/4fbbe121-3838-4225-81ff-02d72b715ff3)

And Good Job you got your flag ! ;) 

Valuable Ressources for format string Vulnrability : 
https://cs155.stanford.edu/papers/formatstring-1.2.pdf
https://www.youtube.com/watch?v=0-ulL3Y0MS8 (Bear with his russian accent he's really good)





