#! /usr/bin/bash 

# Instructions: Create 2 txt file called 1.txt and 2.txt. Inside 1.txt, put the ls -l information inside, ask the user what prefix he wants for 1.txt
# Then, change the name of 1.txt adding to it the prefix choosen by user.

touch 1.txt 2.txt 

ls -lt > 1.txt

read -p "Please enter the prefix you want to give to the file 1.txt: " prefix_input

mv 1.txt "${prefix_input}1.txt"

echo -e "\nThe name of the file 1.txt has changed into ${prefix_input}1.txt"