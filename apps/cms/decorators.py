from flask import session, redirect, render_template, url_for
from functools import wraps
from config import CMS_USER_ID
from flask import g, render_template
from .models import CMSPermission


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):

        if CMS_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('cms.login'))

    return inner


def permission_required(permission):
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            user = g.cms_user
            if user.has_permission(permission):
                return func(*args, **kwargs)
            else:
                print("权限不够")
                return render_template("cms/cms_index.html")

        return inner

    return outer
