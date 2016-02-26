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

1) mkdir -p dir 1/dir 2: Make nested directory (2 in 1). Use -p option to create multiple (nested) directories in one command!

2) cd .. : Move UP a directory. Use ../.. to move up multiple directories

3) ls path: Prints contents of directory at path within working directory (ls alone prints WD contents).

4) rmdir dir: Delete directory. DIR MUST BE EMPTY!

5) rm -rf dir: Delete directory and all contents. Directory does not have to be empty.

6) mv file path: This is command is terribly named. It does not move the file, it merely renames it.

7) pushd dir: Go down to dir, but "back burner" current location for later

8) popd: Return to "back burnered" directory

9) cp -r dir 1 dir 2: Copy dir 1 to dir 2 within same working directory ("r"="robocopy")

10) code 1 | command: Performs command on output produced by code 1 (e.g. "Pipes" output to command).

11) find . - name "key" -print: Find and print all files with "key" in the file name within working directory

12) grep keyword file: Search for keyword within a specific file.

13) export var = value: Set environmental variable as value.

14: unset var : remove environmental variable.


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  - List contents (files and directories) within the working directory.

`ls -a`  - List contents within working directory, including dot files.

`ls -l`  - List contents of WD in "long format" (i.e. including file mode, number of links, owner name, group name, file size (in bytes), date-time file was last modified, and path name.

`ls -lh`  - Same output as ls -l, except file size is displayed in kilobites, megabytes, etc. (with units indicated) if files are large enough in order to reduce the number of digits needed to capture file size.

`ls -lah`  - Same output as ls -lh, except that dot files are included.

`ls -t`  - List contents of working directory, sorted by last modified datetime (most recent first).

`ls -Glp`  - Same output as ls -l, except output is colorized (i.e. directories are colored differently from files) and all directories contain a "/" after their names.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

1) -m: Display files as comma-delimited list (potentially useful for creating CSV datafiles.

2) -R: Diplay subdirectories and subdirectory contents in addition to WD contents. Helpful for looking at overall file structure.

3) -g: Display contents in long format with username (i.e. all me) remove. I love to reduce clutter.

4) -1: Display contents as a list. I like this better than columnar format.

5) -u: Sort by file access date, rather than file last modification date.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

The xargs command reads in a list of arguments from standard input and breaks the arguement list into one or more sublists. Xargs is useful for perfomring commands on long lists of arguments. Many Unix systems won't accept long lists of standard input, so xargs is necessary to break up the output into "bitesized chunks" the command line interface can work with. 

For example, I could use xargs to find and delete all text documents in my working directory with the command:

find . -name ".txt" | xargs rm -rf

Without the xargs command, the above code may not execute if the list of text files in my working directory (e.g. the output produced by the find command, piped to rm) is sufficiently long.
 

