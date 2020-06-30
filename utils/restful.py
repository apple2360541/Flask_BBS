from flask import jsonify


class HttpCode(object):
    ok = 200
    not_found = 400
    unauth_error = 401
    server_error = 500


def restful_result(code=HttpCode.ok, msg="ok", data=None):
    return jsonify(code=code, msg=msg, data=data)


def success(msg="成功", data=None):
    return jsonify(code=HttpCode.ok, msg=msg, data=data)


def un_authorized(msg="请登录"):
    return jsonify(code=HttpCode.unauth_error, msg=msg, data=None)


def params_error(msg="参数异常"):
    return jsonify(code=HttpCode.not_found, msg=msg, data=None)


def server_error(msg="服务器异常"):
    return jsonify(code=HttpCode.server_error, msg=msg)
