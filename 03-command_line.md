# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

mkdir -p <dir 1>/<dir 2> :  Make nested directory (2 in 1). Use -p option to create multiple (nested) directories in one command!
cd <dir 1> :                Move down into directory 1. Can use dir 1/dir 1 to move down multiple directories.
cd .. :                     Move UP a directory. Use ../.. to move up multiple directories
ls <path> :                 Prints contents of directory at <path> within working directory. (ls alone prints WD contents).
rmdir <dir> :               Delete directory. MUST BE EMPTY!
rm -rf <dir> :              Delete directory and all contents. Directory does not have to be empty :)
mv <file path>  :           This is command is terribly named. It does not move the file, it merely renames it.
pushd <dir>:                Go down to <dir>, but "back burner" current location for later
popd:                       Return to "back burnered" directory
cp -r <dir 1> <dir 2>:      Copy <dir 1> to <dir 2> within same working directory ("r"="robocopy")
<code 1> | <command>:       Performs command on output produced by code 1 (e.g. "Pipes" output to command).
grep <keyword> | <file>:    Search for keyword within a specific file.

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

