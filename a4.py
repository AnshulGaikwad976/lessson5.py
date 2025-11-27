file_read = open('codingal.txt', 'r')
print("file in read mode-")
file_read.close()

file_write = open('codingal.txt' ,'w')
file_write.write("hi iam a pngu")
file_write.close()

file_append = open('codingal.txt', 'a')
file_append.write("\n file in append mode")
file_append.write("i am a pingu and i am 2years old")
file_append.close()