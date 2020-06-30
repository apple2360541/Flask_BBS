from .views import cms
from flask import g, session
import config
from .models import CMSUser, CMSPermission


@cms.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        print(user_id)
        user = CMSUser.query.get(user_id)
        print(user)
        if user:
            g.cms_user = user


@cms.context_processor
def cms_context_processor():
    return {"CMSPermission": CMSPermission}

