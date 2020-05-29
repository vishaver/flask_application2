from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import Add,Del
from flask_login import login_user,login_required,logout_user



puppies_blueprint = Blueprint('puppies',__name__,template_folder='templates/puppies')

@puppies_blueprint.route('/add',methods=['GET','POST'])
@login_required
def add():

    form = Add()
    if form.validate_on_submit():
        name = form.name.data
        new_puppy = Puppy(name)
        db.session.add(new_puppy)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('add.html',form=form)

@puppies_blueprint.route('/list')
@login_required
def list():
    puppy_list = Puppy.query.all()
    return render_template('list.html',puppies=puppy_list)

@puppies_blueprint.route('/delete',methods=['GET','POST'])
@login_required
def delete():

    form = Del()

    if form.validate_on_submit():
        id_num = form.id.data
        id_to_del = Puppy.query.get(id_num)
        db.session.delete(id_to_del)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('delete.html',form=form)