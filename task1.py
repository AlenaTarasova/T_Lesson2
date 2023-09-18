import subprocess
import string


def check_out(cmd, text, split_mode=False):

    output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    if split_mode:
    
        s = output.stdout
        for c in string.punctuation:
            s = s.replace(c, "")

        list_out = s.split()

        if text in list_out and output.returncode == 0:
            return True
        else:
            return False
    else:
      
        if text in output.stdout and output.returncode == 0:
            return True
        else:
            return False

print(check_out('uname -a', 'Linux', split_mode=True))