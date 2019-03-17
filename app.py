from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Asset
from forms import ContactForm, AssetSearchForm

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
    return redirect(url_for('assets'))


@app.route("/new_asset", methods=('GET', 'POST'))
def new_asset():
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
            return redirect(url_for('assets'))
        except:
            db.session.rollback()
            flash('Error generating asset.', 'danger')

    return render_template('web/new_asset.html', form=form)


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


def query_db(search_str, search_field):
    if search_field == 'name':
        results = Asset.query.filter(Asset.name.contains(
            search_str)).order_by(Asset.name).all()
    elif search_field == 'emp_no':
        results = Asset.query.filter(Asset.emp_no.contains(
            search_str)).order_by(Asset.emp_no).all()
    elif search_field == 'location':
        results = Asset.query.filter(Asset.location.contains(
            search_str)).order_by(Asset.location).all()
    elif search_field == 'sl_no_1':
        results = Asset.query.filter(Asset.sl_no_1.contains(
            search_str)).order_by(Asset.sl_no_1).all()
    elif search_field == 'model':
        results = Asset.query.filter(Asset.model.contains(
            search_str)).order_by(Asset.model).all()
    elif search_field == 'make':
        results = Asset.query.filter(Asset.make.contains(
            search_str)).order_by(Asset.make).all()
    elif search_field == 'tel_tvm':
        results = Asset.query.filter(Asset.tel_tvm.contains(
            search_str)).order_by(Asset.tel_tvm).all()
    elif search_field == 'test_pc':
        results = Asset.query.filter(Asset.test_pc.contains(
            search_str)).order_by(Asset.test_pc).all()
    elif search_field == 'processor':
        results = Asset.query.filter(Asset.processor.contains(
            search_str)).order_by(Asset.processor).all()
    elif search_field == 'ram':
        results = Asset.query.filter(Asset.ram.contains(
            search_str)).order_by(Asset.ram).all()
    elif search_field == 'hdd':
        results = Asset.query.filter(Asset.hdd.contains(
            search_str)).order_by(Asset.hdd).all()
    elif search_field == 'asset_no':
        results = Asset.query.filter(Asset.asset_no.contains(
            search_str)).order_by(Asset.asset_no).all()
    elif search_field == 'project_name':
        results = Asset.query.filter(Asset.project_name.contains(
            search_str)).order_by(Asset.project_name).all()
    elif search_field == 'won_no':
        results = Asset.query.filter(Asset.won_no.contains(
            search_str)).order_by(Asset.won_no).all()
    else:
        results = None
    return results


@app.route("/assets", methods=['GET', 'POST'])
def assets():
    '''
    Show alls assets
    '''
    search_form = AssetSearchForm(request.form)
    search_str = request.args.get('search')
    search_field = request.args.get('select')
    if search_str:
        results = query_db(search_str, search_field)
        flash('results found: {}'.format(len(results)))
        return render_template('web/assets.html', rows=results, search_form=search_form)
    else:
        # If 'search' field is empty, return all results
        results = Asset.query.order_by(Asset.name).all()
    return render_template('web/assets.html', rows=results, search_form=search_form)


@app.route("/contacts/delete", methods=('POST',))
def assets_delete():
    '''
    Delete asset
    '''
    try:
        result_row = Asset.query.filter_by(id=request.form['id']).first()
        db.session.delete(result_row)
        db.session.commit()
        flash('Deleted successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error deleting  asset.', 'danger')

    return redirect(url_for('assets'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
