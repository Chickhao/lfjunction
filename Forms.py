from wtforms import Form, StringField, PasswordField, BooleanField, DateField, RadioField, validators, SelectField, \
    IntegerField
from wtforms.validators import InputRequired, Email, Length, NumberRange


class QuizForm(Form):
    answer = SelectField(label='Answer: ', choices=[('a', '(a)'),
                                                                 ('chinese', 'Chinese'),
                                                                 ('malay', 'Malay'),
                                                                 ('indian', 'Indian')])


class LoginForm(Form):
    username = StringField('Username: ', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password: ', validators=[InputRequired(), Length(min=4, max=80)])


class AdminForm(Form):
    firstname = StringField('Firstname: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    username = StringField('Username: ', [validators.Length(min=4, max=150), validators.DataRequired()])
    lastname = StringField('Lastname: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = StringField('Password: ', [validators.Length(min=4, max=150), validators.DataRequired()])


class TutorRegisterForm(Form):
    firstname = StringField('Firstname: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    username = StringField('Username: ', [validators.Length(min=4, max=150), validators.DataRequired()])
    lastname = StringField('Lastname: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = StringField('Password: ', [validators.Length(min=8, max=150), validators.DataRequired()])
    dateOfBirth = DateField('Date Of Birth: ', format='%Y-%m-%d')
    email = StringField('Email: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender: ', choices=[('female', 'Female'), ('male', 'Male')])
    postalCode = StringField('Postal Code: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    race = SelectField('Race: ', choices=[('chinese', 'Chinese'), ('malay', 'Malay'), ('indian', 'Indian')])
    phone = StringField('Phone Number: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    subject = SelectField(label='Subject Preference: ', choices=[('english', 'English'),
                                                                 ('chinese', 'Chinese'),
                                                                 ('malay', 'Malay'),
                                                                 ('indian', 'Indian')])


class StudentRegisterForm(Form):
    firstname = StringField('Firstname: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    username = StringField('Username: ', [validators.Length(min=4, max=150), validators.DataRequired()])
    lastname = StringField('Lastname: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = StringField('Password: ', [validators.Length(min=8, max=150), validators.DataRequired()])
    dateOfBirth = DateField('Date Of Birth: ', format='%Y-%m-%d')
    email = StringField('Email: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender: ', choices=[('female', 'Female'), ('male', 'Male')])
    postalCode = StringField('Postal Code: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    race = SelectField('Race: ', choices=[('chinese', 'Chinese'), ('malay', 'Malay'), ('indian', 'Indian')])
    phone = StringField('Phone Number: ', [validators.Length(min=8, max=8), validators.DataRequired()])


class CreateExpensesForm(Form):
    Invoice_code = IntegerField('Invoice code', [validators.Length(min=1, max=4), validators.DataRequired()])
    Payment_amount = IntegerField('Payment amount', [validators.Length(min=1, max=150), validators.DataRequired()])
    date_rental = DateField('Date of rental', format='%Y-%m-%d')
    Status = RadioField('Status', choices=[('U', 'Upcoming'), ('S', 'Due'), ('P', 'Paid')])


class CreateRentalForm(Form):
    Invoice_code = IntegerField('Invoice code', [validators.Length(min=1, max=4), validators.DataRequired()])
    Payment_amount = IntegerField('Payment amount', [validators.Length(min=1, max=150), validators.DataRequired()])
    date_rental = DateField('Date of rental', format='%Y-%m-%d')
    Status = RadioField('Status', choices=[('U', 'Upcoming'), ('S', 'Due'), ('P', 'Paid')])


class CreateQuestionForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    message = StringField('What is Your Message?', [validators.Length(min=1, max=150), validators.DataRequired()])
    date = DateField('Date', format='%Y-%m-%d')


class CreateScheduleForm(Form):
    tutor_name = StringField('Tutor Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    subject = SelectField('Subject', [validators.DataRequired()],
                          choices=[('', 'Select'), ('Math', 'Mathematics'), ('EL', 'English Language'),
                                   ('MTL', 'Mother Tongue Language'), ('Sci', 'Sciences')], default='')
    level = SelectField('Level', [validators.DataRequired()],
                        choices=[('', 'Select'), ('Pri', 'Primary School'), ('Sec', 'Secondary School'),
                                 ('JC', 'Junior College')], default='')
    date = DateField('Date', format='%Y-%m-%d')
    time_slot = RadioField('Time Slot',
                           choices=[('Morn', '10am to 12pm'), ('Aft', '1pm to 3pm'), ('Eve', '4pm to 6pm')], default='')


class CreatePaymentForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = StringField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])
    account_number = StringField('Account Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    account_name = StringField('Account Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    security = StringField('Security Code', [validators.Length(min=1, max=150), validators.DataRequired()])
    expiration_month = SelectField('Month',
                                   choices=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                                            'Dec'], default='Jan')
    expiration_year = SelectField('Year', choices=['2022', '2023', '2024', '2025', '2026'], default='2022')
