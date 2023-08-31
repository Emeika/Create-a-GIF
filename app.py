import imageio.v2 as imageio

#add the images to this list
filenames = ["images/bear1.png", "images/bear2.png", "images/bear3.png", "images/bear4.png", "images/bear5.png"]
gif =[]

for filename in filenames:
    gif.append(imageio.imread(filename))

imageio.mimsave("./created_gif/filename.gif", gif, loop=400, duration = 0.1)
