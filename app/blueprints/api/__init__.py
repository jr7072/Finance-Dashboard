from flask import Blueprint
from flask_login import current_user
import plotly as px

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/expenseVsIncome', methods=['GET'])
def expenseVsIncome():

    user_id = current_user.id

    return


@api.route('/essentialExpense', methods=['GET'])
def essentialExpense():

    user_id = current_user.id

    return


@api.route('/nonEssentialExpense', methods=['GET'])
def nonEssentialExpense():

    user_id = current_user.id

    return