from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import Addowner
from flask_login import login_user,login_required,logout_user

owner_blueprint = Blueprint('owners',__name__,template_folder='templates/owners')

@owner_blueprint.route('/add',methods=['GET','POST'])
@login_required
def add():

    form = Addowner()

    if form.validate_on_submit():
        name = form.name.data
        puppyid = form.puppy_id.data
        owner_details = Owner(name,puppyid)
        db.session.add(owner_details)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('add_owner.html',form=form)