// Samson Wu, Ravindra Mangar pd7

var c = document.getElementById("playground");
var animButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "green";

var requestID;

var clear = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;
var growing = true;

var drawCircle = () => {
    //console.log("DRAWING!");
    clear();

    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, 2*Math.PI);
    ctx.fill();
    ctx.closePath();

    if(growing){
        radius++;
    }
    else{
        radius--;
    }

    if(radius == c.width/2){
        growing = false;
    }
    if(radius == 0){
        growing = true;
    }

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawCircle);
    console.log(requestID);
}

var stopAnim = (e) => {
    window.cancelAnimationFrame(requestID);
    //console.log("STOPPED", requestID);
}

animButton.addEventListener("click", drawCircle);
stopButton.addEventListener("click", stopAnim);