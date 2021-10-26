var game_elem = document.querySelector("game");
var game_width = game_elem.offsetWidth;
var game_height = game_elem.offsetHeight;
var center_of_game = {x: (game_width / 2), y: (game_height / 2)};

var cursor_position = {x: 0, y: 0};

var score_elem = document.querySelector("score p");
var health_bar_elem = document.querySelector("water_meter div");
var health_bar_text_elem = document.querySelector("water_meter p");
var water_meter_elem = document.querySelector("water_meter div");
var water_meter_text_elem = document.querySelector("water_meter p");

var aim_trace_elem = document.querySelector("aim_trace");
aim_trace_elem.style.left = center_of_game.x + "px";
aim_trace_elem.style.top = center_of_game.y + "px";
var crosshair_elem = document.querySelector("crosshair");
crosshair_elem.style.left = center_of_game.x + "px";
crosshair_elem.style.top = center_of_game.y + "px";



/*==============Main Game Loop============*/
let game_params = {};
function gameMain(){

  spawnPond();

  window.setInterval(function(){spawnCactus(spawnChance(cacti_types))}, 1000);
}




/*===========Main Game Functions==========*/

function spawnPond(){
  var pos = {x: (game_width / 2) - (64), y: (game_height / 2) - (64)};
  var id = "POND";
  var pond = document.createElement("pond");
  pond.classList.add("pond");
  pond.id = id;
  pond.style.left = pos.x + "px";
  pond.style.top = pos.y + "px";
  pond.setAttribute('onclick', "changeWater(50)");
  document.querySelector("game").appendChild(pond);
}


function spawnCactus(type = "normal_cactus"){
  if(all_cacti.length < max_num_of_cacti){
    var pos = {x: center_of_game.x, y: center_of_game.y};
    while(getLinearDistance(pos, center_of_game) < cacti_max_spawn_distance){
      pos = {x: (Math.random() * game_width), y: (Math.random() * game_height)};
    }
    var id = generateID();
    var cactus = document.createElement("cactus");
    cactus.classList.add(type);
    cactus.id = id;
    //cactus.setAttribute('onclick', "explode(event)");
    cactus.style.left = pos.x - 32 + "px";
    cactus.style.top = pos.y - 32 + "px";
    document.querySelector("game").appendChild(cactus);
    all_cacti.push(id);
  }
}

function moveAllCacti(){

}

function checkAmmo(){
  return parseInt(water_meter_elem.style.height.split("%")[0]);
}

function explode(event){
  if(checkAmmo() > 0){
    var elem = event.target;
    var x = elem.offsetLeft + (elem.offsetWidth / 2);
    var y = elem.offsetTop + (elem.offsetHeight / 2);
    var pos = {clientX: x, clientY: y};
    var id = elem.id;
    var type = elem.classList.value;
    var color = '034206';
    var score = 0;
    for(var i = 0; i < cacti_types.length; i++){
      if(cacti_types[i].type == type){
        color = cacti_types[i].color;
        score = cacti_types[i].points;
      }
    }
    changeColour(color);
    elem.remove();
    const index = all_cacti.indexOf(id);
    if (index > -1) {
      all_cacti.splice(index, 1);
    }
    createEmitter(pos);
    changeScore(score);
    changeWater(-10);
  }
}


function shoot(pos){
  var hit = checkHit(pos);
  if(checkAmmo() > 0){
    var pos = {clientX: x, clientY: y};
    var id = elem.id;
    var type = elem.classList.value;
    var color = '034206';
    var score = 0;
    for(var i = 0; i < cacti_types.length; i++){
      if(cacti_types[i].type == type){
        color = cacti_types[i].color;
        score = cacti_types[i].points;
      }
    }
    changeColour(color);
    elem.remove();
    const index = all_cacti.indexOf(id);
    if (index > -1) {
      all_cacti.splice(index, 1);
    }
    createEmitter(pos);
    changeScore(score);
    changeWater(-10);
  }
}


function checkHit(pos){
  return 1;
}


function handleClickEvent(e){
  var elem = e.target;
  console.log(elem.tagName);
  if(elem.tagName == "GAME_BACKGROUND"){
    var x = elem.offsetLeft + (elem.offsetWidth / 2);
    var y = elem.offsetTop + (elem.offsetHeight / 2);
  }else if(elem.tagName == "cactus"){
    var x = elem.offsetLeft + (elem.offsetWidth / 2);
    var y = elem.offsetTop + (elem.offsetHeight / 2);
    checkHit({x: x, y: y});
  }
}