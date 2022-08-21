// Anonymous "self-invoking" function
(function() {
    // Load the script
    var script = document.createElement("SCRIPT");
    script.src = '/static/jquery/jquery-3.3.1.min.js';
    script.type = 'text/javascript';
    script.onload = function() {
        var $ = window.jQuery;
        // Use $ here...
    };
    document.getElementsByTagName("head")[0].appendChild(script);
})();


Interestingly enough I get asked about the IIFE (immediately-invoked function expression) a lot,
which takes the following setup:

(function (window, document, undefined) {
  //
})(window, document);

So why not write a post about it? ;-)
First, this does a series of different things. From the top:

(function (window, document, undefined) {
  var name = 'Todd';
})(window, document);

console.log(name); // name is not defined, it's in a different scope

A normal function looks like this:

var logMyName = function (name) {
  console.log(name);
};

logMyName('Todd');

We get to invoke it by choice, and wherever we want/can scope providing.

The reason “IIFE” was coined was because they’re immediately-invoked function expressions.
Which means they’re immediately called at runtime - also we can’t call them again they run just once like this:

var logMyName = (function (name) {
  console.log(name); // Todd
})('Todd');

The secret sauce here is this, (which I’ve assigned to a variable in the previous example):
(function () {
})();

The extra pair of parentheses is necessary as this doesn’t work:

function () {
}();

Though several tricks can be done to trick JavaScript into “making it work”.
These force the JavaScript parser to treat the code following the ! character as an expression:

!function () {
}();

There are also other variants:

+function () {
}();

-function () {
}();

~function () {
}();

But I wouldn’t use them.

Check out Disassembling JavaScript’s IIFE Syntax by @mariusschulz for a detailed explanation of the IIFE syntax and its variants.

Arguments
Now we know how it works, we can pass in arguments to our IIFE:

(function (window) {
})(window);

How does this work? Remember, the closing (window); is where the function is invoked,
and we’re passing in the window Object. This then gets passed into the function, which
I’ve named window also. You could argue this is pointless as we should name it something
different - but for now we’ll use window as well.

So what else can we do? Pass in all the things! Let’s pass in the document Object:

(function (window, document) {
  // we refer to window and document normally
})(window, document);

Local variables are faster to resolve than the global variables, but this is on a huge scale
and you’ll never notice the speed increase - but also worth considering if we’re referencing our globals a lot!

What about undefined?
In ECMAScript 3, undefined is mutable. Which means its value could be reassigned, something like
undefined = true; for instance, oh my! Thankfully in ECMAScript 5 strict mode ('use strict';)
the parser will throw an error telling you you’re an idiot. Before this, we started protecting our IIFE’s by doing this:

(function (window, document, undefined) {
})(window, document);

Which means if someone came along and did this, we’d be okay:

undefined = true;
(function (window, document, undefined) {
  // undefined is a local undefined variable
})(window, document);

Minifying your local variables is where the IIFE pattern’s awesomeness really kicks in.
Local variable names aren’t really needed if they’re passed in, so we can call them what we like.

Changing this:

(function (window, document, undefined) {
  console.log(window); // Object window
})(window, document);

To this:

(function (a, b, c) {
  console.log(a); // Object window
})(window, document);

Imagine it, all your references to libraries and window and document nicely minified.
Of course you don’t need to stop there, we can pass in jQuery too or whatever is available in the lexical scope:

(function ($, window, document, undefined) {
  // use $ to refer to jQuery
  // $(document).addClass('test');
})(jQuery, window, document);

(function (a, b, c, d) {
  // becomes
  // a(c).addClass('test');
})(jQuery, window, document);

This also means you don’t need to call jQuery.noConflict(); or anything as $ is assigned locally to the module.
Learning how scopes and global/local variables work will help you even further.

A good minifier will make sure to rename undefined to c (for example, and only if used) throughout your script too.
Important to note, the name undefined is irrelevant. We just need to know that the referencing Object is undefined,
as undefined has no special meaning - undefined is the value javascript gives to things that are declared but have no value.

Non-browser global environments
Due to things such as Node.js, the browser isn’t always the global Object which can be a pain if you’re trying to create
IIFE’s that work across multiple environments. For this reason, I tend to stick with this as a base:

(function (root) {

})(this);

In a browser, the global environment this refers to the window Object, so we don’t need to pass in window at all,
we could always shorten it to this.

I prefer the name root as it can refer to non-browser environments as well as the root of the browser.

If you’re interested in a universal solution (which I use all the time nowadays when creating open source
project modules) is the UMD wrapper:

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define(factory);
  } else if (typeof exports === 'object') {
    module.exports = factory;
  } else {
    root.MYMODULE = factory();
  }
})(this, function () {
  //
});

This is some sexy stuff. The function is being invoked with another function passed into it.
We can then assign it to the relevant environment inside.
In the browser, root.MYMODULE = factory(); is our IIFE module, elsewhere (such as Node.js) it’ll
use module.exports or requireJS if typeof define === 'function' && define.amd resolves true.


