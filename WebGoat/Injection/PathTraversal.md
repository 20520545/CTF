# Path Traversal

2.Path traversal while uploading files

While uploading profiles, we can see that files are create at /{username}. So to overwrite file, we just write `../{something}` in Full Name.

3.Path traversal while uploading files

Filter `../`, we can use our previous technique is concatenating 2 string to complete the challenge.

Full Name: `....//{something}`

4.Path traversal while uploading files

Just like previous challenge but the path create from the filename, so we can intercept the request and change the name of the file uploading in request to complete the challenge.

`------WebKitFormBoundary9PGKAmTKnuRnmqW4
Content-Disposition: form-data; name="uploadedFileRemoveUserInput"; filename="../1.jpg"`

5.Retrieving other files with a path traversal.

Observing request and response, in `Locaation` header of response, we can see that the picture is selected randomly from id parameter.

`Location: /PathTraversal/random-picture?id=8.jpg`

Try to go to `?id=../../path-traversal-secret.jpg`, it has been forbbidden for filter, so URL encode can pass the block: `?id=%2e%2e%2f%2e%2e%2fpath-traversal-secret`.

7.Zip Slip assignment

Zip any file and upload it to the server. The file doesn't replace the avater but it will overwrite the the current one.
