const loadExpenseVsIncome = async () => {

    const endpoint = '/api/expenseVsIncome'

    const response = await fetch(endpoint).catch(error => {
        console.log(error)
    })
    const jsonReponse = await response.json()

    let plotlyGraph = jsonReponse['data']
    Plotly.newPlot('expense-vs-income', plotlyGraph, {})

}

const loadEssentialExpense = async () => {

    const endpoint = '/api/essentialExpense'

    const response = await fetch(endpoint)
    const jsonReponse = await response.json()

    let plotlyGraph = jsonReponse['data']

    Plotly.newPlot('essential-expense', plotlyGraph, {})

}

const loadNonEssentialExpense = async () => {
    
    const endpoint = '/api/nonEssentialExpense'

    const response = await fetch(endpoint)
    const jsonReponse = await response.json()

    let plotlyGraph = jsonReponse['data']

    Plotly.newPlot('non-essential-expense', plotlyGraph, {})

}


loadExpenseVsIncome()
loadEssentialExpense()
loadNonEssentialExpense()