var player = {
  health: 100
};

var pond_item = {
  'pond_hit_distance': 40,
  'pond_health': 100
};

var heart_item = {
  'health_regen': 10,
  'spawn_chance': 20,
  'heart_min_spawn_distance': 400
};

var spawn_speed = 1000
var difficulty = [
  {'level': '1', 'maxCacti': 10, 'scoreThreshold': 10, 'spawnSpeed': 1000, 'cactiMovingSpeed': 1, 'fireCacti': 2},
  {'level': '2', 'maxCacti': 15, 'scoreThreshold': 50, 'spawnSpeed': 950, 'cactiMovingSpeed': 1.2, 'fireCacti': 5},
  {'level': '3', 'maxCacti': 20, 'scoreThreshold': 75, 'spawnSpeed': 850, 'cactiMovingSpeed': 1.4, 'fireCacti': 10},
  {'level': '4', 'maxCacti': 25, 'scoreThreshold': 100, 'spawnSpeed': 800, 'cactiMovingSpeed': 1.5, 'fireCacti': 20},
  {'level': '5', 'maxCacti': 30, 'scoreThreshold': 150, 'spawnSpeed': 750, 'cactiMovingSpeed': 1.6, 'fireCacti': 25},
  {'level': '6', 'maxCacti': 35, 'scoreThreshold': 200, 'spawnSpeed': 600, 'cactiMovingSpeed': 1.75, 'fireCacti': 30},
  {'level': '7', 'maxCacti': 40, 'scoreThreshold': 300, 'spawnSpeed': 550, 'cactiMovingSpeed': 1.85, 'fireCacti': 35}
];