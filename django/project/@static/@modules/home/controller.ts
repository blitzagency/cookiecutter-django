import * as Backbone from "backbone";
import * as Marionette from "backbone.marionette";
import * as _ from "underscore";
import {on, Options} from "../utils/decorators";
import TestView from "./views/test-view";

/**
 * This controller is a good spot to initialize any javascript comonents
 * that might need setup for demo in the UI Docs.
 */

@Options({
    template: false,
    el: "body",
    regions: {
        "main": ".js-region-main"
    }
})
export default class ViewController extends Marionette.View<Backbone.Model>{
    constructor() {
        super();
    }

    onRender() {
        // Temp
        console.log("Home ViewController Rendered!");
        (<any>this).showChildView("main", new TestView());
    }
}
