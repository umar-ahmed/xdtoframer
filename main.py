from xdtools import XDFile
from xdtools.style.drop_shadow import DropShadow

with XDFile('test.xd') as xd:
    for artboard in xd.artboards:
        for artwork in artboard.artwork:
            name = artwork.name.replace(' ', '')
            x = artwork.position.x
            y = artwork.position.y
            border_radius = '50%' if artwork.type == 'ellipse' else 0

            backgroundColor = 'red'
            if 'fill' in artwork.styles:
                fill = artwork.styles['fill']
                backgroundColor = fill.color.to_hex()

            border_width = 0
            border_color = 'black'
            if 'stroke' in artwork.styles:
                stroke = artwork.styles['stroke']
                border_width = stroke.width
                border_color = stroke.color.to_hex()

            drop_shadow_radius = 0
            drop_shadow_color = 'transparent'
            drop_shadow_x = 0
            drop_shadow_y = 0
            if 'filter' in artwork.styles:
                for filter_ in artwork.styles['filter']:
                    if isinstance(filter_, DropShadow):
                        drop_shadow_radius = filter_.blur_radius
                        drop_shadow_color = filter_.color.to_hex()
                        drop_shadow_x = filter_.offset_x
                        drop_shadow_y = filter_.offset_y

            framer = str.format('{} = new Layer({{ x: {}, y: {}, width: {}, height: {}, ' +
                                'borderRadius: {}, borderWidth: {}, borderColor: {}, ' +
                                'backgroundColor: {}, shadow1: {{ x: {}, y: {}, blur: {}, color: {} }} }});',
                                name, x, y, artwork.width, artwork.height, repr(
                                    border_radius),
                                border_width, repr(border_color), repr(backgroundColor),
                                drop_shadow_x, drop_shadow_y, drop_shadow_radius,
                                repr(drop_shadow_color))
            print(framer)
