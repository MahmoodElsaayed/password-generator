# password-generator

The program is a simple password generator that generates a password based on user input for password length and complexity level. The generated password can then be copied to the clipboard or the user can choose to try again and generate a new password.

The program starts by importing necessary modules such as the 'random' module for choosing random characters, 'string' module for getting different character sets (ascii_letters, digits, punctuation), and 'clipboard' module for copying the generated password to the clipboard.

The 'main' function is defined first, which is the starting point of the program. It calls the 'generate_password' function to generate a password and assigns it to the 'password' variable. The 'copy_or_retry' function is then called to ask the user if they want to copy the password to the clipboard or try again.

The 'generate_password' function is defined next, which takes user input for password length and complexity level. It then generates a password of the specified length by choosing random characters from the character set determined by the complexity level.

The 'password_length_picker' function prompts the user to enter the password length and ensures that the input is a valid integer and is greater than or equal to 8.

The 'complexity_picker' function prompts the user to select the complexity level for the password and ensures that the input is a valid integer and is either 1, 2, or 3. It then calls the 'characters_picker' function to return the appropriate character set based on the complexity level.

The 'characters_picker' function takes the complexity level as input and returns the appropriate character set based on the level. Level 1 returns only lowercase and uppercase letters, level 2 returns letters and digits, and level 3 returns letters, digits, and punctuation.

The 'copy_or_retry' function is defined to ask the user if they want to copy the generated password to the clipboard or try again. It displays the password to the user and takes their input. If the user chooses 'y', the password is copied to the clipboard and the program terminates. If the user chooses 'n', the 'main' function is called again to generate a new password. If the input is invalid, the function displays an error message and prompts the user again.

Finally, the 'if name == "main"' block is used to ensure that the 'main' function is only called when the program is run directly and not when it is imported as a module.
