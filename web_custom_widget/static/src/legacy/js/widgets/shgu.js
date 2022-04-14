odoo.define('web_custom_widget.shgu', function (require) {
    'use strict';
    
    // console.log(' yes im here shgu!!!!!!!')
    var widgetRegistry = require('web.widget_registry');
    var Widget = require('web.Widget');

    var RibbonWidget = Widget.extend({
        template: 'web_custom_widget.shgu',
        xmlDependencies: ['/web_custom_widget/static/src/legacy/xml/shgu.xml'],

      
        init: function (parent, data, options) {
            this._super.apply(this, arguments);
            this.text = options.attrs.title || options.attrs.text;
            this.tooltip = options.attrs.tooltip;
            this.className = options.attrs.bg_color ? options.attrs.bg_color : 'bg-success';
            if (this.text.length > 15) {
                this.className += ' o_small';
            } else if (this.text.length > 10) {
                this.className += ' o_medium';
            }
        },
    });

    widgetRegistry.add('web_custom_widget_shgu', RibbonWidget);

    return RibbonWidget;
});
