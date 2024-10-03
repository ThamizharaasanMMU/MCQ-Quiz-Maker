import PySimpleGUI as sg
import json
import random
import os

from PySimpleGUI.PySimpleGUI import _refresh_debugger
current_user = ""

	
#Clearscreen
def clearScreen():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def menu():
	sg.theme('DarkBlue14')

	layout = [[sg.Button('Teacher Login', size=(40,1), pad=(10,10))],
			[sg.Button('Student Login', size=(40,1), pad=(10,10))],
			[sg.Button('Administrator Login', size=(40,1), pad=(10,10))],
			[sg.Button('Teacher Registration', size=(40,1), pad=(10,10))],
			[sg.Button('Student Registration', size=(40,1), pad=(10,10))]]
			

	window = sg.Window('Main Menu', layout)

	while True:
			event, values = window.read()
			print(event, values)

			if event == None:
				exit()
			if event == 'Teacher Login':
				window.close()
				teacher_log()
				
			if event == 'Student Login':
				window.close()
				log()
			if event == "Administrator Login":
				window.close()
				admin_log()

			if event == "Teacher Registration":
				window.close()
				teach_reg()

			if event == "Student Registration":
				window.close()
				student_reg()

				
def teach_reg():
	sg.theme('DarkBlue14')

	layout = [[sg.Text('Enter your name : ')],
			[sg.Input(key='-IN1-')],
			[sg.Text('Enter your age : ')],
			[sg.Input(key='-IN2-')],
			[sg.Text('Set your password : ')],
			[sg.Input(key='-IN3-')],
			[sg.Button('Register', size=(40,1), pad=(10,10))],
			[sg.Button('Back', size=(40,1), pad=(10,10))],
			[sg.Text(size=(40,1), key='-OUTPUT1-')],
			[sg.Text(size=(40,1), key='-OUTPUT2-')]]

	window_reg = sg.Window('Teacher Registration', layout)
	t_name = []    # to store teachers name and to make sure the name is already exist or not
	with open('teacher.json', 'r') as f_teacher:
		db_teacher = json.load(f_teacher)

	for i in db_teacher["teachers_det"]:
		t_name.append(i["name"])

	while True:
			event, values = window_reg.read()
			print(event, values)

			if event == None:
				break

			if event == 'Register':
				if values["-IN1-"].upper() in t_name:
					window_reg['-OUTPUT1-'].update(f"NAME ALREADY EXIST")
					window_reg['-OUTPUT2-'].update(f"REGISTRATION FAILED. TRY AGAIN")	
				elif values["-IN1-"] == "" or values["-IN2-"] == "" or values["-IN3-"] == "":
					window_reg["-OUTPUT1-"].update("YOU LEAVE SOME BLANK SPACE THERE.")
					window_reg["-OUTPUT2-"].update("YOU MUST FILL IN ALL THE INFORMATION.")
				else:
					dictionary_t ={
					"name" : values["-IN1-"].upper(),
					"age" : values["-IN2-"],
					"ID" : f'{random.randint(20000,29999)}',
					"password" : values["-IN3-"],
					"quizzes" : []
					}

					db_teacher['teachers_det'].append(dictionary_t)

					# Write the updated 'db_teacher' to the teacher.json file
					with open('teacher.json', 'w') as f_teacher:
						json.dump(db_teacher, f_teacher, indent=4)
					window_reg.close()
					lname = db_teacher["teachers_det"][-1]["name"]
					l_ID = db_teacher["teachers_det"][-1]["ID"]
					lpass = db_teacher["teachers_det"][-1]["password"]
					
					layout = [
							[sg.Text(F"HELLO {lname} !!")],
							[sg.Text("YOUR TEACHER ACCOUNT HAD REGISTERED.")],
							[sg.Text("")],
							[sg.Text(f'Your user ID is "{l_ID}" and your password is "{lpass}"')],
							[sg.Text("")],
							[sg.Text("NOTE:")],
							[sg.Text("Use your ID and password given for login system")],
							[sg.Text("Press the 'Back' button to main menu")],
							[sg.Button("Back", size=(40,1), pad=(10,10))]
							] 

					window_reg1 = sg.Window('REGISTRATION SUCCESS', layout)
					while True:
						event, values = window_reg1.read()
						print(event, values)

						

						if event == None:
							break


						if event == "Back":
							window_reg1.close()
							menu()
						

					window_reg1.close()

			if event == 'Back':
				window_reg.close()
				menu()	
	window_reg.close()
			









def student_reg():
	sg.theme('DarkBlue14')

	layout = [[sg.Text('Enter your name : ')],
			[sg.Input(key='-IN1-')],
			[sg.Text('Enter your age : ')],
			[sg.Input(key='-IN2-')],
			[sg.Text('Set your password : ')],
			[sg.Input(key='-IN3-')],
			[sg.Button('Register', size=(40,1), pad=(10,10))],
			[sg.Button('Back', size=(40,1), pad=(10,10))],
			[sg.Text(size=(40,1), key='-OUTPUT1-')],
			[sg.Text(size=(40,1), key='-OUTPUT2-')]]

	window_stud = sg.Window('Student Registration', layout)
	stud_name = []      # to store students name and to make sure their name is already exist or not
	with open('student.json', 'r') as f_student:
		db_student = json.load(f_student)

	for i in db_student["students_det"]:
		stud_name.append(i["name"])

	while True:
			event, values = window_stud.read()
			print(event, values)

			if event == None:
				break

			if event == 'Register':
				if values["-IN1-"].upper() in stud_name:
					window_stud['-OUTPUT1-'].update(f"NAME ALREADY EXIST")
					window_stud['-OUTPUT2-'].update(f"REGISTRATION FAILED. TRY AGAIN")	
				elif values["-IN1-"] == "" or values["-IN2-"] == "" or values["-IN3-"] == "":
					window_stud["-OUTPUT1-"].update("YOU LEAVE SOME BLANK SPACE THERE.")
					window_stud["-OUTPUT2-"].update("YOU MUST FILL IN ALL THE INFORMATION.")
				else:
					dictionary_t ={
					"name" : values["-IN1-"].upper(),
					"age" : values["-IN2-"],
					"ID" : f'{random.randint(10000,19999)}',
					"password" : values["-IN3-"],
					"quizzes" : []
					}

					db_student['students_det'].append(dictionary_t)
					#db_ques['question_det'].insert(index, q_dict)

					# Write the updated 'db_student' to the student.json file
					with open('student.json', 'w') as f_student:
						json.dump(db_student, f_student, indent=4)
					window_stud.close()
					lname = db_student["students_det"][-1]["name"]
					l_ID = db_student["students_det"][-1]["ID"]
					lpass = db_student["students_det"][-1]["password"]
					layout = [
							[sg.Text(F"HELLO {lname} !!")],
							[sg.Text("YOUR STUDENT ACCOUNT HAD REGISTERED.")],
							[sg.Text("")],
							[sg.Text(f'Your user ID is "{l_ID}" and your password is "{lpass}"')],
							[sg.Text("")],
							[sg.Text("NOTE:")],
							[sg.Text("Use your ID and password given for login system")],
							[sg.Text("Press the 'Back' button to main menu")],
							[sg.Button("Back", size=(40,1), pad=(10,10))]
							] 

					window_stud1 = sg.Window('REGISTRATION SUCCESS', layout)
					while True:
						event, values = window_stud1.read()
						print(event, values)

						

						if event == None:
							break


						if event == "Back":
							window_stud1.close()
							menu()
						

					window_stud1.close()

			if event == 'Back':
				window_stud.close()
				menu()	
	window_stud.close()




def admin_home():
	sg.theme('DarkBlue14')

	layout =[[sg.Button('View all teachers', size=(40,1), pad=(10,10))],
			[sg.Button('View all students', size=(40,1), pad=(10,10))],
			[sg.Button('Delete a teacher', size=(40,1), pad=(10,10))],
			[sg.Button('Delete a student', size=(40,1), pad=(10,10))],
			[sg.Button('Logout', size=(40,1), pad=(10,10))]]


	window = sg.Window(f'Administrator: {nam2[0]}', layout)


	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == "View all teachers":
					view_teacher()

				if event == "View all students":
					view_student()

				if event == "Delete a teacher":
					window.close()
					del_teacher()
					

				if event == "Delete a student":
					window.close()
					del_student()

				
				if event == "Logout":
					clearScreen
					window.close()
					adm_out()
					
					


	window.close()

def view_teacher():
    with open('teacher.json', 'r') as f_teacher:
            db_teacher = json.load(f_teacher)

    count = 0
    for teacher in db_teacher["teachers_det"]:
        count += 1

        c = []
        c.append(count)

    sg.theme('DarkBlue14')


    jj = (db_teacher["teachers_det"])

    data = []
    for x in jj:
        d = []
        d.append(x['name'])
        d.append(x['age'])
        d.append(x['ID'])
        data.append(d)

    print (data)


    header_list = ['          Name          ','     Age     ', '          Teacher ID          ']



    layout = [
                [sg.Table(values=data, headings=header_list,  justification ="center",
                        enable_events=True, key='TABLE',
                        select_mode='extended',auto_size_columns=True)],
                [sg.Button('Close', size=(20,1))]
            ]

    window_teach = sg.Window('TEACHERS LISTS', layout, size=(600,400))
    while True:
        event, values = window_teach.Read()
        if event in ('Close', None): 
            break

        if event == 'TABLE':
            print (values)
            print(values["TABLE"])
    window_teach.close()
    
def view_student():
    with open('student.json', 'r') as f_student:
            db_student = json.load(f_student)

    count = 0
    for student in db_student["students_det"]:
        count += 1

        c = []
        c.append(count)

    sg.theme('DarkBlue14')


    jj = (db_student["students_det"])

    data = []
    for x in jj:
        d = []
        d.append(x['name'])
        d.append(x['age'])
        d.append(x['ID'])
        data.append(d)

    print (data)


    header_list = ['          Name          ','     Age     ', '          Student ID          ']



    layout = [
                [sg.Table(values=data, headings=header_list,  justification ="center",
                        enable_events=True, key='TABLE',
                        select_mode='extended',auto_size_columns=True)],
                [sg.Button('Close', size=(20,1))]
            ]

    window_stud = sg.Window('STUDENTS LISTS', layout, size=(600,400))
    while True:
        event, values = window_stud.Read()
        if event in ('Close', None): 
            break

        if event == 'TABLE':
            print (values)
            print(values["TABLE"])
    window_stud.close()



