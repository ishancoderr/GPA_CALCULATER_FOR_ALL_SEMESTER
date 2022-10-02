import sys
class subject_credit_assign:
    def __init__(self, number_of_semester):
        self.number_of_semester = number_of_semester

    def subject_range(self, number_of_semester):
        sem_GPA = []
        sem_credit = []
        for r in range(number_of_semester):

            number_of_subject = int(input("Enter the number of subjects in this semester:"))
            if (number_of_subject < 0):
                print("++++++++++++++++++please enter value more than 0+++++++++++++++++++++++")
                sys.exit()
            sub_marks = []
            credit = []
            full = 0
            sum = 0
            for i in range(number_of_subject):
                sub = int(input("Enter the"+" "+ str(i+1) +" " +"subject marks :"))
                if(sub<0 ):
                    print("++++++++++++++++++please enter value more than 0  +++++++++++++++++++++++")
                    sys.exit()
                cred = int(input("Enter the"+" "+ str(i+1) +" " +"subject credit:"))
                if (cred < 0):
                    print("++++++++++++++++++please enter value more than 0   +++++++++++++++++++++++")
                    sys.exit()

                sub_marks.append(sub)
                credit.append(cred)

            print(sub_marks)

            grade_point = []
            grade_alp = []
            for M in sub_marks:
                if (100<=M >= 90):
                    grade_point.append(4.0)
                    grade_alp.append("A+")
                elif (80 <= M < 90):
                    grade_point.append(4.0)
                    grade_alp.append("A")
                elif (75 <= M < 80):
                    grade_point.append(3.7)
                    grade_alp.append("A-")
                elif (70 <= M < 75):
                    grade_point.append(3.3)
                    grade_alp.append("B+")
                elif (65 <= M < 70):
                    grade_point.append(3.0)
                    grade_alp.append("B")
                elif (60 <= M < 65):
                    grade_point.append(2.7)
                    grade_alp.append("B-")
                elif (55 <= M < 60):
                    grade_point.append(2.3)
                    grade_alp.append("C+")
                elif (50 <= M < 55):
                    grade_point.append(2.0)
                    grade_alp.append("C")
                elif (45 <= M < 50):
                    grade_point.append(1.7)
                    grade_alp.append("C-")
                elif (40 <= M < 45):
                    grade_point.append(1.3)
                    grade_alp.append("D+")
                elif (30 <= M < 40):
                    grade_point.append(1.0)
                    grade_alp.append("D")
                elif (M < 30):
                    grade_point.append(0.0)
                    grade_alp.append("E")
                else:
                    print("marks are not in requred range")
                    sys.exit()

            for i in credit:
                sum = sum + i

            print(sum)

            for j in range(len(credit)):
                full = credit[j] * grade_point[j] + full

            avg = (full) / sum

            print("Semester GPA     :"+str(avg))
            print("Semester Grades  :"+str(grade_alp))

            sem_GPA.append(avg)
            sem_credit.append(sum)
        sum_c = 0
        full_m = 0
        for i in sem_credit:
            sum_c = sum_c + i

        #print(sum_c)

        for f in range(len(sem_GPA)):
            full_m = sem_credit[f] * sem_GPA[f] + full_m

        cgpa = (full_m) / (sum_c)

        return(cgpa)

if __name__ == '__main__':
    number_of_semester = int(input("Enter the number of  semester To calculate CGPA:"))
    if (number_of_semester < 0):
        print("++++++++++++++++++please enter value more than 0+++++++++++++++++++++++")
        sys.exit()
    c=subject_credit_assign(number_of_semester)
    print("Your all semester CGPA is :"+str(c.subject_range(number_of_semester)))


