from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from Forms import TutorRegisterForm, LoginForm, StudentRegisterForm, CreateQuestionForm, CreateExpensesForm, \
    CreateRentalForm, CreateScheduleForm, CreatePaymentForm, AdminForm, QuizForm
import shelve, Tutor, User, Student, Admin, Expenses, Salary, Rental, Question, Schedule, PaymentDetails, Quiz

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'Thisisasecretkey!'




@app.route('/')
def home():
    db1 = shelve.open('admin.db', 'c')
    db2 = shelve.open('user.db', 'c')
    admins_dict = {}
    users_dict = {}
    try:
        admins_dict = db1['Admins']
        users_dict = db2['Users']
    except:
        print("Error in retrieving tutor from Tutors.db.")
    admin = Admin.Admin('Long', 'meow', 'Long Fei', 'Chen')
    user = User.User('Long', 'meow')
    admins_dict[admin.get_adminId()] = admin
    users_dict['Long'] = user
    users_dict['Long'].set_userId(admin.get_adminId())
    db1['Admins'] = admins_dict
    db2['Users'] = users_dict

    db1.close()
    db2.close()

    db = shelve.open('quiz.db', 'c')
    quizs_dict = {}
    try:
        quizs_dict = db['Quizs']
    except:
        print("Error in retrieving tutor from Tutors.db.")
    question1 = Quiz.Quiz('1', 'Her thinking leans ____ democracy.', 'with', 'towards', 'for', 'None of these', 'b')
    quizs_dict['1'] = question1
    db['Quizs'] = quizs_dict

    question2 = Quiz.Quiz('2', 'He got too tired _____ over work.', 'because of', 'because off', 'on', 'for', 'a')
    quizs_dict['He got too tired _____ over work.'] = question2
    db['Quizs'] = quizs_dict

    question3 = Quiz.Quiz('3', '_____ his principles, he has to be very careful.', 'with regard of', 'with regard on', 'with regard to', 'None of these', 'c')
    quizs_dict['3'] = question3
    db['Quizs'] = quizs_dict

    question4 = Quiz.Quiz('4', 'Building has been built _____ the new plan.', 'accordance to', 'in accordance with', 'for', 'about', 'b')
    quizs_dict['4'] = question4
    db['Quizs'] = quizs_dict

    question5 = Quiz.Quiz('5', 'He crossed the broken bridge ____ warning.', 'in spite of', 'in spite off', 'on', 'about', 'a')
    quizs_dict['5'] = question5
    db['Quizs'] = quizs_dict

    question6 = Quiz.Quiz('6', 'The train ____ as fast as the bus.', 'went', 'running', 'moves', 'going', 'c')
    quizs_dict['6'] = question6
    db['Quizs'] = quizs_dict

    question7 = Quiz.Quiz('7', 'He was seen _____ to the school.', 'went', 'going', 'gone', 'go', 'b')
    quizs_dict['7'] = question7
    db['Quizs'] = quizs_dict

    question8 = Quiz.Quiz('8', 'She ____ in the sun for 1 hour.', 'sitting', 'has been sitting', 'has been sit', 'has sit', 'b')
    quizs_dict['8'] = question8
    db['Quizs'] = quizs_dict

    question9 = Quiz.Quiz('9', '____ it help you in your studies?', 'will', 'was', 'is', 'are', 'a')
    quizs_dict['9'] = question9
    db['Quizs'] = quizs_dict

    question10 = Quiz.Quiz('10', 'I ____ never seen such a picture before.', 'did', 'was', 'have', 'has', 'c')
    quizs_dict['10'] = question10
    db['Quizs'] = quizs_dict

    db.close()

    return render_template('home.html')


@app.route('/userHome')
def userHome():
    return render_template('userHome.html')


@app.route('/adminHome')
def adminHome():
    return render_template('adminHome.html')


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/quizDesc')
def quizDesc():
    return render_template('quizDesc.html')


@app.route('/quizDetail')
def quizDetail():
    quiz_form = QuizForm(request.form)
    ans = quiz_form.answer
    print(ans)
    quizs_dict = {}
    db = shelve.open('quiz.db', 'r')
    quizs_dict = db['Quizs']
    db.close()

    quizs_list = []
    for key in quizs_dict:
        quiz = quizs_dict.get(key)
        quizs_list.append(quiz)

    if quiz_form.validate():
        for key in quizs_dict:
            quiz = quizs_dict.get(key)


    return render_template('quizDetail.html', count=len(quizs_list), quizs_list=quizs_list, form=quiz_form)


