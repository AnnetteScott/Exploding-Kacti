var game_elem = document.querySelector("game");
var game_width = game_elem.offsetWidth;
var game_height = game_elem.offsetHeight;
var cactus_ids = [];

function game_main(){
}


function spawnPond(){
  var pos = {x: (game_width / 2) - (64), y: (game_height / 2) - (64)};
  var id = "POND";
  var pond = document.createElement("div");
  pond.classList.add("pond");
  pond.id = id;
  pond.style.left = pos.x + "px";
  pond.style.top = pos.y + "px";
  document.querySelector("game").appendChild(pond);
}

function spawnCactus(){
  var pos = {x: (Math.random() * game_width), y: (Math.random() * game_height)};
  var id = generateID();
  var cactus = document.createElement("div");
  cactus.classList.add("cactus");
  cactus.id = id;
  cactus.style.left = pos.x + "px";
  cactus.style.top = pos.y + "px";
  document.querySelector("game").appendChild(cactus);
}


function jump(e){
  var elem = e.target;
  elem.classList.add("a_jump");
  elem.addEventListener("animationend", function(){elem.classList.remove("a_jump")});
}

function explode(event){
  changeColour('034206');
  var x = event.target.offsetLeft + (event.target.offsetWidth / 2);
  var y = event.target.offsetTop + (event.target.offsetHeight / 2);
  var pos = {clientX: x, clientY: y};
  event.target.remove();
  createEmitter(pos);
}

function generateID(){
  const chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
  var id = "";
  for(var i = 0; i < 10; i++){
    id += chars[parseInt(Math.random() * chars.length)];
  }
  return id;
}