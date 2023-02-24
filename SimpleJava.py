import re

class SimpleJava:
    def __init__(self, filename):
        with open(f"{filename}.java", "a") as PublicStaticAndShit:
            # PublicStaticAndShit.write("""public class Main {\n\tpublic static void main(String[] args) {\n""")
            PublicStaticAndShit.write("public class " + filename + "{\n\tpublic static void main(String[] args) {\n")
    def Interpreter(self, filename):
        with open(f'{filename}.sjava', 'r') as f:
            for line in f:
                print(line)
                line = line.strip()
                if(line.startswith("pf") and line.endswith(");") or line.startswith("pf(\"") and line.endswith(");")):
                    line = line.replace("pf(", "System.out.printf(")
                elif(line.startswith("p") and line.endswith(");") or line.startswith("p(\"") and line.endswith(");")):
                    line = line.replace("p(", "System.out.println(")
                # elif(line.startswith("i ") and line.endswith(";")):
                elif not re.match(r'^[A-Za-z0-9]+$', line.split()[1]) and (line.split()[1][0]).isalpha():
                    # do something if the second word contains only alphabetic characters and/or numbers
                    print("Error the variable must start with letters and cannot start with numbers or have spaces")
                    line = line.replace("i ", "int ")
                elif(line.startswith("s ") and line.endswith(";")):
                    line = line.replace("s ", "String ")
                elif(line.startswith("f ") and line.endswith("f;")):
                    line = line.replace("f ", "float ")
                elif(line.startswith("d ") and line.endswith(";")):
                    line = line.replace("d ", "double ")
                elif(line.startswith("b ") and line.endswith("true;") or line.startswith("b ") and line.endswith("false;")):
                    line = line.replace("b ", "boolean ")
                elif(line.startswith("wh (") and line.endswith("{") or line.startswith("wh(") and line.endswith("{")):
                    line = line.replace("wh", "while (")
                elif(line.startswith("class (") and line.endswith("{") or line.startswith("class(") and line.endswith("{")):
                    line = line.replace("class", "public class ")
                with open(f"{filename}.java", "a") as out_file:
                    out_file.write(f"\t{line}\n")
            with open(f"{filename}.java", "a") as TheEndBrackets:
                TheEndBrackets.write("""\t}\n}""")

WhatColorIsYourBugatti = SimpleJava("Main")

WhatColorIsYourBugatti.Interpreter("Main")