@app.route('/quizResult')
def quizResult():
    return render_template('quizResult.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    pageNumber = 0
    if form.validate():
        id = form.username.data
        pas = form.password.data
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        users_list = []
        for key in users_dict:
            user = users_dict.get(key)
            users_list.append(user)
            if user.get_username() == id and user.get_password() == pas:
                if user.get_userId() >= 10000:
                    pageNumber = 1
                elif user.get_userId() >= 1000:
                    pageNumber = 2
                elif user.get_userId() >= 100:
                    pageNumber = 3



            if pageNumber == 0:
                print('Account Not exist')
            elif pageNumber == 1:
                return redirect(url_for('adminHome'))
            elif pageNumber == 3:
                return redirect(url_for('userHome'))
    return render_template('login.html', form=form)

@app.route('/adminRegister', methods=['GET', 'POST'])
def adminRegister():
    admin_form = AdminForm(request.form)
    if admin_form.validate():
        admins_dict = {}
        users_dict = {}
        db1 = shelve.open('admin.db', 'c')
        db2 = shelve.open('user.db', 'c')

        try:
            admins_dict = db1['Admins']
            users_dict = db2['Users']
        except:
            print("Error in retrieving tutor from Tutors.db.")

        admin = Admin.Admin(admin_form.username.data, admin_form.password.data, admin_form.firstname.data, admin_form.lastname.data)
        user = User.User(admin_form.username.data, admin_form.password.data)
        admins_dict[admin.get_adminId()] = admin
        users_dict[admin.get_username()] = user
        users_dict[admin.get_username()].set_userId(admin.get_adminId())
        db1['Admins'] = admins_dict
        db2['Users'] = users_dict

        db1.close()
        db2.close()
    return render_template('adminRegister.html', form=admin_form)


@app.route('/tutorRegister', methods=['GET', 'POST'])
def tutorRegister():
    tutor_register_form = TutorRegisterForm(request.form)
    if tutor_register_form.validate():
        tutors_dict = {}
        users_dict = {}
        db1 = shelve.open('tutor.db', 'c')
        db2 = shelve.open('user.db', 'c')

        try:
            tutors_dict = db1['Tutors']
            users_dict = db2['Users']
        except:
            print("Error in retrieving tutor from Tutors.db.")

        tutor = Tutor.Tutor(tutor_register_form.username.data, tutor_register_form.password.data,
                            tutor_register_form.firstname.data, tutor_register_form.lastname.data,
                            tutor_register_form.dateOfBirth.data, tutor_register_form.email.data,
                            tutor_register_form.gender.data, tutor_register_form.postalCode.data,
                            tutor_register_form.race.data, tutor_register_form.phone.data,
                            tutor_register_form.subject.data)
        user = User.User(tutor_register_form.username.data, tutor_register_form.password.data)
        tutors_dict[tutor.get_tutorId()] = tutor
        users_dict[tutor.get_username()] = user
        users_dict[tutor.get_username()].set_userId(tutor.get_tutorId())
        db1['Tutors'] = tutors_dict
        db2['Users'] = users_dict

        db1.close()
        db2.close()
    return render_template('tutorRegister.html', form=tutor_register_form)


@app.route('/studentRegister', methods=['GET', 'POST'])
def studentRegister():
    student_register_form = StudentRegisterForm(request.form)
    if student_register_form.validate():
        users_dict = {}
        students_dict = {}
        db1 = shelve.open('student.db', 'c')
        db2 = shelve.open('user.db', 'c')

        try:
            students_dict = db1['Students']
            users_dict = db2['Users']
        except:
            print("Error in retrieving Users from Users.db.")

        student = Student.Student(student_register_form.username.data, student_register_form.password.data,
                                  student_register_form.firstname.data, student_register_form.lastname.data,
                                  student_register_form.dateOfBirth.data, student_register_form.email.data,
                                  student_register_form.gender.data, student_register_form.postalCode.data,
                                  student_register_form.race.data, student_register_form.phone.data)
        user = User.User(student_register_form.username.data, student_register_form.password.data)
        students_dict[student.get_studentId()] = student
        users_dict[student.get_username()] = user
        users_dict[student.get_username()].set_userId(student.get_studentId())
        db1['Students'] = students_dict
        db2['Users'] = users_dict

        db1.close()
        db2.close()
    return render_template('studentRegister.html', form=student_register_form)


@app.route('/retrieveExpense')
def retrieve_Expense():
    expenses_dict = {}
    db = shelve.open('expense.db', 'r')
    expenses_dict = db['Expenses']
    db.close()

    expenses_list = []
    for key in expenses_dict:
        expense = expenses_dict.get(key)
        expenses_list.append(expense)

    return render_template('retrieveExpense.html', count=len(expenses_list), expenses_list=expenses_list)


@app.route('/createExpense', methods=['GET', 'POST'])
def create_expenses():
    create_expenses_form = CreateExpensesForm(request.form)
    if request.method == 'POST':
        expenses_dict = {}
        db = shelve.open('expense.db', 'c')

        try:
            expenses_dict = db['Expenses']
        except:
            print("Error in retrieving Customers from customer.db.")

        Expense = Expenses.Expenses(create_expenses_form.Invoice_code.data,
                                    create_expenses_form.date_rental.data,
                                    create_expenses_form.Payment_amount.data,
                                    create_expenses_form.Status.data)
        expenses_dict[Expense.get_id()] = Expense
        db['Expenses'] = expenses_dict

        db.close()

        return redirect(url_for('adminHome'))
    return render_template('createExpense.html', form=create_expenses_form)


@app.route('/updateExpense/<int:id>/', methods=['GET', 'POST'])
def update_Expense(id):
    update_expense_form = CreateExpensesForm(request.form)
    if request.method == 'POST':
        db = shelve.open('expense.db', 'w')
        expenses_dict = db['Expenses']

        Expense = expenses_dict.get(id)
        Expense.set_Invoice_Code(update_expense_form.Invoice_code.data)
        Expense.set_Status(update_expense_form.Status.data)
        Expense.set_Payment_Amount(update_expense_form.Payment_amount.data)

        db['Expenses'] = expenses_dict
        db.close()

        return redirect(url_for('retrieve_Expense'))
    else:
        expenses_dict = {}
        db = shelve.open('expense.db', 'r')
        expenses_dict = db['Expenses']
        db.close()

        expense = expenses_dict.get(id)
        update_expense_form.Invoice_code.data = expense.get_Invoice_Code()
        update_expense_form.Status.data = expense.get_Status()
        update_expense_form.Payment_amount.data = expense.get_Payment_Amount()

        return render_template('updateExpense.html', form=update_expense_form)


@app.route('/deleteExpense/<int:id>', methods=['POST'])
def delete_Expense(id):
    customers_dict = {}
    db = shelve.open('expense.db', 'w')
    expenses_dict = db['Expenses']

    expenses_dict.pop(id)

    db['Expenses'] = expenses_dict
    db.close()

    return redirect(url_for('retrieve_Expense'))


@app.route('/salary')
def salary():
    expenses_dict = {}
    db = shelve.open('expense.db', 'r')
    expenses_dict = db['Expenses']
    db.close()

    expenses_list = []
    for key in expenses_dict:
        expense = expenses_dict.get(key)
        expenses_list.append(expense)

    return render_template('salary.html', count=len(expenses_list), expenses_list=expenses_list)


@app.route('/rental')
def rental():
    expenses_dict = {}
    db = shelve.open('expense.db', 'r')
    expenses_dict = db['Expenses']
    db.close()

    expenses_list = []
    for key in expenses_dict:
        expense = expenses_dict.get(key)
        expenses_list.append(expense)

    return render_template('rental.html', count=len(expenses_list), expenses_list=expenses_list)


@app.route('/createQuestion', methods=['GET', 'POST'])
def create_question():
    create_question_form = CreateQuestionForm(request.form)
    if request.method == 'POST' and create_question_form.validate():
        questions_dict = {}
        db = shelve.open('question.db', 'c')

        try:
            questions_dict = db['Questions']
        except:
            print("Error in retrieving Questions from question.db.")

        question = Question.Question(create_question_form.first_name.data, create_question_form.last_name.data,
                                     create_question_form.message.data, create_question_form.date.data, )
        questions_dict[question.get_question_id()] = question
        db['Questions'] = questions_dict

        db.close()

        return redirect(url_for('retrieve_questions'))
    return render_template('createQuestion.html', form=create_question_form)


@app.route('/createSchedule', methods=['GET', 'POST'])
def create_schedule():
    create_schedule_form = CreateScheduleForm(request.form)
    if request.method == 'POST' and create_schedule_form.validate():
        schedules_dict = {}
        db = shelve.open('schedule.db', 'c')

        try:
            schedules_dict = db['Schedules']
        except:
            print("Error in retrieving Schedules from schedule.db.")

        schedule = Schedule.Schedule(create_schedule_form.tutor_name.data, create_schedule_form.subject.data,
                                     create_schedule_form.level.data, create_schedule_form.date.data,
                                     create_schedule_form.time_slot.data)
        schedules_dict[schedule.get_schedule_id()] = schedule
        db['Schedules'] = schedules_dict

        db.close()

        return redirect(url_for('retrieve_schedules'))
    return render_template('createSchedule.html', form=create_schedule_form)


@app.route('/retrieveSchedules')
def retrieve_schedules():
    schedules_dict = {}
    db = shelve.open('schedule.db', 'r')
    schedules_dict = db['Schedules']
    db.close()

    schedules_list = []
    for key in schedules_dict:
        schedule = schedules_dict.get(key)
        schedules_list.append(schedule)

    return render_template('retrieveSchedules.html', count=len(schedules_list), schedules_list=schedules_list)


@app.route('/updateSchedule/<int:id>/', methods=['GET', 'POST'])
def update_schedule(id):
    update_schedule_form = CreateScheduleForm(request.form)
    if request.method == 'POST' and update_schedule_form.validate():
        schedules_dict = {}
        db = shelve.open('schedule.db', 'w')
        schedules_dict = db['Schedules']

        schedule = schedules_dict.get(id)
        update_schedule_form.tutor_name.data = schedule.get_tutor_name()
        update_schedule_form.subject.data = schedule.get_subject()
        update_schedule_form.level.data = schedule.get_level()
        update_schedule_form.date.data = schedule.get_date()
        update_schedule_form.time_slot.data = schedule.get_time_slot()

        db['Schedules'] = schedules_dict
        db.close()

        return redirect(url_for('retrieve_schedules'))
    else:
        schedules_dict = {}
        db = shelve.open('schedule.db', 'r')
        schedules_dict = db['Schedules']
        db.close()

        schedule = schedules_dict.get(id)
        update_schedule_form.tutor_name.data = schedule.get_tutor_name()
        update_schedule_form.subject.data = schedule.get_subject()
        update_schedule_form.level.data = schedule.get_level()
        update_schedule_form.date.data = schedule.get_date()
        update_schedule_form.time_slot.data = schedule.get_time_slot()

        return render_template('updateSchedule.html', form=update_schedule_form)


@app.route('/deleteSchedule/<int:id>', methods=['POST'])
def delete_schedule(id):
    schedules_dict = {}
    db = shelve.open('schedule.db', 'w')
    schedules_dict = db['Schedules']

    schedules_dict.pop(id)

    db['Schedules'] = schedules_dict
    db.close()

    return redirect(url_for('retrieve_schedules'))


@app.route('/retrieveQuestions')
def retrieve_questions():
    questions_dict = {}
    db = shelve.open('question.db', 'r')
    questions_dict = db['Questions']
    db.close()

    questions_list = []
    for key in questions_dict:
        question = questions_dict.get(key)
        questions_list.append(question)

    return render_template('retrieveQuestions.html', count=len(questions_list), questions_list=questions_list)


@app.route('/updateQuestions/<int:id>/', methods=['GET', 'POST'])
def update_question(id):
    update_question_form = CreateQuestionForm(request.form)
    if request.method == 'POST' and update_question_form.validate():
        questions_dict = {}
        db = shelve.open('question.db', 'w')
        questions_dict = db['Questions']

        question = questions_dict.get(id)
        question.set_message(update_question_form.message.data)
        question.set_date(update_question_form.date.data)

        db['Questions'] = questions_dict
        db.close()

        return redirect(url_for('retrieve_questions'))
    else:
        questions_dict = {}
        db = shelve.open('question.db', 'r')
        questions_dict = db['Questions']
        db.close()

        question = questions_dict.get(id)
        update_question_form.message.data = question.get_message()
        update_question_form.date = question.get_date()

        return render_template('updateQuestions.html', form=update_question_form)


@app.route('/deleteQuestion/<int:id>', methods=['POST'])
def delete_question(id):
    questions_dict = {}
    db = shelve.open('question.db', 'w')
    questions_dict = db['Questions']

    questions_dict.pop(id)

    db['Questions'] = questions_dict
    db.close()

    return redirect(url_for('retrieve_questions'))


@app.route('/programmes')
def programmes():
    return render_template('programmes.html')


@app.route('/createPayment', methods=['GET', 'POST'])
def create_payment():
    create_payment_form = CreatePaymentForm(request.form)
    if request.method == 'POST' and create_payment_form.validate():
        payment_dict = {}
        db = shelve.open('payment.db', 'c')

        try:
            payment_dict = db['Payment']
        except:
            print("Error in retrieving Users from payment.db.")

        payment = PaymentDetails.Payment(create_payment_form.username.data, create_payment_form.password.data,
                                         create_payment_form.account_number.data, create_payment_form.account_name.data,
                                         create_payment_form.security.data, create_payment_form.expiration_month.data,
                                         create_payment_form.expiration_year.data)
        payment_dict[payment.get_payment_id()] = payment
        db['Payment'] = payment_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('createPayment.html', form=create_payment_form)


@app.route('/retrievePayment')
def retrieve_payment():
    payment_dict = {}
    db = shelve.open('payment.db', 'r')
    payment_dict = db['Payments']
    db.close()

    customers_list = []
    for key in payment_dict:
        customer = payment_dict.get(key)
        customers_list.append(customer)

    return render_template('retrieveCustomers.html', count=len(customers_list), customers_list=customers_list)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run()
