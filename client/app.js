    function onClickedChurn() {
    var ttAmount = document.getElementById("uiTTAmount");
    var ttAccount = document.getElementById("uiTTAccount");
    var trBalance = document.getElementById("uiTRBalance");
    var ttChange = document.getElementById("uiTTChange");
    var tnAccounts = document.getElementById("uiTNAccounts");
    var taChange = document.getElementById("uiTAChange");
    var auRatio = document.getElementById("uiAURatio");
    var churnResult = document.getElementById("churnResult");

    var url = "http://127.0.0.1:5000/predict_churn";

    
    $.post(url, {
        'total_transaction_on_account': parseInt(ttAmount.value),
        'total_transaction_amount': parseInt(ttAccount.value),
        'total_revolving_balance': parseInt(trBalance.value),
        'total_transactions_change_q4-q1': parseFloat(ttChange.value),
        'total_number_of_accounts': parseFloat(tnAccounts.value),
        'total_amount_change_q4-q1': parseFloat(taChange.value),
        'average utilization ratio': parseFloat(auRatio.value),
    },function(data, status) {
        console.log(data.churn_proba);
        churnResult.innerHTML = "<h2>" + data.churn_proba[1].toString() + ' | ' + data.churn_proba[0].toString() + "</h2>";
        console.log(status);
    });

    

}