t_name = []
def del_teacher():
	t_id = []    # to store teachers' ID in a list
	with open('teacher.json', 'r') as f_teacher:
		db_teacher = json.load(f_teacher)

	for i in db_teacher["teachers_det"]:
		t_id.append(i["ID"])

	sg.theme('DarkBlue14')

	layout = [[sg.Text('Select the teacher ID : ')],
				[sg.Combo(t_id, key="COMBO")],
				[sg.Button('Delete', size=(40,1), pad=(10,10))],
				[sg.Button('Back', size=(40,1), pad=(10,10))],
				[sg.Text(size=(40,1), key='-OUTPUT1-')],
				[sg.Text(size=(40,1), key='-OUTPUT2-')]]

	window_del = sg.Window('Delete a teacher', layout)


		
	while True:
				event, values = window_del.read()
				print(event, values)

				if event == None:
					break

				if event == 'Back':
					window_del.close()
					admin_home()

				if event == 'Delete':
					if values["COMBO"] == '':
						window_del["-OUTPUT1-"].update("ERROR:")
						window_del["-OUTPUT2-"].update("YOU HAVE NOT SELECT THE TEACHER ID YET !!")
					elif values["COMBO"] != '':
						t_id1 = []
						index = (t_id).index(values["COMBO"])  
						x_dict = (db_teacher["teachers_det"][index])
						t_name.append(x_dict["name"])
						t_id1.append(x_dict)
						window_del.close()
						def confirm():

							sg.theme('DarkBlue14')

							layout = [
								        [sg.Text(f"This account belongs to {t_name[0]}")],
										[sg.Text("")],
										[sg.Text('Are you sure want to delete this account? ')],
										[sg.Button('YES', size=(40,1), pad=(10,10))],
										[sg.Button('NO', size=(40,1), pad=(10,10))]]


							window_del1 = sg.Window('Confirmation(Delete account)', layout)
							with open('teacher.json', 'r') as f_teacher:
								db_teacher = json.load(f_teacher)
							while True:
										event, values = window_del1.read()
										print(event, values)

										if event == None:
											break

										if event == 'NO':
											window_del1.close()
											return del_teacher()

										if event == 'YES':
											db_teacher["teachers_det"].remove(t_id1[0])
											window_del1.close()
											sg.theme('DarkBlue14')
											layout = [
													[sg.Text("This account had been DELETED")],
													[sg.Text("Press the 'Back' button to back home")],
													[sg.Button("Back", size=(40,1), pad=(10,10))]
													] 

											window_del2 = sg.Window('', layout)
											while True:
												event, values = window_del2.read()
												print(event, values)

												

												if event == None:
													break


												if event == "Back":
													window_del2.close()
													

											window_del2.close()	
											

							with open('teacher.json', 'w') as f_teacher:
									json.dump(db_teacher, f_teacher, indent=4)


							window_del1.close()

						confirm()
						
						window_del['-OUTPUT2-'].update(f"")		
					else:
						window_del['-OUTPUT1-'].update(f"NAME NOT FOUND")
						window_del['-OUTPUT2-'].update(f"")	
				


				


	window_del.close()





s_name = []
def del_student():

	stud_id = []    #to store students' ID
	with open('student.json', 'r') as f_student:
		db_student = json.load(f_student)

	for i in db_student["students_det"]:
		stud_id.append(i["ID"])

	sg.theme('DarkBlue14')

	layout = [[sg.Text('Select the student ID : ')],
				[sg.Combo(stud_id, key="COMBO")],
				[sg.Button('Delete', size=(40,1), pad=(10,10))],
				[sg.Button('Back', size=(40,1), pad=(10,10))],
				[sg.Text(size=(40,1), key='-OUTPUT1-')],
				[sg.Text(size=(40,1), key='-OUTPUT2-')]]

	window_stud = sg.Window('Delete a student', layout)


		
	while True:
				event, values = window_stud.read()
				print(event, values)

				if event == None:
					break

				if event == 'Back':
					window_stud.close()
					admin_home()

				if event == 'Delete':
					if values["COMBO"] == '':
						window_stud["-OUTPUT1-"].update("ERROR:")
						window_stud["-OUTPUT2-"].update("YOU HAVE NOT SELECT THE STUDENT ID YET !!")

					elif values["COMBO"] != '':	
						stud_id1 = []
						index = (stud_id).index(values["COMBO"])  
						x_dict = (db_student["students_det"][index])
						s_name.append(x_dict["name"])
						stud_id1.append(x_dict)
						window_stud.close()
						def confirm():

							sg.theme('DarkBlue14')

							layout = [
								        [sg.Text(f"This account belongs to {s_name[0]}")],
										[sg.Text("")],
										[sg.Text('Are you sure want to delete this account? ')],
										[sg.Button('YES', size=(40,1), pad=(10,10))],
										[sg.Button('NO', size=(40,1), pad=(10,10))]]


							window_stud1 = sg.Window('Confirmation(Delete account)', layout)
							with open('student.json', 'r') as f_student:
								db_student = json.load(f_student)
							while True:
										event, values = window_stud1.read()
										print(event, values)

										if event == None:
											break

										if event == 'NO':
											window_stud1.close()
											return del_student()

										if event == 'YES':
											db_student["students_det"].remove(stud_id1[0])
											window_stud1.close()
											sg.theme('DarkBlue14')
											layout = [
													[sg.Text("This account had been DELETED")],
													[sg.Text("Press the 'Back' button to back home")],
													[sg.Button("Back", size=(40,1), pad=(10,10))]
													] 

											window_stud2 = sg.Window('', layout)
											while True:
												event, values = window_stud2.read()
												print(event, values)

												

												if event == None:
													break


												if event == "Back":
													window_stud2.close()
												

											window_stud2.close()	
											

							with open('student.json', 'w') as f_student:
									json.dump(db_student, f_student, indent=4)


							window_stud1.close()

						confirm()
						
						window_stud['-OUTPUT2-'].update(f"")
					else:
						window_stud['-OUTPUT1-'].update(f"NAME NOT FOUND")
						window_stud['-OUTPUT2-'].update(f"")	
				


				


	window_stud.close()





def adm_out():

	sg.theme('DarkBlue14')

	layout = [[sg.Text('Are you sure want to log out? ')],
				[sg.Button('YES', size=(40,1), pad=(10,10))],
				[sg.Button('NO', size=(40,1), pad=(10,10))]]


	window = sg.Window('Confirmation', layout)

	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == 'NO':
					window.close()
					admin_home()
					

				if event == 'YES':
					window.close()
					menu()		
				
				

	window.close()



def admin_home():
	sg.theme('DarkBlue14')

	layout =[[sg.Button('View all teachers', size=(40,1), pad=(10,10))],
			[sg.Button('View all students', size=(40,1), pad=(10,10))],
			[sg.Button('Delete a teacher', size=(40,1), pad=(10,10))],
			[sg.Button('Delete a student', size=(40,1), pad=(10,10))],
			[sg.Button('Logout', size=(40,1), pad=(10,10))]]


	window = sg.Window(f'Administrator: {nam2[0]}', layout)


	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == "View all teachers":
					view_teacher()

				if event == "View all students":
					view_student()

				if event == "Delete a teacher":
					window.close()
					del_teacher()
					admin_home()
					

				if event == "Delete a student":
					window.close()
					del_student()
					admin_home()

				
				if event == "Logout":
					clearScreen
					window.close()
					adm_out()
					
					


	window.close()
					
					


	window.close()


