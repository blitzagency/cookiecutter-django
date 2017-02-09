import * as Marionette from "backbone.marionette";


Marionette.Renderer.render = function(template, data) {
    if(!template) {
        // had to use <any> here to avoid bad types error
        // Marionette.Error _does_ exist
        throw new (<any>Marionette).Error({
            name: "TemplateNotFounError",
            message: "Cannot render the template since it is not defined."
        });
    }

    try {
        return template.render(data);
    }
    catch(e) {
        // had to use <any> here to avoid bad types error
        // Marionette.Error _does_ exist
        throw new (<any>Marionette).Error({
            name: "TemplateRenderError",
            message: e.message
        });
    }
};
