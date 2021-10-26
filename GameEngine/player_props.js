var player = {
  health: 100
};

var pond_item = {
  'pond_hit_distance': 40,
  'pond_health': 100
};

var heart_item = {
  'health_regen': 10,
  'spawn_chance': 2,
  'heart_min_spawn_distance': 400
};


var difficulty = [
  {'level': 'L1', 'maxCacti': 10, 'scoreThreshold': 10},
  {'level': 'L2', 'maxCacti': 15, 'scoreThreshold': 50},
  {'level': 'L3', 'maxCacti': 20, 'scoreThreshold': 100},
  {'level': 'L4', 'maxCacti': 25, 'scoreThreshold': 150},
  {'level': 'L5', 'maxCacti': 30, 'scoreThreshold': 200},
  {'level': 'L6', 'maxCacti': 35, 'scoreThreshold': 250}
];