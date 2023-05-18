{
    'name': "Auto-Alter",
    'depends': ['base','mail','website'],
    'application': True,
    'license':'LGPL-3',
    'data':[
        'security/ir.model.access.csv',
        'wizard/autoalter_wizard_views.xml',
        'views/autoalter_order_views.xml',
        'views/autoalter_vehicles_views.xml',
        'views/autoalter_design_views.xml',
        'views/autoalter_customizer_views.xml',
        'views/autoalter_auction_views.xml',
        'views/autoalter_interior_materials_views.xml',
        'views/autoalter_exterior_materials_views.xml',
        'views/autoalter_feature_views.xml',
        'views/autoalter_customizer_type_views.xml',
        'views/autoalter_offer_views.xml',
        'views/autoalter_auctprice_views.xml',
        'views/autoalter_auctconnect_views.xml',
        'views/autoalter_order_views.xml',
        'controller/controller_view.xml',
        'controller/template.xml',
        'views/autoalter_menus.xml',
        'report/autoalter_report.xml',
        'report/autoalter_templates.xml',
        
    ],
    'demo':[
        'demo/autoalter_demo.xml',
    ],
    
}