teach_name = []    # to store teachers' name
def q_create():
	# global current_user
	# with open ("teacher.json") as f :
	#     teachers = json.load(f)
	# for item in teachers ["teachers_det"]:
	# 	if item ["ID"] == current_user :
	# 		quizzes = item ["quizzes"]
	# 		break

	sg.theme('DarkBlue14')

	layout = [[sg.Text('Enter the quiz name : ')],
				[sg.Input(key='-IN1-')],
				[sg.Text('Enter the quiz topic : ')],
				[sg.Input(key='-IN2-')],
				[sg.Button('Create', size=(40,1), pad=(10,10))],
				[sg.Button('Back', size=(40,1), pad=(10,10))],
				[sg.Text(size=(40,1), key='-OUTPUT1-')],
				[sg.Text(size=(40,1), key='-OUTPUT2-')]]

	with open('quiz.json', 'r') as f_quiz:
		db_quiz = json.load(f_quiz)

	with open("teacher.json", "r") as f_teacher:
		db_teacher = json.load(f_teacher)

	for name in db_teacher["teachers_det"]:
		teach_name.append(name["name"])

	ind = teach_name.index(nam1[-1])    #indentify the position of teacher
	

	window = sg.Window('Teacher Home Page', layout)

	while True:
			event, values = window.read()
			print(event, values)

			if event == None:
				break

			if event == 'Back':
				window.close()
				teacher_home()

			if event == "Create":
				if values["-IN1-"] == "" or values["-IN2-"] == "":
					window['-OUTPUT1-'].update("THERE IS A BLANK SPACE")	
					window['-OUTPUT2-'].update("TRY AGAIN ")	
					
			
				elif values["-IN1-"] != "" and values["-IN2-"] != "":
					window.close()
					q_nam = values["-IN1-"].upper()
					q_top = values["-IN2-"].upper()
					sg.theme('DarkBlue14')

					layout = [[sg.Text('Select the status of the quiz')],
								[sg.Button('PUBLISH', size=(40,1), pad=(10,10))],
								[sg.Button('DRAFT', size=(40,1), pad=(10,10))]]


					window = sg.Window('Confirmation', layout)

					while True:
								event, values = window.read()
								print(event, values)

								if event == None:
									break

								if event == 'DRAFT':
									dictionary_quiz ={
									"Quizname" : q_nam,
									"topic" : q_top,
									"QuizID" : str(random.randint(600000,699999)),
									"status": "DRAFT"
									}
									db_quiz['quiz_det'].append(dictionary_quiz)

									(db_teacher["teachers_det"][ind]["quizzes"]).append(f"{dictionary_quiz['QuizID']}")

									window.close()
									def created():
										sg.theme('DarkBlue14')
										layout = [
											    [sg.Text(f"Quiz name  : {dictionary_quiz['Quizname']}")],
												[sg.Text(f"Quiz topic : {dictionary_quiz['topic']}")],
												[sg.Text(f"Quiz ID    : {dictionary_quiz['QuizID']}")],
												[sg.Text(f"Quiz status : {dictionary_quiz['status']}")],
												[sg.Text("This quiz had been CREATED")],
												[sg.Text("Press the 'Back' button to back home")],
												[sg.Button("Back", size=(40,1), pad=(10,10))]
										        ]

										window = sg.Window('', layout)
										while True:
											event, values = window.read()
											print(event, values)

											

											if event == None:
												break


											if event == "Back":
												window.close()
										

										window.close()
									created()

																
									#admin_home()
								with open('quiz.json', 'w') as f_quiz:
									json.dump(db_quiz, f_quiz, indent=4)

								with open('teacher.json', 'w') as f_teacher:
									json.dump(db_teacher, f_teacher, indent=4)

								
								

								if event == 'PUBLISH':

									dictionary_quiz ={
									"Quizname" : q_nam,
									"topic" : q_top,
									"QuizID" : str(random.randint(600000,699999)),
									"status" : "PUBLISHED"
									}
									window.close()
									with open("student.json", "r") as f:
											db_student = json.load(f)
									name = []
									for i in db_student["students_det"]:
											print(i["name"])
											name.append([sg.Checkbox(f'{i["name"]}')])


									layout = [
											[sg.Text("Select the students", font=12)],
											[sg.Text("")],
											[sg.Column(name,
											scrollable=True, size=(600,400))],
											[sg.Button("Select", size=(40,1), pad=(210,10))],
											[sg.Text(size=(40,1), key='-OUTPUT1-')]
											]
													

									window = sg.Window('Publish to students', layout, size=(600,600))

									while True:
													event, values = window.read()
													print(event, values)

													if event == None:
															break

													if event == "Select":
															window["-OUTPUT1-"].update("YOU HAVE NOT SELECT THE STUDENTS YET")

															n = []
															for i in range(0,len(db_student["students_det"])):
																	if values[i] == True:
																			window.close()
																			n.append(i)
															

											

									window.close()



									for num in n:
											if len(n) == 1:
													i = 0
													while i < len(n):
															(db_student["students_det"][num]["quizzes"]).append(dictionary_quiz['QuizID'])

															i += 1
											else:
													i = 1
													while i < len(n):
															(db_student["students_det"][num]["quizzes"]).append(dictionary_quiz['QuizID'])

															i += 1


									with open("student.json","w") as f:
											db_student = json.dump(db_student, f, indent=4)
									db_quiz['quiz_det'].append(dictionary_quiz)

									(db_teacher["teachers_det"][ind]["quizzes"]).append(f"{dictionary_quiz['QuizID']}")
								
									window.close()
									def created():
										sg.theme('DarkBlue14')
										layout = [
											    [sg.Text(f"Quiz name  : {dictionary_quiz['Quizname']}")],
												[sg.Text(f"Quiz topic : {dictionary_quiz['topic']}")],
												[sg.Text(f"Quiz ID    : {dictionary_quiz['QuizID']}")],
												[sg.Text(f"Quiz status : {dictionary_quiz['status']}")],
												[sg.Text("This quiz had been CREATED")],
												[sg.Text("Press the 'Back' button to back home")],
												[sg.Button("Back", size=(40,1), pad=(10,10))]
												] 

										window = sg.Window('', layout)
										while True:
											event, values = window.read()
											print(event, values)

											

											if event == None:
												break


											if event == "Back":
												window.close()
												

										window.close()
									created()
								
							
									#menu()					
								with open('quiz.json', 'w') as f_quiz:
									json.dump(db_quiz, f_quiz, indent=4)


								with open('teacher.json', 'w') as f_teacher:
									json.dump(db_teacher, f_teacher, indent=4)
								    

					window.close()		
            
	window.close()



teach_name = []
def q_del():
	with open ("teacher.json") as f_teacher :
	    teachers = json.load(f_teacher)

	for item in teachers["teachers_det"]:
		teach_name.append(item["name"])
		print("")

	ind = teach_name.index(nam1[-1])

	quizzes = (teachers["teachers_det"][ind]["quizzes"])




	sg.theme('DarkBlue14')

	layout = [[sg.Text('Enter the quiz ID : ')],
				[sg.Combo(quizzes, key="COMBO")],
				[sg.Button('Delete', size=(40,1), pad=(10,10))],
				[sg.Button('Back', size=(40,1), pad=(10,10))],
				[sg.Text(size=(40,1), key='-OUTPUT1-')],
				[sg.Text(size=(40,1), key='-OUTPUT2-')]]

	window = sg.Window('Delete a student', layout)
	q_id = []        # store quizzes' id
	with open('quiz.json', 'r') as f_quiz:
		db_quiz = json.load(f_quiz)

	for i in db_quiz["quiz_det"]:
		q_id.append(i["QuizID"])

		
	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == 'Delete':
					if values["COMBO"] == '':
						window["-OUTPUT1-"].update("ERROR:")
						window["-OUTPUT2-"].update("YOU HAVE NOT SELECT THE QUIZ ID YET")
					else:
						q_dict = []   # to store a whole dictionary from quiz.json
						q_name = []     # to store Quiz name from the selected dictionary
						index = (q_id).index(values["COMBO"])  
						x_dict = (db_quiz["quiz_det"][index])
						window['-OUTPUT2-'].update(f"Quiz name : {x_dict['Quizname']}")
						print(f'Quiz name = {x_dict["Quizname"]}')
						q_dict.append(x_dict)
						q_name.append(x_dict['Quizname'])
						
						window.close()
						def confirm():

							sg.theme('DarkBlue14')

							layout = [[sg.Text(f'Are you sure want to delete this quiz? ')],
							          [sg.Text(f'Quiz name : {q_name[0]} ')],
										[sg.Button('YES', size=(40,1), pad=(10,10))],
										[sg.Button('NO', size=(40,1), pad=(10,10))]]


							window = sg.Window('', layout)
							with open('quiz.json', 'r') as f_quiz:
								db_quiz = json.load(f_quiz)
							while True:
										event, values = window.read()
										print(event, values)

										if event == None:
											break

										if event == 'NO':
											window.close()
											return q_del()

										if event == 'YES':
											db_quiz["quiz_det"].remove(q_dict[0])
											(teachers["teachers_det"][ind]["quizzes"]).remove(q_dict[0]['QuizID'])
											
											window.close()	
											def created():
												sg.theme('DarkBlue14')
												layout = [
														[sg.Text(f"Quiz name  : {q_dict[0]['Quizname']}")],
														[sg.Text(f"Quiz topic : {q_dict[0]['topic']}")],
														[sg.Text(f"Quiz ID    : {q_dict[0]['QuizID']}")],
														[sg.Text(f"Quiz status : {q_dict[0]['status']}")],
														[sg.Text("This quiz had been DELETED")],
														[sg.Text("Press the 'Back' button to back home")],
														[sg.Button("Back", size=(40,1), pad=(10,10))]
														] 

												window = sg.Window('', layout)
												while True:
													event, values = window.read()
													print(event, values)

													

													if event == None:
														break


													if event == "Back":
														window.close()
													

												window.close()
											created()

							with open('quiz.json', 'w') as f_quiz:
									json.dump(db_quiz, f_quiz, indent=4)
							with open("teacher.json", "w") as f_teacher:
								json.dump(teachers,f_teacher, indent=4)


							window.close()
                        
						confirm()
						

					# else:
					# 	window['-OUTPUT1-'].update(f"QUIZ NOT FOUND")
					# 	window['-OUTPUT2-'].update(f"")
					# 	print("QUIZ NOT FOUND. TRY AGAIN")
					# 	window.close()
					# 	return q_del()
                

				if event == 'Back':
					window.close()
					
				

				
	window.close()


