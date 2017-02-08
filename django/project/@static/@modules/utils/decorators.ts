import * as _ from 'underscore';

export function Options(value: any){
    return function(target: any): any {
        let proto = target.prototype;
        proto.className = value.className;
        proto.template = value.template;
        proto.regions = _.extend({}, proto.regions, value.regions);
        proto.triggers = _.extend({}, proto.triggers, value.triggers);
        proto.ui = _.extend({}, proto.ui, value.ui);
        proto.el = value.el || undefined;
        proto.tagName = value.tagName || "div";
        proto.childViewEvents = _.extend({}, proto.childViewEvents, value.childViewEvents);
        proto.bindings = _.extend({}, proto.bindings, value.bindings);
    }
}

export function childView(eventName: string): any{
    return function(target, name, descriptor){
        if(!target.childViewEvents) {
            target.childViewEvents = {};
        }

        if(_.isFunction(target.childViewEvents)) {
            throw new Error('The "childView" decorator is not compatible with a childViewEvents method');
        }

        if(!eventName) {
            throw new Error('The "childView" decorator requires an eventName argument');
        }

        target.childViewEvents[eventName] = name;
        return descriptor;
    }
}


export function model(eventName: string): any{
    return function(target, name, descriptor){
        if(!target.modelEvents) {
            target.modelEvents = {};
        }

        if(_.isFunction(target.modelEvents)) {
            throw new Error('The on decorator is not compatible with an modelEvents method');
        }

        if(!eventName) {
            throw new Error('The on decorator requires an eventName argument');
        }

        target.modelEvents[eventName] = name;
        return descriptor;
    }
}


export function on(eventName: string): any{
    return function(target, name, descriptor){
        if(!target.events) {
            target.events = {};
        }

        if(_.isFunction(target.events)) {
            throw new Error('The on decorator is not compatible with an events method');
        }

        if(!eventName) {
            throw new Error('The on decorator requires an eventName argument');
        }

        target.events[eventName] = name;
        return descriptor;
    }
}
