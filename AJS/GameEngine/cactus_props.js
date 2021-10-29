// function cactus_constructor(id,creation_tick,start,end,speed,lifespan,velocity){
//   this.id = id,
//   this.creation_tick = creation_tick,
//   this.start = start,
//   this.age = 0;
//   this.end = end,
//   this.speed = speed,
//   this.lifespan = lifespan,
//   this.velocity = velocity
// }

var cacti_movement_speed = 0.5;
var cacti_min_spawn_distance = 400;
var max_num_of_cacti = 10;
var all_cacti = {};
var cacti_types = {
  "normal_cactus": {
    spawn_chance: 60,
    health: 10,
    points: 1,
    color: "034206"
  },
  "left_cactus": {
    spawn_chance: 15,
    health: 10,
    points: 2,
    color: "034206"
  },
  "right_cactus": {
    spawn_chance: 15,
    health: 10,
    points: 2,
    color: "034206"
  },
  "blob_cactus":  {
    spawn_chance: 10,
    health: 20,
    points: 3,
    color: "034206"
  },
  "dead_cactus": {
    spawn_chance: 8,
    health: 10,
    points: 4,
    color: "7A3400"
  },
  "tumbleweed": {
    spawn_chance: 5,
    health: 20,
    points: 4,
    color: "A04400"
  },
  "fire_cactus": {
    spawn_chance: 2,
    health: 40,
    points: 5,
    color: "FE9300"
  }
};
