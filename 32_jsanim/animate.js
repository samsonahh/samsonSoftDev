// Samson Wu, Ravindra Mangar pd7

var c = document.getElementById("playground");
var animButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var DVDButton = document.getElementById("buttonDVD");

var ctx = c.getContext("2d");

ctx.fillStyle = "green";

var requestID;

var clear = (e) => {
    // e.preventDefault();
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;
var growing = true;

var drawCircle = (e) => {
    //console.log("DRAWING!");
    stopAnim(e);
    clear(e);

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

var rectW = 150;
var rectH = 75;

var rectX;
var rectY;

var xVel = 1;
var yVel = 1;

var logo = new Image();
logo.src = "logo_dvd.jpg";

var setupDVD = (e) => {
    rectX = Math.random() * (c.width - rectW);
    rectY = Math.random() * (c.height - rectH);
    startDVD(e);
}

var startDVD = (e) => {
    stopAnim(e);
    clear(e);

    ctx.drawImage(logo, rectX, rectY, rectW, rectH);
    
    if(rectX < 0 || rectX + rectW > c.width){
        xVel *= -1;
    }
    if(rectY < 0 || rectY + rectH > c.height){
        yVel *= -1;
    }

    rectX += xVel;
    rectY += yVel;

    requestID = window.requestAnimationFrame(startDVD);

    console.log("DVD!");
}

animButton.addEventListener("click", drawCircle);
stopButton.addEventListener("click", stopAnim);
DVDButton.addEventListener("click", setupDVD);