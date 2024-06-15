
###
# error messages 
###

### latest
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
Main.java:12: error: no suitable method found for getNumericValue(String)
        int Y=Character.getNumericValue(X);
                       ^
    method Character.getNumericValue(char) is not applicable
      (argument mismatch; String cannot be converted to char)
    method Character.getNumericValue(int) is not applicable
      (argument mismatch; String cannot be converted to int)
1 error
```
---
```
Main.java:5: error: cannot find symbol
        String X = sc.next();
                   ^
  symbol:   variable sc
  location: class Main
Main.java:12: error: no suitable method found for getNumericValue(String)
        int Y=Character.getNumericValue(X);
                       ^
    method Character.getNumericValue(char) is not applicable
      (argument mismatch; String cannot be converted to char)
    method Character.getNumericValue(int) is not applicable
      (argument mismatch; String cannot be converted to int)
2 errors

```
---
```
127.0.0.1/:1 Uncaught (in promise) Error: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
```
---
```
# atcoder.jp/golang
./main.go:13:9: err declared and not used
./main.go:13:29: cannot use r (variable of type rune) as string value in argument to strconv.Atoi
```
---
```
RuntimeError: shape '[-1, 46656]' is invalid for input of size 184512
```
---
```
% cargo run
   Compiling my_proj v0.1.0 (/Users/shun_ishii/DockerProjects/pj2/my_proj)
error[E0432]: unresolved import `rocket::response::content::Html`
 --> src/main.rs:7:5
  |
7 | use rocket::response::content::Html;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ no `Html` in `response::content`

error[E0599]: no method named `ok` found for opaque type `impl std::future::Future<Output = Result<NamedFile, std::io::Error>>` in the current scope
  --> src/main.rs:19:54
   |
19 |     NamedFile::open(Path::new("static/").join(file)).ok()
   |                                                      ^^ method not found in `impl Future<Output = Result<NamedFile, Error>>`
   |
help: consider `await`ing on the `Future` and calling the method on its `Output`
   |
19 |     NamedFile::open(Path::new("static/").join(file)).await.ok()
   |                                                      ++++++

Some errors have detailed explanations: E0432, E0599.
For more information about an error, try `rustc --explain E0432`.
error: could not compile `my_proj` (bin "my_proj") due to 2 previous errors
```
---


