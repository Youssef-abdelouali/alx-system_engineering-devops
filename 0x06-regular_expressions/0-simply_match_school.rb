#!/usr/bin/env ruby

# Output the matching occurrences of "School" in the input string
# ARGV[0] - first argument from the command line
# scan(/School/) - find occurrences of "School" using regex
# join - concatenate matching occurrences into a single string
puts ARGV[0].scan(/School/).join
