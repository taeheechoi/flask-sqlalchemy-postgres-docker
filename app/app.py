import json

from flask import request

from . import create_app, database
from .models import Contacts, db

app = create_app()

@app.route('/', methods=['GET'])
def fetch():
    contacts = Contacts.query.all()
    all_contacts = []
    for contact in contacts:
        new_contact =  {
                "id": contact.id,
                "name": contact.name,
                "title": contact.title,
                "phone": contact.phone
            }
        all_contacts.append(new_contact)
    return json.dumps(all_contacts), 200

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json(force=True) 
    name = data['name']
    title = data['title']
    phone = data['phone']
    # contact = Contacts(name=name, title=title, phone=phone)
    # db.session.add(contact)
    # db.session.commit()
    database.add_instance(Contacts, name=name, title=title, phone=phone)
    return json.dumps("Added"), 200

@app.route('/edit/<contact_id>', methods=['PUT'])
def edit(contact_id):
    data = request.get_json(force=True)
    name = data['name']
    title = data['title']
    phone = data['phone']
    # contact_to_update = Contacts.query.filter_by(id=contact_id).all()[0]
    # contact_to_update.name = name
    # contact_to_update.title = title
    # contact_to_update.phone = phone
    # db.session.commit()
    database.edit_instance(Contacts, id=contact_id, name=name, title=title, phone=phone)
    return json.dumps('Edited'), 200

@app.route('/delete/<contact_id>', methods=['DELETE'])
def remove(contact_id):
    # Contacts.query.filter_by(id=contact_id).delete()
    # db.session.commit()
    database.delete_instance(Contacts, id=contact_id)
    return json.dumps("Deleted"), 200
