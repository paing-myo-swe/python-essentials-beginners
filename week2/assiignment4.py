# Pass or Fail Exam

englishMarks = int(input("Enter marks of English subject "))
mathMarks = int(input("Enter marks of Math subject "))
scienceMarks = int(input("Enter marks of Science subject "))
computerMarks = int(input("Enter marks of Computer subject "))

averageMarks = (englishMarks + mathMarks + scienceMarks + computerMarks) / 4

if(averageMarks > 40):
    print("Conguratulation! You passed exam")
else:
    print("Sorry! You failed exam")
