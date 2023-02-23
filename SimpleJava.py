with open('Main.sjava', 'r') as f:
    with open("Main.java", "a") as PublicStaticAndShit:
        PublicStaticAndShit.write("""public class Main {\n\tpublic static void main(String[] args) {\n""")
    for line in f:
        print(line)
        line = line.strip()
        if(line.startswith("pf") and line.endswith(");") or line.startswith("pf(\"") and line.endswith(");")):
            line = line.replace("pf(", "System.out.printf(")
        elif(line.startswith("p") and line.endswith(");") or line.startswith("p(\"") and line.endswith(");")):
            line = line.replace("p(", "System.out.println(")
        elif(line.startswith("i ") and line.endswith(";")):
            line = line.replace("i ", "int ")
        elif(line.startswith("s ") and line.endswith(";")):
            line = line.replace("s ", "String ")
        elif(line.startswith("f ") and line.endswith("f;")):
            line = line.replace("f ", "float ")
        elif(line.startswith("d ") and line.endswith(";")):
            line = line.replace("d ", "double ")
        elif(line.startswith("b ") and line.endswith("true;") or line.startswith("b ") and line.endswith("false;")):
            line = line.replace("b ", "boolean ")
        with open("Main.java", "a") as out_file:
            out_file.write(f"\t{line}\n")
    with open("Main.java", "a") as TheEndBrackets:
        TheEndBrackets.write("""\t}\n}""")
