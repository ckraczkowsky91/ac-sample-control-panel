from . import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.model import BaseModelView
from .models import AsylumSeeker, Entity, Users
from flask_admin.model.template import EndpointLinkRowAction, LinkRowAction
from wtforms.validators import DataRequired

# define views
class UnverifiedEntities(ModelView):
    can_create = False
    can_delete = False
    can_edit = True
    # Adds a read-only Detail view and an icon to the List view
    can_view_details = True
    column_list = ['id', 'name', 'is_verified']
    column_searchable_list = ['id', 'name']
    create_template = 'create.html'
    form_excluded_columns = ['is_searchable', 'marked_deleted', 'date_created',
     'date_updated_ac', 'date_updated_org', 'is_verified', 'last_verified', 'rating',
     'is_closed', 'attachement', 'attachements', 'comments', 'emails', 'entity_languages', 'entity_properties',
     'entity_tags', 'service_providers', 'user_favorites', 'schedules']
    form_args = dict(name=dict(label='Org Name', validators=[DataRequired()]))

    def get_query(self):
        return self.session.query(self.model).filter(self.model.is_verified==None)

admin = Admin(app, name='Control Panel', template_mode='bootstrap3')

# add views
admin.add_view(UnverifiedEntities(Entity, db.session))

from . import routes
