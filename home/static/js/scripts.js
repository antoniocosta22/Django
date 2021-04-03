function relogio(){
    var data = new Date ()
    var hora = data.getHours()
    var min = data.getMinutes()
    var sec = data.getSeconds()

    if( hora < 10){
        hora='0'+hora;
    }
    if( min < 10){
        min = '0'+min;
    }
    if( sec < 10){
        sec = '0'+sec;
    }

    document.getElementById('hora').innerHTML = hora+':'+min+':'+sec;
}

var timer=setInterval(relogio,1000);

