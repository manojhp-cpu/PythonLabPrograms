class failedExamMarks(Exception):
    pass


try:
    Exam_marks = int(input('Enter the marks: '))
    if Exam_marks < 39:
        raise failedExamMarks
    else:
        print('You are passed Exam')

except failedExamMarks:
    print('Exception occurred:you are failed in exam')