teach_name = []
def edits():

	with open ("teacher.json") as f_teacher :
	    teachers = json.load(f_teacher)

	for item in teachers["teachers_det"]:
		teach_name.append(item["name"])
		print("")

	ind = teach_name.index(nam1[-1])    #nam[-1] refer to the current user

	quizzes = (teachers["teachers_det"][ind]["quizzes"])


	sg.theme('DarkBlue14')

	layout = [[sg.Text('Enter the quiz ID : ')],
				[sg.Combo(quizzes, key="COMBO")],
				[sg.Button('Edit quiz name', size=(40,1), pad=(10,10))],
				[sg.Button('Edit quiz topic', size=(40,1), pad=(10,10))],
				[sg.Button('Edit quiz status', size=(40,1), pad=(10,10))],
				[sg.Button('Back', size=(40,1), pad=(10,10))],
				[sg.Text(size=(40,1), key='-OUTPUT1-')],
				[sg.Text(size=(40,1), key='-OUTPUT2-')]]

	window = sg.Window('Edit quiz', layout)
	q_Id = []   # to store all the quiz ID's to find the position of the selected quiz ID later
	id_l = []
	with open('quiz.json', 'r') as f_quiz:
		db_quiz = json.load(f_quiz)

	for i in db_quiz["quiz_det"]:
		q_Id.append(i["QuizID"])

	
	with open('question.json', 'r') as f_ques:
		db_ques = json.load(f_ques)


	for i in db_ques["question_det"]:
		id_l.append(i["QuizID"])

		
	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == 'Back':
					window.close()
					teacher_home()

				if event == "Edit quiz name":
					if values["COMBO"] == '':
						window['-OUTPUT1-'].update(f"ERROR:")	
						window['-OUTPUT2-'].update(f"YOU HAVE NOT SELECT THE QUIZ ID YET.")
					
					else:
						qu_dict = []    # to store the whole dictionary of the selected quiz from quiz.json
						index = (q_Id).index(values["COMBO"])  
						x_dict = (db_quiz["quiz_det"][index])
						qu_dict.append(x_dict)
						window.close()
						def confirm():

							sg.theme('DarkBlue14')

							layout = [  
								        [sg.Text("Current Quiz Name: ")],
										[sg.Text(f"{qu_dict[0]['Quizname']}")],
								        [sg.Text('Are you sure want to edit the quiz name? ')],
										[sg.Button('YES', size=(40,1), pad=(10,10))],
										[sg.Button('NO', size=(40,1), pad=(10,10))]]


							window = sg.Window('Confirmation(Edit quiz name)', layout)
							with open('quiz.json', 'r') as f_quiz:
								db_quiz = json.load(f_quiz)
							while True:
										event, values = window.read()
										print(event, values)

										if event == None:
											break

										if event == 'NO':
											window.close()
											return edits()

										if event == 'YES':
											window.close()		
											sg.theme('DarkBlue14')

											layout = [[sg.Text('Enter the new quiz name ')],
														[sg.Input(key='-IN1-')],
														[sg.Button('Edit', size=(40,1), pad=(10,10))]]
													

											window = sg.Window('', layout)
											with open('quiz.json', 'r') as f_quiz:
												db_quiz = json.load(f_quiz)
											while True:
														event, values = window.read()
														print(event, values)

														if event == None:
															break

														if event == "Edit":
															y_dict ={
															"Quizname" : values["-IN1-"].upper(),
															"topic" : list(x_dict.values())[1],
															"QuizID" : list(x_dict.values())[2],
															"status" : list(x_dict.values())[3]
															}
															db_quiz["quiz_det"].remove(qu_dict[0])
															(db_quiz["quiz_det"]).insert(index, y_dict)
															window.close()
															
															def name_edited():
																sg.theme('DarkBlue14')
																layout = [
																		[sg.Text("This quiz name had been EDITED")],
																		[sg.Text("Press the 'Back' button to back home")],
																		[sg.Button("Back", size=(40,1), pad=(10,10))]
																		]

																window = sg.Window('', layout)
																while True:
																	event, values = window.read()
																	print(event, values)

																	

																	if event == None:
																		break


																	if event == "Back":
																		window.close()
																		

																window.close()
															name_edited()

															with open('quiz.json', 'w') as f_quiz:
																json.dump(db_quiz, f_quiz, indent=4)
															
															
																
											window.close()
						confirm()
						with open("quiz.json", "r") as f_quiz:
							db_quiz = json.load(f_quiz)				
				if event == "Edit quiz topic":
					if values["COMBO"] == '':
						window['-OUTPUT1-'].update(f"ERROR:")	
						window['-OUTPUT2-'].update(f"YOU HAVE NOT SELECT THE QUIZ ID YET")
					
					else:
						qu_dict = []
						index = (q_Id).index(values["COMBO"])  
						x_dict = (db_quiz["quiz_det"][index])
						qu_dict.append(x_dict)
						window.close()
						def confirm():

							sg.theme('DarkBlue14')

							layout = [ 
								        [sg.Text("Current quiz topic : ")],
										[sg.Text(f'{qu_dict[0]["topic"]}')],
								        [sg.Text('Are you sure want to edit the quiz topic? ')],
										[sg.Button('YES', size=(40,1), pad=(10,10))],
										[sg.Button('NO', size=(40,1), pad=(10,10))]]


							window = sg.Window('', layout)
							with open('quiz.json', 'r') as f_quiz:
								db_quiz = json.load(f_quiz)
							while True:
										event, values = window.read()
										print(event, values)

										if event == None:
											break

										if event == 'NO':										
											window.close()
											return edits()
                                            

										if event == 'YES':
											window.close()		
											sg.theme('DarkBlue14')

											layout = [[sg.Text('Enter the new quiz topic ')],
														[sg.Input(key='-IN1-')],
														[sg.Button('Edit', size=(40,1), pad=(10,10))]]
													

											window = sg.Window('Quiz topic', layout)
											with open('quiz.json', 'r') as f_quiz:
												db_quiz = json.load(f_quiz)
											while True:
														event, values = window.read()
														print(event, values)

														if event == None:
															break

														if event == "Edit":
															y_dict ={
															"Quizname" : list(x_dict.values())[0],
															"topic" : values["-IN1-"].upper(),
															"QuizID" : list(x_dict.values())[2],
															"status" : list(x_dict.values())[3]
															}
															db_quiz["quiz_det"].remove(qu_dict[0])
															(db_quiz["quiz_det"]).insert(index, y_dict)
															window.close()
															def topic_edited():
																sg.theme('DarkBlue14')
																layout = [
																		[sg.Text("This quiz topic had been EDITED")],
																		[sg.Text("Press the 'Back' button to back home")],
																		[sg.Button("Back", size=(40,1), pad=(10,10))]
																		]

																window = sg.Window('', layout)
																while True:
																	event, values = window.read()
																	print(event, values)

																	

																	if event == None:
																		break


																	if event == "Back":
																		window.close()
																		

																window.close()
															topic_edited()

															with open('quiz.json', 'w') as f_quiz:
																json.dump(db_quiz, f_quiz, indent=4)
															
																
											window.close()
						confirm()
						with open("quiz.json", "r") as f_quiz:
							db_quiz = json.load(f_quiz)

				if event == "Edit quiz status":
					if values["COMBO"] == '':
						window['-OUTPUT1-'].update(f"ERROR:")	
						window['-OUTPUT2-'].update(f"YOU HAVE NOT SELECT THE QUIZ ID YET")

					else:
						qu_dict = []
						index = (q_Id).index(values["COMBO"])  
						x_dict = (db_quiz["quiz_det"][index])
						qu_dict.append(x_dict)
						window.close()
						if x_dict['status'] == "PUBLISHED":
							def confirm():

								sg.theme('DarkBlue14')

								layout = [ 
									        [sg.Text("Current quiz status:")],
											[sg.Text(qu_dict[0]["status"])],
									        [sg.Text('Do you want to revert this quiz to the draft? ')],
											[sg.Button('YES', size=(40,1), pad=(10,10))],
											[sg.Button('NO', size=(40,1), pad=(10,10))]]


								window = sg.Window('Confirmation(Edit quiz status)', layout)
								with open('quiz.json', 'r') as f_quiz:
									db_quiz = json.load(f_quiz)
								while True:
											event, values = window.read()
											print(event, values)

											if event == None:
												break

											if event == 'NO':										
												window.close()
												return edits()

											if event == 'YES':
												window.close()
												z_dict ={
												"Quizname" : list(x_dict.values())[0],
												"topic" : list(x_dict.values())[1],
												"QuizID" : list(x_dict.values())[2],
												"status" : "DRAFT"
												}
												with open("student.json", "r") as f:
														db_student = json.load(f)


												quiz = []
												rem = []
												for i in db_student["students_det"]:
														quiz.append(i["quizzes"])


												for j in range(0,len(quiz)):
														if list(x_dict.values())[2] in (db_student["students_det"][j]["quizzes"]):
																rem.append(j)

												for num in rem:
														(db_student["students_det"][num]["quizzes"]).remove(list(x_dict.values())[2])


												with open("student.json","w") as f:
														db_student = json.dump(db_student, f, indent=4)

												db_quiz["quiz_det"].remove(qu_dict[0])
												(db_quiz["quiz_det"]).insert(index, z_dict)

												def status_edited():
													sg.theme('DarkBlue14')
													layout = [
															[sg.Text("This quiz status had been EDITED")],
															[sg.Text("Press the 'Back' button to back home")],
															[sg.Button("Back", size=(40,1), pad=(10,10))]
															]

													window = sg.Window('', layout)
													while True:
														event, values = window.read()
														print(event, values)

														

														if event == None:
															break


														if event == "Back":
															window.close()
															

													window.close()
												status_edited()

												with open('quiz.json', 'w') as f_quiz:
													json.dump(db_quiz, f_quiz, indent=4)	
												
																	
												
							confirm()
							with open("quiz.json", "r") as f_quiz:
								db_quiz = json.load(f_quiz)
			
						if x_dict['status'] == "DRAFT":
							def confirm():

								sg.theme('DarkBlue14')

								layout = [
									        [sg.Text("Current quiz status:")],
											[sg.Text(qu_dict[0]["status"])],
									        [sg.Text('Do you want to publish this quiz to students? ')],
											[sg.Button('YES', size=(40,1), pad=(10,10))],
											[sg.Button('NO', size=(40,1), pad=(10,10))]]


								window = sg.Window('Confirmation(Edit quiz status)', layout)
								with open('quiz.json', 'r') as f_quiz:
									db_quiz = json.load(f_quiz)
								while True:
											event, values = window.read()
											print(event, values)

											if event == None:
												break

											if event == 'NO':										
												window.close()
												return edits()

											if event == 'YES':
												window.close()
												z_dict ={
												"Quizname" : list(x_dict.values())[0],
												"topic" : list(x_dict.values())[1],
												"QuizID" : list(x_dict.values())[2],
												"status" : "PUBLISHED"
												}
												db_quiz["quiz_det"].remove(qu_dict[0])
												(db_quiz["quiz_det"]).insert(index, z_dict)
												with open("student.json", "r") as f:
														db_student = json.load(f)
												name = []
												for i in db_student["students_det"]:
														print(i["name"])
														name.append([sg.Checkbox(f'{i["name"]}')])


												layout = [
														[sg.Text("Select the students", font=12)],
														[sg.Text("")],
														[sg.Column(name,
														scrollable=True, size=(600,400))],
														[sg.Button("Select", size=(40,1), pad=(210,10))],
														[sg.Text(size=(40,1), key='-OUTPUT1-')]
														]
																

												window = sg.Window('Publish to students', layout, size=(600,600))

												while True:
																event, values = window.read()
																print(event, values)

																if event == None:
																		break

																if event == "Select":
																		window["-OUTPUT1-"].update("YOU HAVE NOT SELECT THE STUDENTS YET")

																		n = []
																		for i in range(0,len(db_student["students_det"])):
																				if values[i] == True:
																						window.close()
																						n.append(i)
																		

														

												window.close()



												for num in n:
														if len(n) == 1:
																i = 0
																while i < len(n):
																		(db_student["students_det"][num]["quizzes"]).append(list(x_dict.values())[2])

																		i += 1
														else:
																i = 1
																while i < len(n):
																		(db_student["students_det"][num]["quizzes"]).append(list(x_dict.values())[2])

																		i += 1


												with open("student.json","w") as f:
														db_student = json.dump(db_student, f, indent=4)
												
												def status_edited():
													sg.theme('DarkBlue14')
													layout = [
															[sg.Text("This quiz status had been EDITED")],
															[sg.Text("Press the 'Back' button to back home")],
															[sg.Button("Back", size=(40,1), pad=(10,10))]
															]

													window = sg.Window('', layout)
													while True:
														event, values = window.read()
														print(event, values)

														

														if event == None:
															break


														if event == "Back":
															window.close()
															

													window.close()
												status_edited()
												


												with open('quiz.json', 'w') as f_quiz:
													json.dump(db_quiz, f_quiz, indent=4)	
												
																	
												window.close()
							confirm()


	window.close()




