
## matplotlib.axes.Axes.scatter
___
* Axes.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, **kwargs)
> Make a scatter plot of x vs y  
marker size is scaled by s and marker color is mapped to c.


Parameters | Description
-----------|------------
x, y     | rray_like, shape (n, )
s  | scalar or array_like, shape (n, ), optional
c | color, sequence, or sequence of color, optional, default: ‘b’
marker |  MarkerStyle
cmap |  Colormap
norm | A Normalize instance is used to scale luminance data to 0, 1. norm is only used if c is an array of floats.
vmin, vmax | vmin and vmax are used in conjunction with norm to normalize luminance data. If either are None, the min and max of the color array is used. Note if you pass a norm instance, your settings for vmin and vmax will be ignored.
alpha | The alpha blending value, between 0 (transparent) and 1 (opaque)
linewidths | scalar or array_like, optional, default: None
verts | sequence of (x, y), optional, If marker is None, these vertices will be used to construct the marker. The center of the marker is located at (0,0) in normalized units. The overall marker is rescaled by s.
edgecolors | color or sequence of color, optional, default: None
return | PathCollection


