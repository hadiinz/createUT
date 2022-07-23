import os
import shutil
path = "C:\\Users\\Acer\\Desktop\\9730034\\emailProject\\src\\main\\java\\com\\emailProject\\emailProject\\service"
outPath = "C:\\Users\\Acer\\Desktop\\9730034\\emailProject\\src\\test\\java\\com\\emailProject"


# find pubic methods in a file and return the names
def find_public_methods_names(lines, filename):
    methodNames = []
    for l in lines:
        # find public methods
        if l.find("(") != -1:
            ind = l.find("(")
            l = l[0:ind]
            words = l.split()
            if len(words) > 0 and words[0] == "public" and words[1] != "class" :
                methodNames.append(words[len(words)-1])

    return methodNames


def create_new_File(publicMethodNames, filename):
    outFilePath = outPath+"\\"+filename[0].lower()+filename[1:len(filename)]
    if os.path.exists(outFilePath):
        shutil.rmtree(outFilePath)
    os.mkdir(outFilePath)
    packageAddr = outFilePath
    for pmn in publicMethodNames:
        if os.path.exists(pmn+".java"):
            os.remove(pmn+".java")
        if outFilePath.find("com") != -1 :
            ind = outFilePath.find("com")
            packageAddr = outFilePath[ind:len(outFilePath)]
        packageAddr = packageAddr.replace("\\", ".")
        f = open(outFilePath+"\\"+pmn[0].upper()+pmn[1:len(pmn)] +"IT.java", "x")
        f.write("package " + packageAddr + ";\n\n\n")
        f.write("public class " + pmn[0].upper()+pmn[1:len(pmn)] + "IT {}")
        f.close()
    return outFilePath

def createSuiteClass(outFilePath, suiteName):
    packageAddr = outFilePath
    if str(outFilePath).find("com") != -1:
        ind = outFilePath.find("com")
        packageAddr = outFilePath[ind:len(outFilePath)]
    packageAddr = str(packageAddr).replace("\\", ".")
    f = open(str(outFilePath)+ "\\" + str(suiteName) + "ITSuite.java", "x")
    f.write("package " + packageAddr + ";\n\n\n")
    f.write("import org.junit.runner.RunWith;\n"
            "import org.junit.runners.Suite;")
    f.write("@RunWith(Suite.class)\n")
    f.write("@Suite.SuiteClasses({")
    for filename in os.listdir(outFilePath):
        if filename != str(suiteName) + "ITSuite.java":
            f.write(filename.split(".")[0]+".class,")
    f.write("})\n")
    f.write("public class " +str(suiteName) + "ITSuite" + "{}")
    pass

if __name__ == '__main__':
    file_Text_dict = {}
    for filename in os.listdir(path):
       with open(os.path.join(path, filename), 'r') as f:
           lines = f.readlines()
           filename = filename.split(".")[0]
           file_Text_dict[filename] = lines
           publicMethodNames = find_public_methods_names(lines, filename)
           outFilePath = create_new_File(publicMethodNames, filename)
           createSuiteClass(outFilePath, filename)
           print(publicMethodNames)










