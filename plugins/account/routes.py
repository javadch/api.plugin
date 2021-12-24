from flask import Blueprint, jsonify, request

account_plugin = Blueprint(name="account", import_name=__name__)

@account_plugin.route('/acc', methods=['GET'])
def acc():
    output = {"msg": "I'm the ACC endpoint from the account plugin."}
    return jsonify(output)

@account_plugin.route('/plus', methods=['GET'])
def plus():
    data = request.get_json()
    result = 10
    output = {"msg": f"Your result is: '{result}'"}
    return jsonify(output)