def whole():
    pos = []

    with open("teacher.json", "r") as f_teacher:
        db_teacher = json.load(f_teacher)

    with open("quiz.json", "r") as f_quiz:
            db_quiz = json.load(f_quiz)

    q = []
    for i in db_quiz["quiz_det"]:
            q.append(i["QuizID"])
    teacher = []
    for i in db_teacher["teachers_det"]:
            teacher.append(i["name"])

    ind = teacher.index(nam1[-1])    

    quiz = (db_teacher["teachers_det"][ind]["quizzes"])
	

    for item in quiz:
            for i in range(0,len(q)):
                    if item in (db_quiz["quiz_det"][i]["QuizID"]):
                            pos.append(i)
						


    def show_quiz():
        with open('quiz.json', 'r') as f_quiz:
                db_quiz = json.load(f_quiz)

        count = 0
        for quiz in db_quiz["quiz_det"]:
            count += 1

            c = []
            c.append(count)

        sg.theme('DarkBlue14')
        

        jj = pos


        data = []
        for x in jj:
            d = []
            d.append((db_quiz["quiz_det"][x]["Quizname"]))
            d.append((db_quiz["quiz_det"][x]["topic"]))
            d.append((db_quiz["quiz_det"][x]["QuizID"]))
            d.append((db_quiz["quiz_det"][x]["status"]))
            data.append(d)

        print (data)


        header_list = ['        Quiz Name        ','    Topic   ', '    Quiz ID    ', '    Status    ']



        layout = [
                    [sg.Table(values=data, headings=header_list,justification ="center",
                            enable_events=True, key='TABLE',
                            select_mode='extended',auto_size_columns=True)],
                    [sg.Button('Close', size=(20,1)),sg.Button('Show questions', size=(20,1))],
                    [sg.Text(size=(40,1), key='-OUTPUT1-')]
                ]

        window = sg.Window('QUIZ LISTS', layout, size=(800,400))
        while True:
            event, values = window.Read()
            if event in ('Close', None): 
                break

            if event == 'TABLE':
                # window["-OUTPUT1-"].update("YOU HAVE NOT SELECT THE QUIZ YET!!")
                #jj = [0, 8, 9, 10]
                
                num = (values["TABLE"][0])  
                a = (db_quiz["quiz_det"][jj[num]]["QuizID"])
                


            if event == "Show questions":
                if (values["TABLE"]) == []:
                    window["-OUTPUT1-"].update("YOU HAVE NOT SELECT THE QUIZ YET!!")
                else:
                    window["-OUTPUT1-"].update("")
                    window.close()
                    sg.theme('DarkBlue14')

                    #view questions

                    ques_item = []
                    with open("question.json", "r") as f_ques:
                        db_ques = json.load(f_ques)

                    for i in range(0,len(db_ques["question_det"])):

                        if a == (db_ques["question_det"][i]["QuizID"]) and db_ques["question_det"][i]["Correct"][0] == True:
                    
                            (ques_item.append([sg.Text(f'{db_ques["question_det"][i]["QuizNo"]}. Question : {db_ques["question_det"][i]["Question"]}')]))
                            (ques_item.append([sg.Text(f'A. {db_ques["question_det"][i]["Answers"][0]}', text_color="green")]))
                            (ques_item.append([sg.Text(f'B. {db_ques["question_det"][i]["Answers"][1]}')]))
                            (ques_item.append([sg.Text(f'C. {db_ques["question_det"][i]["Answers"][2]}')]))
                            (ques_item.append([sg.Text(f'D. {db_ques["question_det"][i]["Answers"][3]}')]))
                            (ques_item.append([sg.Text(f'')]))
                            

                        elif a == (db_ques["question_det"][i]["QuizID"]) and db_ques["question_det"][i]["Correct"][1] == True:    
                            (ques_item.append([sg.Text(f'{db_ques["question_det"][i]["QuizNo"]}. Question : {db_ques["question_det"][i]["Question"]}')]))
                            (ques_item.append([sg.Text(f'A. {db_ques["question_det"][i]["Answers"][0]}')]))
                            (ques_item.append([sg.Text(f'B. {db_ques["question_det"][i]["Answers"][1]}', text_color="green")]))
                            (ques_item.append([sg.Text(f'C. {db_ques["question_det"][i]["Answers"][2]}')]))
                            (ques_item.append([sg.Text(f'D. {db_ques["question_det"][i]["Answers"][3]}')]))
                            (ques_item.append([sg.Text(f'')]))


                        elif a == (db_ques["question_det"][i]["QuizID"]) and db_ques["question_det"][i]["Correct"][2] == True:    
                            (ques_item.append([sg.Text(f'{db_ques["question_det"][i]["QuizNo"]}. Question : {db_ques["question_det"][i]["Question"]}')]))
                            (ques_item.append([sg.Text(f'A. {db_ques["question_det"][i]["Answers"][0]}')]))
                            (ques_item.append([sg.Text(f'B. {db_ques["question_det"][i]["Answers"][1]}')]))
                            (ques_item.append([sg.Text(f'C. {db_ques["question_det"][i]["Answers"][2]}', text_color="green")]))
                            (ques_item.append([sg.Text(f'D. {db_ques["question_det"][i]["Answers"][3]}')]))
                            (ques_item.append([sg.Text(f'')]))


                        if a == (db_ques["question_det"][i]["QuizID"]) and db_ques["question_det"][i]["Correct"][3] == True:    
                            (ques_item.append([sg.Text(f'{db_ques["question_det"][i]["QuizNo"]}. Question : {db_ques["question_det"][i]["Question"]}')]))
                            (ques_item.append([sg.Text(f'A. {db_ques["question_det"][i]["Answers"][0]}')]))
                            (ques_item.append([sg.Text(f'B. {db_ques["question_det"][i]["Answers"][1]}')]))
                            (ques_item.append([sg.Text(f'C. {db_ques["question_det"][i]["Answers"][2]}')]))
                            (ques_item.append([sg.Text(f'D. {db_ques["question_det"][i]["Answers"][3]}', text_color="green")]))
                            (ques_item.append([sg.Text(f'')]))

                    # tmz.append([sg.Button('Close', size=(20,1))])

                        
        
                    

                    layout = [
                        [sg.Column(ques_item,
                        scrollable=True, size=(800,300))],
                        [sg.Button("Close", size=(40,1), pad=(210,10))]
                    ]



                    window = sg.Window('QUESTIONS', layout, size=(800,400))
                    while True:

                                event, values = window.read()
                                print(event, values)

                                if event == None:
                                    break
                                if event == "Close":
                                    window.close()
                                    show_quiz()


                    window.close()

                    
                    


        window.close()

    show_quiz()

def teacher_out():

	sg.theme('DarkBlue14')

	layout = [[sg.Text('Are you sure want to log out? ')],
				[sg.Button('YES', size=(40,1), pad=(10,10))],
				[sg.Button('NO', size=(40,1), pad=(10,10))]]


	window = sg.Window('Confirmation', layout)

	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == 'NO':
					window.close()
					teacher_home()
					break

				if event == 'YES':
					window.close()

				

	window.close()


def teacher_home():
	sg.theme('DarkBlue14')

	layout =[
			[sg.Frame(layout=[
			[sg.Button('Create quiz', size=(20,1), pad=(10,10))],
			[sg.Button('Edit quiz', size=(20,1), pad=(10,10))],
			[sg.Button('Delete quiz', size=(20,1), pad=(10,10))],
			], title='Quiz',title_color='white', font='Any12'),
			sg.Frame(layout=[
			[sg.Button('Create question', size=(20,1), pad=(10,10))],
			[sg.Button('Edit question', size=(20,1), pad=(10,10))],
			[sg.Button('Delete question', size=(20,1), pad=(10,10))],
			],title='Question',title_color='white', font='Any12')],
			[sg.Button('Show own quiz', size=(20,1), pad=(120,10))],
			[sg.Button('Logout', size=(20,1), pad=(120,10))]
        	]


	window = sg.Window(f'Teacher: {nam1[-1]}', layout)    #current user = nam[-1]


	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == "Create quiz":
					window.close()
					q_create()
					teacher_home()

				if event == "Edit quiz":
					window.close()
					edits()
					teacher_home()

				if event == "Delete quiz":
					window.close()
					q_del()
					teacher_home()


				if event == "Show own quiz":
					clearScreen()
					whole()

				if event == "Create question":
					window.close()
					add_ques()
					teacher_home()
				
				if event == "Edit question":
					window.close()
					edit_ques()
					teacher_home()

				if event == "Delete question":
					window.close()
					delete_question()
					teacher_home()

				if event == "Logout":
					clearScreen()
					window.close()
					teacher_out()
					menu()

	window.close()

#teacher_home()

def whole_student():
    pos = []
    q = []
    student = []
    with open("student.json", "r") as f_student:
        db_student = json.load(f_student)

    with open("quiz.json", "r") as f_quiz:
            db_quiz = json.load(f_quiz)


    for i in db_quiz["quiz_det"]:
            q.append(i["QuizID"])

    for i in db_student["students_det"]:
        student.append(i["name"])

    ind = student.index(nam[-1])

    quiz = (db_student["students_det"][ind]["quizzes"])

    for item in quiz:
            for i in range(0,len(q)):
                    if item in (db_quiz["quiz_det"][i]["QuizID"]):
                            pos.append(i)


    def stud_quiz():
        with open('quiz.json', 'r') as f_quiz:
                db_quiz = json.load(f_quiz)

        count = 0
        for quiz in db_quiz["quiz_det"]:
            count += 1

            c = []
            c.append(count)

        sg.theme('DarkBlue14')
        

        jj = pos


        data = []
        for x in jj:
            d = []
            d.append((db_quiz["quiz_det"][x]["Quizname"]))
            d.append((db_quiz["quiz_det"][x]["topic"]))
            d.append((db_quiz["quiz_det"][x]["QuizID"]))
            d.append((db_quiz["quiz_det"][x]["status"]))
            data.append(d)

        print (data)


        header_list = ['        Quiz Name        ','    Topic   ', '    Quiz ID    ', '    Status    ']



        layout = [
                    [sg.Table(values=data, headings=header_list,justification ="center",
                            enable_events=True, key='TABLE',
                            select_mode='extended',auto_size_columns=True)],
                    [sg.Button('Close', size=(20,1))],
                    [sg.Text(size=(40,1), key='-OUTPUT1-')]
                ]

        window = sg.Window('QUIZ LISTS', layout, size=(800,400))
        while True:
            event, values = window.Read()
            if event in ('Close', None): 
                break

            if event == 'TABLE':
                # window["-OUTPUT1-"].update("YOU HAVE NOT SELECT THE QUIZ YET!!")
                #jj = [0, 8, 9, 10]
                
                num = (values["TABLE"][0])  
                a = (db_quiz["quiz_det"][jj[num]]["QuizID"])
                


        

        window.close()

    stud_quiz()

   
        


