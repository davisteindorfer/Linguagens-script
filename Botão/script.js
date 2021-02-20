var button = document.createElement("button");
button.innerHTML = "Aperta Aqui!";

var body = document.getElementsByTagName("body")[0];
body.appendChild(button);

button.addEventListener ("click", function() {button.style.display = "none";} );
