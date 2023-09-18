const loadExpenseVsIncome = async () => {

    const endpoint = '/api/expenseVsIncome'

    const response = await fetch(endpoint).catch(error => {
        console.log(error)
    })
    const jsonReponse = await response.json()

    const plotlyGraph = jsonReponse['data']
    const config = {
        "title": 'Transaction Breakdown By Month (2023)'
    }

    Plotly.newPlot('expense-vs-income', plotlyGraph, config)

}

const loadEssentialExpense = async () => {

    const endpoint = '/api/essentialExpense'

    const response = await fetch(endpoint)
    const jsonReponse = await response.json()

    const plotlyGraph = jsonReponse['data']
    const config = {
        'title': 'Essential Expense Breakdown For Current Month'
    }

    Plotly.newPlot('essential-expense', plotlyGraph, config)

}

const loadNonEssentialExpense = async () => {
    
    const endpoint = '/api/nonEssentialExpense'

    const response = await fetch(endpoint)
    const jsonReponse = await response.json()

    const plotlyGraph = jsonReponse['data']
    const config = {
        'title': 'Non-Essential Expense Breakdown For Current Month'
    }

    Plotly.newPlot('non-essential-expense', plotlyGraph, config)

}


loadExpenseVsIncome()
loadEssentialExpense()
loadNonEssentialExpense()