def attempt():
    with open('quiz.json', 'r') as f_quiz:
            db_quiz = json.load(f_quiz)

    count = 0
    for quiz in db_quiz["attempted_det"]:
        count += 1

        c = []
        c.append(count)

    sg.theme('DarkBlue14')


    jj = (db_quiz["attempted_det"])

    data = []
    for x in jj:
        d = []
        d.append(x['Quizname'])
        d.append(x['topic'])
        d.append(x['QuizID'])
        d.append(x['totalquestion'])
        d.append(x['correctanswer'])
        data.append(d)

    print (data)


    header_list = ['Quiz Name','Topic', 'Quiz ID', 'Total question', 'Correct answer']



    layout = [
                [sg.Table(values=data, headings=header_list,  justification ="center",
                        enable_events=True, key='TABLE',
                        select_mode='extended',auto_size_columns=True)],
                [sg.Button('Close', size=(20,1))]
            ]

    window = sg.Window('ATTEMPTED QUIZ', layout, size=(800,400))
    while True:
        event, values = window.Read()
        if event in ('Close', None): 
            break

        if event == 'TABLE':
            print (values)
            print(values["TABLE"])
    window.close()



def student_out():

	sg.theme('DarkBlue14')

	layout = [[sg.Text('Are you sure want to log out? ')],
				[sg.Button('YES', size=(40,1), pad=(10,10))],
				[sg.Button('NO', size=(40,1), pad=(10,10))]]


	window = sg.Window('Confirmation', layout)

	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == 'NO':
					window.close()
					student_home()  # need to change to student later
					break

				if event == 'YES':
					window.close()
					menu()		
					break
				

	window.close()



def student_home():
	sg.theme('DarkBlue14')

	layout =[
		    [sg.Button('Show new quiz', size=(40,1), pad=(10,10))],
			[sg.Button('Show attempted quiz', size=(40,1), pad=(10,10))],
			[sg.Button('Logout', size=(40,1), pad=(10,10))]
			]


	window = sg.Window(f'Student :{nam[0]}', layout)


	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == "Show new quiz":
					whole_student()

				if event == "Show attempted quiz":
					attempt()


				if event == "Logout":
					clearScreen()
					window.close()
					student_out()

	window.close()





teach_name = []
def add_ques():

	with open ("teacher.json") as f_teacher :
	    teachers = json.load(f_teacher)

	for item in teachers["teachers_det"]:
		teach_name.append(item["name"])
		print("")

	ind = teach_name.index(nam1[-1])

	quizzes = (teachers["teachers_det"][ind]["quizzes"])

	sg.theme('DarkBlue14')

	layout = [[sg.Text('Enter the quiz ID : ')],
				[sg.Combo(quizzes, key="COMBO")],
				[sg.Button('Add question', size=(40,1), pad=(10,10))],
				[sg.Button('Back', size=(40,1), pad=(10,10))],
				[sg.Text(size=(40,1), key='-OUTPUT1-')],
				[sg.Text(size=(40,1), key='-OUTPUT2-')]]

	window = sg.Window('Question', layout)
	q_l = []         # to store quiz id in quiz.json
	id_l = []        # to store quiz id in question.json
	with open('quiz.json', 'r') as f_quiz:
		db_quiz = json.load(f_quiz)

	for i in db_quiz["quiz_det"]:
		q_l.append(i["QuizID"])


	with open('question.json', 'r') as f_ques:
		db_ques = json.load(f_ques)


	for j in db_ques["question_det"]:
		id_l.append(j["QuizID"])
		
	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == 'Back':
					window.close()
					teacher_home()

				if event == "Add question":
					if values["COMBO"] == '':
						window['-OUTPUT1-'].update(f"ERROR::")	
						window['-OUTPUT2-'].update(f"YOU HAVE NOT SELECT QUIZ YET")
					
					else:
						qu_l = []
						index = (q_l).index(values["COMBO"])
						x_dict = (db_quiz["quiz_det"][index])
						qu_l.append(x_dict)
						window.close()
						sg.theme('DarkBlue14')


						layout = [
							[sg.Frame(layout=[
							[sg.Input(key='-IN1-',  size=(60,1), pad=(10,10))],
							], title='Question text',title_color='white', font='Any12')],
							sg.Frame('Answer choices',[[
							sg.Input()],
							[sg.Input()],
							[sg.Input()],
							[sg.Input()]]),
							],[sg.Button("Choose the correct answer", size=(40,1), pad=(10,10))],[sg.Text(size=(40,1), key='-OUTPUT1-'),
							[sg.Text(size=(40,1), key='-OUTPUT2-')]]
							
						

						window = sg.Window(f'Add question to {x_dict["Quizname"]}', layout)


						while True:
									event, values = window.read()
									print(event, values)

									if event == None:
										break

									if event == "Choose the correct answer":
										if values["-IN1-"] == "" or values[0] == "" or values[1] == "":
											window["-OUTPUT1-"].update("YOU LEAVE SOME BLANK SPACE THERE.")
											window["-OUTPUT2-"].update("YOU MUST HAVE ATLEAST 2 ANSWER CHOICES.")

										elif values["-IN1-"] != "" or values[0] != "" or values[1] != "":
											window["-OUTPUT1-"].update("")
											ques = []
											v0 = []
											v1 = []
											v2 = []
											v3 = []
											ques.append(values["-IN1-"])
											v0.append(values[0])
											v1.append(values[1])
											v2.append(values[2])
											v3.append(values[3])
											window.close()

											def answer():
												sg.theme('DarkBlue14')
												layout = [ 
														[[sg.Radio(f'{v0[0]}', "RADIO1",  size=(10,1))], 
														[sg.Radio(f'{v1[0]}', "RADIO2")],
														[sg.Radio(f'{v2[0]}', "RADIO3")],
														[sg.Radio(f'{v3[0]}', "RADIO4")]],
														[sg.Button("Create question", size=(40,1), pad=(10,10))],
														[sg.Text("PLEASE SELECT ONE ANSWER ONLY")],
														[sg.Text(size=(40,1), key='-OUTPUT1-')]
														]
												window = sg.Window('Add question', layout)
												

												while True:
													event, values = window.read()
													print(event, values)

													

													if event == None:
														break

													if event == 'Create question':
														if values[0] == True and values[1] == False and values[2] == False and values[3] == False:	
															#window.close()		
															#return answer() please select only one answer
                                                            
															with open("question.json", "r") as f_ques:
																db_ques = json.load(f_ques)
															

															q_dict ={
																		"QuizID" : list(x_dict.values())[2],
																		"QuizNo" : f'{(id_l.count(list(x_dict.values())[2])+1)}',
																		"Question" : ques[0],
																		"Answers" : [v0[0], v1[0], v2[0], v3[0]],
																		"Correct" : [values[0], values[1], values[2], values[3]]
																		}

															
															window.close()
															db_ques['question_det'].append(q_dict)
															sg.theme('DarkBlue14')
															layout = [
																	[sg.Text("Your question had been created")],
																	[sg.Text("Press the 'Back' button to back home")],
																	[sg.Button("Back", size=(40,1), pad=(10,10))]
																	] 

															window = sg.Window('Add question', layout)
															while True:
																event, values = window.read()
																print(event, values)

																

																if event == None:
																	break


																if event == "Back":
																	window.close()
																	
															
															window.close()
															

														elif values[0] == False and values[1] == True and values[2] == False and values[3] == False:
															with open("question.json", "r") as f_ques:
																db_ques = json.load(f_ques)

															

															q_dict ={
																		"QuizID" : list(x_dict.values())[2],
																		"QuizNo" : f'{(id_l.count(list(x_dict.values())[2])+1)}',
																		"Question" : ques[0],
																		"Answers" : [v0[0], v1[0], v2[0], v3[0]],
																		"Correct" : [values[0], values[1], values[2], values[3]]
																		}
															window.close()
															db_ques['question_det'].append(q_dict)
															sg.theme('DarkBlue14')
															layout = [
																	[sg.Text("Your question had been created")],
																	[sg.Text("Press the 'Back' button to back home")],
																	[sg.Button("Back", size=(40,1), pad=(10,10))]
																	] 

															window = sg.Window('Add question', layout)
															while True:
																event, values = window.read()
																print(event, values)

																

																if event == None:
																	break


																if event == "Back":
																	window.close()
																	
															
															window.close()

														
														elif values[0] == False and values[1] == False and values[2] == True and values[3] == False:
															with open("question.json", "r") as f_ques:
																db_ques = json.load(f_ques)

															

															q_dict ={
																		"QuizID" : list(x_dict.values())[2],
																		"QuizNo" : f'{(id_l.count(list(x_dict.values())[2])+1)}',
																		"Question" : ques[0],
																		"Answers" : [v0[0], v1[0], v2[0], v3[0]],
																		"Correct" : [values[0], values[1], values[2], values[3]]
																		}
															window.close()
															db_ques['question_det'].append(q_dict)
															sg.theme('DarkBlue14')
															layout = [
																	[sg.Text("Your question had been created")],
																	[sg.Text("Press the 'Back' button to back home")],
																	[sg.Button("Back", size=(40,1), pad=(10,10))]
																	] 

															window = sg.Window('Add question', layout)
															while True:
																event, values = window.read()
																print(event, values)

																

																if event == None:
																	break


																if event == "Back":
																	window.close()
																	
															
															window.close()	

														elif values[0] == False and values[1] == False and values[2] == False and values[3] == True:
															with open("question.json", "r") as f_ques:
																db_ques = json.load(f_ques)

															

															q_dict ={
																		"QuizID" : list(x_dict.values())[2],
																		"QuizNo" : f'{(id_l.count(list(x_dict.values())[2])+1)}',
																		"Question" : ques[0],
																		"Answers" : [v0[0], v1[0], v2[0], v3[0]],
																		"Correct" : [values[0], values[1], values[2], values[3]]
																		}
															window.close()
															db_ques['question_det'].append(q_dict)
															sg.theme('DarkBlue14')
															layout = [
																	[sg.Text("Your question had been created")],
																	[sg.Text("Press the 'Back' button to back home")],
																	[sg.Button("Back", size=(40,1), pad=(10,10))]
																	] 

															window = sg.Window('Add question', layout)
															while True:
																event, values = window.read()
																print(event, values)

																

																if event == None:
																	break


																if event == "Back":
																	window.close()
																	
															
															window.close()


														else:
															# window["-OUTPUT1-"].update("PLEASE SELECT ONE ANSWER ONLY")
															window.close()
															return answer()										
															

												with open('question.json', 'w') as f_ques:
													json.dump(db_ques, f_ques, indent=4)

																									

												window.close()

											answer()	


						window.close()
						
	window.close()




#EDIT_QUES


# a = input("Enter Quiz ID : ")
# b = input("Enter Question No. : ")

