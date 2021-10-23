function zeropad(str, len){
  str = str.toString();
  var pad = "";
  for(var i = 0; i < (len - str.length); i++){
    pad = pad + "0";
  }
  return pad + str;
}


function spawnChance(obj_arr){
  var output;
  var chance_total = 0;
  for(var i = 0; i < obj_arr.length; i++){
    chance_total += obj_arr[i].spawn_chance;
  }
  var rand = Math.random() * chance_total;

  var i = 0;
  var prevoius_chance = 0;
  while(i < obj_arr.length){
    if(prevoius_chance < rand && rand < (prevoius_chance + obj_arr[i].spawn_chance)){
      output = obj_arr[i].type;
      i = obj_arr.length + 1;
    }else{
      prevoius_chance += obj_arr[i].spawn_chance;
    }
    i++;
  }
  return output;
}


function jump(e){
  var elem = e.target;
  elem.classList.add("a_jump");
  elem.addEventListener("animationend", function(){elem.classList.remove("a_jump")});
}


function changeScore(modifier){
  var score = parseInt(score_elem.innerHTML);
  score += modifier;
  score = zeropad(score, 4);
  score_elem.innerHTML = score;
}


function changeWater(modifier){
  var current_amount = parseInt(water_meter_elem.style.height.split("%")[0]);
  if(current_amount + modifier < 0){
    current_amount = 0;
  }else if(current_amount + modifier > 100){
    current_amount = 100;
  }else{
    current_amount = current_amount + modifier;
  }
  water_meter_elem.style.height = current_amount + "%";
  water_meter_text_elem.innerHTML = current_amount + "%";
}


function changeHealth(modifier){
  var current_amount = parseInt(health_bar_elem.style.height.split("%")[0]);
  if(current_amount + modifier < 0){
    current_amount = 0;
  }else if(current_amount + modifier > 100){
    current_amount = 100;
  }else{
    current_amount = current_amount + modifier;
  }
  health_bar_elem.style.height = current_amount + "%";
  health_bar_text_elem.innerHTML = current_amount + "%";
}


function getLinearDistance(p1, p2){
  return Math.sqrt(((p2.x - p1.x) * (p2.x - p1.x)) + ((p2.y - p1.y) * (p2.y - p1.y)));
}


function cartesianToPolar(p1, p2){
  var output = [];
  var rad = degToRad(angle);
  output[0] += length * Math.cos(rad);
  output[1] += length * Math.sin(rad);
  return output;
}


function degToRad(deg){
  return deg * (Math.PI / 180);
}


function radToDeg(rad){
  return rad * (180 / Math.PI);
}


function generateID(){
  const chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
  var id = "";
  for(var i = 0; i < 10; i++){id += chars[parseInt(Math.random() * chars.length)];}
  return id;
}


function moveObject(){
  document.getElementById("tunnel").animate([
    { transform: 'translate3D(0, 0, 0)' }, 
    { transform: 'translate3D(0, -300px, 0)' }
  ], {
    duration: 1000,
    iterations: Infinity
  })

  var aliceTumbling = [
    { transform: 'rotate(0) translate3D(-50%, -50%, 0', color: '#000' }, 
    { color: '#431236', offset: 0.3},
    { transform: 'rotate(360deg) translate3D(-50%, -50%, 0)', color: '#000' }
  ];

  var aliceTiming = {
    duration: 3000,
    iterations: Infinity
  }

  document.getElementById("alice").animate(
    aliceTumbling, 
    aliceTiming
  )
}


function updateCursorPosition(e){
  cursor_position.x = e.clientX;
  cursor_position.y = e.clientY;
  aimTrace();
  crosshair();
}

function aimTrace(){
  var pos = {x: (cursor_position.x - center_of_game.x + 1), y: (cursor_position.y - center_of_game.y - 1)}
  aim_trace_elem.style.width = getLinearDistance(center_of_game, cursor_position) + "px";
  aim_trace_elem.style.transform = "rotate(" + radToDeg(Math.atan2(pos.y, pos.x)) + "deg)";
}

function crosshair(){
  crosshair_elem.style.left = cursor_position.x - 8 + "px";
  crosshair_elem.style.top = cursor_position.y - 8 + "px";
}