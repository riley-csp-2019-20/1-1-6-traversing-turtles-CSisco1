import turtle as trtl
# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "triangle", "square", "circle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

# coordinates for where the turtle goes 
'''startx = -100
starty = -100'''
turn = 0
forward = 10

#makes the turtle go somewhere
for t in my_turtles:
	'''t.goto(startx, starty)'''
	t.right(turn)     
	t.forward(forward)

#changes where the turtle goes
	'''	startx = startx + 50
	starty = starty + 50'''
	turn = turn + 45
	forward = turn/4

wn = trtl.Screen()
wn.mainloop()