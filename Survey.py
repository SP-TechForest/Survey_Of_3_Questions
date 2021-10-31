import sys
import time
def main():
    program = animate()
    program.data = "Shivamkumar Patel"
    program.width = 30
    program.animate()


class animate:
    def __init__(self):
        self.data = ""
        self.width = 0

    def animate(self):
        temp = 1
        try:
            while temp == 1:
                for x in range(0, self.width):
                    time.sleep(0.1)
                    msg = "\r{}{}".format(" " * x, self.data)
                    sys.stdout.write(msg)
                    sys.stdout.flush()

                for x in range(self.width, 0, -1):
                    time.sleep(0.1)
                    msg = "\r{}{}".format(" " * x, self.data)
                    sys.stdout.write(msg)
                    sys.stdout.flush()
                temp = 0
        except KeyboardInterrupt:
            print("Exiting")


if __name__ == "__main__":
    main()
class print_edit:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
print("\n")
print(print_edit.UNDERLINE + print_edit.BOLD + "Give your survey based on the criterias\n" + print_edit.END +
          print_edit.RED + "Your Answer should be between 0 to 4 otherwise you have to again fill the survey\n"
                           "Your Answer should be integer" + print_edit.END )
def print_data():
    print("0. Strongly Agree\n"
          "1. Agree\n"
          "2. Neither Agree Nor Disagree\n"
          "3. Disagree\n"
          "4. Strongly Disagree")

def check_answer():
    while True:
        answer = input(" : ")
        if answer.isnumeric() == True:
            answer = int(answer)
            if answer >=0 and answer <= 4:
                return answer
            else:
                print(print_edit.BOLD+ print_edit.RED+"Your input should be in between 0 to 4" + print_edit.END)
                continue
        else:
            print(print_edit.BOLD+ print_edit.RED+"Your input should be integer" + print_edit.END)
            continue

def Collect_Answer(number):
    number = number
    print(print_edit.BLUE + f"Number of survey : {number}" + print_edit.END)
    print_data()
    print(print_edit.BOLD+ print_edit.DARK_CYAN+ "Q1. Rate your experience with Loyalist college's student facilities " + print_edit.END)
    answer1 = check_answer()
    print(print_edit.BOLD +print_edit.DARK_CYAN+ "Q2. How you define your college's Education schema " + print_edit.END)
    answer2 = check_answer()
    print(print_edit.BOLD +print_edit.DARK_CYAN+ "Q3. Canadian government is going to make their institutes offline for students" + print_edit.END)
    answer3 = check_answer()
    return answer1, answer2, answer3

def calculate_data(q_list1, q_list2, q_list3):
    avg1 = round(sum(q_list1)/len(q_list1))
    avg2 = round(sum(q_list2)/len(q_list2))
    avg3 = round(sum(q_list3)/len(q_list3))
    return avg1, avg2, avg3

Temp = "Y"
number_of_survey = 0
question1_ans = []
question2_ans = []
question3_ans = []
q1_dict = {"Rate your experience with Loyalist college's student facilities":[]}
q2_dict = {"How you define your college's Education schema":[]}
q3_dict = {"Canadian government is going to make their institutes offline for students":[]}
while Temp == "Y":

    Temp = input(print_edit.BOLD+ print_edit.UNDERLINE+"Do you want to start survey Y/N :" + print_edit.END)
    Temp = Temp.upper()
    if Temp == "Y":
        number_of_survey =number_of_survey +1
        a1,a2,a3 = Collect_Answer(number_of_survey)
        question1_ans.append(a1)
        question2_ans.append(a2)
        question3_ans.append(a3)
        q1_dict["Rate your experience with Loyalist college's student facilities"].append(a1)
        q2_dict["How you define your college's Education schema"].append(a2)
        q3_dict["Canadian government is going to make their institutes offline for students"].append(a3)
    else:
        avg1, avg2, avg3 = calculate_data(question1_ans,question2_ans,question3_ans)
        print(print_edit.BOLD+print_edit.BLUE+"\nResults of the survey...\n"+ print_edit.END)
        print(f"{print_edit.DARK_CYAN}{print_edit.BOLD}Total number of survey : {number_of_survey}{print_edit.END}")
        print(print_edit.GREEN + f"All the reviews given by the users to each survey questions\n" + print_edit.END+
              f"{print_edit.BOLD}question 1.{print_edit.END} Rate your experience with Loyalist college's student facilities : {question1_ans}\n"
              f"{print_edit.BOLD}question 2.{print_edit.END} How you define your college's Education schema : {question2_ans}\n"
              f"{print_edit.BOLD}question 3.{print_edit.END} Canadian government is going to make their institutes offline for students : {question3_ans}\n")
        print(print_edit.GREEN + f"Average of reviews on each question\n" +print_edit.END+
              f"Average reviews on question 1 : {avg1}\n"
              f"Average reviews on question 2 : {avg2}\n"
              f"Average reviews on question 3 : {avg3}\n")
result_list = []
result_list.append(q1_dict)
result_list.append(q2_dict)
result_list.append(q3_dict)
print(f"{print_edit.BOLD} {result_list} {print_edit.END}")
