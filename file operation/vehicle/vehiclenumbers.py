f_read=open("D:\\MY PC\\july_python_works\\file operation\\vehicle\\vehiclenumbers.txt")
f_write=open("D:\\MY PC\\july_python_works\\file operation\\vehicle\\keralavehicle.txt","w")
for line in f_read:
    reg_num=line.rstrip("\n")
    if(reg_num.startswith("kl")):
        f_write.write(reg_num+"\n")
f_read.close()
f_write.close()
