import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **item):
    self.contents = []

    for key,value in item.items():
            for itr in range(value):
              self.contents.append(key)
  
  def draw(self, count):
    draw_items = []
    if count >= len(self.contents):
          return self.contents
    for i in range(count):
          name=self.contents.pop(random.randrange(len(self.contents)))
          draw_items.append(name)
    return draw_items    



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  final_count=0
  for _ in range(num_experiments):
      copyhat = copy.deepcopy(hat)
      temp_list = copyhat.draw(num_balls_drawn)
      success=True
      for key,value in expected_balls.items():
        if temp_list.count(key) < value:
          success=False
          break
      if success:
        final_count+=1

  return final_count/num_experiments  
