# -*- coding: utf-8 -*-
# Name: DJ Porter   
# Evergreen Login: porrog09
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

a = 1

b = -5.86

c = 8.5408


xone = ((-b + math.sqrt (b**2 - (4*a*c)) / (2 * a)))
xtwo = ((-b - math.sqrt (b**2 - (4*a*c)) / (2 * a)))

print str (xone)
print str (xtwo)

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test

print str (hw1_test.a)
print str (hw1_test.b)
print str (hw1_test.c)
print str (hw1_test.d)
print str (hw1_test.e)
print str (hw1_test.f)


###
### Problem 3
###

print "Problem 3 solution follows:"

print str ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))

###
### Collaborators
###

# Betsy Kelley
# Travis Malone

### Reflection
#   Challenging because I'm not a strong programmer. The tutorials helped but I Googled some thing for help. I realized that
#   working with modules is much like working with math such as math.pi.