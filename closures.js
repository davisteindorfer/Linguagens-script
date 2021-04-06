function objeto(a) {
    var variavel = a;
    var obj = {};
    
    function displayVariavel() {
        console.log(variavel)
    }

    obj.variavel = displayVariavel;
    return obj;
}


b = objeto('colher');
b.variavel();
