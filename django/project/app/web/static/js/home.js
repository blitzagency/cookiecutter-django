webpackJsonp([0],{

/***/ 194:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var ReactHabitat = __webpack_require__(33);
var Home_1 = __webpack_require__(86);
var MyApp = (function (_super) {
    __extends(MyApp, _super);
    function MyApp() {
        var _this = _super.call(this) || this;
        var container = new ReactHabitat.Container();
        container.register('Home', Home_1.Home);
        _this.setContainer(container);
        return _this;
    }
    return MyApp;
}(ReactHabitat.Bootstrapper));
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = new MyApp();


/***/ }),

/***/ 86:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var React = __webpack_require__(14);
var Menu_1 = __webpack_require__(88);
var Home = (function (_super) {
    __extends(Home, _super);
    function Home(props) {
        var _this = _super.call(this, props) || this;
        _this.state = { currentOption: 0 };
        return _this;
    }
    Home.prototype.onOptionClick = function (id) {
        console.log("got here " + id);
        this.setState({ currentOption: id });
    };
    Home.prototype.render = function () {
        return React.createElement("div", null,
            React.createElement(Menu_1.Menu, { delegate: this, selectedOption: this.state.currentOption }));
    };
    return Home;
}(React.Component));
exports.Home = Home;


/***/ }),

/***/ 88:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var React = __webpack_require__(14);
var MenuOption_1 = __webpack_require__(89);
var Option1_1 = __webpack_require__(90);
var Option2_1 = __webpack_require__(91);
var Menu = (function (_super) {
    __extends(Menu, _super);
    function Menu() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Menu.prototype.render = function () {
        var _this = this;
        var delegate = this.props.delegate;
        var selected = [0, 1].map(function (each) {
            return each == _this.props.selectedOption ? true : false;
        });
        var options = {
            0: React.createElement(Option1_1.Option1, null),
            1: React.createElement(Option2_1.Option2, null)
        };
        return React.createElement("div", null,
            React.createElement("div", null,
                React.createElement(MenuOption_1.MenuOption, { label: "Option 1", id: 0, selected: selected[0], onClick: function () { return delegate.onOptionClick(0); } }),
                React.createElement(MenuOption_1.MenuOption, { label: "Option 2", id: 1, selected: selected[1], onClick: function () { return delegate.onOptionClick(1); } })),
            React.createElement("div", null, options[this.props.selectedOption]));
    };
    return Menu;
}(React.Component));
exports.Menu = Menu;


/***/ }),

/***/ 89:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var React = __webpack_require__(14);
var MenuOption = (function (_super) {
    __extends(MenuOption, _super);
    function MenuOption() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    MenuOption.prototype.render = function () {
        if (this.props.selected) {
            return React.createElement("span", { className: "selected", style: { color: "red", paddingRight: "10px", cursor: "pointer" } }, this.props.label);
        }
        else {
            return React.createElement("span", { onClick: this.props.onClick, style: { paddingRight: "10px", cursor: "pointer" } }, this.props.label);
        }
    };
    return MenuOption;
}(React.Component));
exports.MenuOption = MenuOption;


/***/ }),

/***/ 90:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var React = __webpack_require__(14);
var Option1 = (function (_super) {
    __extends(Option1, _super);
    function Option1() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Option1.prototype.render = function () {
        return React.createElement("div", null,
            React.createElement("h3", null, "Welcome to Option 1"));
    };
    return Option1;
}(React.Component));
exports.Option1 = Option1;


/***/ }),

/***/ 91:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var React = __webpack_require__(14);
var Option2 = (function (_super) {
    __extends(Option2, _super);
    function Option2() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Option2.prototype.render = function () {
        return React.createElement("div", null,
            React.createElement("h3", null, "Welcome to Option 2"));
    };
    return Option2;
}(React.Component));
exports.Option2 = Option2;


/***/ })

},[194]);
//# sourceMappingURL=home.js.map