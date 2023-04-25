var c = document.getElementById("slate");

//makes our canvas 2d drawing space
var ctx = c.getContext("2d");

var mode = "rect";

var toggleMode = (e) => {
    if(mode == "rect"){
        mode = "cir";
    }
    else{
        mode = "rect";
    }
    console.log("toggling to ", mode);
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;

    ctx.beginPath();
    ctx.rect(mouseX, mouseY, 100, 100);
    ctx.fillStyle = "red";
    ctx.fill();
    ctx.stroke();

    console.log("mouseClick registered at ", mouseX, mouseY);
}

var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;

    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.fillStyle = "blue";
    ctx.fill();
    
    ctx.stroke();
    console.log("mouseClick registered at ", mouseX, mouseY);
}

var draw = (e) => {
    console.log("DRAWING!", e);
    if(mode == "rect"){
        drawRect(e);
    }
    else{
        drawCircle(e);
    }
}

var wipeCanvas = function(){
    //draws an empty rect from (0,0) to (w, h) of canvas
    ctx.clearRect(0, 0, c.width, c.height);
    console.log("WIPING!");
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
