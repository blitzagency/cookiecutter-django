import * as Backbone from "backbone";
import * as Marionette from "backbone.marionette";
import * as $ from "jquery";
import * as _ from "underscore";
import {on, Options} from "../../utils/decorators";

const template = require("../templates/test.njk");


@Options({
    template: template,
    className: "test-view",
    ui: {},
})
export default class TestView extends Marionette.View<Backbone.Model> {
    constructor() {
        super();

        this.model = new Backbone.Model({
            name: "Penny",
            message: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eleifend tellus quam, et ullamcorper elit aliquet a. Mauris bibendum, orci non condimentum interdum, eros velit sollicitudin purus, nec interdum arcu nisi in eros. Aliquam non nisl quis velit condimentum porttitor. Sed vitae ante sapien. Donec scelerisque lectus eu pretium euismod. Integer efficitur ex nunc, eu sollicitudin leo faucibus et. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce condimentum venenatis rutrum. Vivamus iaculis posuere metus at pharetra. Pellentesque placerat felis nisi, sed ullamcorper orci vestibulum id. Praesent a urna ipsum. Aenean vestibulum eleifend risus, ac posuere augue volutpat vitae. Integer et nibh ex."
        })
    }

    onRender() {
        console.log("TestView.onRender");
    }
}
