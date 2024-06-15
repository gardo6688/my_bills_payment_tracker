from flask import Blueprint, request, jsonify
from models import Biller, PaymentActivity, PaymentItem
from config import db
from bson.objectid import ObjectId

billers_bp = Blueprint('billers', __name__)

@billers_bp.route('/billers', methods=['POST'])
def create_biller():
    data = request.get_json()
    payment_activities = [PaymentActivity([PaymentItem(**item) 
                                           for item in 
                                           activity['payment_items']], 
                                           activity['payment_date'], 
                                           activity['is_paid']) 
                                                for activity in data['payment_activities']]
    biller = Biller(data['biller_type'], payment_activities, data['remaining_payment'], data['payee'])
    billers_collection = db.billers
    billers_collection.insert_one(biller.to_dict())
    return jsonify({"message": "Biller created successfully"}), 201

@billers_bp.route('/billers', methods=['GET'])
def get_billers():
    billers_collection = db.billers
    billers = list(billers_collection.find())
    for biller in billers:
        biller['_id'] = str(biller['_id'])
    return jsonify(billers), 200

@billers_bp.route('/billers/<biller_id>', methods=['PUT'])
def update_biller(biller_id):
    data = request.get_json()
    billers_collection = db.billers
    update_data = {}

    if 'biller_type' in data:
        update_data['biller_type'] = data['biller_type']
    if 'payment_activities' in data:
        update_data['payment_activities'] = [PaymentActivity([PaymentItem(**item) 
                                                              for item in 
                                                              activity['payment_items']], 
                                                              activity['payment_date'], 
                                                              activity['is_paid']).to_dict() 
                                             for activity in data['payment_activities']]
    if 'remaining_payment' in data:
        update_data['remaining_payment'] = data['remaining_payment']
    if 'payee' in data:
        update_data['payee'] = data['payee']

    result = billers_collection.update_one({'_id': ObjectId(biller_id)}, {'$set': update_data})

    if result.matched_count > 0:
        return jsonify({"message": "Biller updated successfully"}), 200
    else:
        return jsonify({"message": "Biller not found"}), 404

@billers_bp.route('/billers/<biller_id>', methods=['DELETE'])
def delete_biller(biller_id):
    billers_collection = db.billers
    result = billers_collection.delete_one({'_id': ObjectId(biller_id)})

    if result.deleted_count > 0:
        return jsonify({"message": "Biller deleted successfully"}), 200
    else:
        return jsonify({"message": "Biller not found"}), 404
