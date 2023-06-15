##a script that creates an alias ==> alias ls="rm *"
##a script that prints hello user, where user is the current Linux user ==> echo "hello $USER"
##Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program ==> export PATH=$PATH:/action
## a script that counts the number of directories in the PATH ==> echo $((`echo $PATH | grep -o ":/" | wc -l`+ 1))
## a script that lists environment variables ==> printenv
## a script that lists all local variables and environment variables, and functions ==> set
##  a script that creates a new local variable. ==>BEST="School"
##a script that creates a new global variable ==> export BEST=School
##  a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line ==>echo $(($TRUEKNOWLEDGE + 128))
## a script that prints the result of POWER divided by DIVIDE, followed by a new line ==> echo $(($POWER / $DIVIDE))
##  a script that displays the result of BREATH to the power LOVE==> echo $((BREATH**$LOVE))
##a script that converts a number from base 2 to base 10 ==> echo "$((2#$BINARY))"
##a script that prints all possible combinations of two letters, except oo ==> echo {a..z}{a..z} | tr " " "\n" | grep -v "oo"
##a script that prints a number with two decimal places, followed by a new line ==> printf "%.2f" $NUM | sort
##a script that converts a number from base 10 to base 16 ==> printf '%x\n' $DECIMAL
##a script that encodes and decodes text using the rot13 encryption. Assume ASCII ==>tr 'A-Za-z' 'N-ZA-Mn-za-m'
## a script that prints every other line from the input, starting with the first line ==> perl -lne 'print if $. % 2 ==1'
##a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result ==> echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'bestchol')
 
