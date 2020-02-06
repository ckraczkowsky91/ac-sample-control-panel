from . import app
from .models import db, security
from flask import url_for
from flask_admin import Admin, helpers
from flask_admin.contrib.sqla import ModelView
from flask_admin.model import BaseModelView
from flask_admin.model.form import InlineFormAdmin
from .models import AsylumSeeker, Entity, EntityLanguage, Users
from flask_admin.model.template import EndpointLinkRowAction, LinkRowAction
from flask_security import current_user
from wtforms import Form, IntegerField, StringField, TextField

# define views

class UnverifiedEntities(ModelView):
    inline_models = [(EntityLanguage, dict(form_columns=['id', 'description']))]
    can_create = False
    can_delete = False
    can_edit = True
    # Adds a read-only Detail view and an icon to the List view
    can_view_details = True
    column_list = ['id', 'name', 'entity_languages', 'is_verified']
    column_labels = {
        'entity_languages': 'Description'
        }
    column_searchable_list = ['id', 'name']
    form_columns = ('id', 'name', 'website', 'entity_languages')
    form_widget_args = {
        'id': {
            'readonly': True
        }
    }
    list_template = 'custom_list.html'

    def get_query(self):
        return self.session.query(self.model).filter(self.model.is_verified==None)

    def is_accessible(self):
        return(current_user.is_active and
                current_user.is_authenticated)

class EntityForm(Form):
    id = IntegerField('id')
    name = TextField('name')
    entity_languages = StringField('description')


class EntityView(ModelView):
    column_list = ('id', 'name', 'entity_languages')
    column_labels = {
        'id': 'Id',
        'name': 'Name',
        'entity_languages': 'Description'
    }
    column_default_sort = 'name'
    form = EntityForm


admin = Admin(app, base_template='my_master.html', name='Control Panel', template_mode='bootstrap3')

# add views
admin.add_view(UnverifiedEntities(Entity, db.session, category='Submissions', menu_icon_type='glyph', menu_icon_value='glyphicon-home', ))
# admin.add_view(EntityView(Entity, db.session, category='Submissions'))

# Added a context processor to our instance of Flask-Security to put Flask-Admin views in context
# Need this to override the default login and register views
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template = admin.base_template,
        admin_view = admin.index_view,
        get_url = url_for,
        h = helpers
    )

from . import routes
