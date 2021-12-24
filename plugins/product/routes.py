from flask import Blueprint, jsonify, request

product_plugin = Blueprint(name="product", import_name=__name__)

@product_plugin.route('/', methods=['GET'])
def get_one():
    output = {"msg": "In the Get One endpoint from the product plugin."}
    return jsonify(output)

@product_plugin.route('/all', methods=['GET'])
def get_all():
    output = {"msg": "In the Get All endpoint from the product plugin."}
    return jsonify(output)