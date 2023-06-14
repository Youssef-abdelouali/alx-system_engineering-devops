#Script 0 : print "hello, world"
#Script 1 : display "(Ôo)' we use \
#Script 2 : Display the content of the /etc/passwd file use the commnad cat
#Script 3 : Display the content of /etc/passwd and /etc/hosts using the command cat 
#Script 4 : Display the last 10 lines of /etc/passwd using the command ' tail -n 10  /etc/passwd '
#Script 5 : Display the first 10 lines of /etc/passwd using the command ' head -n 10 /etc/passwd ' 
#Script 6 : displays the third line of the file iacta using the command ' cat iacta | head -n 3 | tail -n 1
#Script 7 : creates a file named exactly " \*\\\'\"Best School"\'\\\*$\?\*\*\*\*\*:)" 
#Script 8 : writes into the file ls_cwd_content the result of the command ls -la using the command ls -la > ls_cwd_content
#Script 9 : script that duplicates the last line of the file iacta using the script " tail -n 1 >>  iacta "
#Script 10 : script that deletes all the regular files (not the directories) with a .js extension use find . -name "*.js" type f  -delete
#Script 11 : script that counts the number of directories and sub-directories in the current directory use find . -mindepth 1 -type d | wc -
#Script 12 :  a script that displays the 10 newest files in the current directory use ls -t | head -n 10
#Script 13 : a script that takes a list of words as input and prints only words that appear exactly once use sort | uniq -u
#Script 14 : Display lines containing the pattern “root” from the file /etc/passwd use ==> grep root /etc/passwd
#Script 15 : Display the number of lines that contain the pattern “bin” in the file /etc/passwd use ==> grep bin /etc/passwd | wc -l
#Script 16 : Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd. use ==> grep -A 3 "root" /etc/passwd
#Script 17 : Display all the lines in the file /etc/passwd that do not contain the pattern “bin”. use ==> grep -v bin /etc/passwd
#Script 18 :Display all lines of the file /etc/ssh/sshd_config starting with a letter. use ==> grep '[[:upper:]]\|^[[:lower:]]' /etc/ssh/sshd_config or use ==> grep "^[A-Za-z]" /etc/ssh/sshd_config
#Script 19 : Replace all characters A and c from input to Z and e respectively. use ==> tr Ac Ze
#Script 20 : Create a script that removes all letters c and C from input. ==> tr -d cC
#Script 21 : Write a script that reverse its input. ==> rev
#Script 22 : Write a script that displays all users and their home directories, sorted by users. use ==> cut -d ':' -fl,6 /etc/passwd | sort
#Script 23 : Write a command that finds all empty files and directories in the current directory and all sub-directories.use ==> find . -empty -printf '%f\n'
#Script 24 :find . -type f -name '*.gif' -exec basename {} .gif \; | LC_ALL=C sort -f
  