# with open("question.json", "r") as f_ques:
# 	db_ques = json.load(f_ques)

# for i in db_ques["question_det"]:
# 	if i["QuizID"] == a and i["QuizNo"] == b:
# 		x_dict = {'QuizID': a, 'QuizNo': b, 'Question': i["Question"], 'Answers': i["Answers"], 'Correct': i["Correct"]}
# 		print("Yeay")
# 		print(i["QuizID"], i["QuizNo"])



# print(db_ques["question_det"].index(x_dict))
teach_name = []
def edit_ques():

	with open ("teacher.json") as f_teacher :
	    teachers = json.load(f_teacher)

	for item in teachers["teachers_det"]:
		teach_name.append(item["name"])
		print("")

	ind = teach_name.index(nam1[-1])

	quizzes = (teachers["teachers_det"][ind]["quizzes"])

	sg.theme('DarkBlue14')

	layout = [
			[sg.Text("Enter the Quiz ID : ")],
			[sg.Combo(quizzes, key="COMBO")],
			[sg.Text("Enter the Question No. : ")],
			[sg.Input(key='-IN2-')],
			[sg.Button('Edit question', size=(40,1), pad=(10,10))],
			[sg.Button('Back', size=(40,1), pad=(10,10))],
			[sg.Text(size=(40,1), key='-OUTPUT1-')],
			[sg.Text(size=(40,1), key='-OUTPUT2-')]
			]

	with open("question.json", "r") as f_ques:
		db_ques = json.load(f_ques)

	window = sg.Window(f'Edit question', layout)


	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break
				if event == "Back":
					window.close()
					teacher_home()

				if event == "Edit question":
					window["-OUTPUT1-"].update("ERROR: QUESTION NOT FOUND")
					for i in db_ques["question_det"]:
						if i["QuizID"] == values["COMBO"] and i["QuizNo"] == values["-IN2-"]:
							x_dict = {'QuizID': values["COMBO"],'QuizNo': values["-IN2-"], 'Question': i["Question"], 'Answers': i["Answers"], 'Correct': i["Correct"]}
							window.close()
							def ed():
								sg.theme('DarkBlue14')
								layout = [
										[sg.Frame(layout=[
										[sg.InputText(f"{list(x_dict.values())[2]}")],
										], title='Question text',title_color='white', font='Any12')],
										sg.Frame('Answer choices',[[
										sg.InputText(list(x_dict.values())[3][0])],
										[sg.InputText(list(x_dict.values())[3][1])],
										[sg.InputText(list(x_dict.values())[3][2])],
										[sg.InputText(list(x_dict.values())[3][3])]]),
										],[sg.Button("Choose the correct answer", size=(40,1), pad=(10,10))],[sg.Text(size=(40,1), key='-OUTPUT1-'),
										[sg.Text(size=(40,1), key='-OUTPUT2-')]]


								window = sg.Window(f'Edit question', layout)


								while True:
											event, values = window.read()
											print(event, values)

											if event == None:
												break

											if event == "Choose the correct answer":
												if values[0] == "" or values[1] == "" or values[2] == "":
													window["-OUTPUT1-"].update("YOU LEAVE SOME BLANK SPACE THERE.")
													window["-OUTPUT2-"].update("YOU MUST HAVE ATLEAST 2 ANSWER CHOICES.")
												elif values[0] != "" or values[1] != "" or values[2] != "":
													window["-OUTPUT1-"].update("")
													window["-OUTPUT2-"].update("")
													ques = []
													v1 = []
													v2 = []
													v3 = []
													v4 = []
													ques.append(values[0])
													v1.append(values[1])
													v2.append(values[2])
													v3.append(values[3])
													v4.append(values[4])
													window.close()
													def ans():
														sg.theme('DarkBlue14')
														layout = [
																[sg.Text(f'Question : {ques[0]}')],
																[[sg.Radio(f'{v1[0]}', "RADIO1",  size=(10,1))], 
																[sg.Radio(f'{v2[0]}', "RADIO2")],
																[sg.Radio(f'{v3[0]}', "RADIO3")],
																[sg.Radio(f'{v4[0]}', "RADIO4")]],
																[sg.Button("Edit question", size=(40,1), pad=(10,10))],
																[sg.Text("PLEASE SELECT ONE ANSWER ONLY")],
																[sg.Text(size=(40,1), key='-OUTPUT1-')]
																]
														window = sg.Window('Choose the answer', layout)

														while True:
															event, values = window.read()
															print(event, values)

														

															if event == None:
																break

															if event == "Edit question":
																if values[0] == True and values[1] == False and values[2] == False and values[3] == False:
																	with open("question.json", "r") as f_ques:
																		db_ques = json.load(f_ques)
																	index = (db_ques["question_det"]).index(x_dict)
																	db_ques['question_det'].remove(x_dict)
																	
																	

																	q_dict ={
																				"QuizID" : list(x_dict.values())[0],
																				"QuizNo" : list(x_dict.values())[1],
																				"Question" : ques[0],
																				"Answers" : [v1[0], v2[0], v3[0], v4[0]],
																				"Correct" : [values[0], values[1], values[2], values[3]]
																				}
																	
																	
																	window.close()
																	db_ques['question_det'].insert(index, q_dict)
																	sg.theme('DarkBlue14')
																	layout = [
																			[sg.Text("Your question had been EDITED")],
																			[sg.Text("Press the 'Back' button to back home")],
																			[sg.Button("Back", size=(40,1), pad=(10,10))]
																			] 

																	window = sg.Window('Add question', layout)
																	while True:
																		event, values = window.read()
																		print(event, values)

																		

																		if event == None:
																			break


																		if event == "Back":
																			window.close()
																			
																	
																	window.close()
																elif values[0] == False and values[1] == True and values[2] == False and values[3] == False:
																	with open("question.json", "r") as f_ques:
																		db_ques = json.load(f_ques)
																	index = (db_ques["question_det"]).index(x_dict)
																	db_ques['question_det'].remove(x_dict)
																	
																	

																	q_dict ={
																				"QuizID" : list(x_dict.values())[0],
																				"QuizNo" : list(x_dict.values())[1],
																				"Question" : ques[0],
																				"Answers" : [v1[0], v2[0], v3[0], v4[0]],
																				"Correct" : [values[0], values[1], values[2], values[3]]
																				}
																	
																	
																	window.close()
																	db_ques['question_det'].insert(index, q_dict)
																	sg.theme('DarkBlue14')
																	layout = [
																			[sg.Text("Your question had been EDITED")],
																			[sg.Text("Press the 'Back' button to back home")],
																			[sg.Button("Back", size=(40,1), pad=(10,10))]
																			] 

																	window = sg.Window('Add question', layout)
																	while True:
																		event, values = window.read()
																		print(event, values)

																		

																		if event == None:
																			break


																		if event == "Back":
																			window.close()
																			
																	
																	window.close()
																elif values[0] == False and values[1] == False and values[2] == True and values[3] == False:
																	with open("question.json", "r") as f_ques:
																		db_ques = json.load(f_ques)
																	index = (db_ques["question_det"]).index(x_dict)
																	db_ques['question_det'].remove(x_dict)
																	
																	

																	q_dict ={
																				"QuizID" : list(x_dict.values())[0],
																				"QuizNo" : list(x_dict.values())[1],
																				"Question" : ques[0],
																				"Answers" : [v1[0], v2[0], v3[0], v4[0]],
																				"Correct" : [values[0], values[1], values[2], values[3]]
																				}
																	
																	
																	window.close()
																	db_ques['question_det'].insert(index, q_dict)
																	sg.theme('DarkBlue14')
																	layout = [
																			[sg.Text("Your question had been EDITED")],
																			[sg.Text("Press the 'Back' button to back home")],
																			[sg.Button("Back", size=(40,1), pad=(10,10))]
																			] 

																	window = sg.Window('Add question', layout)
																	while True:
																		event, values = window.read()
																		print(event, values)

																		

																		if event == None:
																			break


																		if event == "Back":
																			window.close()
																		
																	
																	window.close()
																elif values[0] == False and values[1] == False and values[2] == False and values[3] == True:
																	with open("question.json", "r") as f_ques:
																		db_ques = json.load(f_ques)
																	index = (db_ques["question_det"]).index(x_dict)
																	db_ques['question_det'].remove(x_dict)
																	
																	

																	q_dict ={
																				"QuizID" : list(x_dict.values())[0],
																				"QuizNo" : list(x_dict.values())[1],
																				"Question" : ques[0],
																				"Answers" : [v1[0], v2[0], v3[0], v4[0]],
																				"Correct" : [values[0], values[1], values[2], values[3]]
																				}
																	
																	
																	window.close()
																	db_ques['question_det'].insert(index, q_dict)
																	sg.theme('DarkBlue14')
																	layout = [
																			[sg.Text("Your question had been EDITED")],
																			[sg.Text("Press the 'Back' button to back home")],
																			[sg.Button("Back", size=(40,1), pad=(10,10))]
																			] 

																	window = sg.Window('EDITED', layout)
																	while True:
																		event, values = window.read()
																		print(event, values)

																		

																		if event == None:
																			break


																		if event == "Back":
																			window.close()
																		
																	
																	window.close()
																else:
																	window.close()
																	return ans()



														with open('question.json', 'w') as f_ques:
															json.dump(db_ques, f_ques, indent=4)



														window.close()
													ans()
														
														
								window.close()

			
							ed()


	window.close()

