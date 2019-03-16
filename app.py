from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Asset
from forms import ContactForm

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'
app.config['DEBUG'] = False

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///it_store.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/it_store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def index():
    '''
    Home page
    '''
    return redirect(url_for('contacts'))


@app.route("/new_contact", methods=('GET', 'POST'))
def new_contact():
    '''
    Create new asset
    '''
    form = ContactForm()
    if form.validate_on_submit():
        my_contact = Asset()
        form.populate_obj(my_contact)
        db.session.add(my_contact)
        try:
            db.session.commit()
            # User info
            flash('Asset created correctly', 'success')
            return redirect(url_for('contacts'))
        except:
            db.session.rollback()
            flash('Error generating asset.', 'danger')

    return render_template('web/new_contact.html', form=form)


@app.route("/edit_contact/<id>", methods=('GET', 'POST'))
def edit_contact(id):
    '''
    Edit asset

    :param id: Id from asset
    '''
    my_contact = Asset.query.filter_by(id=id).first()
    form = ContactForm(obj=my_contact)
    if form.validate_on_submit():
        try:
            # Update asset
            form.populate_obj(my_contact)
            db.session.add(my_contact)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update asset.', 'danger')
    return render_template(
        'web/edit_contact.html',
        form=form)


@app.route("/contacts")
def contacts():
    '''
    Show alls assets
    '''
    rows = Asset.query.order_by(Asset.name).all()
    return render_template('web/contacts.html', rows=rows)


@app.route("/search")
def search():
    '''
    Search
    '''
    name_search = request.args.get('name')
    rows = Asset.query.filter(
        Asset.name.contains(name_search)
    ).order_by(Asset.name).all()
    print(rows)
    return render_template('web/contacts.html', rows=rows)


@app.route("/contacts/delete", methods=('POST',))
def contacts_delete():
    '''
    Delete asset
    '''
    try:
        mi_contacto = Asset.query.filter_by(id=request.form['id']).first()
        db.session.delete(mi_contacto)
        db.session.commit()
        flash('Deleted successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error deleting  asset.', 'danger')

    return redirect(url_for('contacts'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
