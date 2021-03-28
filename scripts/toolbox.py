from sys import argv, stdout, stderr, exit

def print(stream, content):
    stream.write(str(content))

def println(stream, content):
    print(stream, f'{content}\n')

def slurp_file(filepath):
    content = ""
    with open(filepath) as f:
        content = f.read()
    return content

def panic(msg):
    println(stderr, msg)
    exit(-1)