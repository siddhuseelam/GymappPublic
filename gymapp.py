from flask import Flask, request, redirect,render_template,url_for,session,flash
import Gymlib
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired








app = Flask(__name__)

bootstrap = Bootstrap(app)


data = Gymlib.load_data("gym_data")
#Gymlib.add_week(data)
#Gymlib.add_group(data,1,"chest")
Gymlib.save_data(data)



@app.route('/')
def index():
    return render_template('index.html')




@app.route('/weeks')
def weeks():
    data = Gymlib.load_data("gym_data")
    return render_template('weeks.html',data = data)


@app.route("/week/<weeknum>")
def muscle_groups(weeknum):
    data = Gymlib.load_data("gym_data")
    muscle_group_list = Gymlib.get_muscle_group_list(data,str(weeknum))
    return render_template('muscle_groups.html',weeknum = weeknum,muscle_group_list = muscle_group_list)
    


@app.route('/week_actions', methods=['POST'])
def week_actions():

    action = request.form.get('action')
    if action == 'remove':
        data = Gymlib.load_data("gym_data")
        # Logic to determine the 'newest' week number

        latest_week_number = data['no_of_weeks']
        Gymlib.remove_week(data, latest_week_number)

        Gymlib.save_data(data)
        return redirect(url_for('weeks'))  # Redirect to update the view
    elif action == 'add_week':
        data = Gymlib.load_data("gym_data")
        Gymlib.add_week(data)
        Gymlib.save_data(data)
        return redirect(url_for('weeks'))
    
    elif action == 'duplicate':
        data = Gymlib.load_data("gym_data")
        Gymlib.new_week_duplicate(data)
        Gymlib.save_data(data)
        return redirect(url_for('weeks'))



@app.route('/add_muscle_group', methods=['POST'])
def add_muscle_group():
    data = Gymlib.load_data("gym_data")
    exercise = request.form.get('group')
    weeknum = request.form.get('weeknum')
    Gymlib.add_group(data,weeknum,exercise)
    Gymlib.save_data(data)
    return redirect(url_for("muscle_groups",weeknum = weeknum))

@app.route('/muscle_group_actions',methods = ['POST'])
def muscle_group_actions():
    data = Gymlib.load_data("gym_data")
    value = "remove not triggered"
    action = request.form.get('action')
    weeknum = request.form.get('weeknum')
    if action.split(",")[0] == "remove ":
        Gymlib.remove_muscle_group(data,str(weeknum),action.split(",")[1])
        Gymlib.save_data(data)
    return redirect(url_for("muscle_groups",weeknum = weeknum))

@app.route('/exercises/<weeknum>/<muscle_group>')
def exercises(weeknum,muscle_group):
    data = Gymlib.load_data("gym_data")
    exercise_list = Gymlib.get_exercise_list(data,str(weeknum),muscle_group)
    return render_template("exercises.html",weeknum = weeknum, muscle_group=muscle_group, exercise_list = exercise_list)

@app.route('/add_exercise', methods=['POST'])
def add_exercise():
    data = Gymlib.load_data("gym_data")
    exercise = request.form.get('exercise')
    weeknum = request.form.get('weeknum')
    muscle_group = request.form.get('muscle_group')
    Gymlib.add_exercise(data,weeknum,muscle_group,exercise)
    Gymlib.save_data(data)
    return redirect(url_for("exercises",weeknum = weeknum,muscle_group =muscle_group))

@app.route('/exercise_actions',methods = ['POST'])
def exercise_actions():
    data = Gymlib.load_data("gym_data")
    value = "remove not triggered"
    action = request.form.get('action')
    weeknum = request.form.get('weeknum')
    muscle_group = request.form.get('muscle_group')
    if action.split(",")[0] == "remove ":
        Gymlib.remove_exercise(data,str(weeknum),muscle_group,action.split(",")[1])
        Gymlib.save_data(data)
    return redirect(url_for("exercises",weeknum = weeknum,muscle_group =muscle_group))

@app.route("/<exercise>/<muscle_group>/<weeknum>")
def details(weeknum,muscle_group,exercise):
    data = Gymlib.load_data("gym_data")
    previous_weeknum = str(int(weeknum)-1)
    previous_data_existance = Gymlib.previous_data_existance(data,previous_weeknum,muscle_group,exercise,"set")
    return render_template("details.html",exercise = exercise,muscle_group = muscle_group,weeknum = weeknum,data = data,previous_weeknum = previous_weeknum,previous_data_existance = previous_data_existance)

@app.route("/save_details", methods = ['POST'])
def save_details():
    data = Gymlib.load_data("gym_data")
    exercise = request.form.get('exercise')
    weeknum = request.form.get('weeknum')
    muscle_group = request.form.get('muscle_group')
    weight = request.form.get('weight')
    set = request.form.get('set')
    rep = request.form.get('rep')
    if weight != "":
        Gymlib.update_weight(data,weeknum,muscle_group,exercise,weight)
    if set != "":
        Gymlib.update_set(data,weeknum,muscle_group,exercise,set)
    if rep != "":
        Gymlib.update_rep(data,weeknum,muscle_group,exercise,rep)
    Gymlib.save_data(data)

    return redirect(url_for("details",weeknum = weeknum,muscle_group =muscle_group,exercise = exercise))
    