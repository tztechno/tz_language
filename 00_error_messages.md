
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
```
---
```
```
---
```
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


