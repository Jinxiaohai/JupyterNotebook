
# matplotlib.axes.Axes.plot
___
* Axes.plot(*args, **kwargs)

> Plot and/or markers to the Axes. args is a variable length argument, allowing for multiple x, y pairs with an optional formats string. For expamle, each of the following is legal:
 1. plot(x, y)
 2. plot(x, y, 'bo')
 3. plot(y)
 4. plot(y, 'r+')
____
> if not used with labeled data, an arbitrary number of x, y, fmt groups can be specified, as in:  
 1. a.plot(x1, y1, 'g^', x2, y2, 'g-')  
return value is a ***list*** of lines that were added.

___
* 下列的格式字符串可以被用来描述line style 和 marker.  

| character | description |   
|:---------:|:-----------:|  
| '-' |	solid line style |
|'--'| 	dashed line style|
|'-.' |	dash-dot line style|
|':' |	dotted line style|
|'.' |	point marker|
|',' |	pixel marker|
|'o' |	circle marker|
|'v' |	triangle_down marker|
|'^' |	triangle_up marker|
|'<' |	triangle_left marker|
|'>'| 	triangle_right marker|
|'1'| 	tri_down marker|
|'2'| 	tri_up marker|
|'3'| 	tri_left marker|
|'4'| 	tri_right marker|
|'s'| 	square marker|
|'p'| 	pentagon marker|
|'*'| 	star marker|
|'h'| 	hexagon1 marker|
|'H' |	hexagon2 marker|
|'+'| 	plus marker|
|'x' |	x marker|
|'D' |	diamond marker|
|'d' |	thin_diamond marker|
|'_' |	hline marker|

## Line2D 的关键字属性控制

  Property |	Description
-----------|:-----------------
agg_filter |	unknown
alpha 	   |float (0.0 transparent through 1.0 opaque)
animated 	| [True , False]
antialiased or aa |	[True , False]
axes   | 	an Axes instance
clip_box | 	a matplotlib.transforms.Bbox instance
clip_on |	[True , False]
clip_path |	[ (Path, Transform) , Patch , None ]
color or c | 	any matplotlib color
contains | 	a callable function
dash_capstyle |	[‘butt’ , ‘round’ , ‘projecting’]
dash_joinstyle |	[‘miter’ , ‘round’ , ‘bevel’]
dashes |	sequence of on/off ink in points
drawstyle |	[‘default’ , ‘steps’ , ‘steps-pre’ , ‘steps-mid’ , ‘steps-post’]
figure |	a matplotlib.figure.Figure instance
fillstyle |	[‘full’ , ‘left’ , ‘right’ , ‘bottom’ , ‘top’ , ‘none’]
gid   | 	an id string
label |	string or anything printable with ‘%s’ conversion.
linestyle or ls  |	[‘solid’ , ‘dashed’, ‘dashdot’, ‘dotted’ , (offset, on-off-dash-seq) , '-' , '--' , '-.' , ':' , 'None' , ' ' , '']
linewidth or lw | 	float value in points
marker |	A valid marker style
markeredgecolor or mec |	any matplotlib color
markeredgewidth or mew |	float value in points
markerfacecolor or mfc |	any matplotlib color
markerfacecoloralt or mfcalt |	any matplotlib color
markersize or ms |	float
markevery |	[None , int , length-2 tuple of int , slice , list/array of int , float , length-2 tuple of float]
path_effects |	unknown
picker |	float distance in points or callable pick function fn(artist, event)
pickradius |	float distance in points
rasterized |	[True , False , None]
sketch_params |	unknown
snap |	unknown
solid_capstyle | 	[‘butt’ , ‘round’ , ‘projecting’]
solid_joinstyle |	[‘miter’ , ‘round’ , ‘bevel’]
transform |	a matplotlib.transforms.Transform instance
url |	a url string
visible |	[True , False]
xdata |	1D array
ydata |	1D array
zorder |	any number
