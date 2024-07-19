#! /usr/bin/bash

# Instructions: Create a script that create an executable script whose name is decided by the user

echo -e "Here is an executable script which the user can choose its name: \n"


# Step 1: Create the executable script after asking user input on name 
read -p "Please enter the name of the script: " script_name

touch ${script_name}.sh

echo "#! /usr/bin/bash" > ${script_name}.sh 

echo 'echo -e "This is an executable script, and here is the evidence." ' >> ${script_name}.sh

# Allow persmission to access the script. On my laptop, this step is NOT necessary. But I am aware other users or computers might need this line:
chmod +x ${script_name}.sh  

# Step 2: Create a Confirmation Message
echo -e "\nThe name of the script is called ${script_name}.sh and it is now ready for you to execute."  