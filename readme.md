# Hangman game

#### Libraries used:

* random ( built-in )

#### How does it work

* There are a hundred random words in words.txt file
* I extracted those words and assigned random word from that list of words to the word variable
* In the while loop I draw blank spots ( _ ) for the letters in the word which are not guessed right just yet
* Then, I display the number of guesses left to the user and ask for input
* I append that guess to the guesses list
* If guess isn't right I take one from the number of guesses and check if there are no more guesses available. If there are no more, I simply break out of the loop ( without using won variable )
* If users guess is right I check if all the letters from our word are in the guesses list ( if all the letters are guessed )
* If that is false I set the won variable to False and continue the loop
* Else, won variable stays True and the loop breaks

#### What I have learned:

* First of all thanks to "Neural Line" guy on YouTube for the inspiration to do this project and for helping me finish it.
* In this project I mostly worked with strings so I got reminded of those things
* Other than that, there weren't actually many new things I've learned doing this project but this is definitely the project I've been wanting to make for some time.