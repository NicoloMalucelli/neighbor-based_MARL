from ipycanvas import Canvas, hold_canvas

class CanvasWithBorders(Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def clear(self):
        super().clear()
        border_color = 'black'  # You can customize the border color here
        border_width = 1  # You can customize the border width here
        self.fill_style = border_color
        # Draw top border
        self.fill_rect(0, 0, self.width, border_width)
        # Draw bottom border
        self.fill_rect(0, self.height - border_width, self.width, border_width)
        # Draw left border
        self.fill_rect(0, 0, border_width, self.height)
        # Draw right border
        self.fill_rect(self.width - border_width, 0, border_width, self.height)