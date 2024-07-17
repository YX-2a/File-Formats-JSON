# File-Formats-JSON
This repo has one json file containing most file formats that i could add.

# Rules :
Before comitting a change here are on some ground rules:

1.The Format Should Be : {"file_Extension" : "file_type"} with the brackets in separate lines to improve human readability.

2.Never ever say "File" when writing "file_type" as it is ambiguous. 

3.Capitalize every first letter of each word when writing "file_type" (Pascal Case).

4.If a file type has multiple extentions, you can write them in seperate JSON objects inside the array.

5.For OS Specific or Progam Specific File Formats, 
The OS or Program Should Be Specified in the "file_type" by adding the name of the OS (or OS Family eg. Unix) or Program First. 

6.If a file type has multiple uses, write the most common usage for it. If all of or most of its uses are equally popular, separate them with a "/".