from flask import Blueprint
from app.backend.db import *
from flask_login import login_required
import plotly.express as px
import plotly.utils as pu
from datetime import datetime
import json

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/expenseVsIncome', methods=['GET'])
@login_required
def expenseVsIncome():

    transaction_data = get_transaction_data()

    # only for current year
    current_year = datetime.now().year
    transaction_data = transaction_data[transaction_data['Date'].dt.year
                                            == current_year]

    # aggregate expenses by month
    aggregated_data = transaction_data \
                                    .groupby(['Month', 'Type', 'Category'],
                                             as_index=False) \
                                    .agg({'Value': 'sum'})
    
    month_to_number = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    aggregated_data = aggregated_data \
                        .sort_values('Month', key=lambda x: x.apply(lambda y: month_to_number[y]))
    
    
    plot = px.bar(aggregated_data, x='Month', y='Value', color="Type",
                    barmode="group")
    
    graphJSON = json.dumps(plot, cls=pu.PlotlyJSONEncoder)
    
    return graphJSON, 200


@api.route('/essentialExpense', methods=['GET'])
@login_required
def essentialExpense():

    transaction_data = get_transaction_data()

    # get the current month '
    current_month = datetime.now().month
    transaction_data = transaction_data[transaction_data['Date'].dt.month
                                            == current_month]

    # aggregate expenses by month
    aggregated_data = transaction_data \
                                    .groupby(['Type', 'Category'],
                                             as_index=False) \
                                    .agg({'Value': 'sum'})
    
    # get only the essential expenses
    essential_expense = aggregated_data[aggregated_data['Type']
                                            == 'Essential Expense']
    
    plot = px.pie(essential_expense, values='Value', names='Category')
    
    graphJSON = json.dumps(plot, cls=pu.PlotlyJSONEncoder)
    
    return graphJSON, 200

@api.route('/nonEssentialExpense', methods=['GET'])
@login_required
def nonEssentialExpense():

    transaction_data = get_transaction_data()

    # get the current month '
    current_month = datetime.now().month
    transaction_data = transaction_data[transaction_data['Date'].dt.month
                                            == current_month]

    # aggregate expenses by month
    aggregated_data = transaction_data \
                                    .groupby(['Type', 'Category'],
                                             as_index=False) \
                                    .agg({'Value': 'sum'})
    
    # get only the essential expenses
    essential_expense = aggregated_data[aggregated_data['Type']
                                            == 'Non-Essential Expense']
    
    plot = px.pie(essential_expense, values='Value', names='Category')
    
    graphJSON = json.dumps(plot, cls=pu.PlotlyJSONEncoder)

    return graphJSON, 200