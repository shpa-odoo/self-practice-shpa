from odoo import http

class Controllers(http.Controller):
    @http.route('/autoalter/vehicles',auth="public",website=True)
    def index(self, **kw):
        vehicles = http.request.env['autoalter.vehicles']
        domain = []
        print(vehicles)
        return http.request.render('autoalter.index', {
             'vehicles': vehicles.search(domain)
        })

    @http.route('/autoalter/designs',auth="public",website=True)
    def design(self, **kw):
        designs = http.request.env['autoalter.design']
        domain = []
        print(designs)
        return http.request.render('autoalter.design_list', {
             'designs': designs.search(domain)
        })

    @http.route('/autoalter/customizer',auth="public",website=True)
    def Customizer(self, **kw):
        customizers = http.request.env['autoalter.customizer']
        domain = []
        print(customizers)
        return http.request.render('autoalter.customizer_list', {
             'customizers': customizers.search(domain)
        })

    @ http.route('/autoalter/vehicles/<model("autoalter.vehicles"):vehicle>/', auth = "public", website = True)
    def vehicles_list(self, vehicle):
        return http.request.render('autoalter.website_vehicle_view', {
            'vehicle': vehicle,
        })

    @ http.route('/autoalter/designs/<model("autoalter.design"):design>/', auth = "public", website = True)
    def designs_list(self, design):
        return http.request.render('autoalter.website_design_view', {
            'design': design,
        })
    
    @ http.route('/autoalter/customizer/<model("autoalter.customizer"):customizer>/', auth = "public", website = True)
    def customizers_list(self, customizer):
        return http.request.render('autoalter.website_customizer_view', {
            'customizer': customizer,
        })