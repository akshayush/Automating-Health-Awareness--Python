import time
import pyglet
import win32api


start_time=time.time()
time_out=10 ##seconds
time_for_exercise_win=10

def display_gif(time_for_exercise_win):
# pick an animated gif file you have in the working directory
	ag_file="C:\\Users\\Akshay\\Desktop\\eye_blinking.gif"
	animation = pyglet.image.load_animation(ag_file)
	sprite = pyglet.sprite.Sprite(animation)

	# create a window and set it to the image size
	win = pyglet.window.Window(width=sprite.width, height=sprite.height)
	
	# set window background color = r, g, b, alpha
	# each value goes from 0.0 to 1.0
	green = 0, 1, 0, 1
	pyglet.gl.glClearColor(*green)
	
	@win.event
	def on_draw():
		win.clear()
		sprite.draw()
	def close(event):
		win.close()
	pyglet.clock.schedule_once(close,time_for_exercise_win)
	pyglet.app.run()
	
def lets_start(time_out,start_time,time_for_exercise_win):
	while True:
		start=win32api.GetLastInputInfo()
	
		if (win32api.GetLastInputInfo() != start) & (time.time()-start_time >=time_out):
			display_gif(time_for_exercise_win)
			start_time=time.time()
			continue
def test():
	print("Testing")

lets_start(time_out,start_time,time_for_exercise_win)