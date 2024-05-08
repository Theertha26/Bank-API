import os
from flask import Blueprint, jsonify
import pandas as pd

bp = Blueprint("main", __name__)

# to get the absolute path to the directory containing the script
script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, '../bank_branches.csv')
print("CSV Path:", csv_path) 

@bp.route('/banks', methods=['GET'])
def get_banks():
    df = pd.read_csv(csv_path)
    banks = df['bank_name'].unique().tolist()
    return jsonify(banks)

@bp.route('/branches/<branch>', methods=['GET'])
def get_branch_details(branch):
    df = pd.read_csv(csv_path)
    branch_details = df[df['branch'].str.lower() == branch.lower()].to_dict('records')
    return jsonify(branch_details)

#For Testing
# @bp.route('/', methods=['GET'])
# def index():
#     return jsonify({"message": "Welcome to the Bank API!"})