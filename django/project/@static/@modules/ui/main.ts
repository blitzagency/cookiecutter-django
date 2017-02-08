import * as Backbone from "backbone";
import * as Marionette from "backbone.marionette";
import * as $ from "jquery";
import ViewController from "./controller";

const app = new Marionette.Application()

app.once("start", () => {
    new ViewController().render()
});

$(() => {
    app.start();
});
