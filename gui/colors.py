background_color = '#caccce'
factory_color = '#616665'
retailer_color = 'white'
wholesale_color = '#eabff6'
outline_default_color = 'black'
text_default_color = 'white'
black = 'black'


class RouteColorsGenerator:
    def __init__(self):
        self.color_families = [
            ['#f8de7e', '#ffd300', '#d2b55b', '#fda50f'],
            ['#63c5da', '#0492c2', '#59788e', '#0A1172'],
            ['#99edc3', '#3cb043', '#b0fc38', '#98bf64', '#728c69', '#597d35'],
            ['#d0312d', '#7e2811', '#a91b0d', '#bc544b'],
            ['#ffffff', '#dfdfdf', '#909090'],
        ]
        self.color_dict = {}
        self.current_family_idx = 0

    @property
    def current_family(self):
        if self.current_family_idx >= len(self.color_families):
            self.current_family_idx = 0
        return self.color_families[self.current_family_idx]

    def get_color(self, route):
        origin = route.origin.name

        if origin in self.color_dict:
            pass
        else:
            self.color_dict[origin] = self.current_family
            self.current_family_idx += 1

        color = self.color_dict[origin].pop()
        self.color_dict[origin].insert(0, color)

        return color
