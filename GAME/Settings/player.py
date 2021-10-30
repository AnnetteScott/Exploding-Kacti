from . import constants

player = {
  'health': 100
}

pond_item = {
  'pond_hit_distance': 40,
  'water_amount': 50,
  'pos': constants.SCREEN_CENTER,
  'dim': {'width': constants.POND_DIM, 'height': constants.POND_DIM},
  'hit_radius': constants.POND_DIM / 2
}