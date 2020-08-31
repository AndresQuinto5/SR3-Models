from gl import Render

render = Render()
render.glColor(0.130, 0.240, 0.750) #Color Azul Mustang

render.load('./cuerpo.obj', translate=[600, 300], scale = [100, 100])
render.glFinish()