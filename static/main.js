function isOk(inputs) {
  for (let i = 0; i < inputs.length; i++) {
    if (inputs[i].value.length == 0) return false;
  }
  return true;
}

function getResult(result) {
  axios
    .post("/model", {
      fields: result,
    })
    .then(function (response) {
      alert("Result = " + response.data[0]);
    })
    .catch(function (error) {
      console.log(error.toString());
    });
}

function go() {
  var inputs = document.getElementsByClassName("input");

  if (isOk(inputs)) {
    var result = [];
    for (let i = 0; i < inputs.length; i++) {
      result.push(parseFloat(inputs[i].value));
    }
    getResult(result);
  } else {
    alert("Please fill the empty fields.");
  }
}