teach_name= []
def delete_question():

	with open ("teacher.json") as f_teacher :
	    teachers = json.load(f_teacher)

	with open("question.json", "r") as f_ques:
		db_ques = json.load(f_ques)

	for item in teachers["teachers_det"]:
		teach_name.append(item["name"])
		print("")

	ind = teach_name.index(nam1[-1])

	quizzes = (teachers["teachers_det"][ind]["quizzes"])


	sg.theme('DarkBlue14')

	layout = [
			[sg.Text("Enter the Quiz ID : ")],
			[sg.Combo(quizzes, key="COMBO")],
			[sg.Text("Enter the Question No. : ")],
			[sg.Input(key='-IN2-')],
			[sg.Button('Delete question', size=(40,1), pad=(10,10))],
			[sg.Button('Back', size=(40,1), pad=(10,10))],
			[sg.Text(size=(40,1), key='-OUTPUT1-')],
			[sg.Text(size=(40,1), key='-OUTPUT2-')]
			]



	window = sg.Window(f'Delete question', layout)


	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break
				if event == "Back":
					window.close()
					teacher_home()

				if event == "Delete question":
					window["-OUTPUT1-"].update("QUESTION NOT FOUND")
					for i in db_ques["question_det"]:
						if i["QuizID"] == values["COMBO"] and i["QuizNo"] == values["-IN2-"]:
							d_dict = {'QuizID': values["COMBO"],'QuizNo': values["-IN2-"], 'Question': i["Question"], 'Answers': i["Answers"], 'Correct': i["Correct"]}
							window.close()
							def del_ques():
								sg.theme('DarkBlue14')

								layout = [
											[sg.Text(f'Question : {list(d_dict.values())[2]}')],
											[
											[sg.Radio(f'{list(d_dict.values())[3][0]}', "RADIO1", default=list(d_dict.values())[4][0],  size=(10,1))],
											[sg.Radio(f'{list(d_dict.values())[3][1]}', "RADIO1", default=list(d_dict.values())[4][1],  size=(10,1))],
											[sg.Radio(f'{list(d_dict.values())[3][2]}', "RADIO1", default=list(d_dict.values())[4][2],  size=(10,1))],
											[sg.Radio(f'{list(d_dict.values())[3][3]}', "RADIO1", default=list(d_dict.values())[4][3],  size=(10,1))]
											],
											[sg.Text('Are you sure want to DELETE this question? ')],
											[sg.Button('YES', size=(20,1), pad=(10,10)), sg.Button('NO', size=(20,1), pad=(10,10))]
										]


								window = sg.Window('Confirmation', layout)

								while True:
											event, values = window.read()
											print(event, values)

											if event == None:
												break

											if event == 'NO':
												window.close()
												teacher_home()  # need to change to student later
												break

											if event == 'YES':
												db_ques["question_det"].remove(d_dict)
												window.close()
												sg.theme('DarkBlue14')
												layout = [
														[sg.Text("This question had been DELETED")],
														[sg.Text("Press the 'Back' button to back home")],
														[sg.Button("Back", size=(40,1), pad=(10,10))]
														] 

												window = sg.Window('DELETE', layout)
												while True:
													event, values = window.read()
													print(event, values)

													

													if event == None:
														break


													if event == "Back":
														window.close()
														# the below code is to rearrange quiz no. in order
														id = []    #used to store all the quiz id in the question.json
														position = []      # to store the position of the quiz ID in the question_det
														num = []         # to arrange question number in order. like 1,2,3 ....


														for j in db_ques["question_det"]:
															id.append(j["QuizID"])


														for i in range(0,len(db_ques["question_det"])):        
															if db_ques["question_det"][i]["QuizID"] == list(d_dict.values())[0]:
																position.append(i)                             # the positions of the questions

														for j in range(1,id.count(list(d_dict.values())[0])+1):
															num.append(j)                                 #the order number

																				
														for i in range(0,len(position)):
															(db_ques["question_det"][position[i]]["QuizNo"]) = (f'{num[i]}')
													
														
												
												window.close()

								with open('question.json', 'w') as f_ques:
									json.dump(db_ques, f_ques, indent=4)

													
													
												

								window.close()

	del_ques()


	window.close()



nam = []
def log():
	sg.theme('DarkBlue14')


	layout = [[sg.Text('Enter your ID :')],
			[sg.Input(key='-IN1-')],
			[sg.Text('Enter your password :')],
			[sg.Input(key='-IN2-')],
			[sg.Button('Login', size=(40,1), pad=(10,10))],
			[sg.Text(size=(40,1), key='-OUTPUT-')]]

	window = sg.Window('Student Log In System', layout)

	# Read student.json and store it in 'db_student'
	with open('student.json', 'r') as f_student:
		db_student = json.load(f_student)
	while True:
		event, values = window.read()
		print(event, values)
		
		if event == None:
			window.close()
			menu()
		
		if event == 'Login':
			window['-OUTPUT-'].update(f"NAME NOT FOUND")
			# Update the "output" text element
			# to be the value of "input" element
			# window['-OUTPUT-'].update("Welcome" + " " +  values['-IN1-'])		
			for student in db_student["students_det"]:
				if values["-IN1-"] == student["ID"] and values["-IN2-"] == student["password"]:
					
					nam.append(student["name"])
					window['-OUTPUT-'].update(f"")
					window.close()
					student_home()


			
	window.close()


nam1 = []
def teacher_log():
	sg.theme('DarkBlue14')


	layout = [[sg.Text('Enter your ID :')],
			[sg.Input(key='-IN1-')],
			[sg.Text('Enter your password :')],
			[sg.Input(key='-IN2-')],
			[sg.Button('Login', size=(40,1), pad=(10,10))],
			[sg.Text(size=(40,1), key='-OUTPUT-')]]

	window = sg.Window('Teacher Log In System', layout)

	# Read student.json and store it in 'db_student'
	with open('teacher.json', 'r') as f_teacher:
		db_teacher = json.load(f_teacher)
	while True:
		event, values = window.read()
		print(event, values)
		
		if event == None:
			window.close()
			menu()
			
		
		if event == 'Login':
			window['-OUTPUT-'].update("NAME NOT FOUND. TRY AGAIN")

			for teacher in db_teacher["teachers_det"]:
				if values["-IN1-"] == teacher["ID"] and values["-IN2-"] == teacher["password"]:
					nam1.append(teacher["name"])
					window['-OUTPUT-'].update(f"")
					window.close()
					teacher_home()
					




		
	window.close()

nam2 = []
def admin_log():
	sg.theme('DarkBlue14')


	layout = [[sg.Text('Enter your ID :')],
			[sg.Input(key='-IN1-')],
			[sg.Text('Enter your password :')],
			[sg.Input(key='-IN2-')],
			[sg.Button('Login', size=(40,1), pad=(10,10))],
			[sg.Text(size=(40,1), key='-OUTPUT-')]]

	window = sg.Window('Administrator Log In System', layout)

	# Read student.json and store it in 'db_student'
	with open('teacher.json', 'r') as f_teacher:
		db_teacher = json.load(f_teacher)
	while True:
		event, values = window.read()
		print(event, values)
		
		if event == None:
			window.close()
			menu()
		
		if event == 'Login':
			window['-OUTPUT-'].update(f"NAME NOT FOUND NOT FOUND. TRY AGAIN")
	
			for teacher in db_teacher["admin_det"]:
				if values["-IN1-"] == teacher["ID"] and values["-IN2-"] == teacher["password"]:

					window['-OUTPUT-'].update(f"")
					window.close()
					nam2.append(teacher["name"])
					admin_home()
			

	window.close()


def student_home():
	sg.theme('DarkBlue14')

	layout =[
		    [sg.Button('Show new quiz', size=(40,1), pad=(10,10))],
			[sg.Button('Show attempted quiz', size=(40,1), pad=(10,10))],
			[sg.Button('Logout', size=(40,1), pad=(10,10))]
			]


	window = sg.Window(f'Student :{nam[-1]}', layout)


	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == "Show new quiz":
					clearScreen()
					whole_student()

				if event == "Show attempted quiz":
					clearScreen()
					attempt()


				if event == "Logout":
					clearScreen()
					window.close()
					student_out()

	window.close()


def teacher_home():
	sg.theme('DarkBlue14')

	layout =[
			[sg.Frame(layout=[
			[sg.Button('Create quiz', size=(20,1), pad=(10,10))],
			[sg.Button('Edit quiz', size=(20,1), pad=(10,10))],
			[sg.Button('Delete quiz', size=(20,1), pad=(10,10))],
			], title='Quiz',title_color='white', font='Any12'),
			sg.Frame(layout=[
			[sg.Button('Create question', size=(20,1), pad=(10,10))],
			[sg.Button('Edit question', size=(20,1), pad=(10,10))],
			[sg.Button('Delete question', size=(20,1), pad=(10,10))],
			],title='Question',title_color='white', font='Any12')],
			[sg.Button('Show own quiz', size=(20,1), pad=(120,10))],
			[sg.Button('Logout', size=(20,1), pad=(120,10))]
			]


	window = sg.Window(f'Teacher: {nam1[-1]}', layout)


	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == "Create quiz":
					window.close()
					q_create()
					teacher_home()

				if event == "Edit quiz":
					window.close()
					edits()
					teacher_home()

				if event == "Delete quiz":
					window.close()
					q_del()
					teacher_home()

				if event == "Show own quiz":
					clearScreen()
					whole()

				if event == "Create question":
					window.close()
					add_ques()
					teacher_home()
				
				if event == "Edit question":
					window.close()
					edit_ques()
					teacher_home()

				if event == "Delete question":
					window.close()
					delete_question()
					teacher_home()

				if event == "Logout":
					clearScreen()
					window.close()
					teacher_out()
					menu()

	window.close()



def admin_home():
	sg.theme('DarkBlue14')

	layout =[[sg.Button('View all teachers', size=(40,1), pad=(10,10))],
			[sg.Button('View all students', size=(40,1), pad=(10,10))],
			[sg.Button('Delete a teacher', size=(40,1), pad=(10,10))],
			[sg.Button('Delete a student', size=(40,1), pad=(10,10))],
			[sg.Button('Logout', size=(40,1), pad=(10,10))]]


	window = sg.Window(f'Administrator: {nam2[0]}', layout)


	while True:
				event, values = window.read()
				print(event, values)

				if event == None:
					break

				if event == "View all teachers":
					view_teacher()

				if event == "View all students":
					view_student()

				if event == "Delete a teacher":
					window.close()
					del_teacher()
					admin_home()
					

				if event == "Delete a student":
					window.close()
					del_student()
					admin_home()

				
				if event == "Logout":
					clearScreen
					window.close()
					adm_out()
					
					


	window.close()


def menu():
	sg.theme('DarkBlue14')

	layout = [[sg.Button('Teacher Login', size=(40,1), pad=(10,10))],
			[sg.Button('Student Login', size=(40,1), pad=(10,10))],
			[sg.Button('Administrator Login', size=(40,1), pad=(10,10))],
			[sg.Button('Teacher Registration', size=(40,1), pad=(10,10))],
			[sg.Button('Student Registration', size=(40,1), pad=(10,10))]]
			

	window = sg.Window('Main Menu', layout)

	while True:
			event, values = window.read()
			print(event, values)

			if event == None:
				exit()
			if event == 'Teacher Login':
				window.close()
				teacher_log()
				
			if event == 'Student Login':
				window.close()
				log()
			if event == "Administrator Login":
				window.close()
				admin_log()

			if event == "Teacher Registration":
				window.close()
				teach_reg()

			if event == "Student Registration":
				window.close()
				student_reg()

				

		

if __name__ == "__main__":
	menu()