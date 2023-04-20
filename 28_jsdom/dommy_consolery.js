/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
// FAC
// GCD
function fact(n){
  if(n<2){
      return 1;
  }
  return n*fact(n-1);
}

var factorial = (n) => {
  return fact(n);}

function fib(n){
  if(n<2){
      return 1;
  }
  return fib(n-1) + fib(n-2);
}

function gcd(x, y){
  if ((typeof x !== 'number') || (typeof y !== 'number')) 
    return false;
  x = Math.abs(x);
  y = Math.abs(y);
  while(y) {
    var t = y;
    y = x % y;
    x = t;
  }
  return x;
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

var addButton = document.getElementById("addItem");
var addInput = document.getElementById("addItemInput");

addButton.addEventListener('click', () => addItem(addInput.value));

var remButton = document.getElementById("removeItem");
var remInput = document.getElementById("removeItemInput");

remButton.addEventListener('click', () => removeItem(remInput.value-1));

var redButton = document.getElementById("redItems");

redButton.addEventListener('click', red);

var stripeButton = document.getElementById("stripeItems");

stripeButton.addEventListener('click', stripe);

var factButton = document.getElementById("factButton");
var factInput = document.getElementById("factInput");

factButton.addEventListener('click', () => addItem(fact(factInput.value)));

var fibButton = document.getElementById("fibButton");
var fibInput = document.getElementById("fibInput");

fibButton.addEventListener('click', () => addItem(fib(fibInput.value)));

var GCNButton = document.getElementById("GCNButton");
var GCN1 = document.getElementById("GCN1");
var GCN2 = document.getElementById("GCN2");

GCNButton.addEventListener('click', () => addItem(gcd(Number(GCN1.value), Number(GCN2.value))));
