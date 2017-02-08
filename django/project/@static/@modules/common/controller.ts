import * as Backbone from "backbone";
import * as Marionette from "backbone.marionette";
import * as _ from "underscore";
import {on, Options} from "../utils/decorators";

/**
 * This controller is a good spot to initialize any javascript comonents
 * that might need setup for demo in the UI Docs.
 */

@Options({
    template: false,
    el: "body",
})
export default class ViewController extends Marionette.View<Backbone.Model>{
    constructor() {
        super();
    }

    onRender() {
        // Temp
        console.log("Common ViewController Rendered!");
    }
}
