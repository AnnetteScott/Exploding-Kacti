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
gameMain();



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

    var cactus = document.createElement("cactus");
    var id = generateID();
    var new_cactus_object = {
      'dom_element': cactus,
      'id': id,
      'type': type,
      'position': {x: pos.x, y: pos.y},
      'remaining_health': cacti_types[type]['health']
    };
    cactus.id = id;
    cactus.classList.add(type);
    cactus.style.left = pos.x - 32 + "px";
    cactus.style.top = pos.y - 32 + "px";
    document.querySelector("game").appendChild(cactus);

    all_cacti[id] = new_cactus_object;
  }
}


function moveAllCacti(){
//TODO
}


function checkAmmo(){
  return parseInt(water_meter_elem.style.height.split("%")[0]);
}


function explode(pos, color){
  changeColour(color);
  createEmitter({clientX: pos.x, clientY: pos.y});
}


function shoot(elem){
  var cacti_type = elem.classList.value;
  if(checkAmmo() >= cacti_types[cacti_type]['health']){
    var pos = {x: elem.offsetLeft + (elem.offsetWidth / 2), y: elem.offsetTop + (elem.offsetHeight / 2)};
    var color = cacti_types[cacti_type]['color'];
    var score = cacti_types[cacti_type]['points'];
    var water_used = cacti_types[cacti_type]['health'];

    const index = all_cacti.indexOf(elem.id);
    if (index > -1) {
      all_cacti.splice(index, 1);
    }
    elem.remove();
    explode(pos, color);
    changeScore(score);
    changeWater(0 - water_used);
  }
}


function handleClickEvent(e){
  var elem = e.target;
  console.log(elem.tagName);
  if(elem.tagName == "GAME_BACKGROUND"){
    explode({x: e.clientX, y: e.clientY}, 'EAD997');
  }else if(elem.tagName == "CACTUS"){
    shoot(elem);
  }
}