import uuid
from . import app, db
from flask import render_template, request
from .models import Entity, EntityLanguage, Email, Address

# create routing for index page
@app.route('/')
def index():
    return render_template('index.html')

# create routing for form on index page
@app.route('/post', methods=['POST'])
def submit_new_resource():
    if request.method=='POST':
        entity_id = uuid.uuid4()
        name = request.form['orgname']
        website = request.form['orgwebsite']
        phone = request.form['orgphone']
        is_verified = None
        entity_data = Entity(entity_id, name, website, phone, is_verified)

        entity_language_id = uuid.uuid4()
        description = request.form['orgdescription']
        misc_data = EntityLanguage(entity_id, entity_language_id, description)

        email_id = uuid.uuid4()
        email = request.form['orgemail']
        email_data = Email(email_id, email, entity_id)

        address_id = uuid.uuid4()
        postal_area = request.form['orgzip']
        address_data = Address(address_id, postal_area)

        db.session.add(entity_data)
        db.session.add(misc_data)
        db.session.add(email_data)
        db.session.add(address_data)
        db.session.commit()
    return render_template('index.html')
