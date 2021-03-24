from .Widget import *


class Button(Widget):
    def __init__(self, rect, command, **kwargs):
        Widget.__init__(self)  # TODO for later...
        self.text = None  # to make warning go away...
        self.rect = pg.Rect(rect)
        self.command = command
        self.clicked = False
        self.hovered = False
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)
        self.render_text()

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.on_release()

    def update(self):
        self.check_hover()

    def draw(self, surface):
        color = self.color
        text = self.text
        border_color = self.border_color
        if not self.disabled:
            if self.clicked and self.clicked_color:
                color, text = self.get_clicked_color(text)
            elif self.hovered:
                border_color, color, text = self.get_hover_color(color, text)
        else:
            color = self.disabled_color
        self.draw_button(surface, self.rect, border_color, color)
        self.draw_text(surface, text)

    def process_kwargs(self, kwargs):
        settings = {
            "font"                  : pg.font.Font(None, 16),
            "text"                  : None,
            "call_on_release"       : True,
            'disabled'              : False,
            "click_sound"           : None,
            "hover_sound"           : None,
            'border_width'          : 2,
            "color"                 : pg.Color('white'),
            "font_color"            : pg.Color("black"),
            "hover_color"           : None,
            "hover_font_color"      : None,
            "clicked_color"         : None,
            "clicked_font_color"    : None,
            "border_color"          : pg.Color("white"),
            "border_hover_color"    : pg.Color("white"),
            "disabled_color"        : pg.Color("grey"),
        }
        self.update_dict(kwargs, settings)

    def update_dict(self, kwargs, settings):
        for arg in kwargs:
            if arg in settings:
                settings[arg] = kwargs[arg]
            else:
                raise AttributeError(f"{self.__class__.__name__} has no keyword: {arg}")
        self.__dict__.update(settings)

    def render_text(self):
        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text, True, color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text, True, color)
            self.text = self.font.render(self.text, True, self.font_color)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release:
                self.command()

    def on_release(self):
        if self.clicked and self.call_on_release:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.command()
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if self.hover_sound:
                    self.hover_sound.play()
        else:
            self.hovered = False

    def get_hover_color(self, color, text):
        if self.hover_color:
            color = self.hover_color
            if self.hover_font_color:
                text = self.hover_text
        border_color = self.border_hover_color
        return border_color, color, text

    def get_clicked_color(self, text):
        color = self.clicked_color
        if self.clicked_font_color:
            text = self.clicked_text
        return color, text

    def draw_text(self, surface, text):
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)

    def draw_button(self, surface, rect, border_color, inside):
        button_surface = pg.Surface(rect.size).convert_alpha()
        button_rect = pg.Rect(0, 0, *rect.size)
        if True:
            button_surface.fill(border_color)
            button_rect.inflate_ip(-self.border_width, -self.border_width)
        button_surface.fill(inside, button_rect)
        surface.blit(button_surface, rect)
