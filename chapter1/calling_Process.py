# Notice: "Good Bye!!" is never seen. This process has been replaced by <called_Process>
import os, sys 

program = "python"
print("Process calling")
arguments = ["called_Process.py"]

# main part 
os.execvp(program, (program,)+tuple(arguments))
print("Good Bye!!")
