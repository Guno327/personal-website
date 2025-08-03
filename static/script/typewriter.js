var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var _this = this;
var typingSpeed = 5; // ms per character
// Sleep function
var sleep = function (ms) { return new Promise(function (r) { return setTimeout(r, ms); }); };
// Main recursive work function
var typewrite = function (parent, element) { return __awaiter(_this, void 0, void 0, function () {
    var tag, emptyElement, children, i, i, children, i;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                if (element == null) {
                    return [2 /*return*/];
                }
                tag = element.tagName;
                emptyElement = document.createElement(tag);
                if (!(parent == null)) return [3 /*break*/, 5];
                console.log("TYPEWRITER: root element of type %s", tag);
                element.replaceWith(emptyElement);
                children = Array.from(element.children);
                i = 0;
                _a.label = 1;
            case 1:
                if (!(i < children.length)) return [3 /*break*/, 4];
                return [4 /*yield*/, typewrite(emptyElement, children[i])];
            case 2:
                _a.sent();
                _a.label = 3;
            case 3:
                i++;
                return [3 /*break*/, 1];
            case 4: return [3 /*break*/, 14];
            case 5:
                if (!(element.children.length == 0)) return [3 /*break*/, 10];
                if (element.textContent == null) {
                    console.log("TYPEWRITER: appending non-typed element of type %s", tag);
                    parent.appendChild(element);
                    return [2 /*return*/];
                }
                console.log("TYPEWRITE: typing element of type %s with text '%s'", tag, element.textContent);
                parent.appendChild(emptyElement);
                emptyElement.textContent = "";
                i = 0;
                _a.label = 6;
            case 6:
                if (!(i < element.textContent.length)) return [3 /*break*/, 9];
                emptyElement.textContent += element.textContent[i];
                return [4 /*yield*/, sleep(typingSpeed)];
            case 7:
                _a.sent();
                _a.label = 8;
            case 8:
                i++;
                return [3 /*break*/, 6];
            case 9: return [3 /*break*/, 14];
            case 10:
                console.log("TYPEWRITE: traversing nested element of type %s", tag);
                parent.append(emptyElement);
                children = Array.from(element.children);
                i = 0;
                _a.label = 11;
            case 11:
                if (!(i < children.length)) return [3 /*break*/, 14];
                return [4 /*yield*/, typewrite(emptyElement, children[i])];
            case 12:
                _a.sent();
                _a.label = 13;
            case 13:
                i++;
                return [3 /*break*/, 11];
            case 14: return [2 /*return*/];
        }
    });
}); };
document.addEventListener("DOMContentLoaded", function () {
    return __awaiter(this, void 0, void 0, function () {
        var container;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    container = document.querySelector(".typewriter");
                    return [4 /*yield*/, typewrite(null, container)];
                case 1:
                    _a.sent();
                    return [2 /*return*/];
            }
        });
    });
});
