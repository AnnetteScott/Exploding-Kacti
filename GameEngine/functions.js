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

function getLinearDistance(p1, p2){
  return Math.sqrt(((p2[0] - p1[0]) * (p2[0] - p1[0])) + ((p2[1] - p1[1]) * (p2[1] - p1[1])));
}

function generateID(){
  const chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
  var id = "";
  for(var i = 0; i < 10; i++){id += chars[parseInt(Math.random() * chars.length)];}
  return id;
}