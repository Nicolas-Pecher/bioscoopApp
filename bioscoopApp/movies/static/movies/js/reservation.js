$(document).ready(function () {
  document.getElementById("plusBtn").addEventListener("click", function(){
    let amount = document.getElementById("amount").value;    
    amount = Number(amount) + 1;
    document.getElementById("amount").value=amount;
  });
  document.getElementById("minusBtn").addEventListener("click", function(){
    let amount = document.getElementById("amount").value;
    if (amount >0)
      amount = Number(amount) - 1;
    document.getElementById("amount").value=amount;
  });
});
