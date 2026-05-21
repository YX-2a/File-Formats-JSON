# Contributing
Contributions of all types are welcome.

# Rules :
Before contributing here are on some ground rules:

0. Each **Unique** Extension has **one unique JSON** Object for ease of parsing.
 
1. The Format Should Be : `{".file_Extension":"file_type"}` with the brackets in separate lines and indented to improve human readability.
 
2. Never **ever** write `File` or `Format` when in `"file_type"` as it is too ambiguous. 
 
3. Capitalize every first letter of each word when writing "file_type" (Pascal Case) *while keeping vendor stylisation*.
 
4. If a file type has **multiple extensions**, you can write them in **separate JSON objects**.
 
5. For OS Specific or Program Specific File Formats, The OS or Program Should Be Specified in the `"file_type"` by adding the name of the OS or OS Family or Program First.
 
6. If a file type has **multiple different uses**, write the most common usage for it. *If* all of or most of its uses are equally popular or heavily context dependent, separate them with a `/`.

7. If a file type has **mutually exclusive** uses or is owned by **different vendors** while having equivalant uses, separate them with a `/`.

8. If there is no *grammatically correct* way to express the intricacies of the format inline, use parentheses `()` to clarify it, Inside the `()` use a `,` *if* the capabilities are related `/` *if* not.

These 9 rules above are fixed and have to be followed carefully in order to preserve the stylistic cohesion of the file.